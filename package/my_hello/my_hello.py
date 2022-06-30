

def do_hello(args=None):
    if args is None:
        args = []
    print("Hello, world!")
    for arg in args:
        print("Arg:", arg)
    return 0