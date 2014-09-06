import sys

class PriceCalculator:

	def calculatePrice(order):
		productFrequencies = {}
		productMap = {}
		for item in order.checkedOutItems:
			# map product objects to names
			productMap[item.product.name] = item.product
			# count number of occurrences for each product
			productFrequencies[item.product.name] = productFrequencies.setdefault(item.product.name, 0) + 1
		sys.stdout.write("\n" + ("-" * 40) + "\n\n\tItemized Receipt\n" 
						+ ("-" * 40) + "\n")
		totalPrice = 0;
		totalItems = 0;
		# calculate price for individual product
		for productName, productItems in productFrequencies.items():
			for mapKey in productMap:
				if(mapKey == productName):
					productObject = productMap[productName]
					remainingItems = productItems
					totalItems = totalItems + productItems
					sys.stdout.write("Item: " + productObject.name 
					+ ("" * 10) +" Total: " + str(productItems))
					productPrice = 0;
					for rule in productObject.pricingRules:
						price, remainingItems, ruleAppliedOn = rule.calculate(remainingItems)
						if(price > 0):
							sys.stdout.write("\n\t" + str(ruleAppliedOn) 
							+ " using " + rule.name + " = " + str(price)) 
							productPrice = productPrice + price
						if(remainingItems == 0):
							break
					sys.stdout.write("\n\tTotal: " + str(productPrice) + "\n" + ("-"* 40) + "\n")
					totalPrice = totalPrice + productPrice
						
		sys.stdout.write(("-"*40) + "\nTotal Items: " + str(totalItems)
						+ "\t\tTotal Price: " + str(totalPrice) + "\n")
		