def budget_calc():
    #Taking input from the user.
    print("------- Personal Budget Calculator -------")
    month_name = input("Enter the month for which you are adding budget: ")
    inc=int(input("Enter your income: "))
    print("Enter your expenses")
    food=int(input("Food: "))
    rent=int(input("Rent: "))
    fare=int(input("Fare: "))
    misc=int(input("Misc: "))
    t_exp=food+rent+fare+misc
    rem_money=inc-t_exp
    #Printing summary.
    heading = f"---- {month_name} Budget Summary ----"
    print(f"\n{heading}")
    print(f"Income = {inc}")
    print(f"Total expenses = {t_exp}")
    print(f"Remaining money = {rem_money}")
    if rem_money<0:
        adv=f"Alert! You are overspending. Try to cut down unnecessary expenses."
    elif rem_money<=0.2*inc:
        adv=f"Consider increasing your savings. Aim for at least 20% of your income."
    elif rem_money>0.2*inc:
        adv=f"Good job! You have a balanced budget. Keep tracking regularly to maintain financial stability."
    print(f"\n{adv}")
    #Saving the budget in the file.
    try:
        with open ("Budget.txt","a") as fh:
            fh.write(f"\n{heading}\n")
            fh.write(f"Income = {inc}\n")
            fh.write(f"Total expenses = {t_exp}\n")
            fh.write(f"Remaining money = {rem_money}\n")
            fh.write(f"\n{adv}\n")
            print(f"Your personal budget summary is ready! It is saved as 'Budget.txt'")
    except Exception as e:
        print(f"Error is {str(e)}")
budget_calc()        