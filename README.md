# ETL
Some utility scripts, tweaks with regards to ETL

###### numeric_downcast.py
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null float64
dtypes: float64(1)
memory usage: 781.3 KB
None
      number
0 -31.094958
1   9.594640
2 -57.508365
3 -57.439762
4 -24.311310
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null float32
dtypes: float32(1)
memory usage: 390.7 KB
None
      number
0 -31.094959
1   9.594640
2 -57.508366
3 -57.439762
4 -24.311310
MSE: 2.1497315989728574e-12

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null int64
dtypes: int64(1)
memory usage: 781.3 KB
None
   number
0      27
1      47
2      16
3      60
4      47
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null int8
dtypes: int8(1)
memory usage: 97.7 KB
None
   number
0      27
1      47
2      16
3      60
4      47
MSE: 0.0
```
###### pydot_hierarchy_diagram.py
![alt text](https://github.com/CAVIND46016/ETL/blob/master/data/pydot.png)
