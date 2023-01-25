s=[]
def main():
    while True:
        x = check()
        s.append(x)

def check():
    while True:
        try:
            return input("")
        except EOFError:
            my_dict = {i:s.count(i) for i in s}
            for i in sorted(my_dict):
                print (my_dict[i], i.upper())
            exit()

main()
