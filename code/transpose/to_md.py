import pandas as pd

df = pd.read_excel("input.xlsx")

print(df.to_markdown(index=False))

print(df.transpose().reset_index().to_markdown(index=False))
