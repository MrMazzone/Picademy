
inloop = 'y'            #initialize while loop
while inloop == 'y':    #start main pgm loop
    cname = input('\n Enter customer name?\n\n')    #get customer name
    cid=input('\n Enter customer id.\n\n')          #get customer id
    cstreet=input('\n Enter customer street.\n\n')  #get customer street
    ccity=input('\n Enter customer city.\n\n')      #get customer city
    cstate=input('\n Enter customer state.\n\n')    #get customer state
    czip=input('\n Enter customer zip code.\n\n')   #get customer zip
    mlst=open('mail_list.txt', 'a') #create file object for writing
    mlst.write(cname)               #write customer name to file
    mlst.write(",")                 #append comma
    mlst.write(cid)                 #write customer name to file
    mlst.write(",")                 #append comma
    mlst.write(cstreet)             #write customer name to file
    mlst.write(",")                 #append comma
    mlst.write(ccity)               #write customer name to file
    mlst.write(",")                 #append comma
    mlst.write(cstate)              #write customer name to file
    mlst.write(",")                 #append comma
    mlst.write(czip)                #write customer name to file
    mlst.write("\n")                #append EOL
##    print(cname)                    #test print of data input
##    print(cid)                      #test print of data input
##    print(cstreet)                  #test print of data input
##    print(ccity)                    #test print of data input
##    print(cstate)                   #test print of data input
##    print(czip)                     #test print of data input
    inloop = input('\n Do you want to enter another customer? y/n \n\n') #more data??
mlst.close()                    #close file

custdata=open ('mail_list.txt', 'r')#open data file, assign file object
print(custdata.read())              #display data file
custdata.close()                    #close data file
     

print('\n Bye!!')                   #exit msg




