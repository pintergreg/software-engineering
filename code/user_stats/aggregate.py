import sqlite3
import pandas as pd

con = sqlite3.connect("data.db")

query = f"SELECT * FROM activity WHERE user_id = {42}"
data = pd.read_sql(query, con)
print(data)
