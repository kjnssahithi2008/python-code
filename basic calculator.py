a=int(input("give 1st number= "))
b=int(input("give 2nd number= "))
operator=input("give operator= ")
if operator=="+":
    print(f"add of a,b={a+b}")
elif operator=="-":
    print(f"sud of a,b={a-b}")
elif operator=="*" :
    print(f"mult of a,b={a*b}")  
elif operator=="/"  :
    print(f"divi oalf a,b={a/b}")  
else:
    print("invalid operator")       