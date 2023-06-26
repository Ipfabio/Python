from item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attribute / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f'Broken Phones {broken_phones} is not greater or equal to zero!'

        # Assing to self object
        self.broken_phones = broken_phones
