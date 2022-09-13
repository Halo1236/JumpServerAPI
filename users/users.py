# -*- coding: utf-8 -*-
#
import json

import requests

from common.auth import AccessKeyAuth


def get_users_list(baseUrl, ak, sk):
    """
    获取用户列表信息
    :param baseUrl:
    :param ak:
    :param sk:
    :return:
    """
    url = baseUrl + '/api/v1/users/users/'
    headers = AccessKeyAuth(ak, sk).sign_request()
    response = requests.get(url, headers=headers)
    print(json.loads(response.text))


def get_user_info_by_id(baseUrl, ak, sk):
    """
    通过userid获取用户信息
    :param baseUrl:
    :param ak:
    :param sk:
    :return:
    """
    url = baseUrl + '/api/v1/users/users/%s/' % '8181cbda-feb5-432a-9dec-037d1ea87db5'
    headers = AccessKeyAuth(ak, sk).sign_request()
    response = requests.get(url, headers=headers)
    print(json.loads(response.text))


def get_user_info_by_username(baseUrl, ak, sk):
    """
    通过userid获取用户信息
    :param baseUrl:
    :param ak:
    :param sk:
    :return:
    """
    url = baseUrl + '/api/v1/users/users/?username=%s' % 'bes'
    headers = AccessKeyAuth(ak, sk).sign_request()
    response = requests.get(url, headers=headers)
    print(json.loads(response.text))


if __name__ == '__main__':
    jmsUrl = 'https://jms1.fit2cloud.com'
    KeyID = '02cc7f6a-7a76-43c9-9b33-7d6d2c2e895d'
    SecretID = '455c0dfb-7298-48b6-9b02-750fb03098b3'
    get_users_list(jmsUrl, KeyID, SecretID)
    get_user_info_by_id(jmsUrl, KeyID, SecretID)
    get_user_info_by_username(jmsUrl, KeyID, SecretID)
