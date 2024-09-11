import utils.imports as imp

df = imp.Diabetes()
df.read_data(path="data/diabetes.tab.txt")

print(df.rows)
print(df.columns)
print("ok")