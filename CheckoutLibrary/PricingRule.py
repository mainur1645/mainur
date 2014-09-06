import sys

class PricingRule:
	def __init__(self, name, quantity, price):
		self.name = name
		self.quantity = quantity
		self.price = price
		
	def calculate(self, totalItems):
		totalPrice = 0
		remainingQuantity = totalItems
		ruleAppliedOn = 0 # items
		units = totalItems / self.quantity
		if(units > 0):
			totalPrice = self.price * (int)(totalItems / self.quantity)
			remainingQuantity = totalItems % self.quantity
			ruleAppliedOn = totalItems - remainingQuantity
		return totalPrice, remainingQuantity, ruleAppliedOn