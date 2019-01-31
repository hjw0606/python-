import pandas as pd
to_read=pd.read_csv('to_read.csv')
to_read_counts=to_read['book_id'].value_counts().sort_values(ascending=False)
hottest_50_book_id=to_read_counts[:50].index
hottest_50_book_counts=to_read_counts[:50].values
hottest_50_book=pd.dataframe({
	'book_id':hottest_50_book_id,
	'to_read_counts':hottest_50_book_counts
	})
print(hottest_50_book)

