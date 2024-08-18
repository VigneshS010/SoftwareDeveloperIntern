# This program finds the guess number is equal to the random number

import random
def guess_the_number(num):
    rnum = random.randrange(1,11)

    if num == rnum:
        print("You win")
    else:
        print("You loss")
        print("The random num is",rnum)

while True:
    num = int(input("Guess a number :"))
    guess_the_number(num)
    ret = input("do u want to play again? (Y/n)").lower()
    if ret == "n":
        break


# Guess a number :3
# You loss
# The random num is 9
# do u want to play again? (Y/n)y
# Guess a number :4
# You win
# do u want to play again? (Y/n)y
# Guess a number :1
# You loss
# The random num is 5
# do u want to play again? (Y/n)n
#
# Process finished with exit code 0