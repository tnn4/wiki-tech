import sys

print("Hello World, Python is definitely the nicest language in the entire universe")
print("Too bad it's so slow...")

class a_class:
    def __init__(self):
        self.data = []

    #fin

#ass

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    #fin
    
#ass

def main():
    scrub = "the biggest scrub in the world, you"
    print(f"python is a gay little language for {scrub}")
    a_point = Point(1,2)
    print(a_point.x)
    print(a_point.y)
#fin

if __name__ == "__main__":
    sys.exit(main())
#fi
