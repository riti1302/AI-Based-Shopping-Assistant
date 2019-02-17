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
	#print(item)

	df = pd.DataFrame(columns=['Item', 'Item_names'])
	df['Item'] = item
	df['Item_names'] = item_names
	df.to_csv('dataset.csv', mode ='w', index=False)

	print(df.head) 
