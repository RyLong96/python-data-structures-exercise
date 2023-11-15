# def product(a, b):
#     """Return product of a and b.

#         >>> product(2, 2)
#         4

#         >>> product(2, -2)
#         -4
#     """

def product(a,b):
    return a * b
print(product())


# def weekday_name(day_of_week):
#     """Return name of weekday.
    
#         >>> weekday_name(1)
#         'Sunday'
        
#         >>> weekday_name(7)
#         'Saturday'
        
#     For days not between 1 and 7, return None
    
#         >>> weekday_name(9)
#         >>> weekday_name(0)
#     """

def weekday_name(day_of_week):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    if day_of_week >= 1 & day_of_week <= 7:
        return days[day_of_week]
    else:
        print(None)


# def last_element(lst):
#     """Return last item in list (None if list is empty.
    
#         >>> last_element([1, 2, 3])
#         3
        
#         >>> last_element([]) is None
#         True
#     """

# def last_element(list):
#     last_el = list[-1]
#     if len(list) == None:
#         return True
#     else: return last_el
# print(last_element)

#mine

def last_element(lst):
  # """Return last item in list (None if list is empty.

  #     >>> last_element([1, 2, 3])
  #     3

  #     >>> last_element([]) is None
  #     True
  # """

  if lst:
      return lst[-1]

print(last_element([]))




# def number_compare(a, b):
#     """Report on whether a>b, b>a, or b==a
    
#         >>> number_compare(1, 1)
#         'Numbers are equal'
        
#         >>> number_compare(-1, 1)
#         'Second is greater'
        
#         >>> number_compare(1, -2)
#         'First is greater'
#     """

def number_comare(a,b):
    if a == b:
        print('Numbers are equal')
    elif b > a:
        print('Second is greater')
    else: 
        print('First is greater')

number_comare(1,1)

#mine



# def reverse_string(phrase):
#     """Reverse string,

#         >>> reverse_string('awesome')
#         'emosewa'

#         >>> reverse_string('sauce')
#         'ecuas'
#     """


#mine
def reverse_string(phrase):
    lst = list(phrase)
    lst.reverse()
    print(lst)
    s = " "
    new = s.join(lst)
    return new

    
print(reverse_string('Hello'))



# def single_letter_count(word, letter):
#     """How many times does letter appear in word (case-insensitively)?
    
#         >>> single_letter_count('Hello World', 'h')
#         1
        
#         >>> single_letter_count('Hello World', 'z')
#         0
        
#         >>> single_letter_count("Hello World", 'l')
#         3
#     """

def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

def multiple_letter_count(phrase):
    counter = {}
    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1
    return counter

    

# def multiple_letter_count(phrase):
#     """Return dict of {ltr: frequency} from phrase.

#         >>> multiple_letter_count('yay')
#         {'y': 2, 'a': 1}

#         >>> multiple_letter_count('Yay')
#         {'Y': 1, 'a': 1, 'y': 1}
#     """

#     counter = {}

#     for ltr in phrase:
#         counter[ltr] = counter.get(ltr, 0) + 1

#     return counter


# def list_manipulation(lst, command, location, value=None):
#     """Mutate lst to add/remove from beginning or end.

#     - lst: list of values
#     - command: command, either "remove" or "add"
#     - location: location to remove/add, either "beginning" or "end"
#     - value: when adding, value to add

#     remove: remove item at beginning or end, and return item removed

#         >>> lst = [1, 2, 3]

#         >>> list_manipulation(lst, 'remove', 'end')
#         3

#         >>> list_manipulation(lst, 'remove', 'beginning')
#         1

#         >>> lst
#         [2]

#     add: add item at beginning/end, and return list

#         >>> lst = [1, 2, 3]

#         >>> list_manipulation(lst, 'add', 'beginning', 20)
#         [20, 1, 2, 3]

#         >>> list_manipulation(lst, 'add', 'end', 30)
#         [20, 1, 2, 3, 30]

#         >>> lst
#         [20, 1, 2, 3, 30]

#     Invalid commands or locations should return None:

#         >>> list_manipulation(lst, 'foo', 'end') is None
#         True

#         >>> list_manipulation(lst, 'add', 'dunno') is None
#         True
#     """

def list_manipulation(lst, command, location, value=None):
    if command == "add" and location == "end":
        return lst.pop()
    elif command == "remove" and location == "beginning":
        return lst.pop(0)
    elif command == "add" and location == "beginning":
        lst.insert(0, value)
    elif command == "add" and location == "end":
        lst.append(value)
    return lst

# def is_palindrome(phrase):
#     """Is phrase a palindrome?

#     Return True/False if phrase is a palindrome (same read backwards and
#     forwards).

#         >>> is_palindrome('tacocat')
#         True

#         >>> is_palindrome('noon')
#         True

#         >>> is_palindrome('robert')
#         False

#     Should ignore capitalization/spaces when deciding:

#         >>> is_palindrome('taco cat')
#         True

#         >>> is_palindrome('Noon')
#         True
#     """
def is_palindrome(phrase):
    one = list(phrase)
    two = one.copy()
    two.reverse()
    if one == two:
        return True
    else:
        return False


# def frequency(lst, search_term):
#     """Return frequency of term in lst.
    
#         >>> frequency([1, 4, 3, 4, 4], 4)
#         3
        
#         >>> frequency([1, 4, 3], 7)
#         0
#     """

def frequencey(lst, search_term):
    count = 0
    for num in lst:
        if num == search_term:
            count += 1
    return count


# def flip_case(phrase, to_swap):
#     """Flip [to_swap] case each time it appears in phrase.

#         >>> flip_case('Aaaahhh', 'a')
#         'aAAAhhh'

#         >>> flip_case('Aaaahhh', 'A')
#         'aAAAhhh'

#         >>> flip_case('Aaaahhh', 'h')
#         'AaaaHHH'

#     """

#mine
def flip_case(phrase, to_swap):
    big = to_swap.upper()
    little = to_swap.lower()

    for letter in phrase:
        if to_swap == big:
            letter.lower()
        elif to_swap == little:
            letter.upper()


def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out

    # Alternate phrasing: a bit clever, same runtime, and harder to
    # read:

    # to_swap = to_swap.lower()
    #
    # fixed = [
    #     (char.swapcase() if char.lower() == to_swap else char)
    #     for char in phrase
    # ]
    #
    # return "".join(fixed)

def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """


#mine
def multiply_even_numbers(nums):
    lst = []
    for num in nums:
        if num % 2 == 0:
            lst.append(num)
    for num in lst:
        result = result * num
    return result
print(multiply_even_numbers([1,2,3,4,5,6,7]))


# def multiply_even_numbers(nums):

#     product = 1

#     for num in nums:
#         if num % 2 == 0:
#             product = product * num

#     return product

#this starts at 1, if it is even, it will take the first even number, multiply it by 1, and then so on...


# def capitalize(phrase):
#     """Capitalize first letter of first word of phrase.

#         >>> capitalize('python')
#         'Python'

#         >>> capitalize('only first word')
#         'Only first word'
#     """


#mine
def capitalize(phrase):
  big = phrase.capitalize()
  return big

def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """


def compact(lst):
    return [el for el in lst if bool(el)]
#return the element, loop the the list, and if the element is true



# def intersection(l1, l2):
#     """Return intersection of two lists as a new list::
    
#         >>> intersection([1, 2, 3], [2, 3, 4])
#         [2, 3]
        
#         >>> intersection([1, 2, 3], [1, 2, 3, 4])
#         [1, 2, 3]
        
#         >>> intersection([1, 2, 3], [3, 4])
#         [3]
        
#         >>> intersection([1, 2, 3], [4, 5, 6])
#         []
#     """
#     both = l1 & l2
#     return both

#mine
def intersection(l1, l2):
    set1 = set(l1)
    both = set1.intersection(l2)
    return both


# def intersection(l1, l2):
#     set2 = set(l2)

#     return [val for val in l1 if val in set2]

#     # Alternatively, using built-in set math:
#     # return list(set(l1) & set(l2))

def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)

    return [true_list, false_list]


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # find the highest value (the most frequent number)

    max_value = max(counts.values())

    # now we need to see at which index the highest value is at

    for (num, freq) in counts.items():
        if freq == max_value:
            return num


def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('subtract', 4, 1.5, make_int=True)
        
    """


def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a -b
    elif operation == 'multipy':
        result = a * b
    elif operation == 'divide':
        result = a / b
    else:
        return
    
    if make_int:
        result = int(result)
    return f"{message} {result}"
    

    
def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """


def friend_date(a,b):
    elmo = ('Elmo', 5, ['hugging', 'being nice'])
    sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
    gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

    if set(a[2]) & set(b[2]):
        return True
    else:
        return False

    # can even do by converting to boolean!
    #
    # return bool(set(a[2] & set(b[2])


def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """

def triple_and_filter(nums):
    lst = []
    for num in nums:
        res = num * 3
        if res % 4 == 0:
            lst.add()
        return lst

def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    
    return [f"{person['first']} {person['last']}" for person in people]


def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    return sum([num for num in nums if isinstance(num, float)])

def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """


#mine
def list_check(lst):
    for val in lst:
        if type(val) == list
        return True
    else: return

#   for item in lst:
#         if not isinstance(item, list):
#             return False

#     return True

def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

def remove_every_other(lst):
    return lst[::2]



def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    already_visited = set()

    for i in nums:
        difference = goal - i

        if difference in already_visited:
            return (difference, i)

        already_visited.add(i)

    return ()


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

def vowel_count(phrase):
    counts = {}
    vowels = set("aeiouAEIOU")
    for char in phrase:
        if char.lower() in vowels:
            counts[char.lower()] = counts.get(char.lower(), 0) + 1
    return counts



VOWELS = set("aeiou")


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    #lowercasing the phrase
    phrase = phrase.lower()
    #making an empty dictionary
    counter = {}
    #for each letter in the phrase
    for ltr in phrase:
        #if the letter shows up in our Vowels set
        if ltr in VOWELS:
            #make the key, that letter, equal to the value of 0, +1 everytime it happens
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter

def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

def titleize(phrase):
    phrase = phrase.title()
    return phrase



def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    n_list = [n for n in range (1, num // 2 + 1) if num % n == 0]

    n_list.append(num)

    return n_list

    # or could write by hand with a while loop
    #
    # factors = []
    #
    # while(n <= num):
    #     if num % n == 0:
    #         factors.append(n)
    #     n += 1
    #
    # return factors

    
def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """


    if isinstance(collection, dict):
        return sought in collection.values()

    if start is None or isinstance(collection, set):
        return sought in collection

    return sought in collection[start:]

def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

def repeat(phrase, num):
    if type(num) == int:
        return f"{phrase *num}"
    else:
        return
    

def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

def truncate(phrase, n):
    if n < 3:
        return "Truncation must be at least 3 characters."

    if n > len(phrase) + 2:
        return phrase

    return phrase[:n - 3] + "..."


def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """


def two_list_dictionary(keys,values):
    new = {}
    for k,v in enumerate(keys):
        new[v] = values[k] if v < len(values) else None
    return new




    out = {}

    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx < len(values) else None

    return out

    # Another way using a feature from Python's standard library. We don't expect
    # you to have found this one---but it's a good example of how knowing the
    # standard library is so useful!

    # from itertools import zip_longest
    # return dict(zip_longest(keys, values))



def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

def sum_range(nums, start = 0, end=None):
    if end is None:  
        end = len(nums) #sets the end index to the length of the list if it not provided

    return sum(nums[start:end + 1]) #this calculates the sum of the numbers from the start of the index to the end index and it is inclusive

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    

def same_frequency(num1, num2):
    counter1 = {}
    counter2 = {}
    for num in num1:
        counter1[1] = counter1.get(num,0) + 1
        return counter1
    
def freq_counter(coll):
    """Returns frequency counter mapping of coll."""

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    return freq_counter(str(num1)) == freq_counter(str(num2))



def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

def two_oldest_ages(ages):
    new_ages = set(ages)
    for age in ages:
        a1 = None
        if age > a1:
            a1 = age
        return a1
    

def two_oldest_ages(ages):
        # find two oldest by sorting unique; this is O(n log n)

    uniq_ages = set(ages) #creating a set to have unique numbers
    oldest = sorted(uniq_ages)[-2:] #sorting them by lowest to highest, grabbing the last 2
    return tuple(oldest) #returning a tuple pair

    # a longer, but O(n) runtime would be:
    #
    # uniq_ages = set(ages)
    # oldest = None
    # second = None
    #
    # for age in uniq_ages:
    #     if oldest is None or age > oldest:
    #         second = oldest
    #         oldest = age
    #     elif second is None or age > second:
    #         second = age
    #
    # return (second, oldest)

def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

def find_the_duplicate(nums):
    num_set = set(nums) #initialize an empty set
    for num in nums:
        if num in num_set:
            return num
        num_set.add(num)


def find_the_duplicate(nums):
    seen = set() #making a set

    for num in nums: #for each number in the list
        if num in seen: #Set starts out empty, so if it IS in the set, then return the number because that means its a duplicate
            return num #return the number
        seen.add(num) #add the number to the set

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total

    # or, probably too tersely:
    #
    # return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))])


def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

def min_max_keys(d):
    keys = d.keys() #retrieves a view of all keys in a dictionary

    return (min(keys), max(keys)) #returns a tuple containing the min and max keys
#min() and max() do what they say, they are built in functions

def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

def find_greater_numbers(nums):
    count = 0
    for num in nums:
        if num[0] < nums[num]:
            count += 1
    return count

def find_greater_numbers(nums):
    count = 0
    for i in range(len(nums)): #iterates over each el in the list
        for j in range(i + 1, len(nums)): #iterates over el to the right of the current element
            if nums[j] > nums[i]:
                count += 1

    return count

def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here



def is_odd_string(word):
    # to find the char position, we'll change it's ordinal ASCII number into
    # a 1-based number ("a" = 1, "b" = 2). To do that, let's subtract
    # this from it

    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 == 1

def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

def valid_parentheses(parens):
    count = 0
    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1

        # fast fail: too many right parens
        if count < 0:
            return False

    return count == 0

def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

def three_odd_numbers(nums):
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True

    return False

def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = set("aeiou")

    string = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)


def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    with open(filename) as f:
        for line in f:
            # remove newline at end of line!
            line = line.strip()
            print(f"- {line}")

