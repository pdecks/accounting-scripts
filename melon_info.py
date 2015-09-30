"""
Prints out all the melons in our inventory
"""

from melons import melon_dict


def print_melon(melon_dict):
    for melon in melon_dict:
        name = melon
        print "{}s have the following attributes:".format(name)
        attributes = melon_dict[name].keys()
        for prop in attributes:
            if prop == 'seeds':
                if melon_dict[name]['seeds'] is False:
                    val = 'N'
                else:
                    val = 'Y'
                print "Seeded: {}".format(val)
            else:
                print "{}: {}".format(prop, melon_dict[name][prop])
        print

    return  


print_melon(melon_dict)
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
