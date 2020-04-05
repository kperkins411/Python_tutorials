import pandas as pd

s = pd.Series(list('abca'))

j = pd.get_dummies(s)

print (j)

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df2 = pd.DataFrame(raw_data, columns = raw_data.keys())
print (df)

idxs= df['last_name'] == '.'
df.loc[idxs,'last_name']="UNKNOWN"



url="https://tinyurl.com/titanic-csv"
df3=pd.read_csv(url)
df4=df3.groupby('Sex').apply(lambda x:x.count())
pass



