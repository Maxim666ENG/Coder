def main():
    account = input("Welcome to gog.com, please enter '1' to sign up")  #asking to create an account
    errors = []
# these 4 lines are like a storage
    class_list = {}
    class_list2 = {}
    username1 = ''
    username2 = ''

    #setting password criteria
    while True:
        if account.isdigit() and account == '1':
           password = input("""Create a password which :
    1)MUST contain at least 7 letters.
    2)MUST contain at least one uppercase letter.
    3)MUST contain at least one lowercase letter.
    4)MUST contain at least one number.
    : """)
    #checking if account meets the criteria
        if (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 7) == False:
            print("Your password doesn't meet the criteria.")
        elif (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 7) == True:
            data1 = 'password1'
            class_list[data1] = password
            print('Password saved in the database.')
            break
    while True: #creating an email
        if account.isdigit() and account == '1':
            email = input("""Enter your email.
    Example: dogbarked@gmail.com
    : """)
        if '@' not in email:  #eliminating basic error with @
            print("Error encountered, try again")
        elif '@' in email:
            data2 = 'email1'
            class_list[data2] = email
            print('Email saved in the database.')
            print('Account created! You will be returned to the homepage.')
            break
    #________________________________________________________________________________________________________________________
    user = input("""Welcome to gog.com, please enter '2' to create another account max(2),
    or enter '1' to sign in: """)
    #checking if user wants to sign in or create another account
    while user == '1':
        if input('Password: ') == (class_list['password1']) and input('Email: ') == (class_list['email1']):
           print('Access granted')
           break
        else:
           print('Access denied')


    #________________________________________________________________________________________________________________________________
    # creating second account, the same block of code as with the first account
    while user == '2':
        if user.isdigit() and user == '2':
           password2 = input("""Create a password which :
    1)MUST contain at least 7 letters.
    2)MUST contain at least one uppercase letter.
    3)MUST contain at least one lowercase letter.
    4)MUST contain at least one number.
    : """)
        if (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 7) == False:
            print("Your password doesn't meet the criteria.")
        elif (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 7) == True:
            data3 = 'password2'
            class_list2[data3] = password2
            print('Password saved in the database.')
            break
    while user == '2':
        if user.isdigit() and user == '2':
            email2 = input("""Enter your email.
    Example: dogbarked@gmail.com
    : """)
        if '@' not in email2:
            print("Error encountered, try again")
        elif '@' in email:
            data4 = 'email2'
            class_list2[data4] = email2
            print('Email saved in the database.')
            print('Second account created! You will be returned to the homepage.')
            break

   # now user is asked with which account if he wants to sign in
    user = input("""Welcome to gog.com, please enter '2' to create another account max(2),
    enter '1' to sign in with your 1st account or '3' to sign in with your 2nd account: """)
   #preventing from creating another account
    while user == '2':
        print('Account number limit reached!')
        break

    user = input("""Welcome to gog.com, please enter '2' to create another account max(2),
    enter '1' to sign in with your 1st account or '3' to sign in with your 2nd account: """)


   # first account
    while user == '1':
        if input('Password: ') == (class_list['password1']) and input('Email: ') == (class_list['email1']):
           print('Access granted')
           break
        else:
           print('Access denied')
   #second account
    while user == '3':
        if input('Password: ') == (class_list2['password2']) and input('Email: ') == (class_list2['email2']):
           print('Access granted')
           break
        else:
           print('Access denied')
#this starts the function
main()
