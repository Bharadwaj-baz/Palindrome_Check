a=input("Enter a word-- ")
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
if(a==b):
    print("The Entered Word is Palindrome!!\n")
else:
    print("The entered Word is Not Palindrome!!!\n")

