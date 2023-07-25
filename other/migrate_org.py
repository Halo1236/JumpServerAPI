import datetime
from typing import List
from urllib.parse import quote

import requests
import urllib3
from httpsig.requests_auth import HTTPSignatureAuth

urllib3.disable_warnings()

jms_url = 'https://blj.nauvpn.cn'
KeyID = '6c51d8c4-9eca-44a8-8b56-d4a8165fb9a8'
SecretID = '6ad81e24-494a-4efd-983b-4b41fdca26ef'

s_id = '450c15f8-a9dd-4064-945b-5eeb39a83659'
s_name = '实验教学'
t_id = '00000000-0000-0000-0000-000000000002'
t_name = '数据中心'

#################################################################
gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
headers = {
    'Accept': 'application/json',
    'X-JMS-ORG': '',
    'Date': datetime.datetime.utcnow().strftime(gmt_form)
}

signature_headers = ['(request-target)', 'accept', 'date']
auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
_t_groups_map = {}
_t_node_map = {}
_s_old_node_map = {}
_t_asset_map = {}


def get_users():
    url = jms_url + '/api/v1/users/users/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    return response.json() if isinstance(response.json(), List) else response.json().get('results')


def invite_user(users):
    url = jms_url + '/api/v1/users/users/invite/'
    headers['X-JMS-ORG'] = t_id
    for user in users:
        data = {'users': user['id'], 'org_roles': [org_role['id'] for org_role in user['org_roles']]}
        requests.post(url, auth=auth, headers=headers, data=data, verify=False)


def get_user_groups():
    url = jms_url + '/api/v1/users/groups/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    return response.json() if isinstance(response.json(), List) else response.json().get('results')


def create_user_group(groups):
    url = jms_url + '/api/v1/users/groups/'
    headers['X-JMS-ORG'] = t_id
    for group in groups:
        users_lst = []
        for user in group['users']:
            users_lst.append({'pk': user['id']})
        data = {'name': group['name'], 'users': users_lst}
        response = requests.post(url, auth=auth, headers=headers, json=data, verify=False)
        if response.json().get('id'):
            _t_groups_map[response.json().get('name')] = response.json().get('id', '')


def get_assets_nodes():
    url = jms_url + '/api/v1/assets/nodes/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    return response.json() if isinstance(response.json(), List) else response.json().get('results')


def create_assets_nodes(nodes):
    url = jms_url + '/api/v1/assets/nodes/'
    headers['X-JMS-ORG'] = t_id
    for node in nodes:
        new_value = node['full_value'].split('/')
        if len(new_value) < 3:
            continue
        data = {'full_value': '/%s/%s' % (t_name, '/'.join(new_value[2:]))}
        response = requests.post(url, auth=auth, headers=headers, json=data, verify=False)
        _t_node_map[node['full_value']] = response.json().get('id', '')
        _s_old_node_map[node['id']] = node['full_value']


def get_assets():
    url = jms_url + '/api/v1/assets/hosts/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    return response.json() if isinstance(response.json(), List) else response.json().get('results')


def get_single_asset(asset_name):
    url = jms_url + '/api/v1/assets/assets/?asset=&node=&name=' + quote(asset_name)
    headers['X-JMS-ORG'] = t_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    return response.json() if isinstance(response.json(), List) else response.json().get('results')


def create_assets(assets):
    url = jms_url + '/api/v1/assets/nodes/?limit=1'
    headers['X-JMS-ORG'] = t_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    nodes = response.json() if isinstance(response.json(), List) else response.json().get('results')
    _t_root_node_id = nodes[0].get('id')

    url = jms_url + '/api/v1/assets/hosts/'
    headers['X-JMS-ORG'] = t_id
    for asset in assets:
        node_ids = []
        for i in asset.get('nodes_display', []):
            node_ids.append(_t_node_map.get(i, _t_root_node_id))
        _data = {'name': asset['name'], 'address': asset['address'], 'comment': asset['comment'],
                 'platform': {'pk': asset['platform'].get('id')}, 'protocols': asset['protocols'], 'nodes': node_ids,
                 'is_active': True}
        response = requests.post(url, auth=auth, headers=headers, json=_data, verify=False)
        if response.json().get('id'):
            _t_asset_map[response.json().get('name')] = response.json().get('id', '')


def migrate_accounts():
    url = jms_url + '/api/v1/accounts/accounts/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    accounts = response.json() if isinstance(response.json(), List) else response.json().get('results')
    for account in accounts:
        url = jms_url + f'/api/v1/accounts/account-secrets/{account["id"]}/'
        headers['X-JMS-ORG'] = s_id
        response = requests.get(url, auth=auth, headers=headers, verify=False)
        sa = response.json()

        _assets_id = _t_asset_map.get(sa['asset'].get('name'))
        _data = {
            "privileged": sa['privileged'],
            "secret_type": sa['secret_type'],
            "push_now": False,
            "on_invalid": "error",
            "is_active": True,
            "assets": [_assets_id],
            "name": sa['name'],
            "secret": sa['secret'],
            "username": sa['username']
        }
        if sa['secret_type'].get('value') == 'ssh_key':
            _data["ssh_key"] = sa['secret']
        else:
            _data["password"] = sa['secret']
        _data['secret'] = sa['secret']
        url = jms_url + '/api/v1/accounts/accounts/bulk/'
        headers['X-JMS-ORG'] = t_id
        requests.post(url, auth=auth, headers=headers, json=_data, verify=False)


def migrate_permissions():
    # if not _t_groups_map or not _t_asset_map or not _t_node_map:
    #     return

    url = jms_url + '/api/v1/users/groups/'
    headers['X-JMS-ORG'] = t_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    groups = response.json() if isinstance(response.json(), List) else response.json().get('results')
    for g in groups:
        _t_groups_map[g.get('name')] = g.get('id', '')

    url = jms_url + '/api/v1/assets/nodes/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    nodes = response.json() if isinstance(response.json(), List) else response.json().get('results')
    for n in nodes:
        _s_old_node_map[n['id']] = n.get('full_value', '')

    url = jms_url + '/api/v1/assets/nodes/'
    headers['X-JMS-ORG'] = t_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    nodes = response.json() if isinstance(response.json(), List) else response.json().get('results')
    _t_root_node_id = nodes[0].get('id')
    for n in nodes:
        _t_node_map[n['full_value']] = n.get('id', '')

    url = jms_url + '/api/v1/assets/assets/'
    headers['X-JMS-ORG'] = t_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    assets = response.json() if isinstance(response.json(), List) else response.json().get('results')
    for a in assets:
        _t_asset_map[a.get('name')] = a.get('id', '')

    url = jms_url + '/api/v1/perms/asset-permissions/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    permissions = response.json()
    for permission in permissions:
        _node_ids = []
        for n in permission['nodes']:
            _old_full_value = _s_old_node_map.get(n['id'])
            new_value = _old_full_value.split('/')
            if len(new_value) < 3:
                _node_ids.append({'pk': _t_root_node_id})
                continue
            _node_ids.append({'pk': _t_node_map.get(_old_full_value, _t_root_node_id)})
        _data = {
            "assets": [_t_asset_map.get(a['name']) for a in permission['assets']],
            "nodes": _node_ids,
            "accounts": permission['accounts'],
            "actions": ["connect", "upload", "download", "copy", "paste"],
            "is_active": permission['is_active'],
            "date_start": permission['date_start'],
            "date_expired": permission['date_expired'],
            "name": permission['name'],
            "users": [{"pk": u['id']} for u in permission['users']],
            "user_groups": [{"pk": _t_groups_map.get(g['name'])} for g in permission['user_groups']]
        }
        print(_data)
        headers['X-JMS-ORG'] = t_id
        s = requests.post(url, auth=auth, headers=headers, json=_data, verify=False)
        print(s.json())


def migrate():
    print('*' * 20 + '开始迁移用户' + '*' * 20)
    #users = get_users()
    #invite_user(users)
    print('*' * 20 + '迁移用户已完成' + '*' * 20)
    print('*' * 50)
    print('*' * 20 + '开始迁移用户组' + '*' * 20)
    #groups = get_user_groups()
    #create_user_group(groups)
    print('*' * 20 + '迁移用户组已完成' + '*' * 20)
    print('*' * 50)
    print('*' * 20 + '开始迁移资产节点' + '*' * 20)
    #nodes = get_assets_nodes()
    #create_assets_nodes(nodes)
    print('*' * 20 + '迁移资产节点已完成' + '*' * 20)
    print('*' * 50)
    print('*' * 20 + '开始迁移资产' + '*' * 20)
    #assets = get_assets()
    #create_assets(assets)
    print('*' * 20 + '迁移资产节点已完成' + '*' * 20)
    print('*' * 50)
    print('*' * 20 + '开始迁移资产账号' + '*' * 20)
    #migrate_accounts()
    print('*' * 20 + '迁移资产账号已完成' + '*' * 20)
    print('*' * 50)
    print('*' * 20 + '开始迁移资产授权' + '*' * 20)
    migrate_permissions()
    print('*' * 20 + '迁移资产授权已完成' + '*' * 20)


if __name__ == '__main__':
    migrate()
