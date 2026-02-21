import random

l=['rock','paper','scissor']
ucount=0
ccount=0


while True:
    u=int(input('''
                    Do you want to start the game?
                    1.Yes|Play
                    2.No|Exit
    '''))
    if u==1:
        for i in range(1,6):
            yourchoice=int(input('''
                    Pick your move....
                    1.Rock
                    2.Paper
                    3.Scissor
            '''))
            if yourchoice==1:
                uchoice='rock'
                print('You chose: ',uchoice)

            elif yourchoice==2:
                uchoice='paper'
                print('You chose: ',uchoice)

            elif yourchoice==3:
                uchoice='scissor'
                print('You chose: ',uchoice)

            computerchoice=random.choice(l)

            print("Computer chose: ",computerchoice)

            if uchoice==computerchoice:
                print("The round is Draw....")
                ucount = ucount + 0
                ccount = ccount + 0

            elif (uchoice=='rock' and computerchoice=='scissor')or(uchoice=='paper'and computerchoice=='rock')or(uchoice=='scissor'and computerchoice=='paper'):
                print("You won the round....")
                ucount = ucount + 1

            else:
                print("Computer won the round....")
                ccount = ccount + 1

        print(" ")
        print(" ")
        print(" ")

        print('''
                                                    The final score is....
        ''')
        print(" ")
        print(" ")
        print(" ")


        if ucount>ccount:
            print("You won the game....")
            print("Your Score: ",ucount)
            print("Computer score: ",ccount)

        elif ucount==ccount:
            print("The game is draw....")
            print("Your Score: ", ucount)
            print("Computer score: ", ccount)

        else:
            print("Computer won the game....")
            print("Your Score: ", ucount)
            print("Computer score: ", ccount)




    elif u==2:
        break
