import random

# users starting money
funds = 100

# array of numbers 1-36
numArray = list(range(1, 37))

# array of possible choices
choiceArray = ['Even', 'even', 'E', 'e', 'Odd', 'odd', 'O', 'o']

# instructions
print('''
    A number between 1 and 36 will be chosen at random.\n
    You're goal is to guess if the number will be even or odd.\n
    Choices should be written as Even, even, E, e or Odd, odd, o, O.\n
    The game will end when you run out of money.\n
    Good luck!\n'''
      )


class NotEnoughFundsException(Exception):
    def __init__(self, message):
        super().__init__(message)


message = '''Either your bet was entered incorrectly\n
or it was greater than your balance. Try again\n'''


def exception_check(bet):
    if bet > funds:
        raise NotEnoughFundsException(message)
    else:
        return True


# iterate until user quits or runs out of money
while funds > 0:

    goodBet = False

    while not goodBet:

        print('Your funds: $' + str(funds))

        betAmount = int(input('Choice an amount to bet: $'))
        
        try:
            
            goodBet = exception_check(betAmount)

        except NotEnoughFundsException:
            
            print('Invalid Bet')

    funds -= betAmount

    userChoice = input('Even or Odd: ')

    while userChoice not in choiceArray:
        
        print('Entry not excepted. Please try again.')
        
        userChoice = input('Even or Odd')

    if userChoice in ['Even', 'even', 'E', 'e']:
        
        userChoice = 0
    
    else:

        userChoice = 1

    randNum = random.choice(numArray)
    
    print('Number: ' + str(randNum))

    if randNum % 2 == userChoice:
        
        print('You win')
        
        funds += betAmount * 2
    
    else:
        
        print('You lose')

    print('Your Balance: $' + str(funds))

