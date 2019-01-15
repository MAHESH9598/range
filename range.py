### this is Example for.....range
"""To organaize sequence(range) of numbers from specified position to ending decide position
                    syntax 1 ----> range(num)
                    syntax 2 ----> range(start,end)
                    syntax 3 ----> range(start,end,step)
"""

### Examples :

sms = range(10)
for x in sms:
    print(x)

print("---Genarate 10 t0 20 numbers---")

for x in range(10, 21):
    print(x)

print("---Even Numbers Within 1 to 50---")
for x in range(2, 51, 2):
    print(x)

print("---Genarate 10 to 1 ---")
for x in range(10, 0, -1):
    print(x)

print("---Genarate Odd Number within 10 to 1 ---")
for x in range(9, 0, -2):
    print(x)

print("---Logic For Multiplication Table---")
n = 4
for k in range(1, 11):
    print(n, '*', k, '=', n * k)









