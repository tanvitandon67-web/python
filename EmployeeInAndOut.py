class employee :
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructer called")


def create_object() :
    print("making object")
    ob = employee()

    print("Function ended")
    return ob

print("Calling create object function")
ob = create_object()
print("Program ended")
