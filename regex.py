import re

def main():
    file = open('google.txt')

    for i in file:
        print(re.sub('(G|g)oogle','********',i))

if __name__ == '__main__' : main()