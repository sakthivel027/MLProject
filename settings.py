settings.py
       city  signup  visitor
city                                 
jaipur        jaipur       2       23
ajmer          ajmer       5      445
bharatpur  bharatpur       6      566
delhi          delhi       7       22
mumbai        mumbai       9      555
           signup  visitor
city                      
jaipur          2       23
ajmer           5      445
bharatpur       6      566
delhi           7       22
mumbai          9      555
df.drop('visitor',axis='columns',inplace=True)
df.drop('delhi',axis='rows',inplace=True)
print(df)
           signup
city             
jaipur          2
ajmer           5
bharatpur       6
mumbai          9
df=pd.read_csv('data.csv',index_col='city')
#index can be reated as index
df.floordiv(12)  #convert dozen units
import numpy as np
np.floor_divide(df,12) #convert dozen units
df.apply(lambda n:n//12)  #convert dozen units
df.index=df.index.str.upper()
df.index=df.index.map(str.upper)
multilevel indexing
data={'city': ['jaipur', 'ajmer', 'bharatpur', 'delhi', 'mumbai'],'name':['harshit','keshav','samyak','rahul','ankur'], 'signup': [9, 5, 3, 2, 9], 'visitor': [23, 445, 566, 22, 555]}
stock=pd.DataFrame(data)
stock=stock.set_index(['name','signup'])
print(stock)
                     city  visitor
name    signup                    
harshit 9          jaipur       23
keshav  5           ajmer      445
samyak  3       bharatpur      566
rahul   2           delhi       22
ankur   9          mumbai      555
stock=stock.sort_index()
print(stock)
                     city  visitor
name    signup                    
ankur   9          mumbai      555
harshit 9          jaipur       23
keshav  5           ajmer      445
rahul   2           delhi       22
samyak  3       bharatpur      566
reshaping data using pivot
data={'id': [1,2,3,4],'treatment':['A','B','B','A'], 'gender': ['M', 'F', 'M', 'F'], 'response': [23, 45, 22, 34]}
trials=pd.DataFrame(data)
trials.pivot(index='treatment',columns='gender',values='response')
gender	F	M
treatment		
A	34	23
B	45	22
trials.pivot(index='treatment',columns='gender')
id	response
gender	F	M	F	M
treatment				
A	4	1	34	23
B	2	3	45	22
Stacking & unstacking DataFrames
trials=trials.set_index(['treatment','gender'])
print(trials)
                  id  response
treatment gender              
A         M        1        23
B         F        2        45
          M        3        22
A         F        4        34
trials.unstack(level='gender')
id	response
gender	F	M	F	M
treatment				
A	4	1	34	23
B	2	3	45	22
trials_by_gender=trials.unstack(level=1)
print(trials_by_gender)
          id    response    
gender     F  M        F   M
treatment                   
A          4  1       34  23
B          2  3       45  22
stacked=trials_by_gender.stack(level='gender')
print(stacked)
                  id  response
treatment gender              
A         F        4        34
          M        1        23
B         F        2        45
          M        3        22
swapped=stacked.swaplevel(0,1)
print(swapped) #index is not sorted
                  id  response
gender treatment              
F      A           4        34
M      A           1        23
F      B           2        45
M      B           3        22
sorted_trial=swapped.sort_index()
print(sorted_trial)
                  id  response
gender treatment              
F      A           4        34
       B           2        45
M      A           1        23
       B           3        22
group by
sales = pd.DataFrame({'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],'bread': [139, 237, 326, 456],'butter': [20, 45, 70, 98]})
print(sales)
  weekday    city  bread  butter
0     Sun  Austin    139      20
1     Sun  Dallas    237      45
2     Mon  Austin    326      70
3     Mon  Dallas    456      98
sales.loc[sales['weekday']=='Sun'].count()
weekday    2
city       2
bread      2
butter     2
dtype: int64
sales.groupby('weekday').count()
city	bread	butter
weekday			
Mon	2	2	2
Sun	2	2	2
sales.groupby('weekday')['bread'].sum()
weekday
Mon    782
Sun    376
Name: bread, dtype: int64
sales.groupby(['city','weekday']).mean()
bread	butter
city	weekday		
Austin	Mon	326	70
Sun	139	20
Dallas	Mon	456	98
Sun	237	45
sales.groupby('weekday')['bread','butter'].agg(['max','min'])
bread	butter
max	min	max	min
weekday				
Mon	456	326	98	70
Sun	237	139	45	20
sales.groupby('weekday')['bread'].agg('sum')
weekday
Mon    782
Sun    376
Name: bread, dtype: int64
sales.groupby('weekday')['bread'].transform('sum')
0    376
1    376
2    782
3    782
Name: bread, dtype: int64
Appending & concatenating
#result of append and concat is equal
import pandas as pd
northeast = pd.Series(['CT', 'ME', 'MA', 'NH', 'RI', 'VT','NJ', 'NY', 'PA'])
south = pd.Series(['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA','DC', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX'])
midwest = pd.Series(['IL', 'IN', 'MN', 'MO', 'NE', 'ND','SD', 'IA', 'KS', 'MI', 'OH', 'WI'])
west = pd.Series(['AZ', 'CO', 'ID', 'MT', 'NV', 'NM','UT', 'WY', 'AK', 'CA', 'HI', 'OR','WA'])

east=northeast.append(south)
print(east)
0     CT
1     ME
2     MA
3     NH
4     RI
5     VT
6     NJ
7     NY
8     PA
0     DE
1     FL
2     GA
3     MD
4     NC
5     SC
6     VA
7     DC
8     WV
9     AL
10    KY
11    MS
12    TN
13    AR
14    LA
15    OK
16    TX
dtype: object
print(east.index)
print(east[3])
Int64Index([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  0,  1,  2,  3,  4,  5,  6,  7,
             8,  9, 10, 11, 12, 13, 14, 15, 16],
           dtype='int64')
3    NH
3    MD
dtype: object
new_east=east.reset_index(drop=True)
print(new_east)




