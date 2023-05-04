# **资产列表**

***

+ **说明**

>资产列表接口

+ **请求url**

>/api/v1/assets/assets/

+ **请求方式**

>Get

***

+ **请求参数**

| 请求参数  | 必选 | 参数类型 |         说明         |
| :-------: | :--: | :------: | :------------------: |
|  offset   |      |   int    |        偏移量        |
|   limit   |      |   int    |       每页数量       |
| hostname  |      |  string  |        主机名        |
|    ip     |      |  string  |        ip地址        |
| protocols |      |  string  | 协议组（例：ssh/22） |
| is_active |      |   bool   |       是否激活       |
|  search   |      |  string  |       模糊搜索       |

+ **请求示例**

~~~ js
https://www.xxxx.com/api/v1/assets/assets/?offset=0&limit=100
~~~

+ **返回参数**

| 返回参数 |  参数类型   |              说明              |
| :------: | :---------: | :----------------------------: |
|  count   |     int     |           列表总数量           |
|   next   |   string    |           下一页连接           |
| previous |   string    |           上一页连接           |
| results  | List<Asset> | 资产数据（字段说明见资产详情） |

+ **返回示例**

~~~ json
// 正确示例
{
  "count": 14,
  "next": "http://www.xxxx.com/api/v1/assets/assets/?limit=10&offset=10",
  "previous": null,
  "results": [
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
        }, 
        ...
    ]
}
~~~

