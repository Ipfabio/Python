from phone import Phone
from keyboards import Keyboard


item1 = Phone("jscPhone", 1000, 3)
item2 = Keyboard("Dagon", 2000, 3)


# item1.apply_increment(0.2)
item1.apply_discount()
item2.apply_discount()

print(item1.price)
print(item2.price)



