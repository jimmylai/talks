import time

def a():
    c(0.1)

def b():
    c(0.2)

def c(n):
    d(n)

def d(n):
    time.sleep(n)

def run():
    a()
    b()

if __name__ == "__main__":
    run()
