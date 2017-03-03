import webbrowser

epassword = None
help = 'All JARVIS commands:\n\nhi\nbye\nlogout\ninternet\nhelp'

print('Welcome to:\nJ  A  R  V  U  S\nPlease log in: ')

while epassword != '13': # breaks out of the loop when the password is right
    eusername = input('Please enter your username:')
    if eusername == 'Justin':
        epassword = input('Please enter your password:')

print('Hello,', eusername)
print()
print(help)

while True:
    user = input('Enter Command: ')
    if user == 'help':
        print(help)
    elif user == 'hi':
        print('hi')
    elif user == 'bye':
        print('bye')
        break
    elif user == 'logout':
        print('logging out')
        break
    elif user == 'internet':
        user = input('Website or google search? [w/g]')
        if user == 'w':
            user = input('Enter website address:')
            if user.startswith('http://') or user.startswith('https://'):
                webbrowser.open(user)
            else:
                webbrowser.open('http://' + user)
        elif user == 'g':
            csearch = input('Search on google: ')
            webbrowser.open('https://www.google.com/search?q=' + csearch)
        else:
            print('Enter a w or g.\nType internet to try again.)

print('Jarvis has closed and you have been logged out.')
