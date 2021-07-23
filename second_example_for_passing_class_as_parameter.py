#https://www.pythonprogramming.in/how-do-i-pass-instance-of-an-object-as-an-argument-in-a-function-in-python.html

class Vehicle:
    def __init__(self):
        self.trucks = []

    def add_truck(self, truck):
        self.trucks.append(truck)


class Truck:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return "{}".format(self.color)


def main():
    v = Vehicle()
    for t in 'Red Blue Black'.split():
        t = Truck(t)
        v.add_truck(t)
    print(v.trucks)


if __name__ == "__main__":
    main()
