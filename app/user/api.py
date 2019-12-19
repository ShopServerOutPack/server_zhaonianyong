
from rest_framework import viewsets
from rest_framework.decorators import list_route

from lib.core.decorator.response import Core_connector

from app.cache.serialiers import UserModelSerializerToRedis
from app.user.models import Users
from app.user.serialiers import UsersSerializers

class UserAPIView(viewsets.ViewSet):

    @list_route(methods=['GET'])
    @Core_connector(isTicket=True,isPasswd=True)
    def getUserInfo(self, request):

        return {"data": {
            "userInfo": {
                "username": request.user.get("uuid"),
                "name": request.user.get("name"),
                'rolecode': request.user.get("role").get("rolecode"),
                "rolename": request.user.get("role").get("rolename"),
                "avatar": 'http://allwin6666.com/nginx_upload/assets/login.jpg'
            },
            "roles": request.user.get("role").get("rolecode"),
            "permission": []
        }}

    @list_route(methods=['GET'])
    @Core_connector(isTicket=True,isPasswd=True)
    def getUser(self, request):

        return {"data": UserModelSerializerToRedis(Users.objects.filter(rolecode=request.query_params_format['rolecode']),many=True).data}

    @list_route(methods=['GET'])
    @Core_connector(isTicket=True, isPasswd=True)
    def getUserByWechat(self, request):

        return {"data": UsersSerializers(Users.objects.get(userid=request.user['userid']),many=False).data}


    @list_route(methods=['POST'])
    @Core_connector(isTransaction=True,isPasswd=True,isTicket=True)
    def updUser(self, request):

        userid = request.data_format['userid']
        user = Users.objects.get(userid=userid)
        user.isvip = request.data_format["isvip"]
        print(user.isvip)
        user.save()
        return None


