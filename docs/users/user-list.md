# **用户列表**

***

+ **说明**
>用户列表接口

+ **请求url**
>/api/v1/users/users/

+ **请求方式**
>Get

***
+ **请求参数**

| 请求参数  | 必选 | 参数类型 |   说明   |
| :-------: | :--------: | :------: | :------: |
|  offset   |      |   int    |  偏移量  |
|   limit   |      |   int    | 每页数量 |
| username  |      |  string  |  用户名  |
|   email   |      |  string  |   邮箱   |
|   name    |      |  string  |   名称   |
|  source   |      |  string  |   来源   |
| is_active |      |  string  | 是否激活 |
|  search   |      |  string  | 模糊搜索 |

+ **请求示例**
~~~ js
https://www.xxxx.com/api/v1/users/users/?offset=0&limit=100
~~~

+ **返回参数**

| 返回参数 |  参数类型  |              说明              |
| :------: | :--------: | :----------------------------: |
|  count   |    int     |           列表总数量           |
|   next   |   string   |           下一页连接           |
| previous |   string   |           上一页连接           |
| results  | List<User> | 用户数据（字段说明见用户详情） |
+ **返回示例**
~~~ json
// 正确示例
{
  "count": 13,
  "next": "http://www.xxxx.com/api/v1/users/users/?limit=10&offset=10",
  "previous": null,
  "results": [
    {
      "id": "db6fd20e-734d-44a4-9bdd-623cb174d6a4",
      "name": "bes",
      "username": "bes",
      "email": "bes@qq.com",
      "wechat": "",
      "phone": null,
      "mfa_level": 0,
      "source": "local",
      "source_display": "数据库",
      "can_public_key_auth": true,
      "need_update_password": false,
      "mfa_enabled": false,
      "is_service_account": false,
      "is_valid": true,
      "is_expired": false,
      "is_active": true,
      "date_expired": "2092/07/28 16:10:53 +0800",
      "date_joined": "2022/08/15 16:12:26 +0800",
      "last_login": "2022/08/27 18:19:12 +0800",
      "created_by": "admin",
      "comment": null,
      "is_wecom_bound": false,
      "is_dingtalk_bound": false,
      "is_feishu_bound": false,
      "is_otp_secret_key_bound": false,
      "wecom_id": null,
      "dingtalk_id": null,
      "feishu_id": null,
      "mfa_level_display": "禁用",
      "mfa_force_enabled": false,
      "is_first_login": false,
      "date_password_last_updated": "2022/08/27 18:10:46 +0800",
      "avatar_url": "/static/img/avatar/user.png",
      "groups": [],
      "groups_display": "",
      "system_roles": [
        "00000000-0000-0000-0000-000000000003"
      ],
      "org_roles": [
        "6bd22c74-f38d-4a61-8823-0146fb2799fc"
      ],
      "system_roles_display": "用户",
      "org_roles_display": "test",
      "login_blocked": false
    },
    ...
  ]
}
~~~

