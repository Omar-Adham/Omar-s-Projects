#Guessing word Game!!!!

import random
import string

words = [
    "cat", "dog", "sun", "car", "sky", "run", "box", "cup", "hat", "pen",
    "book", "tree", "fish", "milk", "rain", "bird", "door", "love", "blue", "wind",
    "happy", "green", "apple", "water", "light", "sweet", "smile", "dream", "plant", "river",
    "stone", "earth", "ocean", "music", "cloud", "peace", "dance", "heart", "angel", "magic",
    "tiger", "spark", "faith", "flame", "honey", "bloom", "grass", "waves", "paper", "sunny",
    "cool", "fast", "kind", "soft", "calm", "jump", "play", "read", "move", "rest",
    "leaf", "ship", "cook", "moon", "star", "gold", "sand", "fire", "cold", "rock",
    "mint", "cake", "shoe", "game", "hand", "bird", "road", "snow", "milk", "wave",
    "smile", "apple", "light", "peace", "dance", "green", "storm", "plant", "faith", "earth",
    "song", "book", "path", "ring", "frog", "hill", "seed", "pond", "rope", "nest",
    "bake", "draw", "shop", "wash", "feed", "lift", "roll", "sing", "walk", "grow",
    "angel", "magic", "happy", "sweet", "dream", "music", "peace", "spark", "flame", "sunny",
    "tiny", "blue", "pink", "gray", "gold", "cold", "warm", "soft", "hard", "fast",
    "mouse", "chair", "table", "house", "clock", "grass", "river", "plant", "smile", "peace",
    "clear", "bloom", "waves", "shine", "dream", "flame", "paper", "ocean", "fruit", "storm",
    "wonder", "planet", "sunset", "flower", "family", "garden", "forest", "silver", "little", "pretty",
    "morning", "holiday", "friends", "journey", "balance", "treetop", "picture", "diamond", "harvest", "teacher",
    "outside", "breathe", "freedom", "rainbow", "mountain", "whisper", "beautiful", "delight", "sunrise", "drawing",
    "ice", "egg", "toy", "bag", "key", "fan", "box", "dog", "cow", "bee",
    "king", "girl", "boy", "baby", "lady", "man", "wife", "aunt", "mom", "dad",
    "silver", "orange", "forest", "planet", "sunrise", "evening", "journey", "holiday", "rainbow", "picture",
    "friends", "morning", "teacher", "mountain", "freedom", "balance", "diamond", "breathe", "delight", "harvest"
]



hangman_art={0:("  ",
                "  ",
                "  "),
             1:(" o ",
                "  ",
                "  "),
             2:(" o ",
                " | ",
                "  "),
             3:(" o ",
                "/| ",
                "  "),
             4:(" o ",
                "/|\\  ",
                "  "),
             5:(" o ",
                "/|\\  ",
                "/  "),
             6:(" o ",
                "/|\\",
                "/ \\")}
letters=string.ascii_letters
letters=list(letters)
letters=letters[0:26]

def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_letters(answer,empty):
    print(" ".join(empty))

def display_answer(answer):
    print(" ".join(answer))

def main():
    while True:
        answer=random.choice(words)
        hint=["_"]*len(answer)
        wrong_guesses=0
        guessed_letters=set()
        is_running=True
        empty = []
        for ans in answer:
            empty.append(ans)
        for i in range(10-len(answer)):
            empty.append(random.choice(letters))
        random.shuffle(empty)

        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            display_letters(answer,empty)

            guess=input("Enter your guess: ").lower()

            if len(guess)!=1 or not guess.isalpha():
                print("Invalid Input!")
                continue
            if guess in guessed_letters:
                print(f"{guess} is already guessed!")
                continue
            guessed_letters.add(guess)


            if guess in answer:
                for i in range(len(answer)):
                    if answer[i]==guess:
                        hint[i]=guess
                        empty.remove(guess)


            else:
                wrong_guesses +=1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You WIN!!!")
                is_running=False
            elif wrong_guesses >=len(hangman_art)-1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You LOSE!!!")
                is_running=False
        game=input("Do you want to play again?(Y/N): ").lower()
        if game=="y":
            continue
        else:
            break



if __name__=="__main__":
    main()

