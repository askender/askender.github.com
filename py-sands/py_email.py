# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib
from email.mime.text import MIMEText
mailto_list = ['527639661@qq.com']
mail_host = "smtp.gmail.com"  # 设置服务器
mail_user = "askender43"  # 用户名
mail_pass = "26129581dnqbGG#"  # 口令
mail_postfix = "gmail.com"  # 发件箱的后缀


def send_mail(to_list, sub, content):
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='UTF-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # ("smtp.gmail.com",465)
        server.starttls()
        server.ehlo()
        # Pretend the SMTP server supports some forms of authentication.
        server.esmtp_features['auth'] = 'LOGIN DIGEST-MD5 PLAIN'
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "hello world！"):
        print "发送成功"
    else:
        print "发送失败 1"
