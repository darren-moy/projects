import random
MAX_NUM_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):                   # 0 is the first row
        symbol = columns[0][line]               #first column at given line
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet    #for else, else doesn't run if for loop breaks
            winning_lines.append(line + 1)      #you want line 1, 2, 3 not line 0, 1, 2

    return winnings, winning_lines


def deposit():
    while True:
        amount = input('What would you like to deposit in dollars? ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')

    return amount


def getSlotMachineSpin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]            #copy of all_symbols
        for row in range(rows):
            value = random.choice(current_symbols)  #picks rand value from current_sym
            current_symbols.remove(value)           #remove so it can't be picked again
            column.append(value)                    #add value to column

        columns.append(column)                      #add column to columns list

    return columns                                  #represented as col1: AAA
                                                                #   col2: BBB, need to flip so its by rows and not columns


def printSlotMachine(columns):                      #transposing
    for row in range(len(columns[0])):              #taking first column length which is equal to the amount of rows
        for i, column in enumerate(columns):
            if i != len(columns) - 1:               #ensure no bar at the end of column
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def getNumLines():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_NUM_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_NUM_LINES:
                break
            else:
                print('Number of lines must be greater than 0')
        else:
            print('Please enter a number')

    return lines


def getBet():
    while True:
        amount = input('How much would you like to bet in dollars? ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between {MIN_BET} and {MAX_BET}')
        else:
            print('Please enter a number')

    return amount


def spin(balance):
    lines = getNumLines()
    while True:
        bet = getBet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'Your balance is too low, your current balance is {balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Your total bet is equal to ${total_bet}')

    slots = getSlotMachineSpin(ROWS, COLS, symbol_count)
    printSlotMachine(slots)
    winnings, winning_lines = checkWinnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    print(f'You won on lines:', *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f'You left with ${balance}')



main()