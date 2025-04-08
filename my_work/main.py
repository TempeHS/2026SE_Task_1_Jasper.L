logins = []
with open('plain_text.txt', 'r') as file:
    datalog = file.readlines()
for login in datalog:
    logins.append(login.strip('\n'))
print(logins)

def login():
    iuser = input('Username? ')
    ipass = input('Password? ')
    ilog = f'{iuser},{ipass}'
    for login in logins:
        if ilog == login:
            return True
    else:
        print('Wrong username or password, try again')
        selection()

def register():
    while True:
        nuser = input('New username? ')
        npass = input('New password? ')
        nlog = f'{nuser},{npass}'
        if len(npass) < 4:
            print('Password must be minimum 4 characters')
        else:
            with open('plain_text.txt', 'a') as file:
                file.write(f'{nlog}\n')
            print('Registered successfully')
            break

def menu():
    while True:
        print(f'1. Change password\n2. Logout')
        try:
            select = int(input('Choice? '))
        except ValueError:
            print('Please enter a valid option')
        if select == 1:
            passwordchange()
        if select == 2:
            print('Logging out')
            break


def selection():
    while True:
        print(f'1. Login\n2. Register\n3. Quit')
        try:
            select = int(input('Choice? '))
        except ValueError:
            print('Please enter a valid option')
        if select == 1:
            if login() == True:
                return True
        if select == 2:
            register()
        if select == 3:
            print('Quitting')
            return False

def main():
    if selection() == True:
        menu()

main()