
import json
from rest_framework import viewsets
from rest_framework.decorators import list_route
from lib.core.decorator.response import Core_connector
from django.db import transaction
from app.user.models import Users
from lib.utils.exceptions import PubErrorCustom
from django.http import HttpResponse
from app.order.utils import wechatPay

from app.order.models import Order

class OrderAPIView(viewsets.ViewSet):


    @list_route(methods=['POST'])
    @Core_connector(isTransaction=True,isPasswd=True,isTicket=True)
    def openVip(self, request):
        """
        开通会员
        :param request:
        :return:
        """
        print(request.data_format)
        try:
            user = Users.objects.get(userid=request.user.get("userid"))
        except Users.DoesNotExist:
            raise PubErrorCustom("用户不存在!")

        order = Order.objects.create(**{
            "userid" : user.userid,
            "amount" : 0.1,
            "payamount":0.1
        })

        data = wechatPay().request({
            "out_trade_no" : order.orderid,
            "total_fee" : int(order.amount * 100),
            "spbill_create_ip" : "192.168.0.1",
            "openid": user.uuid
        })

        return {"data":data}

    @list_route(methods=['POST'])
    @Core_connector(isTransaction=True,isPasswd=True,isTicket=True)
    def txPayOrderQuery(self, request):

        wechatPay().orderQuery(request.data_format['orderid'])
        return None

    @list_route(methods=['POST','GET'])
    def txPayCallback(self, request):
        try:
            with transaction.atomic():
                wechatPay().callback(request)
            return HttpResponse("""<xml><return_code><![CDATA[SUCCESS]]></return_code>
                                <return_msg><![CDATA[OK]]></return_msg></xml>""",
                            content_type='text/xml', status=200)
        except Exception:
            return HttpResponse("""<xml><return_code><![CDATA[FAIL]]></return_code>                          
                                    <return_msg><![CDATA[Signature_Error]]></return_msg></xml>""",
                                         content_type = 'text/xml', status = 200)

