#
#Change Return Program -
# The user enters a cost and then the amount of money given. The program will figure out the change
#   and the number of quarters, dimes, nickels, pennies needed for the change.

import math
i = float(input("\nEnter num for getting change of it\n"))


quart = math.floor(i / .25)
i -= quart * .25
dime = math.floor(i / .1)
i -= dime * .1
nick = math.floor(i / .05)
i -= nick * .05
penn = math.ceil(i / .01)
i = round((i)- penn * .01)
print(quart,dime,nick,penn,i)


assert i == 0

print("quart is {}, dime is {}, nick is {},penn is {}".format(quart,dime,nick,penn))