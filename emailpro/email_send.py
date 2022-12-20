import smtplib

#python have a library SMTP lib for sending mails. it is simple mail transfer protocol client
#session object.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-
#and-payloads-for-sending-email-with-file-atta

#MIME is multipurpose internet mail extensions. it is an internet standard that extends
#the format of email to support text,non-text attachments:audio,video,images,etc
#message body with multiparts

con=smtplib.SMTP('smtp.gmail.com',587)

#TLS is transport Layer Security. it encrypts all the SMTP commands

con.starttls()

sender='shivaninamani2003@gmail.com'
receiver='shivaninamani2003@gmail.com'

con.login(sender,'upax mdog cggi yxfu')

msg="hiiii how are you mayan!!!!"

msg1=MIMEMultipart()

msg1['From']=sender
msg1['To']=receiver
msg1['Subject']="some attachment bro!!"

filename='SE WEEK-9 PROTOTYPE.docx'
attach=open(r'D:\sfolder\sprograms\python\emailpro\attachment\SE WEEK-9 PROTOTYPE.docx','rb')

base=MIMEBase('application','octet-stream')

base.set_payload((attach).read())

encoders.encode_base64(base)

base.add_header('Content-Disposition', "attach; filename= %s" % filename)

msg1.attach(base)

text=msg1.as_string()

con.sendmail(sender,receiver,text)

con.quit()
