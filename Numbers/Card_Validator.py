# # Credit Card Validator - Takes in a credit card number from a common credit card vendor
# # (Visa, MasterCard, American Express, Discoverer)
# # and validates it to make sure that it is a valid number (look into how credit cards use a checksum).



# From the rightmost digit, which is the check digit, and moving left, double the value of every second digit.
# If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then add the digits of the product
# (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or alternatively subtract 9 from the product (e.g., 16: 16 - 9 = 7, 18: 18 - 9 = 9).
# Take the sum of all the digits.
# If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula;
#  else it is not valid.
# 79927398713
def isCardValid(card):
    i=1
    sum = 0
    #initial case is the second to last num to be checked
    max = int(str.__len__(card)/ 2)+1
    temp = list(card)
    for i in range(1,max):
        digi = int(temp[str.__len__(card) - 2 * i])
        digi *= 2
        if digi > 10:
            digi = digi%10+(int(digi/10))%10# get the sum of units of 10th and 1st
        else:
            pass
        temp[str.__len__(card) - 2 * i] = digi
        print(digi)

    for i in range(0,str.__len__(card)):
        sum += int(temp[i]) # get the last one

    print(sum)
    if sum%10 == 0:
        return True
    else:
        return False





card = input("Enter card number for validation\n")
print(isCardValid(card))
