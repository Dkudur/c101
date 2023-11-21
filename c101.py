# 67sec --> 1 min and 7 sec

# 01:07
# 01:06
# 01:05


# 00:01
# 00:00


x = 10

while x > 0:
    print (x)
    x -= 1


y = 0

while y <= 20:
    print(y)
    y += 2

# ------------------------------------------------------------------------------

import time


def countDown(s):
    while s > 0:
        minutes = int(s / 60)
        seconds = int (s % 60)

        timer = f'{minutes} : {seconds}'

        print(timer)
        
        s -= 1

        time.sleep(1)

    print("Times Up!!")



seconds = int(input("Enter the time in seconds: "))

countDown(seconds)