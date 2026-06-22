#EXPENSE TRACKER APP

expensesList = [] #List of all expenses
print("Welcome to Expense Tracker")

while True:
    print("===MENU===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total money spend")
    print("4. Exit")

    choice= int(input("Please Enter your Choice : "))

#ADD EXPENSE
    if(choice ==1):
        date= input("Enter the date of expense: ")
        category= input("Enter the expense category: ")
        description= input("Add more detail: ")
        amount= float(input("Enter total amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n DONE. Expense is added successfully.")

# 2. VIEW ALL EXPENSES
    elif(choice == 2):
        if( len(expense)==0 ):
            print("No Expenses Added.")
        else:
            print("===Here are your expenses===")
            count= 1
            for eachExpense in expensesList:
                print(f"Expense number {count} -> {eachExpense["date"]}, {eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["amount"]}")
                count= count+1


# 3. VIEW TOTAL SPENDING
    elif(choice == 3):
        total= 0
        for eachExpense in expensesList:
            total = total + eachExpense["amount"]

        print("\n TOTAL EXPENSE = ", total)

# 4. EXIT   
    elif(choice == 4):
        print("THANK YOU FOR USING THE APP:)")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
