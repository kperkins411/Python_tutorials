#gotta get some files from diff location
import sys
sys.path.insert(0, '/home/keith/fastAI2/fastai/courses/dl1')

from fastai.structured import *
from fastai.column_data import *
import pandas as pd
import numpy as np

#where stuff stored
PATH = "./SS_Data"
cat_vars = ["Year","Month","Dayofyear","Is_quarter_end","Is_quarter_start","Is_year_end","Is_year_start"]

#reload data
df_trn_val = pd.read_feather(f'{PATH}/df_trn_val')
df_test = pd.read_feather(f'{PATH}/df_test')

yl_trn_val  = np.load(f'{PATH}/yl_trn_val.npy')
yl_test  = np.load(f'{PATH}/yl_test.npy')

# generated from KP_Sunspot.ipynb
val_idx = list(range(1692, 2115))

def inv_y(a): return np.exp(a)
def exp_rmspe(y_pred, targ):
    targ = inv_y(targ)
    pct_var = (targ - inv_y(y_pred))/targ
    return math.sqrt((pct_var**2).mean())
def mse(y_pred, targ):
    targ = inv_y(targ)
    y_pred = inv_y(y_pred)
    return math.sqrt(((y_pred-targ)**2).mean())
max_log_y = np.max(yl_trn_val)
y_range = (0, max_log_y*1.2)

#create a model
md = ColumnarModelData.from_data_frame(PATH, val_idx, df_trn_val, yl_trn_val.astype(np.float32), cat_flds=cat_vars, bs=16, test_df=df_test)

#get categorical sizes, make sure you convert columns in cat_vars to type category before you run this
cat_sz = [(c, len(df_trn_val[c].cat.categories)+1) for c in cat_vars]
cat_sz[0] = ('Year',236)
emb_szs = [(c, min(50, (c+1)//2)) for _,c in cat_sz]

#get a model
m = md.get_learner(emb_szs, len(df_trn_val.columns)-len(cat_vars),0.04, 1, [1000,500], [0.001,0.01], y_range=y_range)

#find a good learning rate
# m.lr_find()
# m.sched.plot(100)
lr = 20e-5

#fit the model
# m.fit(lr, 2, metrics=[exp_rmspe,mse], cycle_len=1, cycle_mult=2)
# m.fit(lr, n_cycle = 3, metrics=[exp_rmspe,mse], cycle_len=2, cycle_mult=2)

# or load model properties
m.load(f'val1')

#create ColumnarDataSet from DataFrame (df)
cds = ColumnarDataset.from_data_frame(df_test,cat_flds=cat_vars,y=yl_test)

# create DataLoader from ColumnarDataSet
dl = DataLoader(cds)

# make predictions for DataLoader
predictions = m.predict_dl(dl)

pass