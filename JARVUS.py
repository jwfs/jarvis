#program start

#add modules
import webbrowser

running = True
while running:
    print('\nWelcome to: \n J  A  R  V  U  S\nPlease log in')
    #login
    eusername = input('Please enter your username:')
    if eusername == 'Justin':
        epassword = input('Please enter your password:')
        if epassword == '13':
            print('\nHello '+(eusername))
            eusername = ()
            epassword = ()
            login = True
            while login:
                user = input('\nEnter Comand: ')
                #comand locations
                if user == 'hi':
                    print('\nhi')
                    continue
                if user == 'bye':
                    print('\nbye')
                    login = False
                    running = False
                if user == 'logout':
                    print('\nloging out')
                    break
                if user == 'chrome':
                    csearch = input('Search: ')
                    webbrowser.open_new_tab((csearch))
                    
