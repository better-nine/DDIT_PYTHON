import os
from twilio.rest import Client
#cmd창에서 twilio를 install 해줍니다



class MySms:
    def mysendSms(self, mobile, content):
        account_sid = 'ACb5f9dacf9e30077d8b91db20742967d0'
        auth_token = 'd7410be1db377c9a1fd0920b17641961'
        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            to="+82"+mobile, 
            from_="+13172254351",
            body=content)


if __name__ == '__main__':
    MySms().mysendSms("01084459916", "민경씨 안녕 반가워요 메롱")
    
    
    