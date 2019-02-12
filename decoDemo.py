class Harley():
# Creating Constructor 

    def __init__(self,**kwargs):
        self.features = kwargs

# Creating Setter Method

    def setFeatures(self , k , v):
        self.features[k] = v

# Createing Getter Method

    def getFeatures(self , k):
        return self.features.get(k , None)

    @property
    def topSpeed(self):
        return self.features.get('topSpeed',None)

    @topSpeed.setter
    def topSpeed(self, ts):
        self.features['topSpeed'] = ts

    @topSpeed.deleter
    def topSpeed(self):
        del self.features['topSpeed']

def main():
    
    streetBob = Harley()
    streetBob.setFeatures('cc','1800')
    print("The StreetBob is {} cc.".format(streetBob.getFeatures('cc')))

    StreetBob.topSpeed = 300
if __name__ == "__main__" : main()