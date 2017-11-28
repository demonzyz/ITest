# coding:utf-8
import base64
import hashlib
import Random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def base64_encode(str):
    return base64.encodestring(str)

def get_sign(token, params, random):
    list = []
    for key, value in params.items():
        if key != 'username':
            list.append(key+'='+value)
    list.sort()
    params_str = '&'.join(list)
    sign_str = "%spara=%s%s" % (token, params_str, random)
    md5 = hashlib.md5()
    md5.update(sign_str.encode('utf-8'))
    sign = md5.hexdigest()
    return sign

#
# if __name__ == '__main__':
#     random = Random.get_str(5)
#     token = 'd06da11c96d37f353fad887d7b49521db2e36b92'
#     params = {'title': '小米发布会', 'time': '2017-11-25', 'address': '地中海风情岛', 'username': 'huice'}
#     print get_sign(token=token, params=params, random=random)
#