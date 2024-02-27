class Animal:
    alive = True

    @staticmethod
    def eat():
        print("This animal is eating")

    @staticmethod
    def sleep():
        print("This animal is sleeping")


class Rabbit(Animal):
    pass


class Fish(Animal):
    pass


class Hawk(Animal):
    pass


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

hawk.eat()
rabbit.sleep()
print(fish.alive)
