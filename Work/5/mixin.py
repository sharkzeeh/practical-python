class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class Loud:
    '''
    This class is not usable in isolation.
    It mixes with other classes via inheritance.

    super() delegates to the next class on the MRO.
    The tricky bit is that you don't know what it is. 
    You especially don't know what it is if multiple inheritance is being used.
    '''
    def noise(self):
        return super().noise().upper()
        

class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass


if __name__ == '__main__':
    # l = Loud()
    # l.noise() # AttributeError: 'super' object has no attribute 'noise'

    loud_dog = LoudDog()
    sound = loud_dog.noise()
    print(sound)
    print(LoudDog.__mro__)