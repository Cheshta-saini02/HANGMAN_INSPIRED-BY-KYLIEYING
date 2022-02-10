#importing 4 things 2 are files i.e vocab,hangman_visual and 2 are library's i.e random,string
import random
from vocab import words
from hangman_visual import lives_visual_dict
import string

#we will create a function  i.e get_valid_word to choose  the valid word out of the list, out of errors  with one argument called words which we have imported from file vocab

def get_valid_word(words):
    #create a variable name chose_word and use random.choice to find the word out of list
   chose_word=random.choice(words)
                                    # a condn is their to find the suitable word for game
   while '-' in chose_word or ' ' in chose_word:
        chose_word=random.choice(words)   #keep chosing if the word contains - and ' '
   return chose_word.upper()          #return the word after selection

#create another function named after the game i.e hangman without arguments  to write the entire code
def hangman():
    chose_word=get_valid_word(words)
    #declaring new variables

    inside_word=set(chose_word)                 #it will contain the game of the word
    alphabets=set(string.ascii_uppercase)     #library to check the 26 strings only for the game in upper case
    used_word=set()                            #it will store the aplha being guessed by the user

    lives=7                                     #lives to play the game
    #condn 2 for the user input
    while len(inside_word)>0 and lives>0:
        print('you have ',lives,'lives left  and you have used the letters:' ,' '.join(used_word))

        #what current word is:
        word_list=[letter if letter in used_word else '_' for letter in chose_word ]
                                                 #list comprehension[x if x in list else '_' for x in list2]
        print(lives_visual_dict[lives])
        print('current word' ,' '.join(word_list))

        user_letter=input('guess the letter: ').upper()   #input letter from the user
        #apply condn to check the letters
        if user_letter in alphabets - used_word:
            used_word.add(user_letter)  #if the letter is present inside the list named uesed_word the go to another condn and remove that selected letter out of the list of that word
            if user_letter in inside_word:
                inside_word.remove(user_letter)
                print(' ')
            else:
                lives-=1
        elif user_letter in used_word:
            print('OOPS!..you have already used the letter',user_letter,'try another word')
        else:
            print("Invalid letter!")

            #gets here when the len(chose_word)==0 or lives==0
    if lives==0:
        print(lives_visual_dict[lives])
        print('You are dead!.Sorry..the word was',chose_word,'!!')

    else:
        print('YAY!!....you won.CONGRATS! THE WORD IS ',chose_word,'!!!')


if __name__ == '__main__':
    hangman()
