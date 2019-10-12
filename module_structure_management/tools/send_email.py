# -*-coding:utf-8 -*-
# File :send_email.py
# Author:George
# Date : 2019/10/12
# motto: Someone always give up while someone always try!
"""
    Simple mail sender
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def send_email_163():
    """
    Simple mail sender
    send to one  and to many
    :return:
    """
    # basic info
    smtpServer = "smtp.163.com"
    account = "onebigbera@163.com"
    password = "george9527"

    # sender and receiver
    sender = "onebigbera@163.com"
    # send to one
    # receiver = "onebigbera@163.com"

    # send to many receiver 1
    receivers = ["onebigbera@163.com", "2578288992@qq.com", "george@126.com"]

    # content
    subject = "Web Selenium Test Report"
    # stringify html
    content = "<html><h4 style='color:red'>Let change happen</h4></html>"

    # content load
    msg = MIMEText(content, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    # send to one
    # msg['To'] = receiver

    # send to many use,join() to connect many receives 2
    msg['To'] = ','.join(receivers)

    # set port and SSL service
    smtp = smtplib.SMTP_SSL(smtpServer, 465)

    # init service connect identify user
    smtp.helo(smtpServer)

    # return response
    smtp.ehlo(smtpServer)

    # simulate user login
    smtp.login(account, password)

    print("Begin to send the email>>>")
    # send email
    # send one
    # smtp.sendmail(sender, receiver, msg.as_string())

    # to send to many people  here to cut them off  3
    smtp.sendmail(sender, msg['To'].split(','), msg.as_string())
    smtp.sendmail(sender, receivers, msg.as_string())

    print("Finish send...")


def send_email_with_attachment():
    """
    send email with attachment
    :return:
    """
    # basic info
    smtpServer = "smtp.163.com"
    account = "onebigbera@163.com"
    password = "george9527"
    sender = "onebigbera@163.com"
    receiver = "2578288992@qq.com"

    # instantiation an mail object
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    content = "<html><h4 style='color:red'>亲爱的小心有熊出没:</br>爱可能会迟到，但永远不会缺席！</br></h4><p><span>下面为测试报告，请查看！</span></p></html>"
    subject = '寒冷的季节，温暖的是人心 ^_^ !'
    message["Subject"] = Header(subject, 'utf-8')

    # attach the content
    message.attach(MIMEText(content, 'html', 'utf-8'))

    # instantiation attachment object
    html_path = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\module_structure_management\test_report\2019-10-12_11_21_57result.html'
    # get attachment stream
    attachment_1 = MIMEText(open(html_path).read(), 'base64', 'utf-8')

    # set property
    attachment_1['Content-Type'] = 'application/octet-stream'
    attachment_1['Content-Disposition'] = 'attachment; filename="report.html"'

    message.attach(attachment_1)

    att2 = MIMEText(open(
        r'F:\Testing_Development\UnittestProjects\UnittestBasic\51zxw_selenium_example\emailSender\attachment\test1.jpg',
        'rb').read(), 'base64', 'utf-8')
    # set attachment
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="test1.jpg"'
    message.attach(att2)

    # txt file
    att3 = MIMEText(open(
        r'F:\Testing_Development\UnittestProjects\UnittestBasic\51zxw_selenium_example\emailSender\attachment\test.txt',
        'rb').read(), 'base64', 'utf-8')
    # attachment setting
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att3)

    smtp = smtplib.SMTP_SSL(smtpServer, 465)
    try:
        smtp.helo(smtpServer)
        smtp.ehlo(smtpServer)
        smtp.login(account, password)
    except BaseException as e:
        print(e)

    try:
        print("Begin to send >>>")
        smtp.sendmail(sender, receiver, message.as_string())
        print("Send finished...")
    except BaseException as e:
        print(e)


def send_report(file_path):
    """
    send the file
    :param file_path:
    :return:
    """
    # basic info
    smtpServer = "smtp.163.com"
    account = "onebigbera@163.com"
    password = "george9527"
    sender = "onebigbera@163.com"
    receiver = "2578288992@qq.com"

    # instantiation an mail object
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver

    content = "<html><h4 style='color:red'>亲爱的小心有熊出没:</br>爱可能会迟到，但永远不会缺席！</br></h4><p><span>下面为测试报告，请查看！</span></p></html>"
    subject = 'Test Report'
    message["Subject"] = Header(subject, 'utf-8')

    # attach the content
    message.attach(MIMEText(content, 'html', 'utf-8'))
    report_path = file_path
    attachment_1 = MIMEText(open(report_path).read(), 'base64', 'utf-8')

    # set property
    attachment_1['Content-Type'] = 'application/octet-stream'
    attachment_1['Content-Disposition'] = 'attachment; filename="report.html"'

    message.attach(attachment_1)

    smtp = smtplib.SMTP_SSL(smtpServer, 465)
    try:
        smtp.helo(smtpServer)
        smtp.ehlo(smtpServer)
        smtp.login(account, password)
    except BaseException as e:
        print(e)

    try:
        print("Begin to send >>>")
        smtp.sendmail(sender, receiver, message.as_string())
        print("Send finished...")
    except BaseException as e:
        print(e)


if __name__ == "__main__":
    # send_email_163()
    # send_email_with_attachment()
    file_path = r'F:\Testing_Development\UnittestProjects\automated_testing\automated_testing\module_structure_management\test_report\2019-10-12_11_21_57result.html'
    send_report(file_path)






