class InventoryControl:
    def __init__(self):
        self.__ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }
        self.__minimum_inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.__total_ingredients = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, _customer, order, _day):
        for item in self.__ingredients[order]:
            if self.__total_ingredients[item] < self.__minimum_inventory[item]:
                self.__total_ingredients[item] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.__total_ingredients
