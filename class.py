class fruit():
    def __init__(self,color, taste,shape,preference):
        self.color = color
        self.taste = taste
        self.shape = shape
        self.preference = preference

    def get_shape(self):
        return self.shape
    def set_shape(self,newshape):
        self.shape = newshape
    def increase_preference(self):
        self.preference +=1
    def showfruit(self):
        print("color:", self.color)
        print("shape", self.shape)
        print("taste", self.taste)

apple = fruit("red","sour","round",1)
apple.showfruit()
apple.increase_preference()
apple.set_shape("sphere")
apple.showfruit()

banana = fruit("yellow","sweet","cylinder",2)
banana.showfruit()
banana.increase_preference()
banana.showfruit()



    

        