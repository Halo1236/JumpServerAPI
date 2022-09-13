# **资产详情**

***

+ **说明**

>资产详情接口

+ **请求url**

>/api/v1/assets/assets/{id}/

+ **请求方式**

>Get

***

+ **请求参数**

| 请求参数 | 必选 | 参数类型 |  说明  |
| :------: | :--: | :------: | :----: |
|    id    |  是  |   uuid   | 资产id |

+ **请求示例**

~~~ js
https://www.xxxx.com/api/v1/assets/assets/d5b38e54-5086-481e-8c8e-3f9288965973/
~~~

+ **返回参数**

|      返回参数      |   参数类型   |           说明           |
| :----------------: | :----------: | :----------------------: |
|         id         |     uuid     |            id            |
|     admin_user     |     uuid     |        特权用户id        |
| admin_user_display |    string    |       特权用户名称       |
|      hostname      |    string    |          主机名          |
|         ip         |    string    |          ip地址          |
|      platform      |    string    |         系统平台         |
|     protocols      | List<string> | 协议组（例：["ssh/22"]） |
|       domain       |     uuid     |          网域id          |
|   domain_display   |    string    |         网域名称         |
|     public_ip      |    string    |          公网ip          |
|       nodes        |  List<uuid>  |    所属节点id（列表）    |
|   nodes_display    | List<string> |       所属节点名称       |
|    connectivity    |    string    |    可连接性（参考值）    |
|     is_active      |     bool     |         是否激活         |
|    date_created    |     date     |         创建日期         |
|      comment       |    string    |           备注           |
|     created_by     |    string    |          创建者          |
|       labels       |  List<uuid>  |      标签id（列表）      |
|   labels_display   | List<string> |     标签名称（列表）     |
|       org_id       |     uuid     |          组织id          |
|      org_name      |    string    |         组织名称         |

+ **返回示例**

~~~ json
// 正确示例
{
	"id": "d5b38e54-5086-481e-8c8e-3f9288965973",
	"hostname": "10.1.12.103",
	"ip": "10.1.12.103",
	"platform": "Linux",
	"protocols": ["ssh/22"],
	"is_active": true,
	"public_ip": null,
	"number": null,
	"comment": "",
	"vendor": null,
	"model": null,
	"sn": null,
	"cpu_model": null,
	"cpu_count": null,
	"cpu_cores": null,
	"cpu_vcpus": null,
	"memory": null,
	"disk_total": null,
	"disk_info": null,
	"os": null,
	"os_version": null,
	"os_arch": null,
	"hostname_raw": null,
	"cpu_info": "",
	"hardware_info": "",
	"domain": null,
	"admin_user": "d393467b-0af1-41f4-9eff-132eccbc9049",
	"admin_user_display": "李鹏程测试root-特权(root)",
	"nodes": ["b311f2fe-4b99-4427-a5e6-c1ecb6639776"],
	"nodes_display": ["/jumpServer测试/江苏电力k8s 验证"],
	"labels": [],
	"labels_display": [],
	"connectivity": "failed",
	"date_verified": "2022/07/15 20:14:13 +0800",
	"created_by": "李鹏程",
	"date_created": "2022/07/15 20:14:01 +0800",
	"org_id": "eca4c934-e022-4ed0-a7dd-ceda5662877a",
	"org_name": "jumpServer测试"
}
~~~

