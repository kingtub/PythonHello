# coding=UTF-8

class Robot:
    """表示一个有名字的机器人"""
    population = 0
    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print("Initializing {}".format(name))

    def die(self):
        print("{} died".format(self.name))
        Robot.population -= 1

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        print("There are {} Robots.".format(cls.population))


r1 = Robot('Rooo')
r1.say_hi()
Robot.how_many()

r2 = Robot('R2-D2')
r2.say_hi()
Robot.how_many()

r1.die()
r2.die()
Robot.how_many()