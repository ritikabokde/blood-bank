import smtplib

content = "Hello "
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('ritikabokde@gmail.com', 'bloodbank.project')
mail.sendmail('ritikabokde@gmail.com', content)
