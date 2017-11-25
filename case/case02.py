#coding:utf-8
import requests
from util import Random

from util import encrypt

url = 'http://127.0.0.1:8000/api/register/'
username = ''
password =  'huicehuice!@#'
data = {'username': username, 'password': encrypt.base64_encode(Random.get_str(3) + password)}
response = requests.request('POST', url=url, data=data)
result = response.json()
assert result.get('error_code', None) == 10001, 'error_code不正确'
assert result.get('token', None) == None , 'token不应该存在'
print '用例执行成功'