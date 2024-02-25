name=input("Enter your Name: ")
print(f"Welcome {name} to the Hangman Game!")
word="secret"
guesses=''
turns=10
while turns:
    failed=0
    for char in word:
        print(char if char in guesses else "_",end="")
        failed+=0 if char in guesses else 1
    if not failed:
        print(" You won")
        break
    guess=input("  Enter Guess:")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong\nYou have",turns,'more guesses')
        if not turns:
            print("You Lose")
