APP_ACCESS_TOKEN = ''#your token here
BASE_URL = 'https://api.instagram.com/v1/'
print "Collecting data...."

#------=======##### function decalaration for self info--===========#############

def self_info():
    import requests                                               #import libaries, colored
    from termcolor import colored
    print colored("Collecting Self Info....","red")
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print '\nGET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])        #output username
            print 'Profile pic:%s' %(user_info['data']['profile_picture'])#output profile picture
            from urllib import urlretrieve
            name = user_info['data']['username'] + '.jpg'
            urlretrieve(user_info['data']['profile_picture'], name)
#------======== impost os is used to display the images download in the images viewer in linux ---==######
            import os
            os.system("display -delay 5 /root/PycharmProjects/untitled2/%s" % name)
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])#output followers
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])#output following
            print 'No. of posts: %s' % (user_info['data']['counts']['media']) #output no of post

        else:
            print 'User does not exist!'                                    #commit messages
    else:
        print 'Status code other than 200 received!'                        #|||||||||

