#HI,welcomes you in spy_chat
import spy_details,chat #calling chat file
while 1==1:
    print"###WELCOME TO SPY_CHAT###"                                            #greetings
    print "IF YOU WANT TO CONTINUE AS A DEFAULT USER OR SIGN FOR NEW-USER?"
    print"SELECT OPTION"
    print"\t1.DEFAULT USER:\n\t2.SIGN UP:"                                     #chosse your choice
    choose = raw_input("")
    if choose == "2" or choose == "2":
        i = False               
        while i != True:                                                       #loop added
                                        #taking a,spy as a variable
            while 1==1:
                a=raw_input("Mr/Mrs?:")                                        #salutation
                if len(a)!=0:
                    break;
                print "invalid salutation\n\t re-enter"
            while 1==1:
                b=raw_input("Enter your name:")                                #spy_name
                if len(b)!=0:
                    break;
                print "invalid name\n\tre-enter "
            c=int(raw_input("Enter your age:"))                                #spy_age
            if c >= 12 and c <= 50:
                print "eligible"
            else:
                print "not eligible"
                exit()
            d=float(raw_input("Enter your rating:"))                           #spy_rating
            if d<= 4:
                print"your rating is poor than defualt user"
                exit()
            if d >= 0 and d <= 4:
                print "very poor"
            elif d >= 4 and d <= 7:
                print "very good"
            elif d >= 7 and d <= 10:
                print "excellent"
            else:
                print "not eligible for this rating"
                exit()
            spy=chat.Name(a,b,c,d)                                             #calling class from chat into varible'''
         #creating a username and password
        
            print"Create your user name:"                                      # creating user name for sign up user
            createun = raw_input()
            print"Create your user password:"                                  # creating password for sign up user
            createps = raw_input()
            print "Thanks for signing up:"                                     # greetings
            while 1==1:
                print "Enter your username:"                                   # created username
                loginun = raw_input()
                if createun== loginun:
                    print "Enter your password:"                               # created password
                    loginps = raw_input()
                    if createps == loginps:
                        print "login sucessful:!!!"
                        break;

                    else:
                        print"Password incorrect"
                        break;
                else:
                    print "login failed!!!\t re-enter"
            break;
    else:
        spy_details.details()                                                  #moving to default user


    chat.msg_check()                                                             # moving to chat file
