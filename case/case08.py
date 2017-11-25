#coding:utf-8
import sys

import requests
from util import Random
from util import encrypt

reload(sys)
sys.setdefaultencoding('utf8')
"""
查询会议接口  正常流程
"""
url = 'http://127.0.0.1:8000/api/get_eventlist/'
random = Random.get_str(5)
token = 'd06da11c96d37f353fad887d7b49521db2e36b92'
headers = {'token': token, 'random': random}
data = {'title': '小米发布会', 'username': 'huice'}
sign = encrypt.get_sign(token, data, random)
data['sign'] = sign
response = requests.request('GET', url=url, headers=headers, params=data).json()
assert response.get('error_code', None) == 0, 'error_code不正确'
assert response.get('event_list', None) != None, 'event_list不正确'
print '成功'