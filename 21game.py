import time

def wrong_input():
    print("wrong input")
    time.sleep(5)
    exit()

print("Start!")
u1 = input("n1 = ").split(' ')
u1 = int(max(u1))

if u1 in range(4):
    if u1 == 1:
        c = [2,3,4]
    elif u1 == 2:
        c = [3,4]
    elif u1 == 3:
        c = [4]
    print(c)
else:
    wrong_input()

u2 = input("n2 = ").split(' ')
u2 = int(max(u2))

if u2 in range(8):
    if u2 == 5:
        c = [6,7,8]
    elif u2 == 6:
        c = [7,8]
    elif u2 == 7:
        c = [8]
    print(c)
else:
    wrong_input()

u9 = input("n3 = ").split(' ')
u9 = [int(u9[0]), int(u9[1]), int(u9[2])]
u9 = max(u9)

if u9 in range(12):
    if u9 == 9:
        c = [10,11,12]
    elif u9 == 10:
        c =[11,12]
    elif u9 == 11:
        c = [12]
    print(c)
else:
    wront_input()

u3 = input("n4 = ").split(' ')
u3 = int(max(u3))

if u3 in range(16):
    if u3 == 13:
        c = [14,15,16]
        print(c)
        u4 = input("n4 = ").split(' ')
        u4 = int(max(u4))

        if u4 == 17:
            c = [18,19,20]
            print(c)
            print("you lost!")
        
        if u4 == 18:
            c = [19,20]
            print(c)
            print("you lost!")

        if u4 == 19:
            c = [20]
            print(c)
            print("you lost!")

    if u3 ==14:
        c = [15,16]
        print(c)
        u4 = input("n4 = ").split(' ')
        u4 = int(max(u4))

        if u4 == 17:
            c = [18,19,20]
            print(c)
            print("you lost!")
        
        if u4 == 18:
            c = [19,20]
            print(c)
            print("you lost!")

        if u4 == 19:
            c = [20]
            print(c)
            print("you lost!")
        
    if u3 == 15:
        c = [16]
        print(c)
        u4 = input("n4 = ").split(' ')
        u4 = int(max(u4))

        if u4 == 17:
            c = [18,19,20]
            print(c)
            print("you lost!")
        
        if u4 == 18:
            c = [19,20]
            print(c)
            print("you lost!")
        
        if u4 == 19:
            c = [20]
            print(c)
            print("you lost!")
else:
    wrong_input()

time.sleep(20)
