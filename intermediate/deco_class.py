
class countcalls:

    def __init__(self, func):
        self.func = func
        self.numcalls = 0

    def __call__(self, *args, **kwargs):
        self.numcalls += 1
        print(f"This is executed {self.numcalls} times")
        return self.func(*args, **kwargs)



@countcalls
def sayhello():
    print("hello")


sayhello()
sayhello()