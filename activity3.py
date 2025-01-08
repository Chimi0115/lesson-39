num=int(input("Enter a number"))
if num>50:
    print(num,"number is greater than 50")
    if num%2==0:
        print("and the number is even")
    else:
        print("and the number is odd")
else:
    print(num,"number is lesser than 50")