"""
    @Time       :   2020/1/21 13:55
    @Author     :   Jana Hu
    @FileName   :   down_html.py
    @Software   :   PyCharm
    @Description:
                    下载网页
"""
import requests
import re

class DownHtml(object):

    def __init__(self, url, path):
        self.headers = self.get_headers()
        self.url = url
        self.path = path
        self.html_name = self.get_html_name()

    def get_headers(self):
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 此处cookie需要修改
            'Cookie': 'Hm_lvt_83df31d49b864f0ebcac80b58631bda1=1579396912,1579484854,1579502178,1579581824; _pk_ref.5.fb23=%5B%22%22%2C%22%22%2C1579581824%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2wijP-_PHbVVpcJD7PCRY7b25bx0rdJEIEjlnflYFIMlxO_FzhqRmYOlrPTFJxON%26wd%3D%26eqid%3D8fa129d60016754b000000045e268179%22%5D; _pk_id.5.fb23=cee5aa2395e322cb.1579325884.9.1579584615.1579581824.; Hm_lpvt_83df31d49b864f0ebcac80b58631bda1=1579584615; ci_session=oh68hq2ahoa7lnqumrufavhec26p4j5m',
            'Host': 'www.tecalliance.cn',
            # 此处Referer,切换品牌时需要修改
            'Referer': 'https://www.tecalliance.cn/cn/search/90?lbid=264',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

    def get_html_name(self):
        # return self.url.split('/')[-1].replace('?', '')
        return re.findall(r'search/(.*?)?lbid', self.url)[0].replace('?', '')

    def req_ser(self):
        """
        请求服务器
        :return:
        """
        return requests.get(self.url, headers=self.headers, timeout=5)

    def save_html(self):
        try:
            temp = self.req_ser()
            response = temp.text
            if response.__contains__("验证码"):
                raise Exception("出现验证码")
            with open(r'{}/{}.html'.format(self.path, self.html_name), 'w', encoding='utf-8') as f:
                f.write(response)
        except Exception as err:
            raise err
