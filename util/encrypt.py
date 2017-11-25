import base64
import hashlib

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