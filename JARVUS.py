import webbrowser

while epassword != 13: # breaks out of the loop when the password is right
    print('Welcome to:\nJ  A  R  V  U  S\nPlease log in: ')
    eusername = input('Please enter your username:')
    if eusername == 'Justin':
        epassword = input('Please enter your password:')

print('Hello,', eusername)

while True:
    user = input('Enter Command: ')
    if user == 'hi':
        print('hi')
    elif user == 'bye':
        print('bye')
        break
    elif user == 'logout':
        print('logging out')
        break
    elif user == 'chrome':
        csearch = input('Search on google: ')
        webbrowser.open_new_tab('https://www.google.com/search?q=' + csearch)

print('Jarvis has closed and you have been logged out.')
