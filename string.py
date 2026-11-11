s=input("Enter a string:")
print("orginal string: ",s)
char=s[0]
s=s.replace(char,'$')
s=char+s[1:]
print(s)
