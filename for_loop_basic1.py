class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def display_info(self):
        print (self.price)
        print (self.max_speed)
        print (self.miles)
        return self
    def  ride(self):
        print('Riding')
        self.miles += 10
        print(self.miles)
        return self
    def reverse(self):
        print('Reversing')
        self.miles -=5
        print(self.miles)
        return self
ride1=Bike(100,30,10)
ride2=Bike(200,40,10)
ride3=Bike(300,50,10)
ride1.ride().ride().ride().reverse().display_info()
ride2.ride().ride().reverse().reverse().display_info()
ride3.reverse().reverse().reverse().display_info()
