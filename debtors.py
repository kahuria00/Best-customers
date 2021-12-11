import os
import pandas as pd

def good_debtors():
	current_directory = os.path.realpath(
	os.path.join(os.getcwd(), os.path.dirname(__file__))) #getting working directory
	sheetname_input = str(input("Enter csv name: "))
	no_of_customers = int(input("Enter number of paying customers you need: "))
	
	csv_file_path = f"{current_directory}/{sheetname_input}"
	customers_df = pd.read_csv(csv_file_path)
	customers_df.columns = customers_df.columns.str.replace(' ', '')
	customers_df = customers_df.sort_values(by=['CustomerID','TransactionDate'],ascending=True)
	customers_df['TransactionDate']= pd.to_datetime(customers_df['TransactionDate']) #convert column to datetime
	customers_df = customers_df.groupby('CustomerID')['TransactionDate'].apply(lambda x: sum(abs((x.shift(-1) - x)) == pd.to_timedelta(1, unit='D')))#grouping according to consecutive days 
	customers_df = customers_df.nlargest(no_of_customers) # return no ofID with with max transaction
	customer_ids = list(customers_df.to_dict().keys()) #convert dict to list then return keys(IDs)
	print(customer_ids)



good_debtors()	





