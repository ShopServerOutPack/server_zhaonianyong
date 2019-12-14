from rest_framework import viewsets
from rest_framework.decorators import list_route
from lib.core.decorator.response import Core_connector
from lib.utils.exceptions import PubErrorCustom

from app.user.models import Users
from app.goods.models import GoodsCateGory,Goods
from app.public.models import Banner,AttachMentGroup,AttachMent


from app.cache.utils import RedisCaCheHandler

class SsyAPIView(viewsets.ViewSet):

    #刷新所有用户缓存数据
    @list_route(methods=['POST'])
    @Core_connector()
    def refeshUserRedis(self,request, *args, **kwargs):

        RedisCaCheHandler(
            method="saveAll",
            serialiers="UserModelSerializerToRedis",
            table="user",
            filter_value=Users.objects.filter(status='0'),
            must_key="userid",
        ).run()

        RedisCaCheHandler(
            method="saveAll",
            serialiers="GoodsCateGoryModelSerializerToRedis",
            table="goodscategory",
            filter_value=GoodsCateGory.objects.filter(),
            must_key="gdcgid",
        ).run()

        RedisCaCheHandler(
            method="saveAll",
            serialiers="GoodsModelSerializerToRedis",
            table="goods",
            filter_value=Goods.objects.filter(),
            must_key="gdid",
        ).run()

        RedisCaCheHandler(
            method="saveAll",
            serialiers="AttachMentGroupModelSerializerToRedis",
            table="AttachMentGroup",
            filter_value=AttachMentGroup.objects.filter(),
            must_key="id",
        ).run()

        RedisCaCheHandler(
            method="saveAll",
            serialiers="AttachMentModelSerializerToRedis",
            table="AttachMent",
            filter_value=AttachMent.objects.filter(),
            must_key="id",
        ).run()

        return None