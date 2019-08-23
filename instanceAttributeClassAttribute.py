class Chicken(object):
        weight = 3 #類別屬性

        def __init__(self):
            self.age = 18 #實例屬性(or 資料屬性)
            self.weight = 2


        def get_age(self):
            return self.age

        def printJack(self):
            print("Jack:" + self.jack)

c = Chicken()

#print("Chicken.age "+Chicken.age)
print("Chicken.weight " + str(Chicken.weight))

# print("c.age " + str(c.age))
# print("c.weight ~ " + str(c.weight))

# print("c.__dict__ " + str(c.__dict__))


# c.jack="Jack~"

# print("After c.__dict__ " + str(c.__dict__))

#print(c.get_age)