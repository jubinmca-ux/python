str1=input("enter first string:")
str2=input("enter second string:")
newstr1 = str2[0] + str1[1:]
newstr2 = str1[0] + str2[1:]
result = newstr1 +" "+newstr2
print("result:",result)
