import sys

if len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == '--help':
        print('''
            This is a program that plays the 21 number game with you!
            Select your preferred mode between easy and impossible with e or i.
            And enter your numbers which should be consecutive suppurated by spaces and hit enter.
            The computer will display it's numbers.
            Now you have to start where the computer has left.
            This goes on until someone says 21.
            Be smart and stop at 20.😉

              All the best!!!
        ''')
        exit(0)

def main():
    print("Enter your consecutive numbers suppurated by spaces.\n")

    # A counter to keep count of turns
    turn = 1

    # A nested list of all the previous computer generated numbers
    previous = [[0]]

    while True:
        player_num = input(f"Turn {turn}: ")
        if check_wrong(player_num):
            continue
        nums = unpack_stringtoint(player_num)
        near = nearestMultiple(max(nums))

        # Some basic checks
        if turn == 1 and max(nums) > 3:
            print("You can only enter consecutive numbers in range(1,3), such as '1 2 3' or '1 2'")
            continue
        if min(nums) <= max(previous[-1]):
            print("Invalid input: your input is not consecutive to computer input")
            continue

        # An empty list to take computer generated numbers and later print them out in order
        comp_num = []
        for i in range(3):
            j = max(nums)+ i + 1
            if j == near:
                comp_num.append(j)
                break
            else:
                comp_num.append(j)

        print("Computer says: ", end = " ")
        for i in range(len(comp_num)):
            print(comp_num[i], end= ' ')
        print()
        turn += 1

        # Appening current computer generated numbers for future use
        previous.append(comp_num)

        # Winner check
        if max(comp_num) == 20:
            print("\n\nComputer won!! \nYou can't win in this game mode 😊")
            exit(0)

# Checks if the input is valid or not
def check_wrong(current_turn,previous_comp_num='0'):
    try:
        current_num = unpack_stringtoint(current_turn)
        previous_num = unpack_stringtoint(previous_comp_num)
    except (TypeError, ValueError):
        print("Invalid input: your input is not a number")
        return True

    if min(current_num) <= max(previous_num):
        print("Invalid input: your input is not consecutive to computer input")
        return True

# Converts a string of numbers into list such as '1 2 3' >> [1,2,3]
def unpack_stringtoint(string):
    nums = []
    num_string = string.strip().split(' ')

    for i in range(len(num_string)):
        nums.append(int(num_string[i]))
    return nums

# Returns the nearest multiple of 4, to be used in impossible mode
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

