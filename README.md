# AI-Based-Shopping-Assistant

This project was submitted in codeutsava3.0 at NIT Raipur 2019.
The main purpose of this project is to create a recommendation system for online shopping. We used unsupervised machine learning strategy (clustering) to cluster the items from the consumer's purchase history which shows same characterstics. When a consumer triggers a search, the model finds the most suitable cluster for searched item and shows all the items of that cluster to the consumer after some filtering under "things you may like" section. 
Also it shows results for the different types of serched item too (this is not a part of the recommendation system. This is just a added feature).

## Requirements
This project is build on python version 3.6
Libraries used:      
[Numpy](http://www.numpy.org/)      
[Pandas](https://pandas.pydata.org/)       
[openCV](https://pypi.org/project/opencv-python/)       
[sklearn](https://scikit-learn.org/stable/)       
[matplotlib](https://matplotlib.org/)       

## Dataset
We created our own [dataset](person.csv). Currently we used the model for 100 items. 
To increase the dataset open the [getDataset.py](getDataset.py) file and add the items in the "item" list. Then delete the person.csv, dataset.csv files and run

    python3 getDataset.py
    

## Usage
Download the Complete Project

	git clone https://github.com/riti1302/AI-Based-Shopping-Assistant
  
Run the main file

    python3 main.py
    
To increse the database, add more files to [Database](data/)


## Outputs








