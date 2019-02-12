import re
import urllib.request
from _codecs import encode

def main():
    print("Hello")

    web = urllib.request.urlopen('https://www.python.org/')

    for code in web:
        print(str(code,encoding='utf-8'),end=' ')

if __name__ == "__main__" : main()