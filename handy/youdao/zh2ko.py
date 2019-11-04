# -*- coding: utf-8 -*-
# from https://irma.youdao.com/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/API%E6%96%87%E6%A1%A3/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html#section-9
import sys
import uuid
import requests
import hashlib
import time

if sys.version_info[0] == 3:
    from imp import reload

reload(sys)

if sys.version_info[0] == 2:
    sys.setdefaultencoding('utf-8')

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '1f17d393214b29f2'
APP_SECRET = 'p24tXj2SUPuJqzoYqcFbXWIA5er5jVEb'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    q_utf8 = q.decode("utf-8") if sys.version_info[0] == 2 else q
    size = len(q_utf8)
    return q_utf8 if size <= 20 else q_utf8[0:10] + str(size) + q_utf8[size - 10:size]

def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(text,src='zh-CHS',dst='ko'):
    data = {}
    data['from'] = src
    data['to'] = dst
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(text) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = text
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    contentType = response.headers['Content-Type']
    return response.content

class YouDaoTranslate():
    """
    有道词典API
    """
    # 可选值xml, json
    DOC_TYPE = 'json'
    def translate(self, text, src='zh-CHS',dst='ko'):
        """
        翻译方法，传入要翻译的文本，返回结果字典
        """
        import json
        result = connect(text)
        jsonstr=json.loads(result, encoding='utf-8')
        if "translation" in jsonstr.keys(): print(jsonstr["translation"][0])
        else: print("Not Found!")

if __name__ == '__main__':
    while True:
        content =  raw_input('请输入翻译内容：') if sys.version_info[0] == 2 else input('请输入翻译内容：')
        if content:
            YouDaoTranslate().translate(content)
        else:
            print('有道翻译： \n\t提示：您已退出！！')
            break