from gmail import GMail, Message
import datetime
from random import choice

html_template = '''
<p>H&ocirc;m nay em bị {{symptom}}, sếp cho em xin nghỉ.</p>
'''
symptom_list = ["đau bụng","đau chân","đau đầu","đau tay"]

html_content = html_template.replace("{{symptom}}",choice(symptom_list))

while True:
    gmail = GMail("linh.th11101998@gmail.com","linhdz123")
    msg = Message("Test message",to="tranhoanglinh11101998@gmail.com",text="i am sick")
    now = datetime.datetime.now()
    day = now.day
    if now.hour > 7 and day == now.day:
        gmail.send(msg)
        day+=1


        