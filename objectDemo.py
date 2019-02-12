from classesDemo import Harley

def main():
    
    streetBob = Harley()
    streetBob.setFeatures('cc','1800')
    print("The StreetBob is {} cc.".format(streetBob.getFeatures('cc')))

    streetBob.setFeatures('hp','45')
    print("The Horsepower of streetbob is {}.".format(streetBob.getFeatures('hp')))

    streetBob.setFeatures('color','orange')
    print("The color of streetbob is {}.".format(streetBob.getFeatures('color')))
    streetBob.tyres();
    streetBob.seat();

    print('\n')

    fatBob = Harley()

    fatBob.setFeatures('cc','2000')
    print("The StreetBob is {} cc.".format(fatBob.getFeatures('cc')))

    fatBob.setFeatures('hp','85')
    print("The Horsepower of streetbob is {}.".format(fatBob.getFeatures('hp')))

    fatBob.setFeatures('color','blue')
    print("The color of streetbob is {}.".format(fatBob.getFeatures('color')))
    fatBob.seat();
    fatBob.tyres();


# # Object One
#     streetBob = Harley(1600)
#     streetBob.bigEngine()
#     streetBob.loudSound()

# # Object two

#     fatBob = Harley(1800)
#     fatBob.bigEngine()
#     fatBob.loudSound()

if __name__ == "__main__" : main()