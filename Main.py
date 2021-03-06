# Printing of colored text on terminal can be done using Colorama Library

# It also makes ANSI escape character sequences (for producing colored terminal text) work Under MS Windows

from colorama import init, Fore

# On Windows, calling init() will filter ANSI escape sequences out of any text sent to stdout or stderr, and replace them with equivalent Win32 calls.

init()

# Python supports regular expressions through the standard python library re

import re

# we will use Steganography to hide our messages

from steganography.steganography import Steganography

#  sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

import sys

from spy_details import spy,Spy,Chat, friends

status_messages = ['Jai Hind, Jai Bharat', 'Jai Jawan Jai Kisan', 'If death strikes before i prove my blood, i swear i will kill death', 'Some goals are so worthy, its glorious even to fail','Only best of the Friends and worst of enemies visit us-Indian Army']

sys.stdout.write(Fore.RED + " \nHello! Let's get started \n")

# Asking the user for input until they give a valid response

while True :

    question = "\nDo you want to continue as %s %s : (Y/N)? \n" % (spy.spy_salutation,spy.spy_name)

    # raw_input is used to take input from the user

    existing = raw_input(question)
    existing = existing.upper()

    # Validating Input

    if existing == 'Y' or existing == 'N' :
        break
    else:
        print "Please enter a valid input \n"
        continue


# add_status function used to add a status update or select status from older messages

def add_status():

    sys.stdout.write(Fore.LIGHTRED_EX+ " ")

    updated_status_message = None

    # if loop to check if user has a current status message or not

    if spy.current_status_message != None:

        print( 'Your current status message is ' + spy.current_status_message + "\n")

    else:

        print ('You don\'t have any status message \n')

    # Asking the user for input until they give a valid response

    while True:

        default = raw_input("Do you want to select older status messages: (Y/N)?: ")

        if default.upper() == 'Y' or default.upper() == 'N':
            break

        else:
            print "Please enter a valid value\n"
            continue


    if default.upper() == 'N':

        while True:

            new_status_message = raw_input("\nWhat status message do you want to set? ")

            # Let's use regular expression

            J4 = r"([a-zA-Z]+)"

            if re.search(J4, new_status_message):

                # append is used to add new status message at the end of list status_message

                status_messages.append(new_status_message)

                updated_status_message = new_status_message

                # I are Happy with your value
                # exiting Loop
                break


            else:

                print "\nPlease Enter a valid message..!"
                continue

    else:

        item_position = 1

        # for loop to print all available status messages

        print "\nOlder Status Messages are: "

        for message in status_messages:

            print '%d. %s \n' % (item_position, message)
            item_position = item_position + 1


        # Asking the user for input until they give a valid response

        while True:

            try:

                message_selection = int(raw_input("\nchoose from above messages : "))

            except ValueError:

                print "\nPlease enter a valid value "
                continue


            if message_selection < 0:
                print "\nSorry, your response must not be negative.\n"
                continue

            elif message_selection > item_position :
                print "\nSorry,your response must be correct"
                continue

            else:

                # value was successfully parsed, and we're happy with its value.
                # exiting the loop
                break

        updated_status_message = status_messages[message_selection - 1]


    if updated_status_message:

        print 'Your updated status message is: %s \n' % (updated_status_message)

    else:

        print "You currently don't have a status message.\n"


    return updated_status_message


def add_friend():

    sys.stdout.write(Fore.YELLOW + " ")

    new_friend = Spy('','',0,0.0)

    # Asking the user for input until they give a valid response

    while True:

        new_friend.spy_name =str(raw_input("\nPlease add your friend's name: "))

        J5 = r"([a-zA-Z]+)"

        if re.search(J5, new_friend.spy_name) :

            # i am happy with the value given
            # exiting loop
            break

        else:

            print "\nPlease Enter a valid value..!!"
            continue

    # Asking the user for input until they give a valid response

    while True:

        new_friend.spy_salutation = raw_input("\nShould i call you Mr. or Ms.?: ")

        J6 = r"([Mm]r)"
        J7 = r"([Mm]s)"

        if re.search(J6, new_friend.spy_salutation) or re.search(J7, new_friend.spy_salutation):

            # i am happy with the vale given
            # exiting loop
            break

        else:

            print "\nPlease enter a valid value.."
            continue



    # Asking the user for input until they give a valid response

    while True:

        try:

            new_friend.spy_age = int(raw_input("\nEnter age: "))

        except ValueError:
            print "\nSorry, i didn't understand that."
            continue

        if new_friend.spy_age < 0:
            print("\nSorry, your response must not be negative")
            continue

        else:
            # i am happy with the value
            # exiting loop
            break

    # Asking the user for input until they give a valid response

    while True:

        try:

            new_friend.spy_rating = float(raw_input("\nEnter rating: "))

        except ValueError:

            print "\nSorry, i didn't understand that."
            continue

        if new_friend.spy_rating < 0:

            print("\nSorry, your response must not be negative")
            continue

        else:
            # i am happy with the value
            # exiting loop
            break




    if len(new_friend.spy_name) > 0 and new_friend.spy_age > 12 and new_friend.spy_age < 50 and new_friend.spy_rating >= spy.spy_rating:

        friends.append(new_friend)

        print '\nFriend Added!'

    else:
        print '\nSorry! Invalid entry. We can\'t add spy with details you provided '


    return len(friends)


def select_a_friend():

    sys.stdout.write(Fore.BLUE + " ")

    item_number = 0

    for friend in friends:

        print '\n%d. %s %s aged %d with rating %.1f is online' % (item_number + 1,friend.spy_salutation, friend.spy_name,friend.spy_age,friend.spy_rating)

        item_number = item_number + 1

    # Asking the user for input until they give a valid response

    while True:

        try:
            friend_choice = int(raw_input("\nChoose from your friends: "))

        except ValueError:

            print "\nSorry, i didn't understand that."
            continue

        if friend_choice < 0:

            print("\nSorry, your response must not be negative")
            continue

        else:
            # i am happy with the value
            # exiting loop
            break


    friend_choice_position = friend_choice - 1

    return friend_choice_position

# sending message to a spy

def send_message():

    sys.stdout.write(Fore.BLACK + "  ")

    friend_choice = select_a_friend()

    # Asking the user for input until they give a valid response

    while True:

        sys.stdout.write(Fore.RED + " ")

        global text

        text = raw_input("\nWhat do you want to say? ")

        J2 = r"([a-zA-z]+" ")"

        # User can only enter a character or words

        if re.search(J2, text):

            # i am happy with the value
            # exiting loop
            break

        else:
            print "\nPlease enter a valid message"
            continue

    # Deleting a spy if it speaks more than 100 words

    if len(text) >100:

        print "\nYou have exceeded the message limit we removing you from chat"
        del friends[friend_choice]

    # If spy sends message like SOS, SAVE ME, YO BRO..... an appropriate message will be displayed  in read message

    elif 'SOS' in text or 'SAVE ME' in text or 'YO BRO' in text:

        app_message = "Help will arrive soon !!"

        new_chat = Chat( app_message, True)

        friends[friend_choice].chats.append(new_chat)

        print "\nYour secret message is ready! "

    else:

        # Enter image name which is currently in project folder
        # Like 1.jpg

        original_image = raw_input("\nWhat is name of the image(Enter image name which is currently in project folder Like 1.jpg): ")

        while True:
            output_path = raw_input("\nEnter the output path: ")

            if len(output_path) > 0 and output_path != " ":
                break

            else:
                print "\n Enter a valid value..!!"
                continue


        Steganography.encode(original_image, output_path, text)

        new_chat = Chat(text,True)

        friends[friend_choice].chats.append(new_chat)

        print "\nYour secret message is ready! "




# read_message function used to read messages send by the user

def read_message():


        sys.stdout.write(Fore.LIGHTBLUE_EX + " ")

        sender = select_a_friend()

        if 'SOS' in text or 'SAVE ME' in text or 'YO BRO' in text:

            for chat in friends[sender].chats:

                if chat.sent_by_me:

                    print "\n" + chat.message

                    # Average Number of words spoken by a spy when receiving a message

            print ("\nAverage Number of words spoken by a spy is: %d") % len(text.split())

        else:

            sys.stdout.write(Fore.LIGHTBLUE_EX + " ")

            while True:
                output_path = raw_input("\nEnter the output path: ")

                if len(output_path) > 0 and output_path != " ":
                    break

                else:
                    print "\n Enter a valid value..!!"
                    continue

            secret_text = Steganography.decode(output_path)

            new_chat = Chat(secret_text, False)

            friends[sender].chats.append(new_chat)

            for chat in friends[sender].chats:

                if chat.sent_by_me:

                    print "\n" + chat.message
                    break

                else:

                    print "\n" + chat.message
                    break

                    # Average Number of words spoken by a spy when receiving a message

            print ("\nAverage Number of words spoken by a spy is: %d") % len(text.split())

# read_chat_history function used to read the chat history of two users

def read_chat_history():

    read_for = select_a_friend()

    print" \n"

    for chat in friends[read_for].chats:

        if chat.sent_by_me:

            # Time will be printed in red colour

            sys.stdout.write(Fore.BLUE +chat.time.strftime("%d %B %Y")+ " ")

            # Spy Salutation and Spy Name will be printed in red colour

            sys.stdout.write(Fore.RED + spy.spy_name)

            # said will be printed in green colour

            sys.stdout.write(Fore.GREEN + " said :")

            # Message will be printed in black colour

            sys.stdout.write(Fore.BLACK + chat.message)

            print '\n'

        else:

            # Time will be printed in blue colour

            sys.stdout.write(Fore.BLUE + chat.time.strftime("%d %B %Y") + " ")

            # Friend Name and salutation will be printed in red colour

            sys.stdout.write(Fore.RED + friends[read_for].spy_salutation + "" + friends[read_for].spy_name)

            # Said will be printed in green colour

            sys.stdout.write(Fore.GREEN + " said: ")

            # Message will be printed in black colour

            sys.stdout.write(Fore.BLACK + " " + chat.message)

            # Style.Reset_All resets foreground, background, and brightness.

            print '\n'




def start_chat(spy):

    spy.spy_name = spy.spy_salutation + " " + spy.spy_name


    if spy.spy_age > 12 and spy.spy_age < 50:


        sys.stdout.write(Fore.BLUE + "\nAuthentication complete. Welcome " + spy.spy_name + " age: " +str(spy.spy_age) + " and rating of: " + str(spy.spy_rating) + ". Proud to have you onboard \n")

        # Printing appropriate message for spy of different ratings

        if spy.spy_rating > 4.5:
            print '\nGreat ace!'
        elif spy.spy_rating > 3.5 and spy.spy_rating <= 4.5:
            print '\nYou are one of the good ones.'
        elif spy.spy_rating >= 2.5 and spy.spy_rating <= 3.5:
            print '\nYou can always do better'
        else:
            print '\nWe can always use somebody to help in the office.'

        show_menu = True


        while show_menu:

            menu_choices =  "\nWhat do you want to do? \n 1. Add a status update \n 2. Add a fiend \n 3. Send a Message \n 4. Read a message \n 5. Read chat history \n 6. Exit the Application \n "


            # Asking the user for input until they give a valid response

            while True:
                try:

                    menu_choice = int(raw_input(menu_choices))

                except ValueError:
                    print "\nSorry, i didn't understand that."
                    continue

                if menu_choice < 0:
                    print("\nSorry, your response must not be negative")
                    continue

                elif menu_choice >= 1 and menu_choice <=6 :
                    # i am happy with the value
                    # exiting loop
                     break

                else:
                    print "Please enter a valid value..!!"
                    continue


            if menu_choice == 1:
                spy.current_status_message = add_status()

            elif menu_choice == 2:
                number_of_friends = add_friend()

                print '\nYou have %d friends' % (number_of_friends)

            elif menu_choice == 3:
                send_message()

            elif menu_choice == 4:
                read_message()

            elif menu_choice == 5:
                read_chat_history()

            else:
                show_menu = False


    else:

        sys.stdout.write(Fore.BLUE +'\nSorry You are not of the correct age to be a spy')



if existing == "Y":

    start_chat(spy)

else:

    spy =Spy('','',0,0.0)

    # Asking the user for input until they give a valid response

    while True:
            sys.stdout.write(Fore.MAGENTA + " ")

            spy.spy_name = raw_input("\nWelcome to spy chat, you must tell me your spy name first: ")

            J3 = r"([a-zA-z]+)"

            if re.search(J3, spy.spy_name):

                # we are happy with the value given
                # Exiting Loop

                break

            else:
                print "\nEnter a valid value..!"
                continue

    # Asking the user for input until they give a valid response

    while True:

        spy.spy_salutation = raw_input("\nShould I call you Mr. or Ms.??? ")

        J = r"([Mm]r)"
        J1 = r"([Mm]s)"

        if re.search(J, spy.spy_salutation) or re.search(J1, spy.spy_salutation):

            break

        else:

            print "\nPlease enter a valid value.."
            continue



    # Asking the user for input until they give a valid response

    while True:

        try:

            spy.spy_age = int(raw_input("\nWhat is your age: "))

        except ValueError:
            print "\nSorry, i didn't understand that."
            continue

        if spy.spy_age < 0:
            print("\nSorry, your response must not be negative")
            continue

        else:
            # i am happy with the value
            # exiting loop
            break

    # Asking the user for input until they give a valid response

    while True:

        try:

            spy.spy_rating = float(raw_input("\nWhat is your spy rating: "))

        except ValueError:
                print "\nSorry, i didn't understand that."
                continue

        if spy.spy_rating < 0:
                print("\nSorry, your response must not be negative")
                continue

        else:
                # i am happy with the value
                # exiting loop

                break

    start_chat(spy)