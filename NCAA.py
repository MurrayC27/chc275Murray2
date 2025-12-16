import random, os

WORDS = ["python","hangman","career","football","string","integer","loop","file","menu","rating","training","contract","summary","player","rookie"]

SAVE_FILE = "hangman_save.txt"

def line():
    print("-"*40)

def read_int(prompt):
    while True:
   try:
            return int(input(prompt))
        except ValueError:
            print("Enter an integer.")

def save_game(word, guessed, attempts):
    with open(SAVE_FILE,"w") as f:
        f.write(word+"\n")
        f.write("".join(guessed)+"\n")
        f.write(str(attempts)+"\n")
    print("Game saved.")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("No save found.")
        return None
    with open(SAVE_FILE,"r") as f:
        lines=[x.strip() for x in f.readlines()]
    if len(lines)<3:
        print("Save corrupted.")
        return None
    word=lines[0]
    guessed=list(lines[1])
    attempts=int(lines[2])
    print("Game loaded.")
    return word,guessed,attempts

def display(word, guessed):
    out=""
    for ch in word:
        if ch in guessed:
            out+=ch+" "
        else:
            out+="_ "
    print(out.strip())

def play(word, guessed, attempts):
    while True:
        line()
        print(f"Attempts left: {attempts}")
        display(word,guessed)
        if all(ch in guessed for ch in word):
            print("You won!")
            break
        if attempts<=0:
            print(f"You lost. Word was {word}")
            break
        print("Menu:\n1. Guess Letter\n2. Save\n3. Quit")
        choice=input("Select: ").strip()
        if choice=="1":
            letter=input("Letter: ").strip().lower()
            if len(letter)!=1 or not letter.isalpha():
                print("Invalid.")
                continue
            if letter in guessed:
                print("Already guessed.")
                continue
            guessed.append(letter)
            if letter not in word:
                attempts-=1
                print("Wrong guess.")
            else:
                print("Correct!")
        elif choice=="2":
            save_game(word,guessed,attempts)
        elif choice=="3":
            print("Quit game.")
            break
        else:
            print("Invalid.")

def main_menu():
    line()
    print("Hangman Game")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")

def new_game():
    word=random.choice(WORDS)
    guessed=[]
    attempts=6
    play(word,guessed,attempts)

def main():
    while True:
        main_menu()
        choice=input("Select: ").strip()
        if choice=="1":
            new_game()
        elif choice=="2":
            data=load_game()
            if data:
                word,guessed,attempts=data
                play(word,guessed,attempts)
        elif choice=="3":
            print("Goodbye.")
            break
        else:
            print("Invalid.")

if __name__=="__main__":
    main()
