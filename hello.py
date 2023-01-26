



def say_hello():
    print("Hello");
    return "Hello"
    
def say_hello_to(name: str) -> str:
    print(f"Hello, {name}")
    return f"Hello, {name}"
    



    
def say_hello_loudly(name: str) -> str:
    print(f"HELLO, {name.upper()}!")
    return f"HELLO, {name.upper()}!"
    
def say_hello_excitedly(name: str) -> str:
    print(f"HELLO, {name}!!!!")
    return f"HELLO, {name}!!!!"

say_hello()
say_hello_to("John")
say_hello_loudly("Jane")
say_hello_excitedly("Bob")