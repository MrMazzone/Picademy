#load library modules
import smtplib  #smtp module
import csv      #csv module
import datetime #date time module

# function reads csv file for gmail user login info
def gmail_setup():
    mailsetup = csv.reader(open('login2.txt','r'))         #open login info file for reading, assign file object
    global GMAIL_USER, GMAIL_PASS, SMTP_SERVER, SMTP_PORT   #declare global variables
    for row in mailsetup:                       #assign user, pw, mail svr, port num from file object mailsetup
        GMAIL_USER = row[0]
        GMAIL_PASS = row[1]
        SMTP_SERVER= row[2]
        SMTP_PORT = row[3]
    return                                      #end of gmail_setup function

#Function sends email using gmail server
def send_email(recipient, subject, text):
##    print(GMAIL_USER)
##    print(GMAIL_PASS)
##    print(SMTP_SERVER)
##    print(SMTP_PORT)
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)   #create smtp object
    smtpserver.ehlo()       #smtp extended cmd to initiate smtp session
    smtpserver.starttls()   #smtp extended cmd to start transport layer security, remaining info encrypted
    smtpserver.login(GMAIL_USER, GMAIL_PASS)                    #tranfer login info
    header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER   #construct header
    header = header + '\n' + 'Subject:' + subject + '\n'        #expand header
    msg = header + '\n' + text + ' \n\n'                        #add text msg to header
    smtpserver.sendmail(GMAIL_USER, recipient, msg)             #transfer email from, to, msg, info 
    smtpserver.quit()                                           #terminate smpt session
    current_time=str(datetime.datetime.now())                   #get current time and date
    print('Message To: '+ recipient + '\n' + '\tFrom: ' + GMAIL_USER + '\n\tSent @ ' + current_time) #send confirmation to hdmi
    return  #end of send_email function
    
#main    
#function call to get email setup info
gmail_setup()

#function call to send smtp message
send_email('vernmace@gmail.com', 'biteme!!', 'this is a test2')

