stack =[]
stack_size=int(input("Please write stack size\n"))

#defined all functions 

def size():
    print(len(stack))

def top():
    if len(stack)>0:
        print(stack[stack_size-1])
    else:
        print("Stack is EMPTY")
    

def pop():
    if len(stack)>0:
        stack.pop()
    else:
        print("Stack is EMPTY")
    

def push():
    g=input()
    if stack_size==len(stack):
        print("Stack is FULL")
    else:
        stack.append(g)
        g=""

def empty():
    stack=[]

def printall():
    print(stack)

def isempty():
    print(len(stack)==0)

def isfull():
    print(len(stack)==stack_size)

print("\nPrint and launch commands")

print("""empty() – Returns whether the stack is empty
size() – Returns the size of the stack 
top() – Returns a reference to the top most element of the stack 
push() – Adds the element you written after launch code at the top of the stack
pop() – Deletes the top most element of the stack
printall() – Print stack
isempty() – Is stack empty?
isfull() – Is stack full?""")

while True:
    eval(input("Print your command and press enter\n"))     # eval(input()) function calling definations 

