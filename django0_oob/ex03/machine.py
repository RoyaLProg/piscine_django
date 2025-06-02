from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
from random import randint


class CoffeeMachine:
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.price = 0.90
            self.name = 'empty cup'

        def description(self):
            return 'An empty cup ?! Gimme my money back!'

    class BrockenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired"

    def __init__(self):
        self.use = 0

    def repair(self):
        self.use = 0

    def serve(self, drink):
        if self.use > 10:
            raise self.BrockenMachineException()
        self.use = self.use + 1
        if randint(0, 99) < 20:
            return self.EmptyCup()
        return drink


def main():
    machine = CoffeeMachine()

    for i in range(0, 20):
        to_command = randint(0, 3)
        match to_command:
            case 0:
                to_command = Coffee()
            case 1:
                to_command = Tea()
            case 2:
                to_command = Chocolate()
            case 3:
                to_command = Cappuccino()
        try:
            drink = machine.serve(to_command)
            print(drink)
        except CoffeeMachine.BrockenMachineException as error:
            print(error.message)
            machine.repair()


if __name__ == "__main__":
    main()
