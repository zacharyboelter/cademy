from datetime import date


# import datetime from date, set it to var
todays_date = date.today()
print(todays_date)

# set vars, print sum and remainder
product = 2 * 2
remainder = 1398 % 11
print(product, remainder)


# set cucumber vars, set cost, print type and total cost
cucumbers = 1
price_per_cucumber = 3.25

total_cost = cucumbers * price_per_cucumber

print(type(total_cost))
print(total_cost)

# jaden case, basically just capitalize the first letter of every word in a given string

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case("hello, how's it going t'day?"))