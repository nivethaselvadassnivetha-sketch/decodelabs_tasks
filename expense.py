total = 0
count = int(input("How many products are there: "))
for i in range(count):
    expense = int(input("Enter expense amount: "))
    total = total + expense
while True:
    choice = input("Do you want to add more products? (yes/no): ")
    if choice == "yes":
        extra=int(input("Enter Extra Expense Amount:"))
        total=total+expense
        print("Current Total:",total)
    elif choice=="no":
        break
print("Final Expense:", total)
