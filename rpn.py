#!/usr/bin/env python3

def add(a,b):
    return a+b

def subtract(a,b):
    return b-a;

ops = {
      '+':add,
      '-':subtract,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg1 = stack.pop()
            arg2 = stack.pop()
            function = ops[token]
            result = function(arg1,arg2)
            stack.append(result)
    print(stack)
    return stack.pop()

def main():
    while True:
        calculate(input("rpm calc> "))



if __name__ == '__main__':
    main()


