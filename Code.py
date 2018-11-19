option = 0
import linecache
print ("Welcome to your calendar")


while option !='4':
    option = input(" 1. View all entries \n 2. Edit/Delete an entry \n 3. Add new entry \n 4. Exit calendar \n Please enter your choice: ")

    if (option == '1'):
        print ("we are in the viewing section")
        f = open("calendar.txt", "r")

        recCount = 0
        lineDate = f.readline()

        print('Record No.') 

        while (lineDate != ""):
            lineInfo = f.readline()
            print(recCount, "\t\t" + lineDate + "\t\t" + lineInfo)
            lineDate = f.readline()
            recCount = recCount + 1
     
        f.close()


    if (option == '2'):
        print ("we are in the editting section")

        f = open("calendar.txt", "r")

        recCount = 0
        lineDate = f.readline()

        print('Record No.')
        dateList = []
        infoList = []

        while (lineDate != ""):
            lineInfo = f.readline()
            print(recCount, "\t\t" + lineDate + "\t\t" + lineInfo)
            
            dateList.insert(recCount, lineDate)
            infoList.insert(recCount, lineInfo)
            
            recCount = recCount + 1
            lineDate = f.readline()
        f.close()

        while True:
            recNum = int(input ("Please select the Record No. you wish to change :"))

            if ( recNum > (len(dateList)-1) or recNum < 0):
                print("You have entered an incorrect record, Please try again")
            else:
                break

        

        while True:
            choice = str(input("Type d to delete or u to update: "))
            print(choice)

            if (choice == 'd' or choice == 'u'):
                break
            else:
               print("You have entered an incorrect choice, Please try again")
 
        if choice == 'u':
            newDate = input ("Enter Date DD-MM-YYYY: ")
            newEvent = input ("Enter your Event ")

            dateList[recNum] = newDate + "\n"
            infoList[recNum] = newEvent + "\n"

            f = open ("calendar.txt" , "w")        
            for index in range (0, len(dateList)):
                f.write(dateList[index])
                f.write(infoList[index])
            f.close()

        if choice == 'd':
            dateList.pop(recNum)
            infoList.pop(recNum)

            f = open ("calendar.txt" , "w")        
            for index in range (0, len(dateList)):
                f.write(dateList[index])
                f.write(infoList[index])
            f.close()



    if (option == '3'):
        print ("we are in the creating section")
        f = open("calendar.txt", "a")
        theDate = input ("Enter Date DD-MM-YYYY: ")        
        theEventEntry = input ("Enter your event: ")
        f.write("\n" + theDate + "\n" + theEventEntry)
        f.close


    if (option  !='1') and (option !='2') and (option !='3') and (option !='4'):
        print ("INVALID OPTION, TRY AGAIN")


print ("Goodbye")




    

