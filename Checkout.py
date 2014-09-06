from CheckoutLibrary.Product import Product
from CheckoutLibrary.PricingRule import PricingRule
from CheckoutLibrary.Order import Order
from CheckoutLibrary.CheckedOutItem import CheckedOutItem
from CheckoutLibrary.PriceCalculator import PriceCalculator

import sys

# products
apple = Product("Apple", "A")
orange = Product("Orange", "O")
pear = Product("Pear", "P")
strawberry = Product("Strawberry", "S")

# please enter the rules in order; put the highest priority rule first

# rules for apple
apple.pricingRules = [
	PricingRule(name = "Buy 3 for $1.3", quantity = 3, price = 1.3),
	PricingRule(name = "Buy 1 for $0.5", quantity = 1, price = 0.5)
	]

# rules for orange
orange.pricingRules = [
	PricingRule(name = "Buy 1 get 1 half", quantity = 2, price = 1.5),
	PricingRule(name = "Buy 1 for $1", quantity = 1, price = 1.0)
	]
	
# rules for pear
pear.pricingRules = [
	PricingRule(name = "Buy 1 get 1 free", quantity = 2, price = 0.5),
	PricingRule(name = "Buy 1 for $0.5", quantity = 1, price = 0.5)
	]
	
# rule for Strawberry
strawberry.pricingRules = [
	PricingRule(name = "Buy 1 pack for $5", quantity = 1, price = 5.0)
	]
	
# unsorted checked out items
# feel free to change the order, add, remove items
order = Order(checkedOutItems = [
					CheckedOutItem(product = apple),
					CheckedOutItem(product = orange),
					CheckedOutItem(product = apple),
					CheckedOutItem(product = pear),
					CheckedOutItem(product = orange),
					CheckedOutItem(product = strawberry),
					CheckedOutItem(product = apple),
					CheckedOutItem(product = apple),
					CheckedOutItem(product = pear),
					CheckedOutItem(product = orange)
					]
			)
			
#print rules for Apple	
sys.stdout.write(("-" * 40) + "\n\tPricing rules for Apple\n" + ("-" * 40) + "\n")
for rule in apple.pricingRules:
	sys.stdout.write(rule.name +"\n")

# print rules for Orange
sys.stdout.write(("-" * 40) + "\n\tPricing rules for Orange\n" + ("-" * 40) + "\n")
for rule in orange.pricingRules:
	sys.stdout.write(rule.name +"\n")
	
# print rules for Pear
sys.stdout.write(("-" * 40) + "\n\tPricing rules for Pear\n" + ("-" * 40) + "\n")
for rule in pear.pricingRules:
	sys.stdout.write(rule.name +"\n")
	
# print rules for Strawberry
sys.stdout.write(("-" * 40) + "\n\tPricing rules for Strawberry\n" + ("-" * 40) + "\n")
for rule in strawberry.pricingRules:
	sys.stdout.write(rule.name +"\n")

sys.stdout.write("\n" + ("-" * 40) + "\n\tItems in Cart\n" + ("-" * 40) + "\n")
for item in order.checkedOutItems:
	sys.stdout.write(item.product.name + " ")
			
PriceCalculator.calculatePrice(order)

sys.stdout.flush()