# this module covers DIP (Dependency Inversion Principle)

from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send():
        pass

class EmailService(NotificationSender):
    def send(self, msg):
        print("Email : ", msg)

class SMSService(NotificationSender):
    def send(self, msg):
        print("SMS : ", msg)

class NotificationService:
    def __init__(self, sending_type: NotificationSender):
        self.sending_type = sending_type

    def notify(self, msg):
        self.sending_type.send(msg)


if __name__=="__main__":
    email_sender =  EmailService()
    email_service = NotificationService(email_sender)

    sms_sender = SMSService()
    sms_service = NotificationService(sms_sender)

    email_service.notify("hello!")
    sms_service.notify("hello!")