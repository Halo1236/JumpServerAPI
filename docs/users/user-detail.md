# **用户详情**

***

+ **说明**
>用户详情接口

+ **请求url**
>/api/v1/users/users/{id}/

+ **请求方式**
>Get

***

+ **请求参数**

| 请求参数 | 必选 | 参数类型 |  说明  |
| :------: | :--: | :------: | :----: |
|    id    |  是  |   uuid   | 用户id |

+ **请求示例**

~~~ js
https://www.xxxx.com/api/v1/users/users/db6fd20e-734d-44a4-9bdd-623cb174d6a4/
~~~

+ **返回参数**

|          返回参数          |   参数类型   |                         说明                          |
| :------------------------: | :----------: | :---------------------------------------------------: |
|             id             |     uuid     |                          id                           |
|            name            |    string    |                         名称                          |
|          username          |    string    |                        用户名                         |
|           email            |    string    |                         邮箱                          |
|           wechat           |    string    |                        微信id                         |
|           phone            |    string    |                        手机号                         |
|         mfa_level          |     int      |          MFA等级（0:禁用 1:启用 2:强制启用）          |
|           source           |    string    | 用户来源（local,ldap,openid,cas,saml2,oauth2,radius） |
|       source_display       |    string    |                     用户来源名称                      |
|    need_update_password    |     bool     |                  下次登录需修改密码                   |
|        mfa_enabled         |     bool     |                      MFA是否开启                      |
|          is_valid          |     bool     |                       是否有效                        |
|         is_expired         |     bool     |                       是否过期                        |
|         is_active          |     bool     |                       是否激活                        |
|        date_expired        |     date     |                       过期日期                        |
|        date_joined         |     date     |                       创建日期                        |
|         last_login         |     date     |                     最近登录日期                      |
|         created_by         |    string    |                        创建者                         |
|  is_otp_secret_key_bound   |     bool     |                  otp软件密钥是否绑定                  |
|     mfa_force_enabled      |     bool     |                    MFA是否强制开启                    |
|     mfa_level_display      |    string    |                      MFA等级名称                      |
|       is_first_login       |     bool     |                    是否第一次登录                     |
| date_password_last_updated |     date     |                   最近修改密码时间                    |
|           groups           |  List<uuid>  |                 所属用户组id（列表）                  |
|       groups_display       | List<string> |                所属用户组名称（列表）                 |
|        system_roles        |  List<uuid>  |                  系统角色id（列表）                   |
|    system_roles_display    |    string    |                     系统角色名称                      |
|         org_roles          |  List<uuid>  |                  组织角色id（列表）                   |
|     org_roles_display      |    string    |                     组织角色名称                      |
|       login_blocked        |     bool     |                      是否被锁定                       |

+ **返回示例**

~~~ json
// 正确示例
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
	"created_by": "李鹏程",
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
	"system_roles": ["00000000-0000-0000-0000-000000000003"],
	"org_roles": ["6bd22c74-f38d-4a61-8823-0146fb2799fc"],
	"system_roles_display": "用户",
	"org_roles_display": "test",
	"login_blocked": false
}
~~~

