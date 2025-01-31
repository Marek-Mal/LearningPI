import yagmail

passowrd = ''
with open('./.email_password', 'r') as f:
    password = f.read().rstrip()

yag = yagmail.SMTP('example@gmail.com', password)

yag.send(to='Exaple@gmail.com',
    subject='subject',
    contents='content',
    attachments='FILE'
)

print('email sent')