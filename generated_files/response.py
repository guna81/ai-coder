import random

def func(x):
    return x * 2

def main():
    for i in range(10):
        print(func(random.randint(1, 100)))

if __name__ == "__main__":
    main()