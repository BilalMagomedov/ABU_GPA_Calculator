print("\033[0;30;47m< GPA CALCULAOR OF ANTALYA BILIM UNIVERSITY >")

amountOFsubs = int(input("\033[1;34;40mEnter the amount of SUBJETCS in your semester: ")) #BRIGHT BLUE
totalAmountOfCredits = int(input("\033[1;35;40mEnter the total amount of CREDITS in your semester: ")) #MAGENTA
result = 0

for x in range(0, amountOFsubs, 1):
    total = 0
    print("\033[1;31;40mEnter the name of the subject", x+1 ,": \033[0;37;40m") #RED
    subject = input("")
    print("\033[1;33;40mEnter the amount of credits for", subject, ": \033[0;37;40m") #YELLOW
    credits = int(input(""))
    print("\033[1;32;40mEnter the letter grade of", subject, ": \033[0;37;40m") #GREEN
    letterGrade = input("")
    
    if letterGrade.upper() == "A+": 
        total = 4.0 * credits
    elif letterGrade.upper() == "A":
        total = 4.0 * credits
    elif letterGrade.upper() == "A-":
        total = 3.7 * credits
    elif letterGrade.upper() == "B+":
        total = 3.3 * credits
    elif letterGrade.upper() == "B":
        total = 3.0 * credits
    elif letterGrade.upper() == "B-":
        total = 2.7 * credits
    elif letterGrade.upper() == "C+":
        total = 2.4 * credits
    elif letterGrade.upper() == "C":
        total = 2.2 * credits
    elif letterGrade.upper() == "C-":
        total = 2.0 * credits
    elif letterGrade.upper() == "D+":
        total = 1.7 * credits
    elif letterGrade.upper() == "D":
        total = 1.5 * credits
    elif letterGrade.upper() == "F":
        total = 0.0
    else:
        total = 0.0
    
    result = result + total
    print("----------------------------------------\n")

print("\033[1;37;40mYour GPA is:", format((result / totalAmountOfCredits),".2f"))




