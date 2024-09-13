# Import smtplib for the actual sending function
import smtplib
import os
from email.message import EmailMessage
from email.utils import make_msgid

from dotenv import load_dotenv

load_dotenv()

code = 2607
template = f'''<div style="background-color: lightblue; padding: 20px;">
               <div style="background-color: white; padding: 10px;">
               Введите проверочный код {code}
               </div>
               </div>
            '''
asparagus_cid = make_msgid()
msg = EmailMessage()
msg.set_content(template.format(asparagus_cid=asparagus_cid), subtype='html')
msg['Subject'] = f'Проверочный код'
msg['From'] = os.getenv("me")
msg['To'] = os.getenv('you')
s = smtplib.SMTP('smtp.yandex.ru')
s.starttls()
s.login(os.getenv("me"), os.getenv("PASS"))
s.send_message(msg)
s.quit()