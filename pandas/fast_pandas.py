# https://towardsdatascience.com/one-word-of-code-to-stop-using-pandas-so-slowly-793e0a81343c

import pandas as pd
import swifter
import time
import random

rev, cost = [], []
for _ in range(900000):
    rev.append(random.uniform(0,9999))
    cost.append(random.uniform(0,9999))

df = pd.DataFrame({'revenue': rev, 'cost': cost})
s = time.time()
df['profit'] = df.apply(lambda x: x['revenue'] - x['cost'], axis=1)
t = time.time()
print(f"Sum: {df['profit'].sum()} | Min: {df['profit'].min()} | Max: {df['profit'].max()}")
print(f"Regular: {t-s} seconds\n")

del df, s, t

df = pd.DataFrame({'revenue': rev, 'cost': cost})
s = time.time()
df['profit'] = df['revenue'] - df['cost']
t = time.time()
print(f"Sum: {df['profit'].sum()} | Min: {df['profit'].min()} | Max: {df['profit'].max()}")
print(f"Regular (Opt): {t-s} seconds\n")

del df, s, t

df = pd.DataFrame({'revenue': rev, 'cost': cost})
s = time.time()
df['profit'] = df.swifter.apply(lambda x: x['revenue'] - x['cost'], axis=1)
t = time.time()
print(f"Sum: {df['profit'].sum()} | Min: {df['profit'].min()} | Max: {df['profit'].max()}")
print(f"Swifter: {t-s} seconds")


"""
OUTPUT:
Sum: 642597.9726776625 | Min: -9997.660827480351 | Max: 9996.42286635719
Regular: 16.056950330734253 seconds

Sum: 642597.9726776625 | Min: -9997.660827480351 | Max: 9996.42286635719
Regular (Opt): 0.005999326705932617 seconds

Sum: 642597.9726776625 | Min: -9997.660827480351 | Max: 9996.42286635719
Swifter: 0.008031606674194336 seconds
"""
