import requests
from lxml import etree



headers = {
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Referer': 'https://www.google.com.hk/',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'zh-CN,zh;q=0.9',
          'cookie': 'openState=false; UM_distinctid=1627052fd32c62-0153f8cfac08b8-3a614f0b-144000-1627052fd3348f; CNZZDATA1272080165=773347913-1522299211-https%253A%252F%252Fwww.baibianip.com%252F%7C1522299211'
           }
def test(headers):
    url = 'http://www.ip3366.net/free/?page=5'
    data = requests.get(url,headers = headers)
    html = etree.HTML(data.text)
    # print(data.text)
    ip_data_list = html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    print(ip_data_list)
    for tr in ip_data_list:
        print(':'.join(tr.xpath('td/text()')[0:2]))
        # yield ':'.join(tr.xpath('td/text()')[0:2])

print(test(headers))