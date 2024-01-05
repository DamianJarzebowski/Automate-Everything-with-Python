import yagmail
import os

sender = 'xxxx'
receiver = 'xxxx'

subject = "This is the subject!"


contents = """
Here is the content of the email! 
Hi!
"""
#Password - set app password at gmail
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")