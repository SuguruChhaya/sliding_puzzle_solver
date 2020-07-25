'''
In this file I will try to study how the continue command operates in while loops.
'''

a = 7
while a > 0:
    if a ==5:
        print("Went through first")
        a -=1
        continue

    #*Continue allows makes it so that the other if statements are ignored and the loop just restarts
    if a ==5:
        print("a equals five!!")
    a -= 1

print(a)