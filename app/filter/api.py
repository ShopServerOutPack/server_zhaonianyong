
from rest_framework import viewsets
from rest_framework.decorators import list_route

from lib.core.decorator.response import Core_connector

from app.cache.utils import RedisCaCheHandler

class FilterAPIView(viewsets.ViewSet):

    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True)
    def getHomeBaseData(self, request):
        """
        获取导航数据
        :param request:
        :return:
        """
        data={
            "pages":{
                "index":{
                    "name": "航歌的商城",
                    "text": "描述",
                    "components": []
                }
            },
            "tarbar":{
                "color": '#ccc',
                "selectedColor": '#E84351',
                "borderStyle": '#ccc',
                "backgroundColor": '#fff',
                "position": 'bottom',
                "list": [
                    {
                        "pagePath": '/pages/index/index',
                        "iconPath": '/static/tab-cart.png',
                        "selectedIconPath": '/static/tab-cart-current.png',
                        "text": '首页'
                    },
                    {
                        "pagePath": '/pages/index/index',
                        "iconPath": '/static/tab-cart.png',
                        "selectedIconPath": '/static/tab-cart-current.png',
                        "text": '吃什么'
                    },
                    {
                        "pagePath": '/pages/index/index',
                        "iconPath": '/static/tab-cart.png',
                        "selectedIconPath": '/static/tab-cart-current.png',
                        "text": '首页'
                    },
                    {
                        "pagePath": '/pages/index/index',
                        "iconPath": '/static/tab-cart.png',
                        "selectedIconPath": '/static/tab-cart-current.png',
                        "text": '首页'
                    },
                ]
            }
        }

        return {"data":data}

    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True)
    def userdata(self, request):
        """
        获取用户所有基础数据
        :param request:
        :return:
        """

        #轮播图
        banner=[{
            'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/banner1.jpg",
            'background': "rgb(203, 87, 60)",
        },
	    {
            'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/banner2.jpg",
            'background': "rgb(205, 215, 218)",
	    },
        {
            'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/banner3.jpg",
            'background': "rgb(183, 73, 69)",
        }]

        #首页菜单
        homemenu = [
            {
                'id':1,
                'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/c3.png",
                'text': "环球美食",
            },
            {
                'id': 2,
                'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/c3.png",
                'text': "环球美食",
            },
            {
                'id': 3,
                'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/c3.png",
                'text': "环球美食",
            },
            {
                'id': 4,
                'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/c3.png",
                'text': "环球美食",
            },
            {
                'id': 5,
                'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/c3.png",
                'text': "环球美食",
            }
            ]
        c = len(homemenu)
        count = 5 - c % 5 if c % 5 >0 else 0
        while count:
            homemenu.append({
                'src': "",
                'text': "",
            })
            count -=1

        #获取中间动态模块
        homeadpage=[
            {
                'id':1,
                'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/ad1.jpg",
                'type': 1, #图片
            },
            # {
            #     'id': 2,
            #     'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/2076ea8dffa0a1f9eae5ead0b9fbf383.mp4",
            #     'type': 2, #视频
            # },
            ]

        #限时抢购
        seckill = [
            {
                "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1553187020783&di=bac9dd78b36fd984502d404d231011c0&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201609%2F26%2F20160926173213_s5adi.jpeg",
                "image2": "http://pic.rmb.bdstatic.com/819a044daa66718c2c40a48c1ba971e6.jpeg",
                "image3": "http://img001.hc360.cn/y5/M00/1B/45/wKhQUVYFE0uEZ7zVAAAAAMj3H1w418.jpg",
                "title": "古黛妃 短袖t恤女夏装2019新款韩版宽松",
                "price": 179,
                "sales": 61,
            },
            {
                "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1553187020783&di=bac9dd78b36fd984502d404d231011c0&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201609%2F26%2F20160926173213_s5adi.jpeg",
                "image2": "http://pic.rmb.bdstatic.com/819a044daa66718c2c40a48c1ba971e6.jpeg",
                "image3": "http://img001.hc360.cn/y5/M00/1B/45/wKhQUVYFE0uEZ7zVAAAAAMj3H1w418.jpg",
                "title": "古黛妃 短袖t恤女夏装2019新款韩版宽松",
                "price": 179,
                "sales": 61,
            },
            {
                "image": "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1620020012,789258862&fm=26&gp=0.jpg",
                "image2": "http://m.360buyimg.com/n12/jfs/t247/42/1078640382/162559/3628a0b/53f5ad09N0dd79894.jpg%21q70.jpg",
                "image3": "http://ikids.61kids.com.cn/upload/2018-12-29/1546070626796114.jpg",
                "title": "巧谷2019春夏季新品新款女装",
                "price": 108.8,
                "sales": 5,
            },
            {
                "image": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1553187020783&di=bac9dd78b36fd984502d404d231011c0&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201609%2F26%2F20160926173213_s5adi.jpeg",
                "image2": "http://pic.rmb.bdstatic.com/819a044daa66718c2c40a48c1ba971e6.jpeg",
                "image3": "http://img001.hc360.cn/y5/M00/1B/45/wKhQUVYFE0uEZ7zVAAAAAMj3H1w418.jpg",
                "title": "古黛妃 短袖t恤女夏装2019新款韩版宽松",
                "price": 179,
                "sales": 61,
            },
            {
                "image": "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1620020012,789258862&fm=26&gp=0.jpg",
                "image2": "http://m.360buyimg.com/n12/jfs/t247/42/1078640382/162559/3628a0b/53f5ad09N0dd79894.jpg%21q70.jpg",
                "image3": "http://ikids.61kids.com.cn/upload/2018-12-29/1546070626796114.jpg",
                "title": "巧谷2019春夏季新品新款女装",
                "price": 108.8,
                "sales": 5,
            },
        ]

        return {"data":{
            "banner":banner,
            "homemenu" : homemenu,
            "homeadpage": homeadpage,
            "seckill" : seckill
        }}

    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True)
    def getBanner(self, request):
        """
        获取轮播图
        :param request:
        :return:
        """

        data = RedisCaCheHandler(
            method="filter",
            serialiers="BannerModelSerializerToRedis",
            table="banner",
            filter_value=request.query_params_format
        ).run()

        return {"data":data}


    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True)
    def getOtherMemo(self, request):
        """
        获取公告数据
        :param request:
        :return:
        """

        obj =RedisCaCheHandler(
            method="filter",
            serialiers="OtherMemoModelSerializerToRedis",
            table="OtherMemo",
            filter_value=request.query_params_format
        ).run()
        print(obj)
        return {"data":obj[0] if obj else False}


    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True,isTicket=True)
    def getVipGoodsList(self, request):
        """
        获取视频数据
        :param request:
        :return:
        """

        # 轮播图
        goodsList = [
        {
            'img' : "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1620020012,789258862&fm=26&gp=0.jpg",
            'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/2076ea8dffa0a1f9eae5ead0b9fbf383.mp4",
            'title':"第一式"
        },
        {
            'img': "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1620020012,789258862&fm=26&gp=0.jpg",
            'src': "https://baseshopserver.oss-cn-hangzhou.aliyuncs.com/test/2076ea8dffa0a1f9eae5ead0b9fbf383.mp4",
            'title': "第二式"
        },
        ]
        return {"data":goodsList}


    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True)
    def getGoodsCategory(self, request):
        """
        获取分类数据
        :param request:
        :return:
        """

        obj =RedisCaCheHandler(
            method="filter",
            serialiers="GoodsCateGoryModelSerializerToRedis",
            table="goodscategory",
            filter_value=request.query_params_format
        ).run()

        obj.sort(key=lambda k: (k.get('sort', 0)), reverse=False)

        return {"data":obj}



    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True)
    def getHomeData(self,request):

        rdata={
            "banners":[],
            "category":[],
            "active":0
        }

        #轮播图数据
        rdata['banners'] = RedisCaCheHandler(
            method="filter",
            serialiers="BannerModelSerializerToRedis",
            table="banner",
            filter_value={}
        ).run()

        #分类数据
        rdata['category'] = RedisCaCheHandler(
            method="filter",
            serialiers="GoodsCateGoryModelSerializerToRedis",
            table="goodscategory",
            filter_value={"isstart":"0","istheme":"1"}
        ).run()

        rdata['category'].sort(key=lambda k: (k.get('sort', 0)), reverse=False)

        #第一条分类数据的视频数据
        if len(rdata['category']):
            rdata['category'][0]['goods'] =RedisCaCheHandler(
                method="filter",
                serialiers="GoodsModelSerializerToRedis",
                table="goods",
                    filter_value={"gdcgid":rdata['category'][0]['gdcgid'],"gdstatus":"0"}
            ).run()
            rdata['active'] = rdata['category'][0]['gdcgid']

        print(rdata)
        #
        return {"data": rdata}


    @list_route(methods=['GET'])
    @Core_connector(isPasswd=True)
    def getGoodsList(self, request):
        """
        获取视频数据
        :param request:
        :return:
        """

        obj =RedisCaCheHandler(
            method="filter",
            serialiers="GoodsModelSerializerToRedis",
            table="goods",
            filter_value=request.query_params_format
        ).run()
        print(obj)
        return {"data":obj}
