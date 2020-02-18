
import pandas as pd
import time

size = 10**6
print("Creating dataframe...")
df = pd.DataFrame(data={'val': range(1, size+1)})
solution = size * (size+1) / 2


s = time.time()
c = 0
for _, row in df.iterrows():
    c += row['val']

t = time.time()
assert c == solution
print(f"sum(val): {c} | iterrows took {t-s} secs")
############################################################

s = time.time()
c = 0
for row in df.itertuples():
    c += row.val

t = time.time()
assert c == solution
print(f"sum(val): {c} | itertuples 1 took {t-s} secs")

############################################################
s = time.time()
c = 0
for row in df.itertuples(index=False):
    c += row.val

t = time.time()
assert c == solution
print(f"sum(val): {c} | itertuples 2 took {t-s} secs")

############################################################
s = time.time()
c = 0
for row in df.itertuples(name=None, index=False):
    c += row[0]

t = time.time()
assert c == solution
print(f"sum(val): {c} | itertuples 3 took {t-s} secs")


