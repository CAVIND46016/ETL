import random
import pandas as pd


# Down-casting float64 to float32
# Random floating point numbers
random_array = [random.uniform(-99, 99) for _ in range(100000)]

A = pd.DataFrame({"number": random_array})
print(A.info(memory_usage="deep"))
print(A.head())

B = A.copy()
B["number"] = pd.to_numeric(B["number"], downcast="float")
print(B.info(memory_usage="deep"))
print(B.head())

mse = ((A.values - B.values) ** 2).mean(axis=None)
print("MSE: {}\n".format(mse))

# Down-casting int64 to uint8
# Random floating point numbers
random_int = [random.randint(0, 99) for _ in range(100000)]

A = pd.DataFrame({"number": random_int})
print(A.info(memory_usage="deep"))
print(A.head())

B = A.copy()
B["number"] = pd.to_numeric(B["number"], downcast="integer")
print(B.info(memory_usage="deep"))
print(B.head())

mse = ((A.values - B.values) ** 2).mean(axis=None)
print("MSE: {}".format(mse))

"""
OUTPUT:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null float64
dtypes: float64(1)
memory usage: 781.3 KB
None
      number
0 -85.280828
1 -10.617595
2  96.511648
3 -20.708218
4 -57.507265
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null float32
dtypes: float32(1)
memory usage: 390.7 KB
None
      number
0 -85.280830
1 -10.617595
2  96.511650
3 -20.708218
4 -57.507263
MSE: 2.1574547254253548e-12

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null int64
dtypes: int64(1)
memory usage: 781.3 KB
None
   number
0      95
1      53
2      22
3      25
4       7
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 1 columns):
number    100000 non-null int8
dtypes: int8(1)
memory usage: 97.7 KB
None
   number
0      95
1      53
2      22
3      25
4       7

Process finished with exit code 0
"""
