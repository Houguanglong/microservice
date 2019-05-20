namespace java com.houguang.thrift.message
namespace py message.api

service MessageService {

    //发送短信
    bool sendMobileMessage(1:string mobile,2:string message);

    //发送邮件
    bool sendEmailMessage(1:string email,2:string message);



}