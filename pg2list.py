#list1=[11,-21,0,45,66,-93]
#for num in list1:
#	if num>=0:
#		print(num,end=" ")
#print("enter  the limit")
#n=int(input())
#square=[i*i for i in range (n)]
#print("square of n numbers \n",square)
#word=input("enter your word")
#for letter in word:
#	if letter in 'a e i o u':
#		print (letter,end = " ")
list1=['aravind','aparna']
print("the orginal list:in"+str(list1))
res=[ord(ele)for sub in list1 for ele in sub]
print("the ASCII list is :\n"+str(res))

