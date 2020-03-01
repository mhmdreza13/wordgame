import random
import os
#========Function========
def clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')
#========================
#==========Main==========
#make word list
word =[
    'bannana','apple','apricot','avocado','blackberry','boysenberry','coconut','fig','grape',
    'grapefruit','lemon','lime','mandarin','peach','mango','melon','orange','pineapple','strawberry',
      ]
secret_word=''
word_length=0
secret_list =[]
final_list = []
final_word = []
wrong_guess = 0
character=''
count = 0
start =''
i = 0
while True:
    clear()
    secret_word = ''
    word_length = 0
    secret_list = []
    final_list = []
    final_word = []
    wrong_guess = 0
    secret_word = random.choice(word)
    secret_list =list(secret_word)
    word_length = len(secret_word)
    wrong_guess = len(secret_word)
    count = 0
    character = ''
    start = ''
    i = 0
    #show * in every character
    for i in range (0,word_length):
        final_list.append("*")
    while True:
        clear()
        print("===============================")
        #connect character with no space by ''.join()
        final_word=''.join(final_list)
        print("word:",final_word)
        if final_word == secret_word:
            print("Wow you got it...")
            start = input("DO you want to try again (yes/no) :")
            if start == "no" or start == "yes":
                break
            break
        print("wrong guess is:{}/{}".format(count, word_length))
        character =input("Enter guessing letter:")
        if character in secret_list:
            for i in range (0,word_length):
                if character is secret_list[i]:
                    final_list[i]=character
        if not character in secret_list:
             count +=1
        if count == wrong_guess:
            print ("Sury!!! you use all your opportunity...")
            start = input("DO you want to try again (yes/no) :")
            if start =="no" or start =="yes":
                break

    if start =="no":
        break
    if start == "yes":
        continue
