
# 1 Create a for loop that counts from 0 to 10, and prints odd numbers
# to the screen. Use the skeleton below
for i in range(1,11):
    if i%2 == 0:
        print(i)
        continue
    
print('#~~#')    
        
# 2 Create a while loop that counts from 0 to 10, and prints odd numbers
# to the screen. Use the skeleton below:
x = 1
while x < 11:
    if x%2 != 0:
        print(x)
    x += 1

print('#~~#')

# 3 Create a program with a for loop and a break statement. The program
# should iterate over characters in an email address, exit the loop when
# it reaches the @ symbol, and print the part before @ on one line.
# Use the skeleton below:
email = 'leninesprj@gmail.com'
for ch in email:
    if ch == '@':
        break
    print(ch, end='')
    

#  4 Create a program with a for loop and a continue statement. The program
# should iterate over a string of digits, replace each 0 with x, and print the
# modified string to the screen. Use the skeleton below:
code = '0165031806510'

for digit in code:
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
