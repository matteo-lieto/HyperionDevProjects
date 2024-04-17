#creating menu list

menu = ["eggs", "steak", "sausages", "steak"]

#creating stock dictionary with values for each item on the menu

stock_dictionary = {
    "eggs" : 100,
    "steak" : 150,
    "lobster" :50,
    "sausages" : 200
    }

#creating dictionary with retail prices
price_dictionary = {"eggs" : 5, 
                    "lobster" : 30, 
                    "sausages" : 8, 
                    "steak" : 20
                    }

# Calculate total cost
# Using dictionary comprehension + keys()
total_stock = {key: stock_dictionary[key] * price_dictionary.get(key)
					for key in stock_dictionary.keys()}

# printing result 
print("The full value of the stock is : " + str(total_stock))