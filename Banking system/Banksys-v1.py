import textwrap

def menu():
    return textwrap.dedent('''\
    ========== MENU ==========
    [d] Deposit
    [s] Withdraw
    [e] Statement
    [c] Create User
    [n] New Account
    [l] List Accounts
    [sc] Select Account
    [q] Exit
    ==========================
    ''')

def deposit(saldo, value, statement):
    if value > 0:
        saldo += value
        statement += f"Deposit: R$ {value:.2f}\n"
        print(f"Deposit successful! Current balance: R$ {saldo:.2f}")
    else:
        print("Operation failed! The value entered is invalid.")
    return saldo, statement

def withdraw(saldo, value, limit, statement, withdrawal_count, WITHDRAWAL_LIMIT):
    exceeded_balance = value > saldo
    exceeded_limit = value > limit
    exceeded_withdrawals = withdrawal_count >= WITHDRAWAL_LIMIT

    if exceeded_balance:
        print("Operation failed! You do not have enough balance.")
    elif exceeded_limit:
        print("Operation failed! The withdrawal amount exceeds the limit.")
    elif exceeded_withdrawals:
        print("Operation failed! Maximum number of withdrawals exceeded.")
    elif value > 0:
        saldo -= value
        statement += f"Withdrawal: R$ {value:.2f}\n"
        withdrawal_count += 1
        print(f"Withdrawal successful! Current balance: R$ {saldo:.2f}")
    else:
        print("Operation failed! The value entered is invalid.")

    return saldo, statement, withdrawal_count

def show_statement(saldo, statement):
    print("\n================ STATEMENT ================")
    print("No transactions have been made." if not statement else statement)
    print(f"\nBalance: R$ {saldo:.2f}")
    print("==========================================")

def create_user(users):
    cpf = input("Enter CPF (numbers only): ")
    user = filter_user(users, cpf)

    if user:
        print("A user with this CPF already exists.")
        return None

    name = input("Enter full name: ")
    birth_date = input("Enter birth date (dd-mm-yyyy): ")
    address = input("Enter address (street, number - neighborhood - city/state abbreviation): ")

    new_user = {
        "name": name,
        "birth_date": birth_date,
        "cpf": cpf,
        "address": address
    }
    users.append(new_user)
    print("User
