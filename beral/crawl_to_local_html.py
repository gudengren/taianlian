"""
    @Time       :   2020/1/21 13:40
    @Author     :   Jana Hu
    @FileName   :   crawl_to_local_html.py
    @Software   :   PyCharm
    @Description:
                    下载网页至本地
"""

import os
from redis import StrictRedis
import time
r = StrictRedis(db=10, decode_responses=True)
from multiprocessing.dummy import Pool
from beral.down_html import DownHtml


brand = input("请输入品牌：[严格注意大小写:此处写大写],举例：(BERAL)\n")
# 存放html的路径
path = 'html_{}'.format(brand)

# 存放路径没有则建立
if not os.path.exists(path):
    os.mkdir(path)

# 拼接未采集的url
urls = []
# redis的表
redis_table = "{}_url_index".format(brand)
keys = r.hkeys(redis_table)
for key in keys:
    value = r.hmget(redis_table, key)[0]
    # 未采集为 0
    # 采集中   1
    # 采集成功 200
    # 采集失败 4
    if value == str(4):
        urls.append(key)

# 多进程运行
def run(url):
    try:
        r.hmset(redis_table, {url: 1})
        time.sleep(0.3)
        # 下载Html至本地的自定义包
        # 使用本自定义包需要修改里面的cookie,Referer
        DownHtml(url, path).save_html()
        r.hmset(redis_table, {url: 200})
    except Exception as err:
        r.hmset(redis_table, {url: 4})
        # 当显示出现验证码时，刷新浏览器网页，填写验证码
        # 20s内操作完成
        print(err.args, "睡眠20s...")
        time.sleep(20)

pool = Pool(3)
pool.map(run, urls)
pool.close()
pool.join()
