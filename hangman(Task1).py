import random
words=["star","player","python","fish"]
chosen_word=random.choice(words)

length=len(chosen_word)
lives=7
list=[]
guessed_words=[]

def hangman(lives):
    if lives == 6:
        print('________')
        print('        |')
    if lives == 5:
        print('________')
        print('        |')
        print('        O')
    elif lives == 4:
        print('_________')
        print('         |')
        print('       \\ O  ')

    elif lives == 3:
        print('_________')
        print('         |')
        print('       \\ O / ')
    elif lives == 2:
        print('_________')
        print('         |')
        print('       \\ O / ')
        print('         |')
        print("Hurry Up")

    elif lives == 1:
         print('_________')
         print('         |')
         print('       \\ O /')
         print('         |')
         print('        /')
    elif lives == 0:
        print('_________')
        print('         |')
        print("       \\ O / ")
        print('         |')
        print('        / \\ ')
        print("You Lost")
         
for letter in chosen_word:
        list.append(letter)

list_len=len(list)
print()
while lives>=0:
    hangman(lives)
    print(f"You have {lives} lives")
    main_word=""
    for letter in chosen_word:
        if letter in guessed_words:
            main_word=main_word+letter
        else:
            main_word=main_word+"_ "
    print(main_word)
    if lives>0:
        guess=input('Enter your guess')
    if guess in list and guess not in guessed_words:
        print('match')
        guessed_words.append(guess)
    elif guess not in list:
        print("Wrong Guess")
        lives-=1
    elif guess in guessed_words:
         print("Already Guessed")
    if len(guessed_words)==len(list):
         print("Congratulation You saved")
         break
    if len(guess)>1:
        print("Please Enter a single letter")
    elif not guess.isalpha():
        print("you can only enter alphabets")
print(chosen_word)