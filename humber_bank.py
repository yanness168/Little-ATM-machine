import re


def continue_or_not():
    answer = input("Do you want to perform another task: (y/n): ")
    return answer.lower()


def check_pin(pin):
    i = 1
    user_pin = input("Hello!\nPlease enter your 4-digit PIN: ")
    while i < 3:
        if user_pin == pin:
            break
        elif not re.match("[0-9][0-9][0-9][0-9]", user_pin) or (user_pin != pin):
            user_pin = input("Your input is invalid/incorrect.\n"
                             "Please try again: ")
            if i == 3:
                quit("Sorry... Your PIN is incorrect")
            else:
                i = i + 1
                continue
        quit("Sorry... Your PIN is incorrect")


def display_menu():
    number = input(f'Choose a task to perform from below:\n'
                   f"1, Display the balance\n"
                   f'2, Make a withdrawal\n'
                   f'3, Make a deposit\n'
                   f'4, Done with transactions\n'
                   f'----------------------------------------------\n'
                   f'Enter a number: ')
    return number


def balance_display():
    global balance
    print(f"Your balance is: ${balance:.2f}.")


def withdraw():
    global balance
    i = 0
    withdrawal = (input(f"Please select a money amount($) you want to withdraw:\n"
                        f"20\t40\t60\t80\t100\tCUSTOM\n"
                        f""))
    while i < 1:
        match withdrawal.strip().lower():
            case ("20"):
                if balance < float(20):
                    print("You don't have enough money to withdraw.\n")
                    withdrawal = input(f"Please select a money amount($) you want to withdraw:\n"
                                       f"20\t40\t60\t80\t100\tcustom\n"
                                       f"")
                    continue
                else:
                    balance = balance - float(20)
                    print(f"Your current balance is: ${balance:.2f}")
                    break
            case ("40"):
                if balance < float(40):
                    print("You don't have enough money to withdraw.\n")
                    withdrawal = input(f"Please select a money amount($) you want to withdraw:\n"
                                       f"20\t40\t60\t80\t100\tcustom\n"
                                       f"")
                    continue
                else:
                    balance = balance - float(40)
                    print(f"Your current balance is: ${balance:.2f}")
                    break
            case ("60"):
                if balance < float(60):
                    print("You don't have enough money to withdraw.\n")
                    withdrawal = input(f"Please select a money amount($) you want to withdraw:\n"
                                       f"20\t40\t60\t80\t100\tcustom\n"
                                       f"")
                    continue
                else:
                    balance = balance - float(60)
                    print(f"Your current balance is: ${balance:.2f}")
                    break
            case ("80"):
                if balance < float(80):
                    print("You don't have enough money to withdraw.\n")
                    withdrawal = input(f"Please select a money amount($) you want to withdraw:\n"
                                       f"20\t40\t60\t80\t100\tcustom\n"
                                       f"")
                    continue
                else:
                    balance = balance - float(80)
                    print(f"Your current balance is: ${balance:.2f}")
                    break
            case ("100"):
                if balance < float(100):
                    print("You don't have enough money to withdraw.")
                    withdrawal = input(f"Please select a money amount($) you want to withdraw:\n"
                                       f"20\t40\t60\t80\t100\tcustom\n"
                                       f"")
                    continue
                else:
                    balance = balance - float(100)
                    print(f"Your current balance is: ${balance:.2f}")
                    break
            case ("custom"):
                wd = input("Please input any dollar amount($) you want to withdraw: ")
                while wd is not None:
                    if balance < float(wd):
                        print("You don't have enough money to withdraw.\n ")
                        wd = input("Please input any dollar amount($) you want to withdraw: ")
                        continue
                    elif balance >= float(wd):
                        balance = balance - float(wd)
                        print(f"Your current balance is: ${balance:.2f}")
                        wd = None
                        continue
                    else:
                        print("Your input is invalid...\n ")
                        wd = input("Please input any dollar amount($) you want to withdraw: ")
                        continue
                break
            case _:
                print("\nYour input is invalid/incorrect... ")
                withdrawal = input(f"Please select a money amount($) you want to withdraw:\n"
                                   f"20\t40\t60\t80\t100\tcustom\n"
                                   f"")
                continue


def deposit():
    global balance
    amount = float(input("How much do you want to deposit: \n$"))
    balance = balance + amount
    print(f"Your new balance is : ${balance:.2f}")


# main function:
PIN = '1223' #set a random PIN
balance = float(1488) #hard code a random balance
k = 1
check_pin(PIN)
while k:
    match (display_menu()):
        case ("1"):
            balance_display()
            if continue_or_not().strip().lower() == 'y':
                continue
            else:
                quit("Goodbye~~~~")
        case ("2"):
            withdraw()
            if continue_or_not().strip().lower() == 'y':
                continue
            else:
                quit("Goodbye~~~~")
        case ("3"):
            deposit()
            if continue_or_not().strip().lower() == 'y':
                continue
            else:
                quit("Goodbye~~~~")
        case ("4"):
            quit("Goodbye~~~~")
