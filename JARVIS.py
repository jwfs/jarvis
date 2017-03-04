import webbrowser

def login():
    epassword = None
    while epassword != '13': # breaks out of the loop when the password is right
        eusername = input('Please enter your username:')
        if eusername == 'Justin':
            epassword = input('Please enter your password:')

running = True
while running:
    print('Welcome to:\nJ  A  R  V  I  S\nPlease log in: ')
    login()
    print('Hello,', eusername)
    login = True
    while login:
        user = input('Enter Command: ')
        if user == 'hi':
            print('hi')
        elif user == 'bye':
            print('bye')
            login = False
            running = False
        elif user == 'logout':
            print('logging out')
            break
        elif user == 'chrome':
            csearch = input('Search on google: ')
            webbrowser.open_new_tab('https://www.google.com/search?q=' + csearch)

print('Jarvis has closed and you have been logged out.')
