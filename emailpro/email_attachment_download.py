import imaplib
import email
import yaml
import os


# yaml is the human readable data serialization language which is used to file
# configuration and data exchange. it is very easy to understand and very easy to
# parse the data so it has the advantage over the the markup languages like JSON
# XML. we need to create yaml file with extension .yaml or .yml

with open('emaildetails.yml', 'r') as det:
    total_details = yaml.safe_load(det)
 


# from emaildetails.yml we must load the user and password

username, password = total_details['details']['user'], total_details['details']['password']

# IMAP is internet messaging access protocol. IMAP allows tou to access your email
# whereever you are and from any device. here the email is maintained by remote server.
# it allows to take any action such as downloading, deelete,create, etc
# url for imap connection

imap_url = 'imap.gmail.com'

# connecting to GMAIL by SSL connection. SSL is secure socket layer is protocol for
# establishing secure links between server and client or networked computers

con = imaplib.IMAP4_SSL(imap_url)

# logging the user in

con.login(username, password)

# calling function to check for email under this label

con.select('Inbox')

attachment_path = 'D:/sfolder/sprograms/python/emailpro/attachment'

# IMAP4.search(charset, criterion[, ...])
#typ, msgnums = M.search(None, 'FROM', '"LDJ"')
# or typ, msgnums = M.search(None, '(FROM "LDJ")')


def search_mail(key,value,con):
    typ, data = con.search(None,key,'"{}"'.format(value))
    return data

# data will be like id's--example: [b'1450 1451 1452']


def getmail(mailid):
    for ids in mailid[0].split():
        typ, data = con.fetch(ids, '(RFC822)')
        if typ != 'OK':
            print('error fetching mail')
        rawdata=data[0][1]
        rawdata_string=rawdata.decode('utf-8')
        #converts byte literal to string by removing b
        msg=email.message_from_string(rawdata_string)
    return msg

# data[0]=b'1450 1451 1452' and data[0].split()=[b'1450', b'1451', b'1452']
# RFC822 is the module that contains the parser for mail and new messages
# Basically, an RFC 822–style message consists of a number of header
# fields, followed by at least one blank line, and the message body itself.

def attachment(message):
    for part in message.walk():
        if part.get_content_maintype()=='multipart':
            print(part.as_string())
            continue
        if part.get('Content-Disposition') is None:
            print(part.as_string())
            continue
        filename=part.get_filename()
        if bool(filename):
            file_path=os.path.join(attachment_path,filename)
            if not os.path.isfile(file_path):
                f=open(file_path,'wb')
                f.write(part.get_payload(decode=True))
                f.close()

key="FROM"
value="janapareddythanmayee29@gmail.com"
details = getmail(search_mail(key,value,con))
attachment(details)
