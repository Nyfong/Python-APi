# import time module (internail module)
import time
name = input("Please enter your name\n:")
gussing_name = '* lemme guess your name'
print(gussing_name, end=" ")
# adding 2 seconds time delay
for i in range(3):
    print('.', end='')
    time.sleep(1)
print("\n")
your_name = f'haha your name is {name}'
print(your_name)