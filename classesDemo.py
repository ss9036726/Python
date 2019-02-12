from inherit import Bike

class Harley(Bike):
# Creating Constructor 

    def __init__(self,**kwargs):
        self.features = kwargs

# Creating Setter Method

    def setFeatures(self , k , v):
        self.features[k] = v

# Createing Getter Method

    def getFeatures(self , k):
        return self.features.get(k , None)

#     def __init__(self, value):
#         self._cc = value

# # Create Two Methods

#     def bigEngine(self):
#         print("Harley has a very big engine of {} cc".format(self._cc))

#     def loudSound(self):
#         print("Potato Sound is very good")

