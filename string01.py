def main():
    print('Hello')

    no1 = 4
    no2 = 6

    print('Value number one is {} and Value number two is {}'.format(no1,no2))

    str1 = "top ten programming languages in 2019"
    u = str1.split()
    print(u)

    for i in u:
        print(i, end='-')

    print('\n')

if __name__ == "__main__" : main()