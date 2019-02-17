import pandas as pd
import numpy as np
from random import randrange
from collections import Counter



def getRecency(Time, item):
	sum = 0
	k = 0
	for i in range(item):
		j = i + 1
		for j in range(item):
			if i == j:
				dif = item[i]-item[j]
				sum += dif
				k = 0
	average = sum/k
	return average


def getData():
	history_size = 1000
	item = []
	search_history = ['shirt', 'watch', 'wallet', 'shoes', 'belt', 'rice', 'sugar', 'skirt', 'sandal', 'heals', 'handbag', 'bagpack', 'pillow', 'teddy', 'suitcase', 'mobiles', 'laptop', 'fridge', 'desk', 'soda', 'hat', 'bangles', 'earrings', 'necklace', 'ring', 'shampoo', 'dates', 'cashew', 'juice', 'lays', 'maggi', 'keyboard', 'paper', 'pen', 'pencil', 'radio', 'rocket fuel', 'bulbs', 'ink', 'pajamas', 'shower', 'letters', 'books', 'bottles', 'juice', 'cars', 'bread', 'chain', 'bullets', 'mutton', 'shampoo', 'cakes', 'cards', 'pearls' , 'rope','bacon','tomatoes','sugar', 'eggs','onions','yeast','vegetables','baking powder','cheese', 'milk', 'handbags', 'boots', 'sweaters', 'dress', 'jacket'
]
	item_names = []
	Time = []
	for i in range(history_size):
		number = randrange(1,70)
		item.append(number)
		item_names.append(search_history[number])
		time = randrange(1550350815, 1550370815, 100)
		Time.append(time)
	#print(item)

	df = pd.DataFrame(columns=['Item', 'Item_names', 'Time'])
	df['Item'] = item
	df['Item_names'] = item_names
	df['Time'] = Time
	df.to_csv('dataset.csv', mode ='w', index=False)


	print(df.head) 

def calculate_frequency():
	df = pd.read_csv('dataset.csv')
	new_frequency= []
	new_names= []
	new_items= []

	items = df['Item'].tolist()
	item_names = df['Item_names'].tolist()

	item_list = dict(zip(items, item_names))
	frequency = Counter(items)

	for item in item_list:
		new_items.append(item)
		new_names.append(item_list[item])
		new_frequency.append(frequency[item])
		
	recency = calculate_recency(item_list,items)
	df = pd.DataFrame(columns=['Item', 'Item_names', 'Frequency'])
	df['Item'] = new_items
	df['Item_names'] = new_names
	df['Frequency'] = new_frequency
	df['Recency'] = recency
	df.to_csv('person.csv', mode ='w', index=False)

def calculate_recency(item_list,items):
	df = pd.read_csv('dataset.csv')
	Time = df['Time'].tolist()
	recency = []
	l = 1	
	for i in item_list:
		t = Time[i]
		l += 1
		j = l+1 
		m = 0
		k = 1
		Sum = 0
		for j in Time:
			if i == items[m]:
				dif = abs(j-t)
				Sum += dif
				k +=1
			m += 1
		average = Sum/k	
		recency.append(average)
	return recency

getData()
calculate_frequency()
