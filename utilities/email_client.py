import os
import smtplib
import logging
from email.header import Header
from email import encoders
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

class EmailClient():
    """
        call Example: 
        email = EmailClient(
            os.getenv("SENDER_EMAIL"),
            os.getenv("SENDER_EMAIL_PASS"),
            os.getenv("RECEIVERS_EMAIL")
        )
        email.setSubject("20240315涨停列表")
        email.addContent("请查阅附件。")
        email.addContent("顺颂商祺")
        email.addAttachment("./")
        email.sendMail()
    """
    def __init__(self, sender, password, receivers):
        self.sender     = sender
        self.password   = password
        self.receivers  = receivers

        if self.sender.endswith("outlook.com"):
            self.smtp_host = "smtp-mail.outlook.com"
            self.smtp_port = 587

        # message = MIMEText(content, mtype, 'utf-8')  # 内容, 格式, 编码
        self.message            = MIMEMultipart()
        self.message['From']    = self.sender
        self.message['To']      = self.receivers # receivers可以以英文逗号隔开

        assert self.smtp_host is not None, "smtp_host不能为空"
        assert self.smtp_port is not None, "smtp_port不能为空"
        assert self.password is not None, "password不能为空"
        assert self.sender is not None, "sender不能为空"
        assert self.receivers is not None, "receivers不能为空"

    def sendMail(self):
        try:
            server = None
            # outlook SMTP encryption use STARTTLS
            if self.smtp_host.endswith("outlook.com"):
                server = smtplib.SMTP(self.smtp_host, self.smtp_port)
                server.starttls()
            else:
                server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)  # 启用SSL发信, 端口一般是465
            server.login(self.sender, self.password)  # 登录验证
            server.sendmail(self.sender, self.receivers, self.message.as_string())  # 发送
            return True
        except smtplib.SMTPException:
            logging.error("An error occurred", exc_info=True)
            return False
    
    def setSubject(self, title):
        self.message['Subject'] = title

    def addContent(self, content):
        part = MIMEText(content, 'plain', 'utf-8')
        self.message.attach(part)

    def addHTML(self, content):
        part = MIMEText(content, 'html', 'utf-8')
        self.message.attach(part)

    def addAttachment(self, path):
        basename = os.path.basename(path)
        with open(path, 'rb') as fileHandle:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(fileHandle.read())
        part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename) )
        encoders.encode_base64(part)
        self.message.attach(part)

    def addImage(self, path):
        with open(path,'rb')as fp:
            image = MIMEImage(fp.read())
            #与txt文件设置相似
            image['Content-Type'] = 'application/octet-stream'
            basename = os.path.basename(path)
            image['Content-Disposition'] = 'attachment;filename="%s"' % basename

        self.message.attach(image)

    def formatAddress(self, address):
        """
            # 这样调用可以把 sender 的邮件地址变成 名字
            self.message['From'] = self.formatAddress("名字 <%s>" % self.sender) 
        """
        name, addr = parseaddr(address)
        return formataddr((Header(name, 'utf-8').encode(), addr))
