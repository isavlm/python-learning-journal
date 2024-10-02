def collectDailyWorkHours():
    print("Gathering daily hours worked, please input 0 if there wasn't any work done that day.")
    myHours = []
    for i in range(5): #Adding a while loop here so user can correct mistakes.
        while True:
            try:
                myDailyHours = float(input(f"Please input the hours worked for day {i+1}: "))
                if myDailyHours < 0:
                    print("Hours cannot be negative. Please try again.")
                else:
                    myHours.append(myDailyHours)
                    break
            except ValueError:
                print("Only numerical inputs accepted. Please enter a valid number.")
    return myHours

def calculateTotalHours(listOfHours):
    myTotalHours = 0
    for i in listOfHours:
        myTotalHours += int(i)
    return myTotalHours

def calculateOverTime(hours):
    myOverTime = 0
    if hours > 40:
        print("Calculating overtime hours...")
        myOverTime = hours - 40
        print(f"Total overtime hours: {myOverTime}")
    return myOverTime

def calculateOverTimePay(hourlyRate):
    return hourlyRate * 1.5

def writeResults(hourlyRate,totalHours,overTimePay):
    myFile = open("payRate.txt","w")
    myFile.write(f"at an hourly rate of {hourlyRate} the {totalHours} worked includes {overTimePay} in overtime pay")
    myFile.close()

def myMainFunction():
    while True: #Adding a while loop and try to catch user errors. 
        try:
            myHourlyRate = float(input("Please input the hourly rate of the employee: "))
            if myHourlyRate <= 0:
                print("Hourly rate must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Hourly rate must be a numerical value. Please try again.")
    
    myHoursWorked = collectDailyWorkHours() 
    myTotalHours = calculateTotalHours(myHoursWorked)
    myOvertimeHours = calculateOverTime(myTotalHours)
    
    if myOvertimeHours > 0:
        myOvertimePayRate = calculateOverTimePay(int(myHourlyRate))
        myOvertimePay = myOvertimeHours * myOvertimePayRate
        myRegularPay = myHourlyRate * 40
        myFinalPay = myOvertimePay + myRegularPay
    else:
        myOvertimePay = 0
        myFinalPay = myHourlyRate * myTotalHours
  
    print(f"Total amount paid for this week is: ${myFinalPay:.2f}")

    writeResults(myHourlyRate, myTotalHours, myOvertimePay)

if __name__ == "__main__":
    myMainFunction()
