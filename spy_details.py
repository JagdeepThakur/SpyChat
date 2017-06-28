from datetime import datetime

# Spy class is used to define a spy personality

class Spy:

    #_ init_ is a constructor

    # It is used for autamatic initialization of member of an object as soon as an object is created

    def __init__(self, spy_name,spy_salutation, spy_age, spy_rating):

        # Self is an refrence to the instance of the class that the method is of
        # Here instance of class refers to  object of class

        self.spy_name = spy_name
        self.spy_salutation = spy_salutation
        self.spy_age = spy_age
        self.spy_rating = spy_rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chat:

    def __init__(self,message,sent_by_me):

        self.message = message

        # now function returns current date and time

        self.time = datetime.now()

        self.sent_by_me = sent_by_me


spy = Spy('Jagdeep Thakur','Mr ',18,4.5)

friend_one = Spy('Vishav Gupta', 'Mr ', 19, 4.6)
friend_two = Spy('keshav Mahajan ', 'Mr ', 20, 4.6)
friend_three = Spy('Ed Sheeran', 'Mr ', 30, 5)

# we created a list named friends

friends = [friend_one, friend_two, friend_three]
