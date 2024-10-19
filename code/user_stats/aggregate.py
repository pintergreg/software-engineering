import sqlite3
import pandas as pd

con = sqlite3.connect("data.db")

query = f"SELECT * FROM activity WHERE user_id = {42}"


query = """
SELECT
    CAST(strftime('%W', timestamp) AS INTEGER) AS week_of_year,
    CAST(strftime('%u', timestamp) AS INTEGER) AS day_of_week,
    count(*) AS count
FROM activity
WHERE
    user_id = 42 AND
    week_of_year > 35 AND
    week_of_year < 40
GROUP BY
    week_of_year,
    day_of_week
;
"""
data = pd.read_sql(query, con)

records = []
for woy in range(37, 40):
    for dow in range(1, 8):
        records.append([woy, dow, 0])
empty = pd.DataFrame.from_records(
    records, columns=["week_of_year", "day_of_week", "count"]
)

data = (
    pd.concat([data, empty])
    .drop_duplicates(subset=["week_of_year", "day_of_week"], keep="first")
    .sort_values(["week_of_year", "day_of_week"])
    .reset_index(drop=True)
)
print(data)
