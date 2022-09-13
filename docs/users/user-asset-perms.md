# **用户授权资产列表**

***

+ **说明**
>资产列表接口

+ **请求url**
>/api/v1/perms/users/{id}/assets/

+ **请求方式**
>Get

***

+ **请求参数**

| 请求参数 | 必选 |   参数类型    |   说明   |
| :------: | :--: | :-----------: | :------: |
|  offset  |      |      int      |  偏移量  |
|  limit   |      |      int      | 每页数量 |
|    id    |  是  | uuid（path）  |  用户id  |
| hostname |      |    string     |  主机名  |
|    ip    |      |    string     |  ip地址  |
|  search  |      |    string     | 模糊搜索 |
|    id    |      | uuid（query） |  资产id  |

+ **请求示例**

~~~ js
https://www.xxxx.com/v1/perms/users/8181cbda-feb5-432a-9dec-037d1ea87db5/assets/?limit=10&offset=0
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
  "count": 12,
  "next": "http://www.xxxx.com/api/v1/perms/users/8181cbda-feb5-432a-9dec-037d1ea87db5/assets/?display=1&draw=1&limit=10&offset=10",
  "previous": null,
  "results": [
    {
      "id": "d5b38e54-5086-481e-8c8e-3f9288965973",
      "hostname": "10.1.12.103",
      "ip": "10.1.12.103",
      "protocols": [
        "ssh/22"
      ],
      "os": null,
      "domain": null,
      "platform": "Linux",
      "comment": "",
      "org_id": "eca4c934-e022-4ed0-a7dd-ceda5662877a",
      "is_active": true,
      "org_name": "jumpServer测试"
    },
    ...
  ]
}
~~~

