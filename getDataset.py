import csv
from random import randrange
import random
import pandas as pd
import numpy as np
from collections import Counter

def getData():
	item = []
	search_history = ['shirt', 'watch', 'wallet', 'shoes', 'belt', 'rice', 'sugar', 'skirt', 'sandal', 'heals', 'handbag', 'bagpack', 'pillow', 'teddy', 'suitcase', 'mobiles', 'laptop', 'fridge', 'desk', 'soda', 'hat', 'bangles', 'earrings', 'necklace', 'ring', 'shampoo', 'dates', 'cashew', 'juice', 'lays', 'maggi', 'keyboard']
	item_names = []
	print(len(item_names))
	for i in range(50):
		number = randrange(1,32)
		item.append(number)
		item_names.append(search_history[number])
	print(item)

	df = pd.DataFrame(columns=['Item', 'Item_names'])
	df['Item'] = item
	df['Item_names'] = item_names
	df.to_csv('dataset.csv', mode ='w', index=False)

	print(df.head) 

def calculate_frequency():
	df = pd.read_csv('dataset.csv')
	new_frequency= []
	new_names= []
	#print(df)
	items = df['Item'].tolist()
	item_names = df['Item_names'].tolist()
	#print(items)
	frequency = Counter(items)
	#print(frequency)

	new_items = set(items)
	new_items = (list(new_items))
	random.shuffle(new_items)
	#print(new_items)
	
	for item in new_items:
		new_frequency.append(frequency[item])
		new_names.append(item_names[item])
		
	#print(new_frequency)

	df = pd.DataFrame(columns=['Item', 'Item_names'])
	df['Item'] = new_items
	df['Item name'] = new_names
	df['Frequency'] = new_frequency

	df.to_csv('person.csv', mode ='w', index=False)

getData()
calculate_frequency()
