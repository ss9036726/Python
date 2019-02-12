def main():
    print("Hello")

    days = dict(
        one = "Monday",
        two = "Tuesday",
        three = "Wednesday",
        four = "Thursday",
        five = "Friday",
        six = "Saturday",
        seven = "Sunday"
    )

    day = "four"

    print(days[day])

    day = "eight"
    # if no match found in the switch case you can use default case by using get method
    
    print(days.get(day, 'No Match'))

if __name__ == "__main__": main()