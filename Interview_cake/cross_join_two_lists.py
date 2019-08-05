from itertools import permutations


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        """
        IceCreamMachine's scoops method

        :return: it returns all combinations of one ingredient and one topping.
        If there are no ingredients or toppings, the method should return an empty list.
        For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
        should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
        """
        combinations = []
        for ingredient in self.ingredients:
            for topping in self.toppings:
                combinations.append([ingredient, topping])
        return combinations


if __name__ == '__main__':
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())
