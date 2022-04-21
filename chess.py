str1 = int(input())
col1 = int(input())
str2 = int(input())
col2 = int(input())

if ((str1+col1) % 2 != 0 and (str2+col2) % 2 != 0) or ((str1+col1) % 2 == 0 and (str2+col2) % 2 == 0):     
    print("YES")
else:
    print("NO")

"""if (str1+col1) % 2 != 0 and (str2+col2) % 2 != 0:
    print ("YES")
elif (str1+col1) % 2 == 0 and (str2+col2) % 2 == 0:
    print("YES")
else:
    print("NO")"""