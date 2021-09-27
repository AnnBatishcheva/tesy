# Test of visual studio code
# Test 1
l = int(input())
if l<=1:
    print("ok")
if l == 2:
    print("Good")
if l>2:
    print("Wrong")
print(type(l))
print("Your number is",l)


# Test 2
numberk=float(input())
checko=100
while checko != 0:
    o=0
    o=int(input())
    if o==0:
        print("Cycle is cancelled")
        break
        
    elif o%2==0:
        numberk+=2
    else:
        numberk/=2
    checko-=20
print(numberk)

# test 3
'''j = True
if l == 2 or l == 1:
    j = False
print(j)'''
