import csv

class Item:
    pay_rate = 0.8 # the pay rate after 20% disscount
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        # Assing to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        # print(f'Es un/a {name}, vale {price} y hay {quantity} en stock')

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price =  self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    

    @classmethod # Para que no pueda ser llamado como instancia
    def instatiate_from_csv(cls):
        with open('./data/items.csv', 'r') as f:
            reader = csv.DictReader(f) # Lee como diccionario
            items = list(reader) # Convertimos el diccionario a una lista
        
        for item in items:
            Item(
                name= item.get('name'),
                price= float(item.get('price')),
                quantity= int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): # We change the name depends on who call it with: __class__.__name__
        return f'{self.__class__.__name__} ("{self.name}", {self.__price}, {self.quantity})'

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, Fabio.
        """
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()