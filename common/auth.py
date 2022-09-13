# -*- coding: utf-8 -*-
# 在线api文档 https://docs.jumpserver.org/zh/master/dev/rest_api/#api_1

import base64
import datetime
import hashlib

_GMT_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"
_ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S.000Z"


class AccessKeyAuth:
    """
    Access Key 对 Http Header 进行签名
    """

    def __init__(self, access_key_id, access_key_secret):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret

    @staticmethod
    def _make_signature(access_key_secret, date_gmt: str):
        """
        计算data的MD5值，经过Base64编码并返回str类型。
        返回值可以直接作为HTTP Content-Type头部的值
        """
        data = str(access_key_secret) + "\n" + date_gmt
        if isinstance(data, str):
            data = hashlib.md5(data.encode('utf-8'))
        value = base64.b64encode(data.hexdigest().encode('utf-8'))
        return value.decode('utf-8')

    def sign_request(self, headers=None):
        if headers is None:
            headers = {}
        date = datetime.datetime.utcnow().strftime(_GMT_FORMAT)
        headers['Date'] = date
        signature = self._make_signature(self.access_key_secret, date_gmt=date)
        headers['Authorization'] = "Sign {0}:{1}".format(self.access_key_id, signature)
        headers['Accept'] = 'application/json'
        headers['X-JMS-ORG'] = 'ROOT'
        return headers

    def __bool__(self):
        return self.access_key_id != "" and self.access_key_secret != ""


class TokenAuth:
    """
    Token 获取一次性 Token，该 Token 有有效期, 过期作废
    """

    def __init__(self, token):
        self.token = token

    def sign_request(self, headers=None):
        if headers is None:
            headers = {}
        headers['Authorization'] = 'Bearer {0}'.format(self.token)
        headers['Accept'] = 'application/json'
        headers['X-JMS-ORG'] = 'ROOT'
        return headers

    def __bool__(self):
        return self.token != ""


class SessionAuth:
    """
    Session 登录后可以直接使用 session_id 作为认证方式
    """

    def __init__(self, session_id, csrf_token):
        self.session_id = session_id
        self.csrf_token = csrf_token

    def sign_request(self, headers=None):
        if headers is None:
            headers = {}
        cookie = [v for v in headers.get('Cookie', '').split(';')
                  if v.strip()]
        cookie.extend(['sessionid=' + self.session_id,
                       'csrftoken=' + self.csrf_token])
        headers['Cookie'] = ';'.join(cookie)
        headers['X-CSRFTOKEN'] = self.csrf_token
        headers['Accept'] = 'application/json'
        headers['X-JMS-ORG'] = 'ROOT'
        return headers

    def __bool__(self):
        return self.session_id != ""


class PrivateTokenAuth:
    """
    Private Token  永久 Token
    """

    def __init__(self, token):
        self.token = token

    def sign_request(self, headers):
        if headers is None:
            headers = {}
        headers['Authorization'] = 'Token {0}'.format(self.token)
        headers['Accept'] = 'application/json'
        headers['X-JMS-ORG'] = 'ROOT'
        return headers

    def __bool__(self):
        return self.token != ""
