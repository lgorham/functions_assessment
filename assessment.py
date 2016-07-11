# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def tax_rate(state, item_cost, default_tax = 0.05):
    """
    Determines the applicable tax rate depending on state, and returns
    the total cost of the item.

    """

    if state == "CA":
        total_cost = (item_cost * 0.07) + item_cost
    else:
        total_cost = (item_cost * default_tax) + item_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def isberry(fruit_name):
    """
    Takes a fruit name as a string, and returns a boolean if the fruit is
    one of the listed berrires

    """


    berries = ["strawberry", "cherry", "blackberry"]
    if fruit_name in berries:
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit_name):
    """
    Calls the is_berry function, and based upon the output determines the
    shipping cost - with 0 for a berry, and 5 for another frutit

    """


    berry = is_berry(fruit_name)
    if berry == "True":
        return 0
    elif berry == "False":
        return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#

def is_hometown(town_name):
    """
    Takes a town name as a string and returns a boolean reflecting whether or
    not it is the same as my hometown

    """

    if town_name == "Sun Valley":
        return True
    else:
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):
    """
    Takes a first and last name as arguments, and returns the full name 
    as a concatenated string

    """

    return first_name + " " + last_name

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town_name, first_name, last_name):
    """
    Takes town name, and first and last names as arguments, and returns a
    greeting customized to that information

    """
    complete_name = full_name(first_name, last_name)
    if is_hometown(town_name) == "True":
        print "Hi", complete_name, "we're from the same place!"
    else:
        print "Hi", complete_name, "where are you from? "

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x=1):
    def add(y):
        return x + y
    return add



# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
addfive(5)
addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append_num(list, x):
    list.append(x)
    return list


#####################################################################