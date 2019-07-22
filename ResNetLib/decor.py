
def decorator(print_somthing, something):
    print("call decorator before")
    print_somthing(something)
    print("call decorator after")


def print_somthing(something):
    print("hello " + something)


if __name__ == "__main__":
    decorator(print_somthing, "apple")