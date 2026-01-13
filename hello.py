def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("What is your name? ")
    message = greet(name)
    print(message)