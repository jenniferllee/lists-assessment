"""List Assessment

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    # List comprehension
    odd_numbers = [number for number in numbers if number % 2 != 0]
    return odd_numbers

    # THIS ALSO WORKS:
    # odd_numbers = []
    # for number in numbers:
    #     if number % 2 != 0:
    #         print number
    #         odd_numbers.append(number)
    # return odd_numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo

    """

    # DOES NOT WORK:
    # for item in items:
    #     index = str(items.index(item))
    #     print index + " " + item

    # Expected:
    #     0 Toyota
    #     1 Jeep
    #     2 Toyota
    #     3 Volvo
    # Got:
    #     0 Toyota
    #     1 Jeep
    #     0 Toyota
    #     3 Volvo

    # THIS WORKS (but uses a built-in function):
    for count, item in enumerate(items):
        print count, item

    # THIS ALSO WORKS (but uses a counter):
    # count = 0
    # for item in items:
    #     print count, item
    #     count += 1


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    # Convert lists to sets to do set math.
    foods1_set = set(foods1)
    foods2_set = set(foods2)

    # Return an empty list if there are no items in common.
    if foods1_set & foods2_set == ([]):
        return []

    # Otherwise, return list with common items sorted alphabetically.
    # (Need to convert back to list to sort)
    else:
        common_foods = list(foods1_set & foods2_set)
        common_foods.sort()
        return common_foods


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    every_other_item = []

    for item in items:
        index = items.index(item)
        if index % 2 == 0:
            every_other_item.append(item)

    return every_other_item


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    # Sort numbers in increasing order.
    items.sort()

    # Return empty list if n is 0.
    if n == 0:
        return []

    # Otherwise, return last three numbers in list
    else:
        largest_items = items[(n*(-1)):]
        return largest_items


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
