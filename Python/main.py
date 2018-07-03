name = input("hello what is your name")

def welcome(name):
    if name == "Max":
        print("hello Max")
    else:
        print("welcome to python {}".format(name))

welcome(name)

Mits = ["Bennett","kaitlin","Rhiannon","Austin","Travis"]

for mit in Mits:
    welcome(mit)
