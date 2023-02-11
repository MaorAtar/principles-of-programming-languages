"""
Homework Number 2
Authors: Maor Atar, ID: 318301231
         Guy Ezra,  ID: 207329509
"""
import random

# ------------------------------------------------
#                       Q1
# ------------------------------------------------


def simpson_rule(f, a, b, n):
    """
    Question Number 1
    Function description: Calculates integral on a given function, using simpson rule method.
    :param f: Function
    :param a: Int
    :param b: Int
    :param n: Int
    :return: Float
    """
    h = (b-a)/n
    calc = f(a) + f(b)

    for k in range(1, n):
        if k % 2 == 0:
            calc += 2*f(a+k*h)
        else:
            calc += 4*f(a+k*h)

    return calc*h/3


print(simpson_rule(lambda x: x**3, 0, 1, 100))

# ------------------------------------------------
#                       Q2
# ------------------------------------------------


def Game():
    """
    Function that draws randomly a 3 digits number, and lets the user find out it with 6 hints.
    After each hint is used the user score decrease by 10 points.
    When the user finds the correct number, the function display the user points on the screen,
    if no points left (0 points) the function display for the user the correct message.
    :return: None
    """
    rand_num = random.randint(100, 999)
    score = 100
    user_guess = None
    flag = None
    # Game hints, defined using lambda functions
    sum_digits_clue = lambda num: 0 if num == 0 else num % 10 + sum_digits_clue(num // 10)
    mul_digits_clue = lambda num: 1 if num == 0 else num % 10 * mul_digits_clue(num // 10)
    even_digits_clue = lambda digit: 'X' if digit % 2 == 0 else '-'
    big_digits_clue = lambda digit: 'X' if digit > 5 else '-'
    ascending_digits_clue = lambda num: True if num % 10 > (num // 10) % 10 > num // 100 else False
    prime_digits_clue = lambda digit: 'X' if digit % 10 == 2 or digit % 10 == 3 or digit % 10 == 5 or digit % 10 == 7 else '-'

    def printF1(msg,f):
        """
        High order function to display on the screen the message according to the given hint
        (used for sum,mul,ascending hints).
        :param String:
        :param Function:
        :return: None
        """
        print("{0}{1}".format(msg, f(rand_num)))

    def printF2(msg,f):
        """
        High order function to display on the screen the message according to the given hint
        (used for even,big,prime hints).
        :param String:
        :param Function:
        :return: None
        """
        print("{0}{1}{2}{3}".format(msg, f(rand_num // 100), f((rand_num // 10) % 10), f(rand_num % 10)))
    # Game algorithm
    print("welcome to game!")
    while user_guess != rand_num:
        rand_num = str(rand_num)
        user_guess = str(input("enter number/Enter to finish :"))
        if user_guess == '':
            flag = 0
            break
        elif score == 0:
            flag = 0
            break
        elif user_guess == rand_num:
            flag = 1
            break
        else:
            rand_num = int(rand_num)
            rand_choice = random.randint(1, 6)
            if rand_choice == 1:
                printF1("sum: ", sum_digits_clue)
                score -= 10
            elif rand_choice == 2:
                printF1("mul: ", mul_digits_clue)
                score -= 10
            elif rand_choice == 3:
                printF2("even digits: ", even_digits_clue)
                score -= 10
            elif rand_choice == 4:
                printF2("big digits: ", big_digits_clue)
                score -= 10
            elif rand_choice == 5:
                printF1("ascending: ", ascending_digits_clue)
                score -= 10
            else:
                printF2("prime digits: ", prime_digits_clue)
                score -= 10
    # Ending conditions
    if flag == 0:
        print("game over !!!")
    elif flag == 1:
        print("yes, correct! you win {0} points".format(score))


Game()
