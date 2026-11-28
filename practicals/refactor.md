legacy function

```python
def get_daily_stop_sequence(seq, res: int = 7):
    result = {}
    for (i, j), (lat1, lat2), (lon1, lon2) in zip(
        more_itertools.pairwise(seq[f"h3_{res}"]),
        more_itertools.pairwise(seq["latitude_mean"]),
        more_itertools.pairwise(seq["longitude_mean"]),
    ):
        if i == j or pd.isna(i) or pd.isna(j):
            continue
        if i not in result:
            result[i] = {}
        if j not in result[i]:
            result[i][j] = 0
        result[i][j] += 1

    if len(result) == 0:
        return np.nan
    else:
        return result
```

- no documentation
- no tests
- missing type hints
    - seq, function
- unused loop variables
- ambiguous return values
- (multiple return statements)
- multiple execution branches
    - (relative) high cyclomatic complexity
- main issue was, that it uses a less performant library
- has an unnecessary dependency

## how to refactor it?

1. no tests, cannot be sure that the changed version would work as expected
2. add test
    - create a simple input data
    - check what the function does
        - basically like black-box testing / reverse engineering

```python
dummy_seq = pd.DataFrame(
    {
        "h3_7": [1, 2, 3, 2, 3],
        "latitude_mean": [47.42, 47.64, 47.23, 47.87, 47.25],
        "longitude_mean": [18.91, 19.12, 19.09, 19.31, 19.08],
    }
)
```

### call function

```
get_daily_stop_sequence(dummy_seq)
```

output (starting point): `{1: {2: 1}, 2: {3: 2}, 3: {2: 1}}` 

notice, that lat1, lat2, lon1, lon2 is not used: remove them


``` python
def get_daily_stop_sequence(seq, res: int = 7) -> dict | float:
    result = {}
    for i, j in more_itertools.pairwise(seq[f"h3_{res}"]):
        if i == j or pd.isna(i) or pd.isna(j):
            continue
        if i not in result:
            result[i] = {}
        if j not in result[i]:
            result[i][j] = 0
        result[i][j] += 1

    if len(result) == 0:
        return np.nan
    else:
        return result
```

output is still: `{1: {2: 1}, 2: {3: 2}, 3: {2: 1}}`


## writing new function

```python
def get_daily_stop_sequence_pl(seq, res: int) -> dict:
    return {}
```
>>> get_daily_stop_sequence_pl(dummy_seq, 7)
{}

## generate

Consider the following Python function which operation on a pandas dataframe.

```python
def get_daily_stop_sequence(seq: pd.DataFrame, res: int = 7) -> dict | float:
    result = {}
    for i, j in more_itertools.pairwise(seq[f"h3_{res}"]):
        if i == j or pd.isna(i) or pd.isna(j):
            continue
        if i not in result:
            result[i] = {}
        if j not in result[i]:
            result[i][j] = 0
        result[i][j] += 1

    if len(result) == 0:
        return np.nan
    else:
        return result
```

a sample input:

```
dummy_seq = pd.DataFrame(
    {
        "h3_7": [1, 2, 3, 2, 3],
        "latitude_mean": [47.42, 47.64, 47.23, 47.87, 47.25],
        "longitude_mean": [18.91, 19.12, 19.09, 19.31, 19.08],
    }
)
get_daily_stop_sequence(dummy_seq)
```
output: `{1: {2: 1}, 2: {3: 2}, 3: {2: 1}}`

Rewrite this function using polars using windowing operators to produce the same result for the dummy_seq input.




https://chatgpt.com/share/6a0c172c-6e70-83eb-b811-13f0a86ce399
