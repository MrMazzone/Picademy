import smtplib  #load smtp module


def send_email(recipient, subject, text): #send_email function definition
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)   #create smtp object
    smtpserver.ehlo()               #smtp extended cmd to initiate smtp session
    smtpserver.starttls()           #smtp extended cmd to start transport layer security, remaining info encrypted
    smtpserver.login(GMAIL_USER, GMAIL_PASS)    ##tranfer login info
    header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER   #construct header
    header = header + '\n' + 'Subject:' + subject + '\n'        #expand header
    msg = header + '\n' + text + ' \n\n'                        #add text msg to header
    smtpserver.sendmail(GMAIL_USER, recipient, msg)             #transfer email from, to, msg, info 
    smtpserver.quit()                                           #terminate smtp session


GMAIL_USER = 'your usr name@gmail.com'          #assign sender's email address
GMAIL_PASS = 'your password'                    #assign sender's email pw
SMTP_SERVER = 'smtp.gmail.com'                  #assign email service provider
SMTP_PORT = 587                                 #assign email service port

send_email('recipient email addr', 'test1', 'this is a test')  #send_email function call
