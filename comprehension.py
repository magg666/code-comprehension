# Program chooses number between 1 and 20 and player can guess 5 time value of number
import random  # import random module
# assign 0 to variable guesses_taken
guesses_taken = 0
# print given string
print('Hello! What is your name?')
# assign input to variable myName
myName = input()
# assign random integer from 1 to 20 (both ends included) to variable number
number = random.randint(1, 20)
# print two strings given with concatenate variable myName in between
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# starts repeating statement below loop until variable guesses_taken reaches value 6 (is smaller than 6)
while guesses_taken < 6:
    print('Take a guess.')  # prints given string
    guess = input()  # assing input to variable guess
    guess = int(guess)  # convert variable guess into integer and assing again to variable guess
# adding 1 to initial value of variable guesses_taken
    guesses_taken += 1
# checks dependency between variables guess and number and define action if guess is smaller than number
    if guess < number:
        print('Your guess is too low.')  # prints given string
# checks dependency between variables guess and number and define action if guess is greater than number
    if guess > number:
        print('Your guess is too high.')  # prints given string
# checks dependency between variables guess and number and define action if guess is equal number
    if guess == number:
        break   # stoping the loop
# checks dependency between variables guess and number and define action if guess is equal number after 5 guesses
if guess == number:
    # converts variable guesses_taken (integer) into string and assignes it to guesses_taken
    guesses_taken = str(guesses_taken)
    # prints given strings with concatenate variable myName and guesses_taken in between
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')

# checks dependency between variables guess and number and define action if guess is not equal number after 5 guesses
if guess != number:
    number = str(number)  # converts variable number (integer) into string and assignes it to number
    # prints given string with variable number
    print('Nope. The number I was thinking of was ' + number)
