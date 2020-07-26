import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr




my_sender = 'izhaoostudio@163.com'  # 发件人邮箱账号
my_pass = 'DUKVWBTAZLXGPVZH'  # 发件人邮箱密码

def mail(email):
    ret = ''
    try:
        dir = 'content.html'  # 指定文件目录
        f = open(dir, 'rb')
        mail_body = f.read()
        print(mail_body)
        f.close()
        msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['From'] = formataddr(["izhaoostudio", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["亲", email])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] =datetime.datetime.now().strftime("%Y-%m-%d") + "成功打卡提醒~"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [email, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
