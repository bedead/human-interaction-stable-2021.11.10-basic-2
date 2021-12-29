
# pip install PyDictionary
# pip install platform
# pip install psutil
# pip install requests
# pip install getpass
# pip install keyboard
# pip install pywhatkit



# to be used in further Versions (pip install tkinter, pip install pysttx3, pip install speechrecogition, pip install wikipedia)

#######################################################################################################################################################################


#######################################################################################################################################################################
import requests
import sys
from time import *
import os
import datetime
from PyDictionary import PyDictionary
import getpass
import platform
import random
import psutil
import keyboard

#######################################################################################################################################################################


url = "https://www.google.com"

try:
    request = requests.get(url, timeout = 2)
    print("You are connected to the Internet")
    import pywhatkit as kit

except(requests.ConnectionError, requests.Timeout) as exception:
    print("No, Internet Connection")


#######################################################################################################################################################################


# predefined and learned data storage

main_passcode = ['sid905030']
main_passcode_digit = 0

user_passcode = {}

ans_yes = ('yes','y')
ans_no = ('n','no')
nexx_info = ['Nexx', 'I am Nexx', 'I am Nexx Version 2021.10.1', 'I have been created by Satyam Mishra Aka Bedead']

greeting = {'good' : ["Good Morning", "Good night", "Good Afternoon", 'Good evening'],
            'casual_start' : ['Hope you are having a good day', 'Nice to meet you','Hey, how do you do?','How do you do?', 'how are you doing?','Pleased to meet you',
                              'How have you been','How’s it going','Nice to see you',"It’s great to see you","Good to see you",'What’s up?','Heyyy'],
            'casual_end_happy' : ['Good Day','Have a nice day','Have a good day', 'Bye, have a nice day','Thanks for this great talk', 'Hope we will meet again'],
            'startup' : ["Hey","hii","Hello","Welcome back"],
            }


q_about_creator = {'who_made': ('who made you', 'who created you', 'how was you created', 'who is your creator', 'who programmed you', 'can i know your creator'),
                   'born_in' : ("your creator was born in",'satyam was born in','bedead was born in','satyam mishra was born in', 'when was satyam born','when was your creator born'),
                   'current_age' : ('what is satyams current age', 'what is bedeads current age', 'how old is satyam mishra','how old is satyam, what is satyams age'),
                   'current_age_total_months' : ('what is satyams age in months','what is bedeads age in months','how old is satyam in months', 'in months how old is satyam',
                                          'how many` months has satyam lived','how many months did satyam live', 'for how many months bedead has lived'),
                   'current_age_total_days' : ('what is satyams age in days','what is bedeads age in days','how old is satyam in days', 'in days how old is satyam',
                                          'how many days has satyam lived','how many days did satyam live', 'for how many days bedead has lived')}                                   

# for checking users entered answer
receive_query_check = {'greeting' : ('i am fine how are you','i am good how are you','i am great how are you','how do you do', 'i am fine how do you do'),
                       'what_doing' : ('what are you doing', 'Are you doing anything','are you doing anything right now','What’s going on','What’s going on in here',
                                       'What is happening right now','What the heck are you doing','What the hell is going on','What are you doing these days'),
                       'help' : ('i need a help', 'i need a small help', 'i need your help', 'i need a small favor from you', 'i have a question','i am having a question',
                                 'can u helpme', 'can you help me', 'Can you help me please', 'I need some assistance','Could you give me a hand','Would you mind helping me please',
                                 'Could you give me a digout'),
                       'what_can_do' : ["what can you do",'what are things you can do','show me what you have got'],
                       'what_time' : ["what time it is",'what is the time', 'what current time',"what is the time now",'can you tell me current time',
                                      'can you tell whats the time'],
                       'send_what_msg' : ["can you send message in whatsapp",'drop a message in whatsapp','deliver a message in whatsapp',
                                          'can you deliver a message in whatsapp','send message']}

# for responding to user
receive_query_check_ans = {'greeting_ans' : (' i am doing great','i am also good','i am fine', 'As allways i am damm good and cool'),
                           'what_doing_ans' : ('just chilling in your devcie', 'what can i program do other then processing?', 'I’m just here thinking about you',
                                               'As usual, missing you','I was just about to ask you that.','Waiting for your question, obviously!','I live here!',
                                               'I was just leaving, bye.', 'What do you mean what am I doing here? It’s a free country','I don’t know, I’m lost.',
                                               'I’m doing what you said to do','None of your business', 'I’m doing my job. What are you doing?'),
                           'help_ans' : ('Let Me Know How I Can Help',' Is there anything you need','Can I get you anything',
                                         'What can I do to help your process','I’m happy to help'),
                           'not_in_data_ans' :('I dont know about this','Sorry, cant help','I am unable to understand','I need more data to understand',
                                               'I am under development'),
                           'what_time_ans' : ("It's around","It's about","Current time is","It's",""),
                           'send_what_msg_phone_ask_ans' : ("What's that number ",'what is that number ',"Please tell me that number ","Enter the number "),
                           'send_what_msg_ask_ans' : ("What should be that msg ","Enter the msg ","What can be that message ","message please ",
                                                      "What's that msg ")}



#######################################################################################################################################################################


def creator_details():
    # defining current_data, born_data, name-
    current = datetime.datetime.now()
    born_in = (2003,"December",6) 
    name = ["Satyam Mishra","Bedead","bedead",'satyam mishra', 'Satyam mishra']


    # calculating totral months and days lived 
    total_months = ((current.year - born_in[0] - 1)*12) + current.month
    total_days = (365*current.year - born_in[0])- ((12 - current.month)*30)
    
    # calculating my current age in year and month
    age = (current.year - born_in[0] - 1, current.month)
    if current.month == 12 and current.day>=6:
        age = (current.year - born_in[0], current.month - 12)

    return name,age,born_in,total_months, total_days, current


 
# method for current data 
def get_current_info():
    
    current = datetime.datetime.now()
    year = current.year
    month = current.month
    day = current.day
    hour = current.hour
    minute = current.minute
    second = current.second
    microsecond = current.microsecond

    time = "%s:%s:%s" % (hour,minute,second)

    return time


# method for getting meanings and translationa and more
def pydictionary():

    # instancing pydictionary
    word = PyDictionary()


    # getting meaning of thr word
    meaning = word.meaning()

    # getting synnonym of the word
    synonym = word.synonym()

    # getting antonym of the word
    antonym = word.antonym()

    # getting words and sentences translated
    translate = word.translate()


# method to fretch device details and user details
def device_user_details():
    
    username = getpass.getuser()
    print(username)

    this_system = platform.uname()

    operating_system = this_system.system

    device_node = this_system.node
    device_release = this_system.release
    device_version = this_system.version
    device_machine = this_system.machine
    device_processor = this_system.processor


def memory_usage():
    # yet to be coded #
    ###################
    memory_detail = psutil.virtual_memory()
    print(memory_detail)


# a method yo send a reset key for password reset
def sending_whatmsg_instantly(phone_number,msg):

    
    try:
        kit.sendwhatmsg_instantly(f"+91{phone_number}", msg)
        sleep(17)
        keyboard.press_and_release("enter")
        return True
    except:
        return False
    

def random_reset_key():
    avail_num = [0,1,2,3,4,5,6,7,8,9]
    reset_key = str()

    for i in range(1, 6):
        reset_key += str(random.choice(avail_num))

    return reset_key


def sending_custom_whatsmsg():
    device_num = input(nexx_info[0]+' - '+random.choice(receive_query_check_ans.get('send_what_msg_phone_ask_ans')))
    if len(device_num) == 10:
        device_msg = input(nexx_info[0]+' - '+random.choice(receive_query_check_ans.get('send_what_msg_ask_ans')))

        if device_msg != None:
            send = sending_whatmsg_instantly(device_num, device_msg)
            
            if send == True:
                print(nexx_info[0]+' - '+"Your message is delivered")
            
            else:
                print(nexx_info[0]+' - '+"Your messege can't be send now\nTry again")
            
        else:
            print(nexx_info[0]+' - '+"Entered msg doesn't contain anything\nRetry sending")
            sending_custom_whatsmsg()
    else:
        print(nexx_info[0]+' - '+"Entered number is greater or less then 10\nRetry sending")
        sending_custom_whatsmsg()
    return send


#######################################################################################################################################################################



# code to start a simple converstiion
def human_interation_text():
    
    
    

    def security_check_for_admin(main_passcode, main_passcode_digit):

        
        pass_code = str(input(nexx_info[0]+' - '+"Can you please enter the passcode : "))


        if pass_code == main_passcode[main_passcode_digit]:
            
            print(nexx_info[0]+' - ', random.choice(greeting.get('casual_start')))
            
            while True:
                
                n = input(opertor_name+" - ")
                n= n.lower()
                   
                if n in q_about_creator.get('who_made'):
                    print(nexx_info[0]+' - ',nexx_info[3])
                    
                elif n in q_about_creator.get('born_in'):
                    print(nexx_info[0]+' - ',"he was born in",born_in[0],",", born_in[2],born_in[1] )
                    
                elif n in q_about_creator.get('current_age'):
                    print(nexx_info[0]+' - ',random.choice(name), "is currently", age[0],'years', age[1],'months old')
                    
                elif n in receive_query_check.get("what_doing"):
                    print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('what_doing_ans')))
                    
                elif n in receive_query_check.get('greeting'):
                    print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('greeting_ans')))
                    
                elif n in receive_query_check.get('help'):
                    print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('help_ans')))
    
                elif n in receive_query_check.get('send_what_msg'):
                    send = sending_custom_whatsmsg()
                elif n == "show me data":
                    # yet to be coded #
                    ###################
                    memory_usage()
                    
                elif n in receive_query_check.get('what_time'):
                    time = get_current_info()
                    print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get("what_time_ans")),time)
                          
                else:
                    print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('not_in_data_ans')))
                    
        else:
            retry = str(input(nexx_info[0]+' - '+"Would you like to re-enter the passcode(y or n) : "))
            retry.lower()

            if retry in ans_yes:
                security_check_for_admin(main_passcode, main_passcode_digit)

            elif retry in ans_no:
                retry_times = 2
                forgot_pass = input(nexx_info[0]+' - '+"Would you like to change your password(y or n) : ")

                if forgot_pass in ans_yes and (retry_times >0):
                    
                    reset_key = random_reset_key()
                    
                    send = sending_whatmsg_instantly(9550739128,"Hey, Satyam this is your password reset key :\n%s" % reset_key)
                    if send == True:

                        sleep(.5)
                        print(nexx_info[0]+' - ',"A reset key has been send to your Whatsapp number")

                        compare_key = str(input(nexx_info[0]+' - '+"Enter the reset key to change your password : "))

                        if compare_key == reset_key:
                            new_passcode_admin = str(input(nexx_info[0]+' - '+"Enter your new password : "))
                            anim = "Changing your passcode...."
                            for i in anim:
                                print(i,end=" ",flush=True);sleep(.2)
                            main_passcode_digit +=1
                            main_passcode += [new_passcode_admin]
                            
                            print(nexx_info[0]+' - '+"Your new password has been saved")
                            print(main_passcode[main_passcode_digit])

                            security_check_for_admin(main_passcode, main_passcode_digit)

                        else:
                            print(nexx_info[0]+' - '+"You have one more change left for today")

                            # yet to be coded #
                            ###################
                            
                elif forgot_pass in ans_no:
                    # yet to be coded #
                    ###################
                    pass




    def opertor_access():
        while True:
                
            n = input(opertor_name+" - ")
            n= n.lower()
                   
            if n in q_about_creator.get('who_made'):
                print(nexx_info[0]+' - ',nexx_info[3])
            elif n in q_about_creator.get('born_in'):
                print(nexx_info[0]+' - ',"he was born in",born_in[0],",", born_in[2],born_in[1] )
            elif n in q_about_creator.get('current_age'):
                print(nexx_info[0]+' - ',random.choice(name), "is currently", age[0],'years', age[1],'months old')
            elif n in receive_query_check.get("what_doing"):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('what_doing_ans')))
            elif n in receive_query_check.get('greeting'):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('greeting_ans')))
            elif n in receive_query_check.get('help'):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('help_ans')))
            else:
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('not_in_data_ans')))
                
            

    
    print(nexx_info[0]+' - ',random.choice(greeting.get('startup'))+",", nexx_info[1], flush=True);sleep(0.2)
    opertor_name = str(input(nexx_info[0]+" - Can I know your name : "))
    
    if opertor_name in name:
        print(nexx_info[0]+' - ',random.choice(greeting.get('startup')), random.choice(name))
        if current.hour >0 and current.hour <= 12:
            print(nexx_info[0]+' - ',greeting.get('good')[0])
        elif current.hour > 12 and current.hour <= 16:
            print(nexx_info[0]+' - ',greeting.get('good')[2])
        elif current.hour > 16 and current.hour <= 19:
            print(nexx_info[0]+' - ',greeting.get('good')[3])
        elif current.hour > 19 and current.hour <=24:
            print(nexx_info[0]+' - ',greeting.get('good')[1])


        security_check_for_admin(main_passcode, main_passcode_digit)

        
            
            
    elif opertor_name in user_passcode.keys():
        pass_code = str(input(nexx_info[0]+' - '+"Can you please enter the passcode : "))
        
        if pass_code == user_passcode.get(opertor_name):
            print(nexx_info[0]+' - ',random.choice(greeting.get('startup')),opertor_name)

            opertor_access()
        else:
            print(user_passcode.get(opertor_name))
            
            
    else:
        print(nexx_info[0]+' - ', "Ohh. you seem new")
        register_y_n = str(input(nexx_info[0]+' - '+"Do you want to register your details to gain access over this program(Y or N):"))
        register_y_n.lower()

        if register_y_n in ans_yes:
            user_name = str(input(nexx_info[0]+' - '+"What should be your name : "))
            pass_code_data = str(input(nexx_info[0]+' - '+'Create a Passcode : '))
            print(nexx_info[0]+' - ',"Let me add you to database")
            anim = "Adding...."
            for i in anim:
                print(i,end=" ",flush=True);sleep(.2)

            
            user_passcode[user_name] = pass_code_data;sleep(.1)

            print("Added")

            main_run()
        elif register_y_n in ans_no:
            print(nexx_info[0]+' - ', "Ok, I am shuting down this program");sleep(.5)
            anim = "Shuting....."
            for i in anim:
                print(i,end=" ",flush=True);sleep(.2)

        
    
name,age,born_in,total_month,total_days,current = creator_details()


#######################################################################################################################################################################



def main_run():
    human_interation_text()

    
main_run()


#######################################################################################################################################################################


