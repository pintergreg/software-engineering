---
title: incomplete
author: Gergő Pintér, PhD
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
slideNumber: "true"
showSlideNumber: "print"
revealjs-url: "../assets/reveal.js-6.0.2/"
link-citations: true
---

# types

- [types vs. tests](https://www.destroyallsoftware.com/talks/ideology)
    - video ~21 min
- [I don't need types](https://dmerej.info/blog/post/trying-mypy/)
    - blogpost about typing systems


# Rob Pike's 5 rules of programming

1. You can't tell where a program is going to spend its time. Bottlenecks occur in surprising places, so don't try to second guess and put in a speed hack until you've proven that's where the bottleneck is.
2. Measure. Don't tune for speed until you've measured, and even then don't unless one part of the code overwhelms the rest.

Pike's rules 1 and 2 restate Donald Knuth's famous statement ["Premature optimization is the root of all evil."]{.background-color-lightblue}

::: {.mt-2}
> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%.
>
> -- Donald Knuth, 1974 [@knuth1974structured]

:::


## Rob Pike's 5 rules of programming

3. Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants. Until you know that n is frequently going to be big, don't get fancy. (Even if n does get big, use Rule 2 first.)
4. Fancy algorithms are buggier than simple ones, and they're much harder to implement. Use simple algorithms as well as simple data structures.

Ken Thompson rephrased Pike's rules 3 and 4 as "When in doubt, use brute force.".

Rules 3 and 4 are instances of the design philosophy [KISS]{.tooltip title="keep it stupidly simple"}.


## Rob Pike's 5 rules of programming

5. Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. Data structures, not algorithms, are central to programming.

Rule 5 was previously stated by Fred Brooks in The Mythical Man-Month. Rule 5 is often shortened to "write stupid code that uses smart objects". 

::: {.wide-quote .mt-2}
> I will, in fact, claim that the difference between a bad programmer and a good one is whether he considers his code or his data structures more important. Bad programmers worry about the code. [Good programmers worry about data structures and their relationships.]{.background-color-lightblue}
>
> -- Linus Torvalds 

:::

# refactoring example

:::::::::::: {.columns}
::::::::: {.column width="60%}

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

:::::::::
::::::::: {.column width="40%"}

- no documentation
- no tests
- missing type hints
    - seq, function
- unused loop variables
- ambiguous return values
- multiple execution branches
- main issue was, that it uses a less performant library
- has an unnecessary dependency
- multiple return statements

:::::::::
::::::::::::

## how to refactor it?

1. no tests, cannot be sure that the changed version would work as expected
2. add test
    - create a simple input data
    - check what the function does
        - basically like black-box testing

```python
dummy_seq = pd.DataFrame(
    {
        "h3_7": [1, 2, 3, 2, 3],
        "latitude_mean": [47.42, 47.64, 47.23, 47.87, 47.25],
        "longitude_mean": [18.91, 19.12, 19.09, 19.31, 19.08],
    }
)
```

## call function

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

>>> get_daily_stop_sequence_pl(dummy_seq, 7)
{}
```

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

using the sample input (`dummy_seq`) as before, the output:

`{1: {2: 1}, 2: {3: 2}, 3: {2: 1}}`

<!-- Rewrite this function using polars using windowing operators to produce the same result for the dummy_seq input. -->
<!-- https://chatgpt.com/share/6a0c172c-6e70-83eb-b811-13f0a86ce399 -->


# references

::: #refs
:::
