"""
    @Time       :   2020/1/21 14:32
    @Author     :   Jana Hu
    @FileName   :   extract_html_to_mysql.py
    @Software   :   PyCharm
    @Description:
"""
import pymysql

db = pymysql.connect('127.0.0.1', 'root', 'root', 'tecalliance', charset='utf8')
from bs4 import BeautifulSoup
from scrapy import Selector
import json

def save_barnd_data(product_no, brand_name, product_group, oe_num, url):
    cursor = db.cursor()
    sql = 'insert into BERAL (product_no, brand_name, product_group, oe_num, url)\
				values \
        (%s, %s, %s, %s, %s)'
    try:
        cursor.execute(sql, (product_no, brand_name, product_group, oe_num, url))
        db.commit()
    except Exception as err:
        db.rollback()
        print(err.args)

def get_html_page(page):
    # 产品编号
    xpath_product_no = '//div[@class="basic-info"]//h2[@class="article-number"]//a/text()'
    # 产品名称
    xpath_product_name = '//div[@class="basic-info"]//h2[@class="brand-name"]//text()'
    # 产品描述
    xpath_product_desc = '//div[@class="basic-info"]//span[@class="additionalDescription"]//text()'
    # 备选URL
    xpath_url = '//div[@class="basic-info"]//h2[@class="article-number"]//a/@href'
    url_head = 'https://www.tecalliance.cn/cn'

    # 注意 html 文件名
    with open('html_BERAL/{}.html'.format(page), 'r', encoding='utf8') as f:
        ls = f.read()
    # 处理 非 OE 数据
    mselector = Selector(text=ls)
    product_no = mselector.xpath(xpath_product_no).extract()
    product_name = mselector.xpath(xpath_product_name).extract()
    product_desc = mselector.xpath(xpath_product_desc).extract()
    url = mselector.xpath(xpath_url).extract()

    # 处理OE号
    json_oe = '-'
    soup = BeautifulSoup(ls, 'lxml')
    soup = soup.select('div[class="oens h-hidden"]')
    # div[class="part-detail-item-body"]
    # div[class="part-detail-item part-detail-oe-number"]
    for leng in range(len(soup)):
        product_no_ = product_no[leng].strip()
        product_name_ = product_name[leng].strip()
        product_desc_ = product_desc[leng].strip()
        url_ = url_head + url[leng][2:]
        sou = soup[leng].select('div[class="part-detail-item part-detail-oe-number"]')
        if len(sou) == 0:
            # OE 号 为 无 的情况
            save_barnd_data(product_no_, product_name_, product_desc_, '-', url_)
            print(json_oe)
        else:
            json_oe = {}
            sou = sou[0].select('div[class="part-detail-item-body"]')[0]
            span = sou.select('p span')
            ul = sou.select('ul')
            for s, u in zip(span, ul):
                brand_name = s.get_text()
                lies = u.select('li')
                # print(brand_name)
                oes = []
                for li in lies:
                    oe = li.get_text().strip()
                    oes.append(oe)
                # print(brand_name, oes)
                json_oe[brand_name] = oes
            # print(json_oe)
            save_barnd_data(product_no_, product_name_, product_desc_, json.dumps(json_oe, ensure_ascii=False), url_)
# 修改
for i in range(1, 91):
    get_html_page(i)

print("结束")
db.close()
