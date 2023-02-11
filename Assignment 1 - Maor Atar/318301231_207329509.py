"""
Homework Number 1
Authors: Maor Atar, ID: 318301231
         Guy Ezra,  ID: 207329509
"""


# ------------------------------------------------
#                       Q1
# ------------------------------------------------
def even_str(word):
    """
    Question Number 1
    Function Description: Returns a new string that includes only the even placed characters
    Parameters List: String
    Return Value: String
    """
    word_size = 0
    for i in word:
        word_size += 1
    new_word = ''
    for j in range(1, word_size, 2):
        new_word += word[j]
    return new_word


# ------------------------------------------------
#                       Q2
# ------------------------------------------------
def pattern(num):
    """
    Question Number 2
    Function Description: Prints a specific pattern full of '*'
    Parameters List: Int
    Return Value: None
    """
    spaces = (num * 2) - 2

    for i in range(0, num):
        for j in range(0, i + 1):
            print("*", end="")

        for k in range(spaces):
            print(' ', end="")

        spaces = spaces - 2

        for j in range(0, i + 1):
            print("*", end="")
        print()
        print()


# ------------------------------------------------
#                       Q3
# ------------------------------------------------
def sort_num(x):
    """
    Question Number 3
    Function Description: Recursive function to check if a number is sorted (low to high order)
    Parameters List: Int
    Return Value: Boolean
    """
    if x // 10 == 0:
        return True
    elif x % 10 >= (x // 10) % 10:
        return sort_num(x // 10)
    else:
        return False


# ------------------------------------------------
#                       Q4
# ------------------------------------------------
def min_dig(x):
    """
    Question Number 4
    Function Description: Recursive function that returns the lowest digit in the number
    Parameters List: Int
    Return Value: Int
    """
    minimum = x % 10
    if x // 10 != 0:
        if (x // 10) % 10 > minimum:
            return min_dig((x // 100) * 10 + minimum)
        else:
            return min_dig(x // 10)
    else:
        return x


# ------------------------------------------------
#                       Q5
# ------------------------------------------------
def unique(word):
    """
    Question Number 5
    Function Description: the function loops through the whole string while checking each
    value for duplicates in the string if any duplicates were found the function will return False
    Parameters List: String
    Return Value: Boolean
    """
    word_size = 0
    for k in word:
        word_size += 1

    for i in range(0, word_size):
        for j in range(i + 1, word_size):
            if word[i] == word[j]:
                return False

    return True


# ------------------------------------------------
#                       Q6
# ------------------------------------------------
def Xnor(arg1, arg2):
    """
    Question Number 6
    Function Description: Function that works as Xnor logic
    Parameters List: Boolean, Boolean
    Return Value: Boolean
    """
    if arg1 is True and arg2 is True or arg1 is False and arg2 is False:
        return True
    else:
        return False
