import pandas as pd
import random

# Downcasting float64 to float32
# Random floating point numbers
random_array = [random.uniform(-99, 99) for _ in range(100000)]

A = pd.DataFrame({'number': random_array})
print(A.info(memory_usage='deep'))
print(A.head())

B = A.copy()
B['number'] = pd.to_numeric(B['number'], downcast='float')
print(B.info(memory_usage='deep'))
print(B.head())

mse = ((A.values - B.values)**2).mean(axis=None)
print("MSE: {}\n".format(mse))

# Downcasting int64 to uint8
# Random floating point numbers
random_int = [random.randint(0, 99) for _ in range(100000)]

A = pd.DataFrame({'number': random_int})
print(A.info(memory_usage='deep'))
print(A.head())

B = A.copy()
B['number'] = pd.to_numeric(B['number'], downcast='integer')
print(B.info(memory_usage='deep'))
print(B.head())

mse = ((A.values - B.values)**2).mean(axis=None)
print("MSE: {}".format(mse))
