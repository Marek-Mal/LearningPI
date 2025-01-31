import os
import yagmail

with open('./.email_password', 'r') as f:
    password = f.read().rstrip()

yag = yagmail.SMTP('example@gmail.com', password)

yag.send(to='example2@gmail.com',
    subject='example',
    contents='example'
)

print('email sent')