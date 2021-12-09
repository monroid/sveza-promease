mport pandas as pd

a = pd.read_csv("list_1_1.csv", low_memory=False)
b = pd.read_csv("list_2_2.csv", low_memory=False)
c = pd.read_csv("list_3_px.csv", low_memory=False)
d = pd.read_csv("list_4_px.csv", low_memory=False)
e = pd.read_csv("list_5_px.csv", low_memory=False)
f = pd.read_csv("list_6_px.csv", low_memory=False)
g = pd.read_csv("list_7_px.csv", low_memory=False)
i = pd.read_csv("list_8_px.csv", low_memory=False)

res = pd.concat([a, b, c, d, e, f, g, i], ignore_index=True)
s = res.reset_index(drop=True)
s["Sorting"] = s.index
s.sort_values(by='CaseID', inplace=True)
ss = s.groupby('CaseID').apply(lambda x : x.ffill().bfill())
## res.sort_values(by='CaseID', inplace=True)
## s = res.fillna(method='ffill')
ss.to_csv("output.csv", index=False, encoding='utf-8-sig')
