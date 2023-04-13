from tqdm import tqdm

b = 10000000
# a = tqdm(total=b)
# a = tqdm(total=b, unit="B") # or tqdm(total=b, unit="B", unit_scale=False)
a = tqdm(total=b, unit="B", unit_scale=True)
# a = tqdm(total=b, unit="B", unit_scale=True, unit_divisor=2)

for i in range(b):
    a.update(1)
    # print(i)

a.close()
