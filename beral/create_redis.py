"""
    @Time       :   2020/1/21 13:34
    @Author     :   Jana Hu
    @FileName   :   create_redis.py
    @Software   :   PyCharm
    @Description:
                    创建redis数据库
"""
from redis import StrictRedis
# 采用db10
r = StrictRedis(db=10, decode_responses=True)

BERAL_url = 'https://www.tecalliance.cn/cn/search/{}?lbid=264'

# 该处 91 是品牌数据有90个网页而确定
# 不同品牌对应的数值需自己查看
for i in range(1, 91):
    r.hmset('BERAL_url_index', {BERAL_url.format(i): 0})
