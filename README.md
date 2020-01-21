# TaiAnLian



#### 项目描述

采集泰案联品牌数据

#### **v1.0**

 https://www.tecalliance.cn/cn 



#### 账号注册

<u>注意：不需要填写的字段请不要填写</u>

需求：

##### 		1.点击品牌

![](.\img\01.jpg)

##### 		2.以 "BERAL "为例

![](.\img\02.jpg)

##### 		3.需采集字段(v1.0)

![](.\img\03.jpg)

##### 		4.需采集字段(v2.0)

​		[待更新]

#### 数据库语句

```mysql
CREATE TABLE IF NOT EXISTS BERAL(
    product_no VARCHAR(30) DEFAULT NULL COMMENT '产品编号',
    brand_name VARCHAR(30) DEFAULT NULL COMMENT '品牌名',
    product_group VARCHAR(30) DEFAULT NULL COMMENT '产品组(产品名)',
    oe_num TEXT DEFAULT NULL COMMENT 'OE号',
    url VARCHAR(100) DEFAULT NULL COMMENT '详情页地址(校验备用)'
) ENGINE=INNODB DEFAULT CHARSET=utf8;
```



#### 代码思路

##### 		1.创建Mysql数据库

##### 		2.创建Redis数据库

​		作用：保证所有网页全部采集完成

​		***create_redis.py***

##### 		3.下载网页的代码

​		***down_html.py***

##### 		4.调用下载网页包，下载网页至本地

​		***crawl_to_local_html.py***

##### 		5.提取本地网页数据至本地数据库

​		***extract_html_to_mysql.py***



#### 日志

| 日志                                                 | 更新人   | 更新时间  |
| :--------------------------------------------------- | -------- | --------- |
| 提交功能代码，<br />实现v1.0的代码<br />需要整合代码 | **Jana** | 2020.1.21 |
|                                                      |          |           |
|                                                      |          |           |



#### 版本需求日志

| 版本号 | 详细信息                     | 更新人   | 更新时间  |
| ------ | ---------------------------- | -------- | --------- |
| V1.0   | 实现v1.0功能<br />分模块整合代码 | **Jana** | 2020.1.21 |
| v2.0   |                              |          |           |
| v3.0   |                              |          |           |

