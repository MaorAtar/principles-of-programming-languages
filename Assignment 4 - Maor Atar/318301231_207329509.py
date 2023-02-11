"""
Homework Number 4
Authors: Maor Atar, ID: 318301231
         Guy Ezra,  ID: 207329509
"""
from functools import reduce
from operator import mul, add
# ------------------------------------------------
#                       Q1
# ------------------------------------------------


class Item:

    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        return "({0}:{1}$:{2}cal)".format(self.name, self.price, self.calories)

    def __repr__(self):
        t = (self.name, self.price, self.calories)
        t = str(t).replace(' ', '')
        return "{0}{1}".format(self.__class__.__name__, t)


class Order:

    def __init__(self, name, order_list=None, index=None):
        self.name = name
        if order_list is None:
            self.order_list = []
        else:
            self.order_list = list(order_list)
        if index is not None:
            self.order_list = []
            self.add_items(order_list, index)

    def __str__(self):
        order = ','.join([str(item) for item in self.order_list])
        return '({0}, ({1}),{2},{3})'.format(self.name, order, self.total(), self.calories())

    def __repr__(self):
        t = (self.name, self.order_list)
        t = str(t).replace(' ', '')
        return '{0}{1}'.format(self.__class__.__name__, t)

    def add_items(self, menu, index):
        """
        Function to add items to a given order
        :param menu: Sequence - list
        :param index: Sequence - list
        :return: Sequence - list
        """
        for i in index:
            self.order_list.append(menu[i - 1])

    def remove_item(self, index):
        """
        Function to remove an item from an order
        :param index: Integer
        :return: Sequence - list
        """
        return 'Remove Item: ' + str(self.order_list.pop(index - 1))

    def total(self):
        """
        Function to calculate the sum of the order
        :return: Integer
        """
        return ' total:' + str(sum([item.price for item in self.order_list])) + '$'

    def calories(self):
        """
        Function to calculate the calories sum of the order
        :return: Integer
        """
        return ' calories:' + str(sum([item.calories for item in self.order_list])) + 'cal'


class Restaurant:
    def __init__(self, name, menu=None, orders=[]):
        self.name = name
        self.menu = list(menu)
        self.orders = list(orders)

    def __repr__(self):
        t = (self.name, self.menu, self.orders)
        t = str(t).replace(' ', '')
        return '{0}{1}'.format(self.__class__.__name__, t)

    def add_menu(self, item):
        """
        Function to add an item to the menu
        :param item: Order
        :return: Sequence - list
        """
        self.menu.append(item)

    def remove_menu(self, index):
        """
        Function to remove an item from a menu
        :param index: Integer
        :return: Sequence - list
        """
        return 'Remove Item from menu: ' + str(self.menu.pop(index - 1))

    def print_menu(self):
        """
        Function to print the menu
        :return: None
        """
        for i, item in enumerate(self.menu):
            print('{0}) {1:<11} {2:>3} {3}cal'.format(i+1, item.name, str(item.price) + '$', item.calories))

    def add_orders(self, *orders):
        """
        function to add an order to the order list
        :param orders: Sequence - list
        :return: None
        """
        for order in orders:
            self.orders.append(order)

    def print_orders(self):
        """
        Function to print the orders
        :return: None
        """
        for item in self.orders:
            if type(item) != tuple:
                order = ','.join([str(item)])
                print(order, end='')
            else:
                for j in range(len(item)):
                    print(item[j], end='')
        print()


def min_calories(restaurant):
    """
    Function to return the order that has the lowest calories
    :param restaurant: Restaurant Object
    :return: Order Object
    """
    if restaurant.orders is None:
        return 'Error - no orders found in the restaurant'
    min_order = min(restaurant.orders[1], key=lambda x: x.calories())
    return min_order


# ------------------------------------------------
#                       Q2
# ------------------------------------------------
def make_class(attrs, base=None):
    """
    Shmyton make class
    """

    def get(name):
        """
        Get object from class
        name: string
        return: object
        """
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    def set(name, value):
        """
        Set object in class
        name: string
        value: object
        """
        attrs[name] = value

    def new(*args):
        """
        Create new class instance
        """
        attrs = {}

        def get(name):
            """
            Get object from class or base
            name: string
            return: object
            """
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set(name, value):
            """
            Set object in class
            name: string
            value: object
            """
            attrs[name] = value

        obj = {'get': get, 'set': set}
        init = get('__init__')
        if init:
            init(*args)
        return obj

    cls = {'get': get, 'set': set, 'new': new}
    return cls


def make_item_class():
    def __init__(self, name='', price=0, calories=0):
        self['set']('name', name)
        self['set']('price', price)
        self['set']('calories', calories)

    def __str__(self):
        t = (str(self['get']('name')) + ':', str(self['get']('price')) + '$:', str(self['get']('calories')) + 'cal')
        t = str(t).replace("'", '')
        t = str(t).replace(", ", '')
        return '{0}'.format(t)

    return make_class(locals(), object())


def make_order_class():
    def __init__(self, name='', order_list=None, index=None):
        self['set']('name', name)
        if order_list is None:
            self['set']('order_list', [])
        else:
            self['set']('order_list', list(order_list))
        if index is not None:
            self['set']('order_list', [])
            self['get']('add_items')(order_list, index)

    def __str__(self):
        order = ",".join(str(item['get']('__str__')()) for item in self['get']('order_list'))
        t = (self['get']('name'), order)
        t = str(t).replace("'", '')
        # t = str(t).replace(" ", '(')
        return '{0},{1},{2})'.format(t, self['get']('total')(), self['get']('calories')())

    def add_items(self, menu, index):
        """
        Function to add items to a given order
        :param menu: Sequence - list
        :param index: Sequence - list
        :return: Sequence - list
        """
        for i in index:
            self['get']('order_list').append(menu[i - 1])

    def remove_item(self, index):
        """
        Function to remove an item from an order
        :param index: Integer
        :return: Sequence - list
        """
        return 'Remove Item from order: {0}'.format(self['get']('order_list').pop(index - 1)['get']('__str__')())

    def total(self):
        """
        Function to calculate the sum of the order
        :return: Integer
        """
        return ' total:' + str(sum([item['get']('price') for item in self['get']('order_list')])) + '$'

    def calories(self):
        """
        Function to calculate the calories sum of the order
        :return: String
        """
        return ' calories:' + str(sum([item['get']('calories') for item in self['get']('order_list')])) + 'cal'

    return make_class(locals(), object())


def make_restaurant_class():
    def __init__(self, name='', menu=None, orders=[]):
        self['set']('name', name)
        self['set']('menu', list(menu))
        self['set']('orders', list(orders))

    def __str__(self):
        menu = ",".join(str(item['get']('__str__')()) for item in self['get']('menu'))
        orders = ",".join(str(item['get']('__str__')()) for item in self['get']('orders'))
        t = (self['get']('name'), menu, orders)
        t = str(t).replace("'", '')
        t = str(t).replace(" ", '(')
        return '{0})'.format(t)

    def add_menu(self, item):
        """
        Function to add an item to the menu
        :param item: Order
        :return: Sequence - list
        """
        self['get']('menu').append(item)

    def remove_menu(self, index):
        """
        Function to remove an item from a menu
        :param index: Integer
        :return: Sequence - list
        """
        return 'Remove Item from order: {0}'.format(self['get']('menu').pop(index - 1)['get']('__str__')())

    def print_menu(self):
        """
        Function to print the menu
        :return: None
        """
        for i, item in enumerate(self['get']('menu')):
            print('{0}) {1:<11} {2:>3} {3}cal'.format(i + 1, item['get']('name'), str(item['get']('price')) + '$',
                                                      item['get']('calories')))

    def add_orders(self, *orders):
        """
        function to add an order to the order list
        :param orders: Sequence - list
        :return: None
        """
        for order in orders:
            self['get']('orders').append(order)

    def print_orders(self):
        """
        Function to print the orders
        :return: None
        """
        for item in self['get']('orders'):
            if type(item) != tuple:
                print(item['get']('__str__')(), end='\n')
            else:
                for j in range(len(item)):
                    print(item[j]['get']('__str__')(), end='\n')

    return make_class(locals(), object())


def min_calories1(restaurant):
    """
    Function to return the order that has the lowest calories
    :param restaurant: Restaurant Object
    :return: Order Object
    """
    if restaurant['get']('orders') is None:
        return 'Error - no orders found in the restaurant'
    min_order = min(restaurant['get']('orders')[1], key=lambda x: x['get']('calories')())
    return min_order


# Object Assignment:
ItemClass = make_item_class()
OrderClass = make_order_class()
RestaurantClass = make_restaurant_class()
# ------------------------------------------------
#                       Q3
# ------------------------------------------------


def make_class1(attrs, base=None):
    """
    Shmyton make class
    """

    def get(name):
        """
        Get object from class
        name: string
        return: object
        """
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    def set(name, value):
        """
        Set object in class
        name: string
        value: object
        """
        if name in attrs:
            try:
                if isinstance(value, type(attrs[name])):
                    attrs[name] = value
                else:
                    raise TypeError
            except TypeError:
                print("The {0} attribute can be given a new value of type {1}".format(name, type(attrs[name])))
        else:
            attrs[name] = value

    def copy(obj):
        """
        Create a copy of the object
        """
        copy_obj = make_save_account_class()['new'](obj['get']('owner'))
        copy_obj['set']('balance', obj['get']('balance'))
        return copy_obj

    def new(*args):
        """
        Create new class instance
        """
        attrs = {}

        def get(name):
            """
            Get object from class or base
            name: string
            return: object
            """
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set(name, value):
            """
            Set object in class
            name: string
            value: object
            """
            if name in attrs:
                try:
                    if isinstance(value, type(attrs[name])):
                        attrs[name] = value
                    else:
                        raise TypeError
                except TypeError:
                    print("The {0} attribute can be given a new value of type {1}".format(name, type(attrs[name])))
            else:
                attrs[name] = value

        def copy(obj):
            """
            Create a copy of the object
            """
            copy_obj = make_save_account_class()['new'](obj['get']('owner'))
            copy_obj['set']('balance', obj['get']('balance'))
            return copy_obj

        obj = {'get': get, 'set': set, 'copy': copy}
        init = get('__init__')
        if init:
            init(*args)
        return obj

    cls = {'get': get, 'set': set, 'new': new, 'copy': copy}
    return cls


def make_account_class():
    return make_class1({'interest': 0.05})


def make_save_account_class():
    def init(self, owner):
        self['set']('owner', owner)
        self['set']('balance', 0)

    return make_class1({'__init__': init, 'interest': 0.03}, Account)


# Object Assignment:
Account = make_account_class()
SaveAccount = make_save_account_class()
# ------------------------------------------------
#                   Q4.a + Q4.d
# ------------------------------------------------


class Shekel(object):
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return 'Shekel({0})'.format(self.amount)

    def __str__(self):
        return '{0:.1f}₪'.format(self.amount)

    def __add__(self, other):
        return coerce_apply('add', self, other)

    def __sub__(self, other):
        return coerce_apply('sub', self, other)


class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return 'Dollar({0})'.format(self.amount)

    def __str__(self):
        return '{0:.1f}$'.format(self.amount)

    def __add__(self, other):
        return coerce_apply('add', self, other)

    def __sub__(self, other):
        return coerce_apply('sub', self, other)


class Euro(object):
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return 'Euro({0})'.format(self.amount)

    def __str__(self):
        return '{0:.1f}€'.format(self.amount)

    def __add__(self, other):
        return coerce_apply('add', self, other)

    def __sub__(self, other):
        return coerce_apply('sub', self, other)


# ------------------------------------------------
#                       Q4.b
# ------------------------------------------------
def type_tag(x):
    return type_tag.tags[type(x)]


type_tag.tags = {Shekel: 'nis', Dollar: 'dollar', Euro: 'euro'}


def apply(operation_name, first_amount, second_amount):
    tags = (type_tag(first_amount), type_tag(second_amount))
    key = (operation_name, tags)
    apply.implementations = {('add', ('nis', 'nis')): add_shekel,
                             ('add', ('dollar', 'dollar')): add_dollar,
                             ('add', ('euro', 'euro')): add_euro,
                             ('add', ('nis', 'dollar')): add_shekel_and_dollar,
                             ('add', ('nis', 'euro')): add_shekel_and_euro,
                             ('add', ('dollar', 'euro')): add_dollar_and_euro,
                             ('add', ('dollar', 'nis')): add_dollar_and_shekel,
                             ('add', ('euro', 'nis')): add_euro_and_shekel,
                             ('add', ('euro', 'dollar')): add_euro_and_dollar}
    return apply.implementations[key](first_amount, second_amount)


rates = {('dollar', 'nis'): 3.45, ('euro', 'nis'): 3.67}
rates[('euro', 'dollar')] = rates[('euro', 'nis')]/rates[('dollar', 'nis')]


def add_shekel(first_amount, second_amount):
    return Shekel(first_amount.amount + second_amount.amount)


def add_dollar(first_amount, second_amount):
    return Dollar(first_amount.amount + second_amount.amount)


def add_euro(first_amount, second_amount):
    return Euro(first_amount.amount + second_amount.amount)


def add_shekel_and_dollar(first_amount, second_amount):
    return Shekel(first_amount.amount + second_amount.amount)


def add_shekel_and_euro(first_amount, second_amount):
    tags = (type_tag(first_amount), type_tag(second_amount))
    return Shekel(first_amount.amount + second_amount.amount * rates[tags])


def add_dollar_and_euro(first_amount, second_amount):
    tags = (type_tag(first_amount), type_tag(second_amount))
    return Dollar(first_amount.amount + second_amount.amount*rates[tags])


def add_dollar_and_shekel(first_amount, second_amount):
    tags = (type_tag(first_amount), type_tag(second_amount))
    return Shekel(first_amount.amount*rates[tags] + second_amount.amount)


def add_euro_and_shekel(first_amount, second_amount):
    tags = (type_tag(first_amount), type_tag(second_amount))
    return Shekel(first_amount.amount*rates[tags] + second_amount.amount)


def add_euro_and_dollar(first_amount, second_amount):
    tags = (type_tag(first_amount), type_tag(second_amount))
    return Dollar(first_amount.amount*rates[tags] + second_amount.amount)


# ------------------------------------------------
#                       Q4.c
# ------------------------------------------------
def dollar_to_shekel(a):
    return Shekel(a.amount*rates['dollar', 'nis'])


def euro_to_shekel(a):
    return Shekel(a.amount*rates['euro', 'nis'])


def euro_to_dollar(a):
    return Dollar(a.amount*rates['euro', 'dollar'])


coercions = {('dollar', 'nis'): dollar_to_shekel, ('euro', 'nis'): euro_to_shekel, ('euro', 'dollar'): euro_to_dollar}


def sub_shekel(first_amount, second_amount):
    return Shekel(first_amount.amount - second_amount.amount)


def sub_dollar(first_amount, second_amount):
    return Dollar(first_amount.amount - second_amount.amount)


def sub_euro(first_amount, second_amount):
    return Euro(first_amount.amount - second_amount.amount)


def type_tag(x):
    return type_tag.tags[type(x)]


type_tag.tags = {Shekel: 'nis', Dollar: 'dollar', Euro: 'euro'}


def coerce_apply(operator_name, first_amount, second_amount):
    type_first_amount, type_second_amount = type_tag(first_amount), type_tag(second_amount)
    if type_first_amount != type_second_amount:
        if (type_first_amount, type_second_amount) in coercions:
            type_first_amount, first_amount = type_second_amount, coercions[(type_first_amount,
                                                                             type_second_amount)](first_amount)
        elif (type_second_amount, type_first_amount) in coercions:
            type_second_amount, second_amount = type_first_amount, coercions[(type_second_amount,
                                                                              type_first_amount)](second_amount)
        else:
            return 'No coercion possible.'
    assert type_first_amount == type_second_amount
    key = (operator_name, type_first_amount)
    return coerce_apply.implementations[key](first_amount, second_amount)


coerce_apply.implementations = {('add', 'nis'): add_shekel,
                                ('add', 'dollar'): add_dollar,
                                ('add', 'euro'): add_euro,
                                ('sub', 'nis'): sub_shekel,
                                ('sub', 'dollar'): sub_dollar,
                                ('sub', 'euro'): sub_euro}


# ------------------------------------------------
#                       Q5.a
# ------------------------------------------------
class Tree():
    def __init__(self, value, nodes=None):
        self.value = value
        self.nodes = nodes

    def __repr__(self):
        """
        __repr__ implementation used for the interpreter
        :return: String
        """
        if self.nodes:
            return 'Tree({0},{1})'.format(self.value, repr(self.nodes))
        return 'Tree({0})'.format(self.value)


# ------------------------------------------------
#                       Q5.b
# ------------------------------------------------
def BuildTree(tree):
    """
    Function to build a tree represented as a Tree Object
    :param tree: Tuple
    :return: Tree Object
    """
    if type(tree) != tuple:
        return Tree(tree)
    nodes = [BuildTree(branch) for branch in tree]
    return Tree(sum([n.value for n in nodes]), nodes)


# ------------------------------------------------
#                       Q5.c
# ------------------------------------------------
def MaxValue(root):
    """
    Function to find the maximum value from all the tree leaves
    :param root: Tree Object
    :return: Integer
    """
    if not root.nodes:
        return root.value
    return max(MaxValue(node) for node in root.nodes)


# ------------------------------------------------
#                       Q6
# ------------------------------------------------
def read_eval_print_loop():
    """
    Run a read-eval-print loop for calculator.
    """
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except SyntaxError as err:
            print(type(err).__name__ + ': unexpected')
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return


class Exp(object):
    """
    A call expression in Calculator.
    """
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def calc_eval(exp):
    """
    Evaluate a Calculator expression.
    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        # Check for the Expression tree type:
        if exp.operator == 'type':
            return calc_apply(exp.operator, exp.operands)
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    """
    Apply the named operator to a list of args.
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom
    # Added the required operators('type' and 'ror'):
    if operator == 'type':
        if type(args[0]) == Exp:
            return '<class {0}>'.format(args[0].__class__.__name__)
        return type(args[0])
    if operator == 'ror':
        try:
            if len(args) != 2:
                raise TypeError(operator + ' requires exactly 2 arguments')
            else:
                digits = number_length(args[0])
                if type(args[1]) is not int:
                    raise TypeError(str(args[1])+' is not <class int>')
                elif args[0] <= 0:
                    raise ValueError
                elif digits[1] != 0:
                    if digits[0] < args[1] or digits[1] < args[1]:
                        raise ValueError
                    else:
                        digits_sep = separate_digits(args[0])
                        for i in range(args[1]):
                            counter = 0
                            for j in map(ror, digits_sep):
                                digits_sep[counter] = j
                                counter += 1
                        return str(digits_sep[0]) + '.' + str(digits_sep[1])
                elif digits[0] < args[1]:
                    raise ValueError
                else:
                    result = args[0]
                    for k in range(args[1]):
                        result = ror(result)
                    return str(result)
        except ValueError:
            if args[0] <= 0:
                return 'ValueError: ' + str(args[0]) + ' is not positive number'
            if args[1] <= 0:
                return 'ValueError: ' + str(args[1]) + ' is not positive number'
            if digits[0] < args[1] or digits[1] < args[1]:
                return 'ValueError: The number ' + str(args[0]) + ' is not possible for rotate'


def calc_parse(line):
    """
    Parse a line of calculator input and return an expression tree.
    """
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    """
    Convert a string into a list of tokens.
    """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()


known_operators = ['add', 'sub', 'mul', 'div', 'type', 'ror', '+', '-', '*', '/']


def analyze(tokens):
    """
    Create a tree of nested lists from a sequence of tokens.
    Operand expressions can be separated by commas, spaces, or both.
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    """
    Analyze a sequence of comma-separated operands.
    """
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)
    return operands


def assert_non_empty(tokens):
    """
    Raise an exception if tokens is empty.
    """
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_token(token):
    """
    Return the value of token if it can be analyzed as a number, or token.
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


# ror - Assistance Functions:
# Assistance Function 1:
def number_length(num):
    """
    Assistance function to calculate the amount of digits before and after the dot
    :param num: Int/Float
    :return: Tuple of integers
    """
    num_string = str(num)
    if '.' in num_string:
        before_dot = len(num_string.split('.')[0])
        after_dot = len(num_string.split('.')[1])
        return before_dot, after_dot
    else:
        return len(num_string), 0


# Assistance Function 2:
def separate_digits(num):
    """
    Assistance function to separate the digits of the number before and after the dot,
    and store them in a list
    :param num: Int/Float
    :return: List of integers
    """
    num_string = str(num)
    if '.' in num_string:
        num_l = list(map(int, num_string.split(".")))
    else:
        num_l = [int(num_string), 0]
    return num_l


# Assistance Function 3:
def ror(num):
    """
    Assistance function to perform the roll to the right action on the given number
    :param num: Int/Float
    :return: Integer
    """
    num_str = str(num)
    return int(num_str[-1:] + num_str[:-1])


def run():
    read_eval_print_loop()


run()
