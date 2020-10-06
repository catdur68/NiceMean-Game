# Python 3.8.5



''' The Tech Academy p159 - exercise
    Nice or Mean Game
    basic Python program
    --> demonstrate how to pass variables from function to function
    --> return values will be returned back to the calling function
'''



def start(nice=0, mean=0, name=""): # that is controlling the default values 
    # sets the default values for 3 variables - variable name is empty as its value will be given by user input
    # invite user to give a name which will really start the program
    name = describe_game(name)
    #now we need to call the function that will change the default values for nice and mean and store them 
    nice, mean, name = nice_mean(nice,mean,name)

def describe_game(name): # this is the first function that the start function is calling
    """
        this will check if this is a new game or not (either the program has just opened, or this is another round.
        If it is new, we will need to obtain a name from the user.
        If it is not new, we thank the player for playing again and continue with the game
    """
    print(name)
    #to check whether this is a new game, we check whether we already have a name (FROM A PREVIOUS GAME)
    if name !="":
        print("\nThank you for playing again, {}".format(name))
    #if the name variable is empty, then we ask for a name and tell the player how the game is played
    else: # that is really what fires up the game
        stop = True # we are creating a variable that will act like a switch 
        while stop is True: # as long as the name variable is empty, do all these things until stop is no longer true, meaning we have obtained a name
            if name == "": # and it is (because we are in the else statement)          
                name = input ("\nWhat is your name? \n>>>").capitalize() # we are getting a name, and now the variable is no longer empty
            if name != "": #if the input from the user is not empty
                print("\nWelcome, {}".format(name))
                print("\nIn this game you will be greeted \n by several different people. \nYou can choose to be nice or mean")
                print("but at the end of the game your fate \nwill be sealed by your actions.")
                stop = False #that ends the while loop, the switch is now off
    return name

def nice_mean(nice, mean, name): # this is the second function that the start function is calling - that is the game function
    # in the start function nice and mean were set at 0 by default
    # now we need to create a swtich on/off which are the conditions under which the games goes on or off
    stop = True
    while stop:
        # show the current scores and the scores after the player's input
        show_score(nice, mean, name)# this is calling a show_score function that will be defined in our next block of code
        pick = input("\nA stranger approaches you for a conversation. Will you be nice or mean? (N/M) \n>>>:").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = nice + 1
            stop = False # we stop asking the "pick" question
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = mean + 1
            stop = False
            
    score(nice, mean, name) # calling the next function that now has current values
    
def score(nice, mean,name): # this function is getting its values obtain when running the previous function (nice_mean)
    if nice > 2:
        win(nice,mean,name) # calling the win function not yet defined
    if mean > 2:
        lose(nice,mean,name) # calling the lose function not yet defined
    else: #calling the nice_mean function again and passing the 3 variables as the new starting points 
        nice_mean(nice,mean,name)

def show_score(nice, mean, name): # we got the name from the beginning of the game, and now the nice-mean function gave us current scores
    print("\n{},your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def win(nice, mean, name): # just interacting with the user in a personal way (message to user using its name)
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way".format(name))
    again(nice, mean, name) # calling the next function which asks whether to play again

def lose(nice, mean, name):
    print("\nGame over: you were too mean, {}!".format(name))
    again(nice, mean, name)

def again(nice, mean, name): # asking user if they want to play again
    # once again we need to create a switch
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False # this stops the request for input
            reset(nice,mean,name) # calling the reset game function not yet defined
        if choice == "n":
            print("\nOh, no, so sad, sorry to see you go")
            stop = False
            quit()
        else: # this is forcing the user to provide an answer to the question "play again?"
            print("\nEnter (Y) for 'YES', (N) for 'NO': \n>>> ")
    

def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)


if __name__ == "__main__":
    start()
