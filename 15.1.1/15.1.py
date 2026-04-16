class Car:
    def __init__(self, brand, price, model, color):
        self.brand = brand
        self.price = price
        self.model = model
        self.color = color

    def display_details(self):
        print(self.brand)
        print(self.price)
        print(self.model)
        print(self.color)


class Car1(Car):
    def display_details(self):
        print(self.brand)
        print(self.price)
        print(self.model)
        print(self.color)


class Car2(Car):
    def display_details(self):
        print(self.brand)
        print(self.price)
        print(self.model)
        print(self.color)


b1, p1, m1, c1 = input().split()
b2, p2, m2, c2 = input().split()

car1 = Car1(b1, float(p1), m1, c1)
car2 = Car2(b2, float(p2), m2, c2)

car1.display_details()
car2.display_details()
