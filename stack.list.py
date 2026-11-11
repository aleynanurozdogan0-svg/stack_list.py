def create():
    S=[]
    top=-1
    print("empty stack created")
    return S,top
 
def isEmpty(top):
    if(top<=-1):
        return True
    else:
        return False
 
def push(S,top):
    no=int(input(("enter a number to push: ")))
    top+=1
    S.insert(top,no)
    return S,top
 
def pop(S,top):
    if(isEmpty(top)==1):
        print("underflow: there is no element in the stack")
    else:
        print("the element to pop is", S[top])
        S.remove(S[top])
        top-=1
    return S,top
   
def peek(S,top):
    if(isEmpty(top)==1):
        print("underflow: there is no element in the stack")
    else:
        print("the element to peek is", S[top])
 
def display(S,top):
    print("top is at index ->",top)
    if(isEmpty(top)==True):
        print("\n stack is empty")
    else:
        print("the elements in the stack is:")
        for i in range(top,-1,-1):
            print(i,"->",S[i])
 
 
def menu():
    print("\n------menu------")
    print("1. push an element")
    print("2. pop from stack")
    print("3. peek from stack")
    print("4. display the stack")
    print("5. exit")
    opt=int(input("enter a valid menu item....."))
    return opt
 
 
St,top=create()
i=1
while(i>0 and i<5):
    i=menu()
    if(i==1):
        St,top=push(St,top)
        display(St,top)
    elif(i==2):
        St,top=pop(St,top)
        display(St,top)
    elif(i==3):
        peek(St,top)
    elif(i==4):
        display(St,top)
    else:
        print("exit")