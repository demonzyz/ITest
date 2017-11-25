#coding:utf-8
import sys

import requests
from util import Random

from util import encrypt

reload(sys)
sys.setdefaultencoding('utf8')
"""
添加会议接口  正常流程
"""
url = 'http://127.0.0.1:8000/api/add_event/'
random = Random.get_str(5)
token = 'd06da11c96d37f353fad887d7b49521db2e36b92'
headers = {'token': token, 'random': random}
data = {'title': '小米发布会', 'time': '2017-11-25', 'address': '地中海风情岛', 'username': 'huice'}
sign = encrypt.get_sign(token, data, random)
data['sign'] = sign
response = requests.request('POST', url=url, headers=headers, data=data).json()
assert response.get('error_code', None) == 0, 'error_code不正确'
assert response.get('data', None).get('event_id', None) != None, 'event_id不正确'
print '成功'