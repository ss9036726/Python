def main():
    buff = 6000000

    newFile = open("lap.jpg","rb")
    outputFile = open("lapnew.jpg","wb")

    buffer = newFile.read(buff)

    while len(buffer):
        outputFile.write(buffer)
        newFile.read(buff)

    print("Work Done!")

if __name__ == "__main__" : main()