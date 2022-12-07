N = int(input())
if 360 % N == 0:
    print("Yes it is possible to cut the cake into N equal pieces.")
else:
    print("No it is not possible to cut the cake into N pieces.")
if N <= 360:
    print("Yes it is possible to cut the cake into N pieces of any size.")
else:
    print("No it is not possible to cut the cake into N pieces of any size")
if N <= int(pow(720, 0.5)):
    print("Yes it is possible to cut the cake into N pieces such that no two of them are equal")
else:
    print("No it is not possible to cut the cake into N pieces such that no two of them are equal")