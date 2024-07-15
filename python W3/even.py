list=[1,2,3,4,5,6,7,8,9]
evensum=0
for num in list:
    if num % 2==0:
        evensum+= num
print(f"the sum of all even numbers are:{evensum}")
