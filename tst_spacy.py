# import spacy
#
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
#
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)



# import spacy
#
# nlp = spacy.load('en_core_web_md')  # make sure to use larger model!
# tokens = nlp(u'dog cat banana')
#
# #how similar to each other are the previous words
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))
import pandas as pd
import numpy as np

#create a dataframe
df3 = pd.DataFrame(np.arange(20).reshape(10,2),columns=list('AB'))


l1 =[2,2,3]
# l1 =  [float(i) for i in l1]
l2 = sum(l1)/len(l1)

df3 = pd.DataFrame(np.arange(20).reshape(10,2),columns=list('AB'))

for val in df3['B']:
    val = df3[]

df4 = df3.rolling(window=3,min_periods=3)
df4 = df3.rolling(window=3,min_periods=3).mean()
df5 = df3.rolling(window=3,min_periods=3).sum()
df6 = df3.rolling(window=3,min_periods=3).min()

df1 = pd.DataFrame(np.arange(4),columns=list('ABCD'))

df2= pd.DataFrame((np.arange(16)*10).reshape(4,4),columns=list('ABCD'))

d1=0
for df in (df1,df2):
    d1=df["A"].apply(lambda x: x if x >0 else -22)
    # df["A"].apply(lambda x: x if x > 0 else -22)
x=5.0
y=2.0
z=x//y
z1 = x/y
table_names = ['train', 'store', 'store_states', 'state_names',
               'googletrend', 'weather', 'test']
dict1={}
for i, table in enumerate(table_names):
    dict1[table]=i

import spacy
tmp = '   xxx0000000thisxxx is       string111 example....wow!!!0000000'.strip('x')

nlp = spacy.load('en_core_web_sm')
tokens = nlp(tmp)
tmp1 = ' '.join( [tok.string.strip('10x ')  for tok in tokens])
print(tmp1)
# for tok in tokens:
#     # tmp1 = tok.text
#     print()
# tmp = 'www.example.com'.strip('cmowz.')
# print(tmp)
# # tmp = '   xxx0000000thisxxx is       string111 example....wow!!!0000000'.strip('x')
# # print(tmp)
#
# str = '  xxx0000000thisxxx is       string111 example....wow!!!0000000'.strip()
# print (str)

# import spacy
#
# nlp = spacy.load('en_core_web_md')
# tokens = nlp(u'dog cat banana afskfsd')
#
# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)