#get_data function: gets input from user for name, id, address, and zip, and appends to file
def get_data():
        cname = input('\n Enter customer name?\n\n')    #get customer name from kybd
        cid=input('\n Enter customer id.\n\n')          #get id
        caddr=input('\n Enter customer addr.\n\n')      #get address
        czip=input('\n Enter customer zip code.\n\n')   #get zip
        custdata=open("custinfo.txt", "a")              #create file object for customer data
        custdata.write(cname)                           #write customer name to file
        custdata.write(",")                             #insert comma
        custdata.write(cid)                             #write customer name to file
        custdata.write(",")                             #insert comma
        custdata.write(caddr)                           #write customer name to file
        custdata.write(",")                             #insert comma
        custdata.write(czip)                            #write customer name to file
        custdata.write("\n")                            #insert eol
        custdata.close()                                #close file
        
#prt_file function: prints contents of file
def prt_file():                         #begin print customer data function
    custdata=open ("custinfo.txt", "r") #open customer data file to read
    print('\n\n Customer List\n ')      #send customer data heading to hdmi
    print(custdata.read())              #send customer data file to hdmi
    custdata.close()                    #close file


#main
inloop = 'y'                    #initialize main program loop variable
while inloop == 'y':                                            #start of main program loop
        get_data()                                              #call get_data function for user input
        prt= input('\n Would you like to see the customer list? y/n \n')#prompt user to display customer list
        if prt == 'y':                                          #query for display of customer list
                prt_file()                                              #call prt_file function to display customer info 
        inloop = input('Would you like to enter another customer?\n')#query for more data
        if inloop == 'n':                                       #if no more data exit program
                break                                                   #exit main loop
print('\n Bye!!')               #exit prompt




