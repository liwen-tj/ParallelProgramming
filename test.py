x = 0
def f():
    #global x
    x = 100 # x is just local variable if not writing "global x"

if __name__ == '__main__':
    f()
    print x
