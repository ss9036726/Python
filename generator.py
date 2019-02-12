def main():
    print("Hello")

# def squareList(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# def squareList(num):
#     for i in num:
#         yield(i*i)

# myNum = squareList([1,2,3,4,5])

# List Comprehension

myNum = [x*x for x in [1,2,3,4,5]]

print(myNum)

# print(next(myNum))

# print(list(myNum))
# print(next(myNum))
# print(next(myNum))
# print(next(myNum))
# print(next(myNum))

# for i in myNum:
#     print(i)

if __name__ == '__main__' : main()