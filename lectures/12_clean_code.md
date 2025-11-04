---
title: clean code
author: Gergő Pintér, PhD
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
    data-background-image: ../assets/by-sa.svg
    data-background-size: 125px
    data-background-position: 1.25rem calc(100% - 1.25rem)
slideNumber: "true"
showSlideNumber: "print"
revealjs-url: "../assets/reveal.js-5.2.1/"
---

# software design and architecture stack

![based on Khalil Stemmel's figure [@stemmler2019how]](figures/the_software_design_and_architecture_stack_generalized.drawio.svg){height=475}

# what is clean code

- the term, _clean code_ refers to code that's easy to read, understand, and maintain
    - popularized by Robert C. Martin
- guideline how to write readable, understandable, and maintainable code
    - although not every "rule" applies to every language / situation

## why it matters

misconception: program code is mostly written, while in reality it is mainly read

a well-written code is easy to read, understand, debug, maintain, extend, etc.

::: {.mt-3}
> Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
>
> -- Martin Fowler [@fowler2018refactoring]

:::

::: {.mt-3}
- where human can be the future you, current or future colleague...
- like having a nice handwriting
:::

## clear is better than clever

::: {.wide-quote}
> In any kind of programming, clarity should always be the primary goal.
>
> Writing code that is straightforward and understandable is more valuable than trying to craft overly clever or intricate solutions.
>
> -- [Go Proverbs](https://go-proverbs.github.io/) by Rob Pike 

:::

source: [Rob Pike’s Go Proverbs](https://golangprojectstructure.com/rob-pike-go-proverbs-3/#clear-is-better-than-clever)

## prime check -- clever vs. clear

:::::::::::: {.columns}
::::::::: {.column width="50%"}
```go
func isPrime(n int) bool {
    if n < 2 {
        return false
    }

    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }

    return true
}
```

:::::::::
::::::::: {.column width="50%"}
```go
func isPrime(n int) bool {
    if n < 2 {
        return false
    }

    for i := 2; i <= n/2; i++ {
        if n%i == 0 {
            return false
        }
    }

    return true
}
```

less efficient, but it may be easier for a reader to understand

:::::::::
::::::::::::

source: [Rob Pike’s Go Proverbs](https://golangprojectstructure.com/rob-pike-go-proverbs-3/#clear-is-better-than-clever)

##

```go
func isPrime(n int) bool {
	if n < 2 {
		return false
	}

	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}
```

::: {.text-smaller}
- iterating only up to the square root of n because if n has any divisor greater than its square root, there must also be a corresponding divisor smaller than the square root
- it is easier to understand than the "clever one", but less wasteful then the "clear one"
- why is the clever on better?
    - [because multiplication is more efficient for the CPU than calculating the square root]{.fragment}

:::

# hierarchy in style guides

:::::::::::: {.columns}
::::::::: {.column width="55"}
- language level:
    - Python: [PEP 8](https://peps.python.org/pep-0008/) or [pep8.org](https://pep8.org/)
    - Ruby: [Ruby Style Guide](https://rubystyle.guide/)
    - Go: [Effective Go](https://go.dev/doc/effective_go)
    - Rust [The Rust Style Guide](https://doc.rust-lang.org/beta/style-guide/index.html)
    - etc.
- organization level:
    - [Google Style Guides](https://google.github.io/styleguide/)
        - [C# at Google Style Guide](https://google.github.io/styleguide/csharp-style.html)
        - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
        - [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)

::: {.fragment}
not just style guides, also best practices
:::
:::::::::
::::::::: {.column width="45%"}
![](figures/style_hierarchy.drawio.svg){width=375}

:::::::::
::::::::::::


# write idiomatic code

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="70" .mt-1}
::: {.text-align-left}
- a prog. language implements a prog. paradigm
- a paradigm defines a certain "way" of writing code
    - using different abstractions / building blocks
    - promoting a given concept
:::
::: {.fragment .text-align-left}
- some languages implements multiple paradigms
:::
::: {.fragment .text-align-left}
- and languages have their own way of doing things
    - languages have pros and cons for a given problem
:::
:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/rural-road-with-signpost.svg){width=250}

:::::::::
::::::::::::

::: {.fragment .mt-3}
just as in the case of natural languages, you ought to use a language properly
:::


## write idiomatic code

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="55"}
```javascript
for (i = 0; i < 10; i++) {
    console.log(i);
}
```

::: {.fragment data-fragment-index="5"}
```javascript
[...Array(10).keys()].forEach(i => {
    console.log(i);
});
```

:::
:::::::::
::::::::: {.column width="20%"}
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

::: {.fragment data-fragment-index="1"}
```python
for i in range(10):
    print(i)
```

:::
:::::::::
::::::::: {.column width="25%"}
::: {.fragment data-fragment-index="2"}
```ruby
for i in 0..9 do
   puts i
end
```

:::
::: {.fragment data-fragment-index="3"}
```ruby
(0..9).each do |i|
    puts i
end
```

:::
::: {.fragment data-fragment-index="4"}
```ruby
(0..9).each {|i| puts i}
```

:::
:::::::::
::::::::::::


# clean code

Clean Code: A Handbook of Agile Software Craftsmanship

by Robert C. Martin (2009) [@martin2009clean]

<!--::: {.fragment .text-smaller}
some recommendations are too specific to C-like languages
:::-->


# meaningful names

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-5}
this section is based on the book *Clean Code* (chapter 2) by Robert C. Martin [@martin2009clean]

with own examples

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/hand-with-bottle.svg){height=300}

:::::::::
::::::::::::


## use intention-revealing names

:::::: {.text-size-3}
```c
int d; // elapsed time in days
```

::: {.text-size-2 .fragment data-fragment-index=1}
the definition is only available ad the declaration
:::

```c
int elapsedTimeInDays;
```

::: {.text-size-2 .fragment data-fragment-index=1}
the definition is available at every usage
:::
::::::


## multi-word names

:::::::::::: {.columns}
::::::::: {.column width="32"}
**camelCase**

::: {.mt-4}
```c
int elapsedTimeInDays;
```
:::

::: {.text-smaller}
- C (local variable)
- Java (variable, method)

:::
:::::::::
::::::::: {.column width="32%"}
**UpperCamelCase (PascalCase)**

```java
public class DataCollector {}
```

::: {.text-smaller}
- Java (class)
- Rust (Type, Enum)

:::
:::::::::
::::::::: {.column width="32%"}
**snake_case**

::: {.mt-4}
```python
elapsed_time_in_days = 17
```
:::

::: {.text-smaller}
- Python
- Rust (variable, function)

:::
:::::::::
::::::::::::

::: {.fragment .mt-4}
<!-- according to a study, camelCase is faster to type but snake_case is faster to read [@sharif2010eye] -->
a study states, camelCase is faster to type but snake_case is faster to read [@sharif2010eye]
:::

::: {.fragment .mt-2}
read the style guide
:::


## avoid disinformation

> Do not refer to a grouping of accounts as an `accountList` unless it’s actually a `List` [@martin2009clean].

::: {.text-smaller}
better to use `accounts`, it does not depend on the collection name
:::

::: {.fragment .mt-3}
inconsistent spelling is also disinformation
:::

::: {.fragment .mt-3}
> disinformative names would be the use of lower-case `L` or uppercase `O` [@martin2009clean]

- they can look almost like the one and zero, respectively -- use the right font
- PEP8 (Python style guide) [forbids](https://pep8.org/#names-to-avoid) to use them

:::


## make meaningful distinctions

> It is not sufficient to add number series or noise words, even though the compiler is satisfied. If names must be different, then they should also mean something different [@martin2009clean].

:::::: {.text-size-2}
```python
def calculate_distance(data: pd.DataFrame) -> pd.Series:
    # do something
```

```python
def calculate_distance2(data: pd.DataFrame) -> pd.Series:
    # do something else
```

::: {.fragment}
```python
def calculate_eucledian_distance(data: pd.DataFrame) -> pd.Series:
    # ...
```

```python
def calculate_levenshtein_distance(data: pd.DataFrame) -> pd.Series:
    # ...
```
:::
::::::


## make meaningful distinctions / noise words

> Noise words are another meaningless distinction.
> Imagine that you have a `Product` class.
> If you have another called `ProductInfo` or `ProductData`, you have made the names different without making them mean anything different [@martin2009clean]. 


## use pronounceable names

> If you can't pronounce it, you can't discuss it without sounding like an idiot [@martin2009clean].

- Should `etid` be an integer?
- Should `elapsed_time_in_days` be an integer?

::: {.fragment .mt-3}
could be especially important for non-native speakers as some words are more difficult to pronounce
:::


## use searchable names

:::::::::::: {.columns}
::::::::: {.column width="70%" .mt-4}

::: {.wide-quote}
> Single-letter names can ONLY be used as local variables inside short methods.
> The length of a name should correspond to the size of its scope [@martin2009clean].

:::

:::::::::::: {.columns}
::::::::: {.column width="40%"}
it's OK to do this:

```python
for i in range(10):
    print(i)
```

:::::::::
::::::::: {.column width="60%"}
it's NOT OK in a large scope:

```c
int d; // elapsed time in days
```
:::::::::
::::::::::::
:::::::::
::::::::: {.column width="30%"}
![](figures/variable_scope.drawio.svg){width=250 preview-image="figures/variable_scope.drawio.svg" preview-fit="contain"}

:::::::::
::::::::::::


## names for classes, functions

:::::::::::: {.columns .mt-3}
::::::::: {.column width="50%"}
- a class is a model / blueprint of *something*
- the name should be a noun
    - e.g., `User`, `Activity`
- an object is an instance of a class
    - still a noun
    - e.g., `user = User()`
:::::::::
::::::::: {.column width="50%"}
- a function *does* something
- the name should contain a verb
    - in imperative
    - e.g., `aggregate_activity`
    - ~~`activity_aggregation`~~

:::::::::
::::::::::::

    
## avoid encodings

with modern IDEs it is pointless to put type or role markers into names


:::::: {.r-frame .text-smaller}
**Hungarian notation**

- invented by Charles Simonyi at Microsoft
- adding a prefix to a name that gives information about type, length, or scope

```python
def fnFactorial(iNum):
    if iNum == 1:
        return iNum
    else:
        return iNum * fnFactorial(iNum - 1)
```

::: {.text-small}
source: [@bhargav2024hungarian]
:::
::::::


:::::::::::: {.columns .r-frame .mt-1}
::::::::: {.column width="50%"}
```csharp
interface IShapeArea // I is also a prefix
{
  void area(); 
}

```
:::::::::
::::::::: {.column width="50%"}
```csharp
interface ShapeArea 
{
  void area(); 
}

```
:::::::::
::::::::::::


## avoid mental mapping

> Readers shouldn't have to mentally translate your names into other names they already know [@martin2009clean].

<!-- CPU, USB, CLI, GUI, LED, RGB, ORM, PEP, RFC, GPS, etc... -->

:::::::::::: {.columns .mt-4}
::::::::: {.column width="50%"}
![](figures/mental_map_1.svg){width=200}
:::::::::
::::::::: {.column width="50%" .fragment}
![](figures/mental_map_2.svg){width=275}
:::::::::
::::::::::::


## don't pun or use humor

- no inside jokes
- no colloquialisms or slang
- be objective and professional

> Say what you mean. Mean what you say [@martin2009clean].


## pick one word per concept

>  it’s confusing to have `fetch` , `retrieve`, and `get` as equivalent methods of different classes [@martin2009clean]

it also helps to search for the term


## add meaningful context

> Imagine that you have variables named firstName, lastName, street, houseNumber, city, state, and zipcode.
> Taken together it’s pretty clear that they form an address.
> But what if you just saw the state variable being used alone in a method? [@martin2009clean]

- adding a prefix?
    - e.g., `addrCity`, `addrStreet`, `addrState`
- as notations are discouraged, use an `Address` class instead to add context


# functions

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-5}
this section is based on the book *Clean Code* (chapter 3) by Robert C. Martin [@martin2009clean]

with own examples

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/cogwheel.svg){height=300}

:::::::::
::::::::::::


## functions should be as small as possible

> Functions should hardly ever be 20 lines long [@martin2009clean]

- shorter functions are easier to understand


## do one thing (single responsibility principle)

:::::::::::: {.columns .column-gapless .fragment}
::::::::: {.column width="68%" .pre-height-100}
::: {.text-smaller .pre-height-100}
```python
import sqlite3
import pandas as pd

con = sqlite3.connect("data.db")
data = pd.read_sql(activity_query, con)

records = []
for woy in range(36, 40):
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
activity = pd.pivot(
    data, index=["week_of_year"], columns=["day_of_week"], values=["count"]
).values
res = con.execute(progress_query)
progress = res.fetchone()[0]
```
:::
:::::::::
::::::::: {.column width="32%"}
::: { .text-smaller}
```sql
SELECT
    CAST(
        strftime('%W', timestamp) 
        AS INTEGER
    ) AS week_of_year,
    CAST(
        strftime('%u', timestamp)
        AS INTEGER
    ) AS day_of_week,
    count(*) AS count
FROM activity
WHERE
    user_id = 42 AND
    week_of_year > 35 AND
    week_of_year < 40
GROUP BY
    week_of_year,
    day_of_week;
```

```sql
SELECT
	lesson / 50.0 AS progress
FROM activity
WHERE
    user_id = 42 AND
    result = 'success'
ORDER BY lesson DESC
LIMIT 1;
```

:::
:::::::::
::::::::::::


## debug tables

:::::::::::: {.columns}
::::::::: {.column width="50%"}
::: {.text-smaller}
|week_of_year|day_of_week|count|
|------------|-----------|-----|
|          36|          2|    1|
|          38|          5|    1|
|          39|          6|    2|
Table: queried user activity

:::

::: {.text-smaller .mt-5}
|day_of_week |1|2|3|4|5|6|7|
|------------|-|-|-|-|-|-|-|
|week_of_year| | | | | | | |
|          36|0|1|0|0|0|0|0|
|          37|0|0|0|0|0|0|0|
|          38|0|0|0|0|1|0|0|
|          39|0|0|0|0|0|2|0|
Table: pivoted user activity table

:::

:::::::::
::::::::: {.column width="50%"}
::: {.text-smaller}
|week_of_year|day_of_week|count|
|------------|-----------|-----|
|          36|          1|    0|
|          36|          2|    0|
|         ...|        ...|  ...|
|          36|          7|    0|
|          37|          1|    0|
|         ...|        ...|  ...|
|          37|          7|    0|
|          38|          1|    0|
|         ...|        ...|  ...|
|          38|          5|    0|
|         ...|        ...|  ...|
|          39|          6|    0|
|          39|          7|    0|
Table: empty activity table

:::
:::::::::
::::::::::::


## the inverse scope law of function names

:::::::::::: {.columns}
::::::::: {.column width="70%"}
::: {.wide-quote}
> **The longer the scope of a function, the shorter its name should be.** Functions that are called locally from a few nearby places should have long descriptive names, and the longest function names should be given to those functions that are called from just one place.
>
> -- [Robert C. Martin](https://www.informit.com/articles/article.aspx?p=1323426)

:::

::: {.text-smaller .mt-3}
"longer scope": more general part of a code
:::
:::::::::
::::::::: {.column width="30%" .fragment}
![](figures/name_and_scope.drawio.svg){width=300}
:::::::::
::::::::::::


## function arguments

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="45%"}
::: {.text-align-left}
- do not use more than three [@martin2009clean]
:::
::: {.text-align-left .fragment data-fragment-index=1}
- what if you'd need more?
    - wrap it into an object
:::
::: {.text-align-left .fragment data-fragment-index=2}
- do not use flags
    - ["Flag arguments are ugly \[...\] loudly proclaiming that this function does more than one thing [@martin2009clean]."]{.text-smaller}
:::

:::::::::
::::::::: {.column width="55%"}
```python
def build_empty_dataframe(start, end, cols):
    records = []
    for woy in range(start, end + 1):
        for dow in range(1, 8):
            records.append([woy, dow, 0])
    return pd.DataFrame.from_records(
        records, columns=cols
    )
```
::: {.fragment data-fragment-index=2}
```python
def query_progress(as_percentage: bool):
    res = con.execute(progress_query)
    progress = res.fetchone()[0]

    if as_percentage:
        return progress * 100
    else:
        return progress
```
:::
:::::::::
::::::::::::


## function as interface

:::::::::::: {.columns}
::::::::: {.column width="60%" .pre-450}
```{.python line-numbers="3,11,14" data-highlight-background="#c6ff8c"}
DataFrame.to_csv(
    path_or_buf=None, *,
    sep=',',
    na_rep='',
    float_format=None,
    columns=None,
    header=True,
    index=True,
    index_label=None,
    mode='w',
    encoding=None,
    compression='infer',
    quoting=None,
    quotechar='"',
    lineterminator=None,
    chunksize=None,
    date_format=None,
    doublequote=True,
    escapechar=None,
    decimal='.',
    errors='strict',
    storage_options=None
)
```
<!--```python
DataFrame.to_csv(path_or_buf=None, *, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', lineterminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)
```-->

:::::::::
::::::::: {.column width="40%" .mt-5}
![Libreoffice Calc CSV settings dialog](figures/lo_calc_save_csv.png){width=450}

:::::::::
::::::::::::


## no side effects

:::::::::::: {.columns}
::::::::: {.column width="50%" .wide-qoute}
> Side effects are lies.
> Your function promises to do one thing, but it also does other hidden things [@martin2009clean].
>
> -- Robert C. Martin

:::::::::
::::::::: {.column width="50%" .text-smaller .wide-qoute}
> an operation, function or expression is said to have a **side effect** if it modifies some state variable value(s) outside its local environment, that is to say has an observable effect besides returning a value (the main effect) to the invoker of the operation [@enwiki:1063806709].

:::::::::
::::::::::::


## side effect example

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="50%"}
```python
class Something:
    foo = 0
    
    def increase(self, by):
        self.foo += by
    
    def decrease(self, by):
        self.foo -= by
    
something = Something()
print(something.foo)  # 0
something.increase(2)
print(something.foo)  # 2
```
:::::::::
::::::::: {.column width="50%" .fragment}
```python
smth = {"foo": 0}

def increase(what, by):
    return what + by

def decrease(what, by):
    return what - by

print(smth["foo"])  # 0
increase(smth["foo"], 2)  # 2
print(smth["foo"])  # 0
smth["foo"] = increase(smth["foo"], 2)
print(smth["foo"])  # 2
```
:::::::::
::::::::::::


## prefer exceptions to returning error codes

- in unix-like systems processes still return 0 if the execution was successful
- but returning error codes in functions are discouraged
- `FileNotFoundException` is better than `ERRCODE_26375`
    - meaningful name
    - no mental mapping
    - exception handling syntactically more readable


# comments

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-5}
this section is based on the book *Clean Code* (chapter 4) by Robert C. Martin [@martin2009clean]

with own examples

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/notebook-papers.svg){height=300}

:::::::::
::::::::::::


## separating comments

```python
# connect to the database
con = sqlite3.connect("data.db")
# query activity data
data = pd.read_sql(activity_query, con)
# create empty dataframe
records = []
for woy in range(36, 40):
    for dow in range(1, 8):
        records.append([woy, dow, 0])
empty = pd.DataFrame.from_records(records, columns=["week_of_year", "day_of_week", "count"])
# combine empty and sparse dataframe
data = (
    pd.concat([data, empty])
    .drop_duplicates(subset=["week_of_year", "day_of_week"], keep="first")
    .sort_values(["week_of_year", "day_of_week"])
    .reset_index(drop=True)
)
# pivot dataframe
activity = pd.pivot(
    data, index=["week_of_year"], columns=["day_of_week"], values=["count"]
).values
```


## separated functions

```python
def create_empty_dataframe(start_week, end_week):
    records = []
    for woy in range(start_week, end_week+1):
        for dow in range(1, 8):
            records.append([woy, dow, 0])
    return pd.DataFrame.from_records(
        records, columns=["week_of_year", "day_of_week", "count"]
    )

def fill_empty_with_activities(empty, activities):
    return (
        pd.concat([activities, empty])
        .drop_duplicates(subset=["week_of_year", "day_of_week"], keep="first")
        .sort_values(["week_of_year", "day_of_week"])
        .reset_index(drop=True)
    )

def pivot_dataframe(data):
    return pd.pivot(
        data, index=["week_of_year"], columns=["day_of_week"], values=["count"]
    ).values
```

::: {.text-smaller}
these functions do one thing
:::

## separated functions - usage

```python
con = sqlite3.connect("data.db")

activities = pd.read_sql(activity_query, con)

empty = create_empty_dataframe(36, 39)

data = fill_empty_with_activities(emty, activities)

activities_matrix = pivot_dataframe(data)
```

only the comments remained, which can be read as a prose


## more bad comments


:::::::::::: {.columns .column-gapless}
::::::::: {.column width="60%"}

:::::: {}
**journal comment**

```python
# 2024-10-17 -- Add idiomatic coding examples 
# 2024-10-18 -- Add meaningful names section 
```

::: {.text-smaller}
the version tracker keeps better journal
:::
::::::

:::::: {}
**noise comments**

```python
# creates an empty dataframe
def create_empty_dataframe(start_week, end_week):
    # ...
```

::: {.text-smaller}
don't write something that is already in the code
:::
::::::

:::::: {}
**closing brace comments**

```javascript
for (i = 0; i < 10; i++) {
    console.log(i);
} // for
```

::: {.text-smaller}
modern editors can find (end display) the block endings
:::
::::::
:::::::::
::::::::: {.column width="40%"}
![by Oliver Widder (Geek and Poke) [CC&nbsp;BY&nbsp;3.0](https://creativecommons.org/licenses/by/3.0/)](figures/borrowed/geek_and_poke/good_comments.jpg){width=375}

:::::::::
::::::::::::


## Apollo 11 - Colossus 2A

``` {.numberLines startFrom="149"}
P21VSAVE	DLOAD			# SAVE CURRENT BASE VECTOR
			TAT
		STOVL	P21TIME		# ..TIME
			RATT1
		STOVL	P21BASER	# ..POS B-29 OR B-27
			VATT1
		STORE	P21BASEV	# ..VEL B-7  OR B-5
		ABVAL	SL*
			0,2
		STOVL	P21VEL		# /VEL/ FOR N73 DSP
			RATT
		UNIT	DOT
			VATT		# U(R).(V)
		DDV	ASIN		# U(R).U(V)
			P21VEL
		STORE	P21GAM		# SIN-1 U(R).U(V), -90 TO +90
		SXA,2	SET
			P21ORIG		# 0 = EARTH  2 = MOON
			P21FLAG
```

[source](https://github.com/chrislgarry/Apollo-11/blob/4d15e4d9d37202847334d4c640058803ed4e782e/Comanche055/GROUND_TRACKING_DETERMINATION_PROGRAM.agc#L149-L167), [GitHub repository](https://github.com/chrislgarry/Apollo-11), more about the Apollo Guidance Computer: [@slavin2015coding]


## good comments

**legal comments**

some open source licences should be included to the beginning of the files 

**informative comments**

```python
import re

timestamp = "2024-10-22 09:30:42"
# matches for timestamps in the format of: YYYY-MM-DD HH:MM:SS
re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", timestamp)
```

::: {.fragment}
**TODOs -- good or bad?**

```python
# TODO: this allows invalid month, day, hour, minute and second values
re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", timestamp)
```

[editors can collect `TODO` (and `FIXME`) annotations and warn about them]{.text-smaller}
:::


## documentation

::: {.pre-475}
```python
def fizzbuzz(i: int) -> str:
    """Fizzbuzz is a game for children to teach them about division.
    It is also a common coding practice.
    
    Parameters
    ----------
    i : int
        Input number tested against division by 3, 5 and 15.
    
    Returns
    -------
    str
        `Fizz` if input divisible by 3, `Buzz` if divisible by 5 and `FizzBuzz` if both.
    """
    result = ""
    if i % 15 == 0:
        result += "FizzBuzz"
    elif i % 3 == 0:
        result += "Fizz"
    elif i % 5 == 0:
        result += "Buzz"
    else:
        result = str(i)
    return result
```
:::


## doctest

:::::::::::: {.columns}
::::::::: {.column width="50%"}
::: {.pre-475}

```python
def fizzbuzz(i: int) -> str:
    """
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(12)
    'Fizz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(17)
    '17'
    """
    result = ""
    if i % 15 == 0:
        result += "FizzBuzz"
    elif i % 3 == 0:
        result += "Fizz"
    elif i % 5 == 0:
        result += "Buzz"
    else:
        result = str(i)
    return result
```

:::

:::::::::
::::::::: {.column width="50%" .fragment}
::: {.pre-475}
``` {.python}
python -m doctest -v fizzbuzz_doctest.py
Trying:
    fizzbuzz(3)
Expecting:
    'Fizz'
ok
Trying:
    fizzbuzz(5)
Expecting:
    'Buzz'
ok
Trying:
    fizzbuzz(15)
Expecting:
    'FizzBuzz'
ok
Trying:
    fizzbuzz(17)
Expecting:
    '17'
ok
4 passed.
Test passed.
```

:::
:::::::::
::::::::::::

# references

::: {#refs}
:::
