# if 5>4:
#     print("a u sb")
# elif 3>1:
#     print("yes you are")
# sum=0
# sum1=0
# number=0
# while number<20:
#     number+=1
#     sum+=number
#     if sum>100 :
#         break
# print("the answer is",sum)
# for num in range(1,100):
#     print(num)
    # sum1+=num
    # num+=1
# print("sum is:",sum1)
def main():
    sum=0.0
    count=0
    x=eval(input("enter a number"))
    while x>=0:
        sum+=x
        count=count+1
        x=eval(input("enter a number"))
    print("the answer is",sum)

main()