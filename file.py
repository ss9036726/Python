def main():
    print('Hello')

    #Open a file in read mode


    # file = open("sample.txt")

    # for text in file:
    #     print(text, end="")


    #create a file from existing file

    newFile = open("sample.txt")
    outputFile = open("MyFile.txt","w")

    for text in newFile:
        print(text, file = outputFile, end="")

    print("Work Done!")


if __name__ == "__main__" : main()
