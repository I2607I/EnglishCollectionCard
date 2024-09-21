# Import smtplib for the actual sending function
import smtplib
import os
from email.message import EmailMessage
from email.utils import make_msgid
import secrets
import string
import bcrypt

from dotenv import load_dotenv
from template_email import gen_template

load_dotenv()

def send_emeil_code(me, you, template):
   asparagus_cid = make_msgid()

   msg = EmailMessage()
   msg.set_content(template.format(asparagus_cid=asparagus_cid), subtype='html')
   msg['Subject'] = f'Проверочный код'
   msg['From'] = me
   msg['To'] = you
   s = smtplib.SMTP('smtp.yandex.ru')
   s.starttls()
   s.login(os.getenv("me"), os.getenv("PASS"))
   s.send_message(msg)
   s.quit()

def check_email_code(code, user_code):
   if code == user_code:
      return True
   return False

def gen_email_code():
   alphabet = string.digits
   password = ''.join(secrets.choice(alphabet) for i in range(4))
   return password
   #  if (any(c.islower() for c in password)
   #          and any(c.isupper() for c in password)
   #          and sum(c.isdigit() for c in password) >= 3):
   #      break

def hash_pass(password):
   password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
   # print(password)
   return password

def check_pass(password, hash_password):
   print(password, hash_password)
   print(bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
   valid = bcrypt.checkpw(password.encode(), hash_password)
   return valid




if __name__ == "__main__":
   me = os.getenv("me")
   you = os.getenv('you')
   code = 2607
   code = gen_email_code()
   template = gen_template(code)
   # send_emeil_code(me, you, template)

   user_code = input("Enter code from email:\n")
   # res = check_email_code(code, user_code)
   # print(res)
   password = '12345'
   a = hash_pass(password)
   print(check_pass(password, a))

# alphabet = string.digits + string.ascii_letters
# while True:
#    password = ''.join(secrets.choice(alphabet) for i in range(4))
#    if (any(c.islower() for c in password)
#          and any(c.isupper() for c in password)
#          and sum(c.isdigit() for c in password) >= 3):
#       break

