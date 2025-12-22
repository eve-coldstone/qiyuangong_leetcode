
def reverse(n):
    rev=0
    temp=n
    n=abs(n)
    while n!=0:
        rev=rev*10+n%10
        n=n//10
    if rev>2**31 or rev==0 or temp>0 and rev==2*31:
        return 0
    return rev*(temp//abs(temp))

if __name__ == "__main__":
    x = -123050
    print(f"Result for reverse integer is: ", reverse(x))



    

