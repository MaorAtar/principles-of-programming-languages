"""
Homework Number 3
Authors: Maor Atar, ID: 318301231
         Guy Ezra,  ID: 207329509
"""
import datetime
from functools import reduce


# ------------------------------------------------
#                       Q1
# ------------------------------------------------
# Level 0:
def make_ticket(flight_num, flight_date_day, flight_date_month, flight_time_hour, flight_time_minute):
    """
    Question Number 1
    Function description: Defines immutable type of flight ticket.
    The implementation apply the data abstraction principle.
    :param String - flight_num:
    :param Integer - flight_date_day:
    :param Integer - flight_date_month:
    :param Integer - flight_time_hour:
    :param Integer - flight_time_minute:
    """
    def dispatch(msg):
        """
        Function description: Dispatch function that returns the required value,
        from the input message.
        :param String - msg:
        :return: Function - dispatch
        """
        if msg == 0:
            return flight_num
        elif msg == 1:
            return flight_date_day
        elif msg == 2:
            return flight_date_month
        elif msg == 3:
            return flight_time_hour
        elif msg == 4:
            return flight_time_minute
    return dispatch


def get_item_pair(obj, i):
    """
    --Assistance Function--
    Function description: Returns the item in the required index
    :param String or Integer - obj:
    :param Integer - i:
    :return: String or Integer
    """
    return obj(i)


def make_date(date_day, date_month):
    """
    --Assistance Function--
    Function description: Returns a date in the "DDMMM" format
    :param Integer - date_day:
    :param Integer - date_month:
    :return: String
    """
    if date_month == 1:
        m = 'JAN'
    elif date_month == 2:
        m = 'FEB'
    elif date_month == 3:
        m = 'MAR'
    elif date_month == 4:
        m = 'APR'
    elif date_month == 5:
        m = 'MAY'
    elif date_month == 6:
        m = 'JUN'
    elif date_month == 7:
        m = 'JUL'
    elif date_month == 8:
        m = 'AUG'
    elif date_month == 9:
        m = 'SEP'
    elif date_month == 10:
        m = 'OCT'
    elif date_month == 11:
        m = 'NOV'
    elif date_month == 12:
        m = 'DEC'
    else:
        m = 'ERROR - Invalid month - {0}'.format(date_month)

    if 0 < date_day < 10:
        d = '0{0}'.format(date_day)
    else:
        d = date_day

    return '{0}{1}'.format(d, m)


def make_time(time_hour, time_minute):
    """
    --Assistance Function--
    Function description: Returns a time in the "hh:mm" format
    :param Integer - time_hour:
    :param Integer - time_minute:
    :return: String
    """
    if 0 <= time_hour < 10:
        h = '0{0}'.format(time_hour)
    else:
        h = time_hour
    if 0 <= time_minute < 10:
        m = '0{0}'.format(time_minute)
    else:
        m = time_minute
    return '{0}:{1}'.format(h, m)


# Level 1
def flight(flight_ticket):
    """
    Function description: Gets an instance of a ticket flight,
    and returns the flight number as a string
    :param Instance - flight_ticket:
    :return: String
    """
    return get_item_pair(flight_ticket, 0)


def day(flight_ticket):
    """
    --Assistance Function--
    Function description: Returns the day of the flight ticket
    :param Instance - flight_ticket:
    :return: Integer
    """
    return get_item_pair(flight_ticket, 1)


def month(flight_ticket):
    """
    --Assistance Function--
    Function description: Returns the month of the flight ticket
    :param Instance - flight_ticket:
    :return: Integer
    """
    return get_item_pair(flight_ticket, 2)


def date(flight_ticket):
    """
    Function description: Returns the date of the flight ticket in the "DDMMM" format
    :param Instance - flight_ticket:
    :return: String
    """
    return make_date(day(flight_ticket), month(flight_ticket))


def hour(flight_ticket):
    """
    Function description: Returns the hour of the flight ticket
    :param Instance - flight_ticket:
    :return: Integer
    """
    return get_item_pair(flight_ticket, 3)


def minute(flight_ticket):
    """
    Function description: Returns the minute of the flight ticket
    :param Instance - flight_ticket:
    :return: Integer
    """
    return get_item_pair(flight_ticket, 4)


def print_ticket_info(flight_ticket, print_choice=None):
    """
    Function description: Prints the flight ticket information in the
    requested format - 'flight date hh:mm or flight hh:mm or date hh:mm or hh:mm'
    :param Instance - flight_ticket:
    :param String - print_choice:
    :return: None
    """
    f, d, t = flight(flight_ticket), date(flight_ticket), make_time(hour(flight_ticket), minute(flight_ticket))
    if print_choice == 'flight date hh:mm' or not print_choice:
        print('{0} {1} {2}'.format(f, d, t))
    elif print_choice == 'flight hh:mm':
        print('{0} {1}'.format(f, t))
    elif print_choice == 'date hh:mm':
        print('{0} {1}'.format(d, t))
    elif print_choice == 'hh:mm':
        print('{0}'.format(t))


def check_amount_of_days(check_month):
    """
    --Assistance Function--
    Function description: Returns the amount of days for each entered month
    :param Integer - check_month:
    :return: Integer
    """
    if check_month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        return 31
    elif check_month == 4 or 6 or 9 or 11:
        return 30
    elif check_month == 2:
        return 28


def time_difference(first_flight_ticket, second_flight_ticket):
    """
    Function description: Calculates the time differences between two given tickets
    :param Instance - first_flight_ticket:
    :param Instance - second_flight_ticket:
    :return: Integer
    """
    month1, month2 = month(first_flight_ticket), month(second_flight_ticket)
    days1, days2 = check_amount_of_days(month1), check_amount_of_days(month2)
    hour1, hour2 = hour(first_flight_ticket), hour(second_flight_ticket)
    min1, min2 = minute(first_flight_ticket), minute(second_flight_ticket)

    diff_month = abs(month1 - month2) * 30 * 24 * 60
    diff_day = abs(days1 - days2) * 24 * 60
    diff_hour = abs(hour1 - hour2) * 60
    diff_min = abs(min1 - min2)

    return diff_month + diff_day + diff_hour + diff_min


def time_correction(flight_ticket, mins):
    """
    Function description: Returns a new ticket instance with the add/sub of the
    entered minutes (Using the datetime libray
    :param Instance - flight_ticket:
    :param Integer - mins:
    :return: Instance
    """
    ticket_date = datetime.datetime(2022, month(flight_ticket), day(flight_ticket), hour(flight_ticket),
                                    minute(flight_ticket))
    if mins <= 0:
        mins *= -1
        ticket_date -= datetime.timedelta(minutes=mins)
    else:
        ticket_date += datetime.timedelta(minutes=mins)
    mon = ticket_date.month
    d = ticket_date.day
    hr = ticket_date.hour
    m = ticket_date.minute

    return make_ticket(flight(flight_ticket), d, mon, hr, m)


# ------------------------------------------------
#                       Q2
# ------------------------------------------------
# Level 0:
def make_tree(node_value, left_c, right_c):
    """
    Question Number 2
    Function description: Defines immutable type of binary tree.
    The implementation apply the data abstraction principle.
    :param Integer - node_value:
    :param Instance(Node) - left_c:
    :param Instance(Node) - right_c:
    :return: Instance(Node)
    """
    def dispatch(msg):
        """
        Function description: Dispatch function that returns the required value,
        from the input message.
        :param String - msg:
        :return: Function - dispatch
        """
        if msg == 0:
            return node_value
        elif msg == 1:
            return left_c
        elif msg == 2:
            return right_c
    return dispatch


def get_item(obj, i):
    """
    --Assistance Function--
    Function description: Returns the item in the required index
    :param String or Integer - obj:
    :param Integer - i:
    :return: String or Integer
    """
    return obj(i)


# Level 1:
def value(node):
    """
    Function description: Returns the value for the entered node
    :param Instance - node:
    :return: Integer
    """
    return get_item(node, 0)


def left(node):
    """
    Function description: Returns the left child of the entered node
    :param Instance - node:
    :return: Instance or None
    """
    if get_item(node, 1):
        return get_item(node, 1)
    return None


def right(node):
    """
    Function description: Returns the right child of the entered node
    :param Instance - node:
    :return: Instance or None
    """
    if get_item(node, 2):
        return get_item(node, 2)
    return None


def print_tree(root):
    """
    Function description: Prints the tree values recursively with the "Inorder" method
    :param Instance - root:
    :return: None
    """
    if root:
        print_tree(left(root))
        print(value(root), end='')
        print(' ', end='')
        print_tree(right(root))


def min_value(root):
    """
    Function description: Prints the minimum value in the tree
    :param Instance - root:
    :return: None or Integer
    """
    if root is None:
        print("Tree is empty")
        return -1
    else:
        minimum = value(root)
        if left(root) is not None:
            left_min = min_value(left(root))
            minimum = min(minimum, left_min)
        if right(root) is not None:
            right_min = min_value(right(root))
            minimum = min(minimum, right_min)
    return minimum


def mirror_tree(root):
    """
    Function description: Returns a new mirrored tree from the original
    :param Instance - root:
    :return: Instance
    """
    if root:
        return make_tree(value(root), mirror_tree(right(root)), mirror_tree(left(root)))


tree = make_tree(12, make_tree(6, make_tree(8, None, None), None),
                 make_tree(7, make_tree(2, None, None), make_tree(15, None, None)))


# ------------------------------------------------
#                       Q3.1
# ------------------------------------------------
def avg_salary(dep_salaries_list):
    """
    Function description: Returns a tuple that contains all the departments
    average salaries, using pipline method
    :param Tuple - dep_salaries_list:
    :return: Tuple
    """
    return tuple(map(lambda x: (x[0], reduce(lambda y, z: y + z, x[1])/len(x[1])), dep_salaries_list))


# ------------------------------------------------
#                       Q3.2
# ------------------------------------------------
def add_bonus_to_salary(dep_salaries_list, dep_bonus_list):
    """
    --Assistance Function--
    Function description: Returns a tuple that contains all the salaries after the bonus added, using pipline method
    :param Tuple - dep_salaries_list:
    :param Tuple - dep_bonus_list:
    :return: Tuple
    """
    return tuple(map(lambda x: x + dep_bonus_list, dep_salaries_list))


def add_bonus(dep_salaries_list, dep_bonus_list):
    """
    Function description: Returns a tuple that contains all departments minimum, maximum and average salaries,
    using pipeline method
    :param Tuple - dep_salaries_list:
    :param Tuple - dep_bonus_list:
    :return: Tuple
    """
    return tuple(map(lambda w: (min(w), max(w), sum(w) / len(w)),
                     tuple(map(lambda y, z: (add_bonus_to_salary(y[1], z[1])), dep_salaries_list, dep_bonus_list))))


# ------------------------------------------------
#                       Q4
# ------------------------------------------------
def make_temperature(degrees, unit):
    """
    Function description: Creates a temperature mutable data using dispatch function and message passing
    :param Integer - degrees:
    :param String - unit:
    :return: Instance
    """
    def get_value(msg):
        """
        Function description: Returns a value with the requested message
        :param String - msg:
        :return: Integer or String
        """
        if msg == 'degrees':
            return degrees
        elif msg == 'unit':
            return unit
        else:
            print('Field does not exist')

    def set_value(msg, val):
        """
        Function description: Sets a value with the requested message
        :param String - msg:
        :param Integer or String - val:
        :return: None
        """
        if msg == 'degrees':
            nonlocal degrees
            degrees = val
        elif msg == 'unit':
            nonlocal unit
            unit = val
        else:
            print('Field does not exist')

    def convert(func, new_unit):
        """
        Function description: Converts the existing temperature instance with entered one
        :param Function - func:
        :param String - new_unit:
        :return: None or String
        """
        nonlocal degrees
        nonlocal unit
        if new_unit == 'C' or 'K' or 'F':
            degrees = func(degrees)
            unit = new_unit
        elif new_unit == 'C' and func is None:
            degrees = temp_convert(unit, new_unit)
            unit = new_unit
        elif new_unit == 'K' and func is None:
            degrees = temp_convert(unit, new_unit)
            unit = new_unit
        elif new_unit == 'F' and func is None:
            degrees = temp_convert(unit, new_unit)
            unit = new_unit
        else:
            print("Invalid unit entered")

    def temp_convert(unit, new_unit):
        """
        --Assistance Function--
        Function description: Returns a function that calculates all the types of temperature to the required one
        :param String - unit:
        :param String - new_unit:
        :return: Function
        """
        if unit == 'C' and new_unit == 'F':
            return lambda x: x * 1.8 + 32
        elif unit == 'F' and new_unit == 'C':
            return lambda x: (x - 32) / 1.8
        elif unit == 'F' and new_unit == 'K':
            return lambda x: (x + 459.67) / 1.8
        elif unit == 'K' and new_unit == 'F':
            return lambda x: x * 1.8 - 459.67
        elif unit == 'C' and new_unit == 'K':
            return lambda x: x + 273.15
        elif unit == 'K' and new_unit == 'C':
            return lambda x: x - 273.15

    def dispatch(msg):
        """
        Function description: Dispatch function that returns the required value,
        from the input message.
        :param String - msg:
        :return: Function - dispatch
        """
        if msg == 'get_value':
            return get_value
        elif msg == 'set_value':
            return set_value
        elif msg == 'str':
            if type(degrees) == float:
                return str(format(degrees, ".1f")) + " " + str(unit)
            return str(format(degrees)) + " " + str(unit)
        elif msg == 'convert':
            return convert
    return dispatch


# ------------------------------------------------
#                       Q5
# ------------------------------------------------
def make_traveler_trip(name, id):
    """
    Function description: Creates a traveler mutable data using dispatch dictionary and message passing
    :param String - name:
    :param Integer - id:
    :return: Dispatch dictionary
    """
    virtual_bag = []

    def add_destination(destination, location, cost, currency_symbol):
        """
        Function description: Adds a new destination to the traveler 'virtual_bag' list
        :param String - destination:
        :param String - location:
        :param Integer or Float - cost:
        :param String - currency_symbol:
        :return: List
        """
        return virtual_bag.append({'destinations': destination, 'locations': location, 'costs': cost,
                                   'currency_symbols': currency_symbol})

    def print_trip():
        """
        Function description: Function to print all the traveler information stored in his virtual bag
        :return: None
        """
        print(str(name) + ' ' + str(id))
        i = 0

        def hasMore():
            """
            Function description: Function to check if there are more values of information to print
            (are we in the end of the list?)
            :return: None
            """
            nonlocal i
            if i == len(virtual_bag):
                return False
            return True

        def next():
            """
            Function description: Function to move forward the values in the list
            :return: None
            """
            nonlocal i
            temp = []
            for values in virtual_bag[i].values():
                temp.append(values)
            print(", ".join(temp))
            i += 1
        return {'hasMore': hasMore, 'next': next}

    def check_duplicate(l):
        """
        --Assistance function--
        Function description: Check for duplicates in a given list
        :param l: List
        :return: List
        """
        result = []
        for i in l:
            if i not in result:
                result.append(i)
        return result

    def view(destination_or_location):
        """
        Fucntion description: Prints all the destination or locations in the traveler bag (depends on the user input)
        :param String - destination_or_location:
        :return: None
        """
        temp = []
        if destination_or_location == 'destinations':
            for i in range(len(virtual_bag)):
                temp.append(virtual_bag[i]['destinations'])
            print(", ".join(check_duplicate(temp)))
        elif destination_or_location == 'locations':
            for i in range(len(virtual_bag)):
                temp.append(virtual_bag[i]['locations'])
            print(", ".join(check_duplicate(temp)))
        else:
            print('Please look for destinations/locations only!')

    def calculate_expenses(currency_type):
        """
        Function description: Calculates the total trip expenses depends on the currency entered
        :param String - currency_type:
        :return: String
        """
        total_cost = 0
        temp_currency_list = []
        temp_costs_list = []
        for i in range(len(virtual_bag)):
            temp_currency_list.append(virtual_bag[i]['currency_symbols'])
        for j in range(len(virtual_bag)):
            temp_costs_list.append(virtual_bag[j]['costs'])

        if currency_type == 'ILS':
            for t in range(len(temp_currency_list)):
                if temp_currency_list[t] == 'EUR':
                    total_cost += float(temp_costs_list[t]) * 3.68
                elif temp_currency_list[t] == 'ILS':
                    total_cost += float(temp_costs_list[t])
                elif temp_currency_list[t] == 'USD':
                    total_cost += float(temp_costs_list[t]) * 1.06
        elif currency_type == 'EUR':
            for t in range(len(temp_currency_list)):
                if temp_currency_list[t] == 'EUR':
                    total_cost += float(temp_costs_list[t])
                elif temp_currency_list[t] == 'ILS':
                    total_cost += float(temp_costs_list[t]) * 0.27
                elif temp_currency_list[t] == 'USD':
                    total_cost += float(temp_costs_list[t]) * 0.94
        elif currency_type == 'USD':
            for t in range(len(temp_currency_list)):
                if temp_currency_list[t] == 'EUR':
                    total_cost += float(temp_costs_list[t]) * 1.06
                elif temp_currency_list[t] == 'ILS':
                    total_cost += float(temp_costs_list[t]) * 0.29
                elif temp_currency_list[t] == 'USD':
                    total_cost += float(temp_costs_list[t])
        return str("{0} {1}".format(int(total_cost), currency_type))

    def delete_destination(destination_name):
        """
        Function description: Gets the name of the destination and deletes all his information from the virtual bag
        :param String - destination_name:
        :return: None
        """
        for i in range(len(virtual_bag)):
            if virtual_bag[i]['destinations'] == destination_name:
                del virtual_bag[i]
                return

    def search_destination(destination_name):
        """
        Function description: Gets the name of the destination and prints all his information from the virtual bag
        :param String - destination_name:
        :return: None
        """
        temp = []
        for i in range(len(virtual_bag)):
            if virtual_bag[i]['destinations'] == destination_name:
                for values in virtual_bag[i].values():
                    temp.append(values)
                print(", ".join(temp))

    return {'add_destination': add_destination, 'print_trip': print_trip, 'view': view,
            'calculate_expenses': calculate_expenses, 'delete_destination': delete_destination,
            'search_destination': search_destination}