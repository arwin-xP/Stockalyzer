import pandas as pd
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def read_fil(FILE_NAME):
    q=pd.read_csv(FILE_NAME)
    k=0
    df=pd.DataFrame(q)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Mnth_Yr'] = df['Date'].apply(lambda x: x.strftime('%m-%Y'))
    del df['Date']
    n=len(df.groupby('Mnth_Yr'))
    y=[[]]*n
    for group,t in df.groupby('Mnth_Yr'):
        s=np.average(t['Adj Close'],weights=t['Volume'])
        y[k]=[s,group]
        k+=1    
    return y

def displ(L_L,no):
    L_L=sorted(L_L,key=itemgetter(0))
    x=[i[0] for i in L_L]
    y=[i[1] for i in L_L]
    plt.plot_date(y,x)
    plt.show()
    print 'The '+str(no)+' worst months and the corresponding shares for Google are:'
    for i in L_L[:no]:
        print i[1],i[0]
    print 'The '+str(no)+' best months and the corresponding shares for Google are:'
    for i in L_L[:-no-1:-1]:
        print i[1],i[0]

FILE_NAME="table.csv"
y=read_fil(FILE_NAME)
x=int(raw_input("Enter no of best/worst months for stocks: "))
displ(y,x)
