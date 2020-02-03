import numpy as np
N=8

days = ["mon", "tues", "wed","thurs","fri","sat","sun","sun"]
days = list(set(days))

days_to_idx = {day:i for i,day in enumerate(days)}
idx_to_days = {i:day for i,day in enumerate(days)}
i = days_to_idx["mon"]
day = idx_to_days[i]

rand_days = [idx_to_days[np.random.randint(0,len(days))] for i in range(10)]





N, D_in1,D_in2, H, D_out = 4, 600,300, 100, 1

# Create random input and output data
x1 = [np.random.randn() for i in range(N)]
x2 = [np.random.randn() for i in range(N)]
y = [np.random.randn() for i in range(N)]

# create some categorical data, days
days = ["Sun","mon","tues","wed","thurs","fri","sat"]
days = list(set(days) )   #how many in category?
num_days = len(days)

cat_days =  [ days[np.random.randint(0,7)] for j in range(0,N)]

#create lookup table
days_to_idx = {day:i for i, day in enumerate(days)}

#convert cat_days to associated indices in days_to_idx
cat_days_index = [days_to_idx[day] for day in cat_days]
pass