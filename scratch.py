from get_drink import Drink
import time

drink = Drink()

print(drink.get_random())
time.sleep(5)
print(drink.get_by_spirit('gin'))
