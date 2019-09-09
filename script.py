import pandas as p
import matplotlib.pyplot as pyp

# load the data
loan_data = p.read_csv('loan_data.csv',header=0)
ownership_data = p.read_csv('home_ownership_data.csv')

# join data together
joined = loan_data.join(ownership_data.set_index('member_id'),on='member_id')

# group by home ownership
grouped = joined.groupby('home_ownership')['loan_amnt'].mean()

print(grouped.to_string())

grouped.plot.bar()

pyp.show()
