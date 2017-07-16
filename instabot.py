import sname  # adding here sname

APP_ACCESS_TOKEN = ''  # your token id
BASE_URL = 'https://api.instagram.com/v1/'  # link of site


# ------######===== definding function for get post id========#######=--------
# by using endpoints on developer page

def get_post_id(username):
    user_id = uname.get_user_id(username, BASE_URL, APP_ACCESS_TOKEN)
    if user_id == None:
        print 'User does not exist!'
        exit()                                                          # exiting here for non valid user id
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (
    user_id, APP_ACCESS_TOKEN)                                          #respones endpoint
    print '\nGET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()                       # calling response for enpoints
    if user_media['meta']['code'] == 200:
        i = 1                                                           # variable use i and j
        j = 0
        post = []                                                       # taking post list here
        if len(user_media['data']):
            for temp in user_media['data']:                             # for loop is use
                if j > 3:
                    break                                               # breaking loop after 3 times
                post.append(temp['id'])
                print "%d. %s" % (i, temp['id'])
                i = i + 1
                j = j + 1
            return post                                                 # return id into the post list
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

# -------###########=======definding function for add a comment----====#####==
# by using endpoints from developer page----/


def add_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    a = int(raw_input("Select post id:"))                       # selecting a user post id to comment
    comment_text = raw_input("Your comment: ")                  # type text tocomment
    payload = {"access_token": APP_ACCESS_TOKEN,
               "text": comment_text}                            # The data being sent with the POST request payload,
    request_url = (BASE_URL + 'media/%s/comments') % (media_id[a - 1])
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()   # sending comment to the request url

    if make_comment['meta']['code'] == 200:                     # enpoints response
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"


# =======-------###### Starting instabot here ##3----========

while 1 == 1:                                                   # loop added
    from termcolor import colored                               # importing colored here

    print colored("WELCOME TO INSTABOT", "green")               # greetings
    print colored("SELECT OPTION", "blue")                      # select option
    print"\t1.Self info:\t2.Other user:"                        # chosse your choice
    choose = raw_input("")
    if choose == "2" or choose == "2":
        username = raw_input("Enter a insta_username: ")        # enter insta username here
        from termcolor import colored

        print colored("Collecting User Info Data.....", "red")
        import requests, uname                                  # importing iibaries and username here

        uname.get_user_id(username, BASE_URL, APP_ACCESS_TOKEN) # called function user id by import
        uname.user_info(username)                               # called function user info by import
        while 1 == 1:                                           # added loop here
            from termcolor import colored                       # colored import here

            print colored("\nSelect option:", "red")

# -------======######## menu option for user detiails----======##########

            print "\t1.Recent post details\n\t2.Post id\n\t3.Like a Post\n\t4.Comment On a Post "
            choose = raw_input("")                              # input your choice
            if choose == "1":
                from termcolor import colored                   # colored import

                print colored("Collecting Recent Post Details....", "blue")
                APP_ACCESS_TOKEN = ''#your token here
                BASE_URL = 'https://api.instagram.com/v1/'


# -----=======#######definding function for get user post---====########

                def get_user_post(username):
                    user_id = uname.get_user_id(username, BASE_URL, APP_ACCESS_TOKEN)  # importing here uname
                    if user_id == None:
                        print 'User does not exist!'
                        exit()
                    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
                    print 'GET request url : %s' % (request_url)
                    user_media = requests.get(request_url).json()  # geting usermedia by request url
                    if user_media['meta']['code'] == 200:          # response endpoints
                        i = 1                                      # variable taken i and j
                        j = 0
                        post = []                                  # taking post list
                        if len(user_media['data']):
                            for temp in user_media['data']:        # for loop use
                                if j > 3:
                                    break                          # breaking loop here

                                print '\nUsername: %s' % (temp['user']['username'])  # output user name
                                print 'post id:%s' % (temp['id'])                    # output post id
                                print 'Caption:%s' % (temp['caption']['text'])       # output cation text
                                print 'No. of likes:%s' % (temp['likes']['count'])   # output no of likes
                                print 'No. of comments %s:' % (temp['comments']['count'])  # output no of comment
                                from urllib import urlretrieve                       # urlretrieve import here
                                name = temp['user']['username'] + '.jpg'             # varialble name
                                urlretrieve(temp['images']['standard_resolution']['url'], name)  # image resolution

# -------------###########importing os to display the images on the images viewer on kali linux----#########

                                import os
                                os.system("display -delay 5 /root/PycharmProjects/untitled2/%s" % name)
                                i = i + 1
                                j = j + 1
                                from termcolor import colored                         # coloured import
                                print colored('Downloaded images....', "red")
                                print colored("\nCollecting Recent post Details.....", "blue")
                                post.append(temp['id'])

                            print 'No. of posts: %d' % i                              # output no of post here
                            return post                                               # return to post list
                        else:
                            print 'User does not exist!'
                    else:
                        print 'Status code other than 200 received!'


                get_user_post(username)                                               # calling function

# ------===###By selecting choose== 2 it will called the function of get post id which is defined in above--###

            if choose == "2":
                from termcolor import colored                                         # colored import

                print colored("Collecting Post ID....", "blue")
                APP_ACCESS_TOKEN = ''  # your token here
                BASE_URL = 'https://api.instagram.com/v1/'

                get_post_id(username)                                                 # called function post id

            if choose == "3":
                while 1 == 1:
                    from termcolor import colored                                     # colored import

                    print colored("Select option")                                    # select option
# ----=====####### Menu for likes,dislikes,back====------#############
                    print "\t1.likes\n\t2.dislikes\n\t3.back"
                    select = raw_input("")                                            # input parameter
                    if select == "1":
                        from termcolor import colored                                 # colored import

                        print colored("Collecting data.....", "blue")
                        print colored("Select post ID to like ", "red")
                        APP_ACCESS_TOKEN = ''  # your token here
                        BASE_URL = 'https://api.instagram.com/v1/'


# -----====##### definding function like a post here---=====###################

                        def like_a_post(insta_username):
                            media_id = get_post_id(insta_username)                    # geting post id here
                            med_id = int(raw_input("Select post id: "))               # select post id
                            request_url = (BASE_URL + 'media/%s/likes') % (media_id[med_id])
                            payload = {
                                "access_token": APP_ACCESS_TOKEN}  # The data being sent with the POST request payload,
                            print 'POST request url : %s' % (request_url)             # output post id here
                            post_a_like = requests.post(request_url, payload).json()  # sending like to the post
                            if post_a_like['meta']['code'] == 200:
                                print 'Like was successful!'
                            else:
                                print 'Your like was unsuccessful. Try again!'        # commit message


                        like_a_post(username)                                         # called function here
                    elif select == "2":
                        from termcolor import colored                                 # colored import

                        print colored("Collecting data.....", "blue")
                        print colored("Select post ID to dislike", "red")
                        APP_ACCESS_TOKEN = ''  # your token here
                        BASE_URL = 'https://api.instagram.com/v1/'


# ----=====############## declaration function for dislike a post===------##################

                        def dislike_post(insta_username):
                            media_id = get_post_id(insta_username)                    # geting post id here
                            med_id = int(raw_input("Select post id: "))               # select post id input
                            request_url = (BASE_URL + 'media/%s/likes/?access_token=%s') % (
                            media_id[med_id], APP_ACCESS_TOKEN)
                            print 'POST request url : %s' % (request_url)
                            post_a_like = requests.delete(request_url).json()         # deleting likes here
                            if post_a_like['meta']['code'] == 200:
                                print 'dislike was successful!'
                            else:
                                print 'Your dislike was unsuccessful. Try again!'     # commit message


                        dislike_post(username)                                        # called function

                    else:

                        print choose                                     # returning to the choose menu
                        break
            if choose == "4":
                while 1 == 1:                                                         # loop added
                    print colored("Select option", "red")

# --------====######### Menu for comments option-----------===========####################

                    print "\t1.Add comment\n\t2.Comment id\n\t3.Del comment\n\t4.Targeted comment\n\t5.Exit"
                    select = raw_input("")                                            # input parameter
                    if select == "1":
                        from termcolor import colored                                 # coloured import

                        print colored("Collecting data.....", "blue")
                        print colored("Select post ID to comment post", "red")
                        APP_ACCESS_TOKEN = ''  # your token here
                        BASE_URL = 'https://api.instagram.com/v1/'

                        add_a_comment(username)                                       # called function
                    if select == "2":
                        from termcolor import colored                                 # coloured import

                        print colored("Collecting data.....", "blue")
                        print colored("Showing comment post ID", "red")
                        APP_ACCESS_TOKEN = ''  # your token here
                        BASE_URL = 'https://api.instagram.com/v1/'


# ------===========##### function declaration of comment id------===========##############

                        def comment_id(insta_username):
                            media_id = get_post_id(insta_username)                    # geting post id here
                            a = int(raw_input("Select post id:"))                     # select post id here
                            request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (
                                media_id[a - 1], APP_ACCESS_TOKEN)
                            print 'comment request url : %s' % (request_url)

                            make_comment = requests.get(request_url).json()

                            if make_comment['meta']['code'] == 200:
                                i = 1                                                 # variable i and j
                                j = 0
                                coment = []                                           # coment list taken here
                                if len(make_comment['data']):
                                    for temp in make_comment['data']:                 # for loop take
# ----------========#### breaking for loop after excueting 3times loop will break here---======####

                                        if j > 3:
                                            break                                     # breaking loop
                                        coment.append(temp['id'])                     # adding comment to list
                                        print "%d. %s" % (i, temp['text'])
                                        i = i + 1
                                        j = j + 1
                                    return coment                                     # returning to list coment
                                else:
                                    print "Error!"
                            else:
                                print "Unable to add comment. Try again!"             # commit messages


                        comment_id(username)                                          # called function

                    if select == "3":
                        from termcolor import colored                                 # colored import

                        print colored("Collecting data.....", "blue")
                        print colored("Select post ID to del comment")
                        APP_ACCESS_TOKEN = ''  # your token here
                        BASE_URL = 'https://api.instagram.com/v1/'


# ----------============######### function declaration for del comments-==----------====####

                        def del_comment_id(insta_username):
                            media_id = get_post_id(insta_username)                    # geting post id here
                            a = int(raw_input("Select post id:"))                     # input parameter
                            request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (
                                media_id[a - 1], APP_ACCESS_TOKEN)
                            print 'comment request url : %s' % (request_url)

                            make_comment = requests.get(request_url).json()

                            if make_comment['meta']['code'] == 200:
                                i = 1                                                 # variables i and j
                                j = 0
                                coment = []                                           # list coment
                                if len(make_comment['data']):
                                    for temp in make_comment['data']:                 # foor loop
                                        if j > 3:
                                            break                                     # breaking loop
                                        coment.append(temp['id'])
                                        print "%d. %s" % (i, temp['text'])
                                        i = i + 1
                                        j = j + 1
                                    b = int(raw_input("Select comment id:"))          # selecting comment id
                                    request_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (
                                        media_id[a - 1], coment[b - 1], APP_ACCESS_TOKEN)
                                    print 'comment request url : %s' % (request_url)
                                    r = requests.delete(request_url).json()           # deleting comment here
                                    if r['meta']['code'] == 200:
                                        print "Comment deleted"
                                    else:
                                        print "Error :%s" % r['meta']['code']
                                else:
                                    print "Error!"
                            else:
                                print "Unable to add comment. Try again!"              # commit message


                        del_comment_id(username)                                       # called function
                    if select == "4":

# -----==============######### function declaration for targetted comment=----=========--------#########

                        def targetted_post(username):
                            from termcolor import colored                              # colored import
                            print colored("Collecting data.....")
                            print colored("Search caption for post", "red")
                            user_id = uname.get_user_id(username, BASE_URL, APP_ACCESS_TOKEN)
                            if user_id == None:
                                print 'User does not exist!'
                                exit()                                                 # exit if doesnot exist

                            request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (
                            user_id, APP_ACCESS_TOKEN)
                            print 'GET request url : %s' % (request_url)
                            user_media = requests.get(request_url).json()              # geting user media here
                            option = raw_input("Search caption post :")                # searching caption post here
                            if user_media['meta']['code'] == 200:
                                if len(user_media['data']):
                                    for temp in user_media['data']:                    # for loop and variable temp
                                        if temp != None and temp['caption'] != None:
                                            if temp['caption']['text'] == option:
                                                from urllib import urlretrieve
                                                name = temp['id'] + '.jpeg'
                                                urlretrieve(temp['images']['standard_resolution']['url'], name)
                                                print "Downloaded post %s" % name      # download cation post here
                                                comment_text = raw_input("Your comment: ")  # add your comments
                                                payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
                                                request_url = (BASE_URL + 'media/%s/comments') % (temp['id'])
                                                print 'POST request url : %s' % (request_url)
                                                raw = requests.post(request_url, payload).json()
                                                if raw['meta']['code'] == 200:
                                                    print "Comment added"
                                                else:
                                                    print "Error while commenting"       # commit messages

                                else:
                                    print 'User does not exist!'
                            else:
                                print 'Status code other than 200 received!'             # |||||||||||


                        targetted_post(username)                                        # called function

                    if select == "5":
                        exit()
                                                                                        # exiting code here
    else:

#--=========##### calling function decalaration of self info----====########

        sname.self_info()                                                               #called function here
    while 1 == 1:                                                                       #loop added

        print "\nSelect option"                                                         #select option

#-----===========#### Menu option for self details-----=========#############
        print "\t1.Recent post details\n\t2.Exit(back to instabot)"
        choice = raw_input("")                                                           #input parameter
        if choice == "1":
            from termcolor import colored                                                #colored import

            print colored("Collecting post....", "red")
            APP_ACCESS_TOKEN = ''     #you token here
            BASE_URL = 'https://api.instagram.com/v1/'

#---------======#####function decalaration for get own post---======##########

            def get_own_post():
                import requests
                request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
                print '\nGET request url : %s' % (request_url)
                own_media = requests.get(request_url).json()                            #geting self media

                if own_media['meta']['code'] == 200:
                    i = 0                                                               #varialble i and j
                    j = 0
                    if len(own_media['data']):
                        for temp in own_media['data']:                                  #foor loop
                            if j > 3:
                                break                                                   #breaking loop
                            print 'Username: %s' % (temp['user']['username'])           #output username
                            print 'post id:%s' % (temp['id'])                           #output post id
                            print 'Caption:%s' % (temp['caption']['text'])              #output caption text
                            print 'No. of likes:%s' % (temp['likes']['count'])          #output likes
                            print 'No. of comments%s:' % (temp['comments']['count'])    #output comments
                            from urllib import urlretrieve
                            name = temp['user']['username'] + '.jpg'
                            urlretrieve(temp['images']['standard_resolution']['url'], name)

# -------------###########importing os to display the images on the images viewer on kali linux----#########

                            import os
                            os.system("display -delay 5 /root/PycharmProjects/untitled2/%s" % name)
                            i = i + 1
                            j = j + 1
                            from termcolor import colored                              #colored import
                            print colored("Downloaded images.....", "red")

                        print 'No. of posts: %d' % i                                   #output no of post

                    else:
                        print 'User does not exist!'                                   #commit messages
                else:
                    print 'Status code other than 200 received!'


            get_own_post()                                                             #called function
        if choice == "2":
            break
#---======##### Breaking while loop Menu option for self details- here---======####
#loop continue to instabot




