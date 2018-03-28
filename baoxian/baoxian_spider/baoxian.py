import requests
import pytesseract
from PIL import Image
import time


'''平安寿险测试'''

def get_cookie():

    url = 'http://property.pingan.com/property_insurance/pa18AutoInquiry/validatePolicy/guaran_check2.jsp?actionType=1&policyNo=10127003900409594150&validateNo=vPVX8b56vtv8ZgT97H'

    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Cache-Control':'max-age=0',
               'Host':'property.pingan.com',
               'Proxy-Connection':'keep-alive',
               'Upgrade-Insecure-Requests':'1',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    data = requests.get(url,headers = headers)
    cookie = data.headers['Set-Cookie']
    fin_cookie = cookie.replace('; path=/', '').replace('HttpOnly, ', '')
    print(fin_cookie)

    return fin_cookie

'''得到验证码'''

def get_verify_code(fin_cookie):


        verify_code_url = 'http://property.pingan.com/property_insurance/pa18AutoInquiry/rand.do'

        verify_headers = {'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
                           'Accept-Encoding':'gzip, deflate',
                           'Accept-Language':'zh-CN,zh;q=0.9',
                           'Host':'property.pingan.com',
                           'Proxy-Connection':'keep-alive',
                           'Referer':'http://property.pingan.com/property_insurance/pa18AutoInquiry/validatePolicy/guaran_check2.jsp?actionType=1&policyNo=10127003900409594150&validateNo=vPVX8b56vtv8ZgT97H',
                           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                           'Cookie':'%s' % fin_cookie
                          }

        pic_data = requests.get(verify_code_url,headers = verify_headers)
        pic_info = pic_data.content

        file_name = 'data' +'.jpg '

        with open(file_name, 'wb') as file:
            file.write(pic_data.content)

        image = Image.open('data.jpg')
        code = pytesseract.image_to_string(image)
        print(code)

        return code


'''测试能否行得通'''

def test_code (fin_cookie,code):

    # verify_code = input('请输入验证码:', )

    post_url = 'http://property.pingan.com/property_insurance/pa18AutoInquiry/validatePolicy/validatePolicy.do?action=validateInfoAsh'

    verify_code_test_headers = {    'Host': 'property.pingan.com',
                                    'Proxy-Connection': 'keep-alive',
                                    'Content-Length': '122',
                                    'Cache-Control': 'max-age=0',
                                    'Origin': 'http://property.pingan.com',
                                    'Upgrade-Insecure-Requests': '1',
                                    'Content-Type': 'application/x-www-form-urlencoded',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                    'Referer': 'http://property.pingan.com/property_insurance/pa18AutoInquiry/validatePolicy/guaran_check2.jsp?actionType=1&policyNo=10127003900409594150&validateNo=vPVX8b56vtv8ZgT97H',
                                    'Accept-Encoding': 'gzip, deflate',
                                    'Accept-Language': 'zh-CN,zh;q=0.9',
                                    'Cookie': '%s' % fin_cookie
                                    }

    post_info = 'inputType=0&inputType_2=4.0&policyNo=10127003900409594150&appCertNo=&certNo=&validateNo=vPVX8b56vtv8ZgT97H&verifyCode=%s' % code

    tested_data = requests.post(post_url, post_info, headers=verify_code_test_headers)
    print(tested_data.text)

    return tested_data.text

if __name__ == '__main__':

    def main():

        fin_cookie = get_cookie()
        time.sleep(1)

        code = get_verify_code(fin_cookie)
        time.sleep(1)

        test_code(fin_cookie, code)


    main()
