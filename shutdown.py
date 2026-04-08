def check_shutdown():
    shutdown = input("Do you want to shut down? (yes/no): ")
    
    if shutdown == "yes":
        print("Shutting down")
    elif shutdown == "no":
        print("Not shutting down")
    else:
        print("Invalid input")

check_shutdown()

    
   