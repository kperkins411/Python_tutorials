import os


def mkdir(pth):
    if (not os.path.exists(pth)):
        os.mkdir(pth)


PATH = "HousePrices"
PATH_TRN = os.path.join(PATH, "trn")
PATH_VAL = os.path.join(PATH, "val")
PATH_TST = os.path.join(PATH, "tst")
mkdir(PATH)
mkdir(PATH_TRN)
mkdir(PATH_VAL)
mkdir(PATH_TST)

def getdata(lnk, pth, file):
    '''
    lnk html link to pull data from
    pth dir where it goes
    file name of the file
    '''
    filename = os.path.join(pth, file)
    if (not os.path.exists(filename)):
        import requests
        download = requests.get(lnk)

        import csv
        with open(filename, 'w') as temp_file:
            cnt = download.content
            temp_file.writelines(cnt)

import requests
url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('google.ico', 'wb').write(r.content)

# go to Kaggle house prices competition for this data
getdata("https://www.kaggle.com/c/house-prices-advanced-regression-techniques/download/train.csv", PATH_TRN,
        "train.csv")
# getdata("https://www.kaggle.com/c/house-prices-advanced-regression-techniques/download/test.csv",PATH_TST,"tst.csv")