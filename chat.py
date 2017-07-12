from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored,cprint
class Name:                                              #taking class name for the new user
    def __init__(self, salutation, spy_name, age, rating):
        self.salutation = salutation                    #salutation
        self.spy_name = spy_name                        #spy name
        self.age = age                                  #spy age
        self.rating = rating                            #spy rating
        self.chat = []                           
defa = Name('Mr',"Lewis",20,4)                          #default user
list_friend=[defa]                                      #taking list for newfriend as well as default user 
old_status = ["blind", "love", "sick"]                  #taking old status list
text_list =[]                                           #taking text list

lol = None                                           
def msg_check():
    current_status = None                              #current status                          
    print"Starting hike chating"                       # starting hike chating                                           
    while 1 == 1:                                      #added loop here
                                                       # \t refers tab and \n refers to new line
                                                       #chating menu opening
        print"\t1.friend list\n\t2.Status update\n\t3.Inbox\n\t4.Back\n\t5.closing app"
        choice = int(raw_input())                      # choice for entering into friend list
        if choice == 1:                                #entering choice in int
            print"Opening firend list"

            while 1 == 1:                              #loop added
                print"\t1.Add-friend\n\t2.select friend\n\t3.back"
                option = int(raw_input())     
                if option == 1:                        
                    def add_friend():                  #defined add friend
                        while 1==1:                    #loop added
                            salutation = raw_input("Mr/Mrs:")        # salution
                            if len(salutation) != 0:   #condition for salutation
                                break;
                            print "Invalid salutation\n\tre-enter"
                        while 1==1:                    #loop added
                            spy_name = raw_input("Enter your name:")  # spy_name
                            if len(spy_name) != 0:     
                                break;
                            print "invalid name\n\tre-enter"
                        age = int(raw_input("Enter your age:"))       # spy_age
                        if age >= 12 and age <= 50:
                            print "Eligible"
                        else:
                            print "Not Eligible"
                            exit()                                    #exiting code for not eligible age
                        print "Enter your rating between 1-10"
                        rating = float(raw_input("Enter your ratings:"))  # spy_rating
                        if rating<=4:
                            print"Your rating is poor than defualt user"
                            exit()                                   #exiting code not greater than user rating
                        if rating>=0 and rating<=4:
                            print "Very poor"
                        elif rating>=4 and rating<=7:
                            print "Very good"
                        elif rating>=7 and rating<=10:
                            print "Excellent"
                        else:
                            print "Not eligible for this rating"
                            exit()                                 #exit code here
                        # calling class into variable

                        frn = Name(salutation, spy_name, age, rating)#variable frn taken for name class
                        print "Adding..."
                        print "Your added to my friend list", '-' + frn.spy_name
                        # inserting frn variable into list of list_friend
                        list_friend.append(frn)                     #addind new user here in list

                    add_friend()                                    #call function
                  # selecting friend from friend_list
                  # checkout friends position

                elif option == 2:                               
                    print"Select a friend"
                    item = 1
                    for new_friend in list_friend:
                        print "%d. %s " % (item, new_friend.spy_name)
                        if new_friend.rating > 4:                    #condition aplly here
                            a = "Very good"
                        else:
                            a = "Poor"
                        print "Age-%d\tRating-%d(%s)" % (new_friend.age, new_friend.rating, a)
                        item = item + 1
                    friend_choice = int(raw_input("Enter your choice:"))
                    friend_choice_position = list_friend[friend_choice - 1]
                    print "selected friend %s" \
                          % friend_choice_position.spy_name
                elif option == 3:
                    print "starting hike chating"
                    print choice                                     # calling  hike message menu
                    break;                                           # closing loop here'''

                   
        elif choice == 2:
            while 1 == 1:                                            # loop added
                print"Opening status update"                         # opening status menu
                print"\t1.Update\n\t2.Old-status\n\t3.Back"
                choose = int(raw_input())
                if choose == 1:
                    print"Loading..."
                    print "Current status is %s " % current_status
                    new_message = raw_input("Enter new status:-")
                    old_status.append(new_message)                   # inserting newmessage in old_status list
                    print"Updating....", (new_message)
                    current_status = new_message  # current status
                    print "Your current status:-" + current_status
                if choose == 2:
                    print "Current status is %s " % current_status
                    print"Select an old-status"
                    item = 1
                    for temp in old_status:
                        print "%d. %s" % (item, temp)
                        item = item + 1
                    spam = int(raw_input("Enter your choice:"))
                    new_message = old_status[spam - 1]
                    old_status.append(new_message)
                    print "Old-status updating... " + new_message
                    current_status = new_message
                    print "Your current status:" + current_status
                    break;

                if choose == 3:                                    # calling hike message menu here
                    print "Start hike chating"
                    print choice

        elif choice == 3:
            while 1 == 1:                                          # loop added
                print "Opening chat message"                       # opening chat_message menu
                print "\t1. Sending message\n\t2. Read message\n\t3.Chat history\n\t4.back"
                select = int(raw_input())
                if select == 1:
                    item_number = 1                                #item is the friend no in the list
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend.spy_name)  # string and int added
                        item_number = item_number + 1
                    friend_choice = raw_input("Choose from your friends")

                    friend_choice_position = int(friend_choice)
                    friend_choice_position = friend_choice_position - 2
                    print "Selected friend %s" \
                          % list_friend[friend_choice_position].spy_name
                    original_image = raw_input("What is the name of the image?")  # path of image
                    output_path = raw_input('Output.jpg:')                        # out-put path of image
                    text = raw_input("What do you want to say?")                  # number of words
                    
                    # hiding secret messsage in pictures (encode by steganograpy

                    Steganography.encode(original_image, output_path, text)
                    new_chat = {                                                   # adding dictionary here
                        "message": text,
                        "time": datetime.now(),
                        "delivered": True, 'by_me': True
                    }           
                    
                    list_friend[friend_choice_position].chat.append(new_chat)

                elif select == 2:

                    item_number = 1                                            #friend position no
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend.spy_name)
                        item_number = item_number + 1
                    friend_choice = raw_input("Choose from your friends")

                    friend_choice_position = int(friend_choice)
                    friend_choice_position = friend_choice_position - 2
                    output_path = raw_input("Path of the output.jpg:")
                    text = Steganography.decode(output_path)                    #decoding message here
                    print "Decoded message :%s" % text
                    if text == None
                        print "There is no secret message"
                    elif text == "SOS":  # emergency code message                 #for sos message
                        print "Save our souls"
                    elif text == "save me":                                     #save me message
                        print "Emergency needs"
                    new_chat = {                                                # adding dictionary  here
                            "message": text,
                            "time": datetime.now(),
                            "delivered": True, 'by_me': False
                        }
                    for temp in text.split():                                    # split is use to calculate word
                        text_list.append(temp) 


                    list_friend[friend_choice_position].chat.append(new_chat)
                    
                    # calculating text more than 100 words delete spy_friend chat

                    if len(text) > 100:
                        print "Maximum message found!!!\t DELETE MESSAGE"
                        del list_friend[2]                                      # deleting friend chat here

                    def average(text):                                          #average of words defined text here
                        lenghts = len(text.split())
                        print 'Average word :%s' % lenghts

                    average(text)                                              #calling function text here

                elif select == 3:
                    # importing datetime and termcolor
                    #chat history
                    print ("Opening chat history")
                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend.spy_name)
                        item_number = item_number + 1
                    friend_choice = int(raw_input("Choose from your friends"))
                    friend_choice = friend_choice - 2
                    for temp in list_friend[friend_choice].chat:
                        cprint("[%s] " % temp['time'], "blue", attrs=['bold']) #using term color here for particular attributes
                        cprint("message:%s" % temp["message"])
                        cprint("new_friend:%s" % new_friend.spy_name, "red")
                        print colored("%s" % datetime.now(), "blue")
                        if temp['by_me'] == True:                              #message sent by me
                            print "Sent by me"
                        elif temp['by_me'] == False:
                            print "Sent by other"                              #message sent by others
                            
                elif select == 4:
                    print"Start hike chating"
                    print choice                                               # returning to hike message menu
                    break;                                                     #breaking loop here
        elif choice == 4:
            print choice
            break;                                                 
        elif choice == 5:
            print "Closing app\n\tVisit us again have a great day"
            exit()
            # loop continue to login and sign up
            # end of coding here
            #closing application




































