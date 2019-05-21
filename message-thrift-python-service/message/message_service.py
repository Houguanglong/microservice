#coding=utf-8
from api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'james_houguang@163.com'
authcode = 'hgl123'
class MessageServiceHandler:
    def sendMobileMessage(self, mobile, message):
        print "sendMobileMessage,mobile"+mobile+"message:"+message
        return True

    def sendEmailMessage(self, email, message):
        print "sendEmailMessage,email:"+email+"message:"+message
        messageOjb = MIMEText(message,"plain","utf-8")
        #发送者
        messageOjb['From'] = sender
        #接收者
        messageOjb['to'] = email
        #邮件主题
        messageOjb['Subject'] = Header('houguang_test','utf-8')
        try:
            smtpObj = smtplib.SMTP('smtp.163.com') #使用163邮箱
            smtpObj.login(sender,authcode)  #登陆邮箱
            smtpObj.sendmail(sender,[email],messageOjb.as_string())#发送邮件
            print "email send sucess"
            return True
        except smtplib.SMTPException,ex:
            print "send email failed!"
            print ex
            return False


if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    #开启server_sockte服务监听9090端口
    transport = TSocket.TServerSocket("localhost","9090")
    #定义传输方式 帧传输方式
    tfactory = TTransport.TFramedTransportFactory()
    #建立传输协议 使用二进制的传输协议
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    #创建server服务 TServer.TSimpleServer(负责处理消息实现具体服务，负责监听网络请求，传输的方式，传输的协议)
    server = TServer.TSimpleServer(processor,transport,tfactory,pfactory)
    print "python thrift server start"
    server.serve()
    print "python thrift server exit"


