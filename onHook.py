# coding=UTF-8
import os

import requests
import urllib3
import time
import re
from lxml import etree

def login():
    try:
        session = requests.Session()
        resp = session.post(login_url, data, verify=False,headers=headers)
    except BaseException as e:
        print(e)
        session.close()
        print("login exception " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return session,False
    else:
        print(resp.content.decode('utf-8'))
        pattern = r"欢迎您回来"
        m = re.search(pattern, resp.content.decode('utf-8'))
        if m.start() > 0:
            print("login_success at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return session,True


if __name__ == '__main__':
    name = os.getenv('NAME', 'default_name')
    password = os.getenv('PASSWORD', 'default_password')
    # 不打印warning
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # 登录时需要POST的数据
    data = {'username': name,
            'password': password,
            'loginfield':'username',
            'refer':'https://bbs.uestc.edu.cn/'}
    # 设置请求头
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    # 登录时表单提交到的地址
    login_url = 'https://bbs.uestc.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcBaK&inajax=1'
    url = 'http://bbs.uestc.edu.cn/forum.php?mod=forumdisplay&fid=174'




    success=False
    while not success:
        session, success = login()

    while True:
        try:
            resp = session.get(url)
        except BaseException as e:
            success = False
            print(e)
            session.close()
            print("Connection disconnected at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("Reconnecting...")
            while not success:
                time.sleep(300)
                session, success = login()

        else:

            html = etree.HTML(resp.content)
            messagetext = html.xpath('//div[@id="messagetext"]/p/text()')
            if messagetext and messagetext[0][0:2] == "抱歉":
                print("Connection disconnected at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                print("Reconnecting...")
                session = login()
                time.sleep(240)  # 防止出现验证码
            else:
                print("login continue at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            time.sleep(45)
