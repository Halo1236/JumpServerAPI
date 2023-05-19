# -*- coding: utf-8 -*-
#

import datetime
from typing import List

import requests
import urllib3
from httpsig.requests_auth import HTTPSignatureAuth

urllib3.disable_warnings()

jms_url = 'https://ayhalo.tpddns.cn'
KeyID = 'xxxxxxxx'
SecretID = 'xxxxxxxxxxx'
org_id = '00000000-0000-0000-0000-000000000002'


def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth


def get_users(jms_url, auth):
    url = jms_url + '/api/v1/users/users/'
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': org_id,
        'Date': datetime.datetime.utcnow().strftime(gmt_form)
    }

    response = requests.get(url, auth=auth, headers=headers, verify=False)
    return response.json() if isinstance(response.json(), List) else response.json().get('results')


def detele_user(jms_url, auth, user_id):
    url = jms_url + '/api/v1/users/users/{}/'.format(user_id)
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': org_id,
        'Date': datetime.datetime.utcnow().strftime(gmt_form)
    }

    response = requests.delete(url, auth=auth, headers=headers, verify=False)
    return True if response.status_code == 204 or response.status_code == 200 else False


def start():
    print("\n", "#" * 20, "读取txt文件", "#" * 20)
    username_white_list = []
    with open('user.txt', mode='r', encoding='utf-8') as f:
        tmps = f.readlines(1000)
        for i in tmps:
            username_white_list.append(i.strip('\n'))
    print(username_white_list)

    print("\n", "#" * 20, "调用用户列表接口，获取所有用户", "#" * 20)

    auth = get_auth(KeyID, SecretID)
    users_all = get_users(jms_url, auth)
    for user_json in users_all:
        if user_json['username'] not in username_white_list:
            print("\n", "#" * 20, "开始删除用户：{}".format(user_json['username']), "#" * 20)
            rs = detele_user(jms_url, auth, user_json['id'])
            if rs:
                print("\n", "#" * 20, "删除：{} 成功！".format(user_json['username']), "#" * 20)
            else:
                print("\n", "#" * 20, "删除：{} 失败！".format(user_json['username']), "#" * 20)

    print("\n", "#" * 20, "清理完成！", "#" * 20)


if __name__ == '__main__':
    start()
