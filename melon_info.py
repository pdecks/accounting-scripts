"""
Prints out all the melons in our inventory
"""
# import the melons dictionary from melons.py
# note: if we write "import melons" we would have to call melons.melons
from melons import melons


def print_melon(melons):
    """ Take melons dictionary and print out all melon information by melon name.

    Takes a dictionary where keys = melon names, values = attr dictionary.
    Returns none.
    """
    for melon in melons:
        # print keys of outer dictionary
        print melon.upper()
        # print values from inner dictionary
        for attr, val in melons[melon].items():
            # convert Boolean to useful information
            if attr == 'seeds':
                if val is False:
                    print_val = 'seeded'
                else:
                    print_val = 'seedless'
                print "Seeded: {}".format(print_val)
            else:
                print "{}: {}".format(attr, val)
        print

    return None


print_melon(melons)



# THIS WAS FROM THE ORIGINAL FILE PROVIDED TO US
# name = melon_dict
# price = melon_dict[key][price]

# print "{}s {} seeds and are ${:.2f}.".format(melon_name, melon_dict[melon_name])

# from melons import melon_names, melon_seedlessness, melon_prices

# def print_melon(name, seedless, price):
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
