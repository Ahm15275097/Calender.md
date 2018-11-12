option = 0
print ("Welcome to your calendar")


while option !='4':
    option = input(" 1. View all entries \n 2. Edit an entry \n 3. Add new entry \n 4. Exit calendar \n Please enter your choice: ")

    if (option == '1'):
        print ("we are in the viewing section")
        f = open("calender.txt", "r")
        textFile = f.read()
        print(textFile)
       

        recCount = 0

        line1 = f.readline()
        print("Record")
        while (line1 != ""):
            recCount = recCount + 1            
            line2 = f.readline()
            print(recCount, "\t" + line1 + "\t" + line2 + "\n")
            line1 = f.readline()
        f.close()


    if (option == '2'):
        print ("we are in the editting section")
        f = open("calendar.txt", "r+")

        editEntry = input ("Please enter the line the corellates with the event you wish to edit ")
        editEntryInteger = int(editEntry)

        if editEntry in open("calendar.txt").read():

        print (linecahce.getline("calender.txt" , editEntryInteger , module_globals=None))
        


        


    if (option == '3'):
        print ("we are in the creating section")
        f = open("calender.txt", "a")
        theDate = input ("Enter Date DD-MM-YYYY: ")        
        theEventEntry = input ("Enter your event: ")
        f.write("\n" + theDate + "\t" + theEventEntry)
        f.close


    if (option  !='1') and (option !='2') and (option !='3') and (option !='4'):
        print ("INVALID OPTION, TRY AGAIN")


print ("Goodbye")




    

