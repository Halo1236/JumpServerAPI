import datetime
from typing import List

import requests
import urllib3
from httpsig.requests_auth import HTTPSignatureAuth

urllib3.disable_warnings()

jms_url = 'https://192.168.0.230:8443'
KeyID = '0b1bc13a-5d49-47f2-9048-9d8615aa6893'
SecretID = '29245c33-1445-4c7c-8ff9-884c901b2d79'

s_id = '00000000-0000-0000-0000-000000000002'
s_name = 'Default'
t_id = 'f90d4675-8545-42cd-9e33-db8cbe6d91d6'
t_name = '江北机房'
root_id = '00000000-0000-0000-0000-000000000000'
pagesize = 1000

gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
headers = {
    'Accept': 'application/json',
    'X-JMS-ORG': '',
    'Date': datetime.datetime.utcnow().strftime(gmt_form)
}

signature_headers = ['(request-target)', 'accept', 'date']
auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)

_t_node_map = {}


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
        requests.post(url, auth=auth, headers=headers, json=data, verify=False)


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


def get_assets():
    url = jms_url + '/api/v1/assets/hosts/'
    headers['X-JMS-ORG'] = s_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    return response.json() if isinstance(response.json(), List) else response.json().get('results')


def create_assets(assets):
    url = jms_url + '/api/v1/assets/nodes/'
    headers['X-JMS-ORG'] = t_id
    response = requests.get(url, auth=auth, headers=headers, verify=False)
    nodes = response.json()
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
        requests.post(url, auth=auth, headers=headers, json=_data, verify=False)



def migrate():
    users = get_users()
    invite_user(users)

    groups = get_user_groups()
    create_user_group(groups)

    nodes = get_assets_nodes()
    create_assets_nodes(nodes)

    assets = get_assets()
    create_assets(assets)


if __name__ == '__main__':
    migrate()
