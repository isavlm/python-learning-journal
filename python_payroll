def collectDailyWorkHours():
    """Collects daily work hours for up to 5 days and ensures valid input."""
    print("Gathering daily hours worked, please input 0 if there wasn't any work done that day.")
    myHours = []
    for i in range(5):
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
    """Calculates the total number of hours worked."""
    myTotalHours = sum(listOfHours)
    return myTotalHours

def calculateOverTime(hours):
    """Calculates overtime hours if applicable."""
    myOverTime = 0
    if hours > 40:
        print("Calculating overtime hours...")
        myOverTime = hours - 40
        print(f"Total overtime hours: {myOverTime}")
    return myOverTime

def calculateOverTimePay(hourlyRate):
    """Calculates overtime pay at 1.5 times the hourly rate."""
    return hourlyRate * 1.5

def writeResults(hourlyRate, totalHours, overTimePay):
    """Writes payroll results to a file."""
    with open("payRate.txt", "w") as myFile:
        myFile.write(f"At an hourly rate of {hourlyRate}, the {totalHours} hours worked includes {overTimePay} in overtime pay.")
    print("Payroll information saved to 'payRate.txt'.")

def myMainFunction():
    """Main function to run the payroll program."""
    while True:
        try:
            myHourlyRate = float(input("Please input the hourly rate of the employee: "))
            if myHourlyRate <= 0:
                print("Hourly rate must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Hourly rate must be a numerical value. Please try again.")
    
    # Collect daily hours worked
    myHoursWorked = collectDailyWorkHours()

    # Calculate total hours and overtime
    myTotalHours = calculateTotalHours(myHoursWorked)
    myOvertimeHours = calculateOverTime(myTotalHours)

    # Calculate pay
    if myOvertimeHours > 0:
        myOvertimePayRate = calculateOverTimePay(myHourlyRate)
        myOvertimePay = myOvertimeHours * myOvertimePayRate
        myRegularPay = myHourlyRate * 40
        myFinalPay = myOvertimePay + myRegularPay
    else:
        myOvertimePay = 0
        myFinalPay = myHourlyRate * myTotalHours

    # Output pay details
    print(f"Total amount paid for this week is: ${myFinalPay:.2f}")

    # Save results to a file
    writeResults(myHourlyRate, myTotalHours, myOvertimePay)

if __name__ == "__main__":
    myMainFunction()
