# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = "My name is Rustam"
char_1 = "m"
result_1 = 0
counter = 0

while counter < len(string_1):
    if string_1 [counter] == char_1:
        result_1 += 1
    counter += 1

# print(result_1)




# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 48872
result_2 = 1
ind = 0
stop = len(str(number_1))



while ind < stop:
    result_2 *= number_1 % 10
    number_1 //= 10
    ind += 1

print(result_2)









# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 12345
result_3 = ''
counter = 1
while counter <= len (str(number_2)):
    result_3 += str(number_2)[- counter]
    counter += 1

print(result_3)