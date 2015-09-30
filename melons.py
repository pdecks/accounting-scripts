melon_names = {
    1: "Honeydew",
    2: "Crenshaw",
    3: "Crane",
    4: "Casaba",
    5: "Cantaloupe",
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

# make new outer dictionary by melon names
melon_dict = {}
for key in melon_names:
    melon_name = melon_names[key]
    melon_price = melon_prices[key]
    melon_seeds = melon_seedlessness[key]
    default = 'N/A'
    melon_dict[melon_name] = {'price': melon_price,
                              'seeds': melon_seeds,
                              'flesh': default,
                              'rind': default,
                              'avg_wt': default}

#print melon_dict

#melon_dict.keys()
#melon_dict.items()
