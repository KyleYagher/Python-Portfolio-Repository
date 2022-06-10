# Modules required for the Application
import math

#Display Program text
print("Welcome to CALC-e-LOAN \n")

#Display User Product Options
#Request user to input product selection
print('''*** DASHBOARD ***
    \nInvestment  \t\t- Calculate the Interest income on your capital investment.
    \nBond  \t\t\t- Calculate the total amount repayable on your home loan.\n''')
prod_Select = input('''Input your selection to proceed... (Investment OR Bond)''')

#convert input string to all lowercase
prod_Select = prod_Select.lower()

#if incorrect input throw an error
if prod_Select != "investment" and prod_Select != "bond":
     print("You have made an incorrect selection. Please try again!!")
    
#If input 'Investment'   
elif prod_Select == "investment":

    #Request user to input investment amount and store as variable
    inv_Principle = float(input("How much will you be depositing? R "))

    #Request user to input investment interest rate and store as variable
    int_Rate = int(input("At what interest rate(%)? "))
    int_divRate = int_Rate / 100

    #Request user to input investment term in years and store as variable
    inv_Length = int(input("How long will you be invested(years)? "))

    #Request user to input the Interest type (simple or compound) and store as variable
    interest = input("Do you want compound or simple interest? ")

    #Convert input string to all lowercase
    interest = interest.lower()

    #if incorrect input selection throw error
    if interest != "simple" and interest != "compound":
        print("You have made an incorrect selection. Please try again!!")

    #if interest type is 'simple' calculate total interest earned and store as variable
    if interest == "simple":
        inv_Tot = inv_Principle * (1 + int_divRate * inv_Length)
    
    #if interest type is 'compound' calculate total interest earned and store as variable
    elif interest == "compound":   
        inv_Tot = int(inv_Principle * (math.pow((1 + int_divRate), inv_Length)))

    #Display result 
    print(f'''\n\n\t\t\t***Investment Summary***\n\n
            Principle Amount:\t\tR{float(inv_Principle)}\n
            Interest Rate:\t\t{int_Rate}%\n
            Term of Investment:\t\t{inv_Length}/years\n
            Interest Type:\t\t{interest}\n
            Total investment:\t\t|> R{float(inv_Tot)} <|''')

#If input 'bond'
elif  prod_Select == "bond":

    #Request user to input the house value and store as variable
    prop_Val = int(input("What is the value of the house? R"))

    #Request user to input interest rate and store as variable
    #calculate monthly interest
    int_Rate = int(input("What is the interest rate(%) "))
    int_divRate = int_Rate / 12
    int_divRate = int_Rate / 100

    #Request user to input loan term and store as variable
    loan_Trm = int(input("How long will the repayment term be(months)? "))

    #calculate monthly repayment amount and store as variable
    bond_Paym = int((int_divRate * prop_Val) / (1 - math.pow((1 + int_divRate), -loan_Trm)))

    #Display result
    print(f'''\n\n\t\t\t***Bond Repayment Summary***\n\n
           Property Value:\t\tR{prop_Val}\n
           Interest Rate:\t\t{int_Rate}%\n
           Loan Term:\t\t\t{loan_Trm}/months\n
           Bond Payment:\t\t|> R{float(bond_Paym)}/pm <|''')


   




    

