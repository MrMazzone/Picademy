import smtplib                      #load smtp module

#gmail setup info
GMAIL_USER = 'your gmail user name@gmail.com'   #assign sender's email address
GMAIL_PASS = '**********'           #assign sender's email pw
SMTP_SERVER = 'smtp.gmail.com'      #assign email service provider
SMTP_PORT = 587                     #assign email service port
recipient= 'recipient email address'#assign email destination address
subject= 'this is test0.0'          #assign subject line info
text= 'this is the message content' #actual text to be sent

#send email
smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)   #create smtp object
smtpserver.ehlo()               #smtp extended cmd to initiate smtp session
smtpserver.starttls()           #smtp extended cmd to start transport layer security, remaining info encrypted
smtpserver.login(GMAIL_USER, GMAIL_PASS)    #tranfer login info
header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER   #construct header
header = header + '\n' + 'Subject:' + subject + '\n'        #expand header
msg = header + '\n' + text + ' \n\n'                        #add text msg to header
smtpserver.sendmail(GMAIL_USER, recipient, msg)             #transfer email from, to, msg, info 
smtpserver.quit()                                           #terminate smtp session

