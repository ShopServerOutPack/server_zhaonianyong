

import os

BASEURL = os.getenv("BASEURL","https://www.hanggetuiguang.xyz")
APIURL = "{}{}".format(BASEURL,"/v1/api")
CALLBACKURL = "{}{}".format(APIURL,"/order/txPayCallback")

#腾讯对象存储
TX_SECRET_ID = os.getenv("TX_SECRET_ID",None)
TX_SECRET_KEY = os.getenv("TX_SECRET_KEY",None)

#小程序
WECHAT_APPID = os.getenv("WECHAT_APPID","wxfa544b7fd00148c9")
WECHAT_SECRET = os.getenv("WECHAT_SECRET","6da15882b011789294a97a0055cb0f67")
WECHAT_PAY_MCHID = os.getenv("WECHAT_PAY_MCHID","1569651221")
WECHAT_PAY_KEY = os.getenv("WECHAT_PAY_KEY","fsdafsdafAfdsNNNFFHH12dak1203813")
WECHAT_PAY_RETURN_KEY = os.getenv("WECHAT_PAY_RETURN_KEY","sdfsdkllvljAFSAFnncsdf21klsjfl12")
