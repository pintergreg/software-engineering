---
title: testing
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
revealjs-url: "../assets/reveal.js-5.1.0/"
---

# V model [@forsberg1991relationship]

:::::::::::: {.columns .column-gapless .text-smaller}
::::::::: {.column width="50%" .mt-5}
- each phase has output and a _review process_
    - errors are found at early stage
    - decreases the risk of failure
- testing is done in a hierarchical perspective

:::::::::
::::::::: {.column width="50%"}
![](figures/v_model_unit_testing.drawio.svg){width=450}

:::::::::
::::::::::::

<!-- https://lostechies.com/content/derekgreer/uploads/2011/03/TestDrivenDevelopment_thumb_107D31DD.png -->


## test pyramid

:::::::::::: {.columns .mt-3}
::::::::: {.column width="50%"}
![](figures/test_pyramid_ice_cream.drawio.svg){width=500}

:::::::::
::::::::: {.column width="50%" .fragment data-fragment-index=1}
:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=2}
![](figures/test_pyramid_no_text.drawio.svg){width=500}

:::
::: {.fragment data-fragment-index=2}
![](figures/test_pyramid.drawio.svg){width=500}

:::

::::::
:::::::::
::::::::::::

::: {.fragment data-fragment-index=2 .text-size-1}
the turtle and rabbit figures by [Delapouite](https://delapouite.com/) under [CC&nbsp;BY&nbsp;3.0](https://creativecommons.org/licenses/by/3.0/) via [game-icons.net](https://game-icons.net)
:::


# what is a unit test?

:::::::::::: {.columns}
::::::::: {.column width="55%"}
- what is a unit?
    - smallest testable part of a program
    - usually a method
- a unit test is another piece of code, that tests the given unit 

:::::::::
::::::::: {.column width="45%"}
```python
def fizzbuzz(i: int) -> str:
    """
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
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

[doctest in Python]{.text-smaller}
:::::::::
::::::::::::


## what really is a unit?

- defined as a **single behaviour** exhibited by the system under test
    - usually corresponding to a requirement
- it may imply that it is a function or a module / method or a class
    - depending on the paradigm
- functions / methods, modules or classes don't always correspond to units
- "only entry points to externally-visible system behaviours define units"
    - by Kent Beck [@beck2002test]

<!-- > Unit is defined as a single behaviour exhibited by the system under test, usually corresponding to a requirement.
> While it may imply that it is a function or a module (in procedural programming) or a method or a class (in object-oriented programming) **it does not mean functions/methods, modules or classes always correspond to units**.
> From the system-requirements perspective only the perimeter of the system is relevant, thus **only entry points to externally-visible system behaviours define units**.
>
> -- Kent Beck via Wikipedia-->

::: {.text-smaller}
source: [@enwiki:1249792515]
:::


## unit vs integration testing

::: {.wide-quote}
> The terms 'unit test' and 'integration test' have always been rather murky, even by the slippery standards of most software terminology.
>
> -- [ Martin Fowler](https://martinfowler.com/articles/2021-test-shapes.html) [@fowler2021diverse]

:::

:::::::::::: {.columns .mt-3}
::::::::: {.column width="40%"}
unit test
~ tests a single behaviour

:::::::::
::::::::: {.column width="60%"}
integration test
~ test a set of units, working together

:::::::::
::::::::::::

::: {.text-smaller .mt-3}
in most of my examples a unit will be represented by a method
:::


## unit test example

:::::::::::: {.columns}
::::::::: {.column width="50%"}
`code/fizzbuzz.py`

```python
def fizzbuzz(i: int) -> str:
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

:::::::::
::::::::: {.column width="50%"}
`code/test_fizzbuzz.py`

```python
from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(12) == "Fizz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(17) == "17"
```

:::::::::
::::::::::::


## arrange, act, assert pattern

parts of a unit test

:::::::::::: {.columns}
::::::::: {.column width="50%"}
arrange
~ set up the testing environment (e.g., create objects)

act
~ call the tested unit

assert
~ compare the result of the 'act' step to the expected value

:::::::::
::::::::: {.column width="50%"}
```python
def test_fizzbuzz():
    # arrange
    test_input = 3
    # act
    result = fizzbuzz(test_input)
    # assert
    assert result == "Fizz"

```

:::::::::
::::::::::::

## arrange, act, assert(, annihilate) pattern

parts of a unit test

arrange
~ set up the testing environment
~ (e.g., create objects)

act
~ call the tested unit

assert
~ compare the result of the 'act' step to the expected value

annihilate
~ free resources
~ automatic in modern languages


# how to unit test this funciton?

:::::::::::: {.columns}
::::::::: {.column width="50%"}
```python
def query_progress(user_id: int) -> float:
    # establish database connection
    con = sqlite3.connect("data.db")
    # build query
    progress_query = f"""
    SELECT
        lesson / 50.0 AS progress
    FROM activity
    WHERE
        user_id = {user_id} AND
        result = 'success'
    ORDER BY
        lesson DESC
    LIMIT 1
    ;
    """
    # execute query
    res = con.execute(progress_query)
    progress = res.fetchone()[0]
    return progress
```

:::::::::
::::::::: {.column width="50%" .fragment .mt-1}
- short answer: you can't
- because it is not a unit
    - it does 3 things
- single responsibility principle makes unit testing easier
- a 'stable' database would be needed for testing
    - if the DB content changed, the expected value would become obsolete
:::::::::
::::::::::::


## separate business logic from persistence

<!-- ![hexagonal arcitectural pattern (a.k.a. ports & adapters)](figures/hexagonal_interface.drawio.svg){width=700} -->

:::::::::::: {.columns}
::::::::: {.column width="40%"}
architectural styles provides patterns to separate the business logic from the persistence layer

unit testing usually targets the business logic

:::::: {.fragment .text-smaller .mt-2}
which was embedded into the query in the previous example

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
::::::

:::::::::
::::::::: {.column width="30%"}
![](figures/layered_4.drawio.svg){width=200}

:::::::::
::::::::: {.column width="30%"}
![](figures/onion.drawio.svg){width=275}

![](figures/hexagonal_extend.drawio.svg){width=275}

:::::::::
::::::::::::


## separated business logic

:::::::::::: {.columns}
::::::::: {.column width="50%"}
```python
def query_last_finished_lesson(
    user_id: int
) -> float:
    # establish database connection
    con = sqlite3.connect("data.db")
    # build query
    query = f"""
    SELECT lesson
    FROM activity
    WHERE
        user_id = {user_id} AND
        result = 'success'
    ORDER BY lesson DESC
    LIMIT 1;
    """
    # execute query
    res = con.execute(query)
    return res.fetchone()[0]
```

:::::::::
::::::::: {.column width="50%"}
```python
def calculate_progress(
    finished: int, total: int
) -> float:
    return finished / total


def calculate_user_progress(
    user_id: int, total: int
) -> float:
    f = query_last_finished_lesson(user_id)
    return calculate_progress(f, total)
```

::: {.text-smaller}
- now, the query is only responsible for getting the last finished lesson
    - the DB connection is still in a bit out of the place, but the testability improved
:::
:::::::::
::::::::::::


## separated data connection

:::::::::::: {.columns}
::::::::: {.column width="50%"}
```python
def query_last_finished_lesson(
    con: sqlite3.Connection,
    user_id: int
) -> float:
    # build query
    query = f"""
    SELECT lesson
    FROM activity
    WHERE
        user_id = {user_id} AND
        result = 'success'
    ORDER BY lesson DESC
    LIMIT 1;
    """
    # execute query
    res = con.execute(query)
    return res.fetchone()[0]
```

:::::::::
::::::::: {.column width="50%"}
```python
def establish_database_connection(
    path: str = "data.db"
) -> sqlite3.Connection:
    return sqlite3.connect(path)
```

::: {.text-smaller}
- now, there is a function responsible for the DB connection
    - it is easy to use a test database from the test suite and the production database in the production code
- the test DB can store 'stable' values
    - the expected values in the assert statements are safe
:::
:::::::::
::::::::::::


## mocking

:::::::::::: {.columns}
::::::::: {.column width="70%" .mt-4}
- the whole _unit test_ suite should be able to run in milliseconds
    - to give immediate feedback
- slow elements of the software should be mocked
    - e.g., database, network connection
- part of arrange step

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/running-turtle.svg){width=300}

:::::::::
::::::::::::


## what to test?

:::::::::::: {.columns}
::::::::: {.column width="50%"}
```python
def calculate_progress(
    finished: int,
    total: int,
    as_percentage: bool
) -> float:
    progress = finished / total

    if as_percentage:
        return progress * 100
    else:
        return progress
```

:::::::::
::::::::: {.column width="50%"}

:::::::::
::::::::::::


# test-driven development (TDD)

:::::::::::: {.columns}
::::::::: {.column width="55%" .mt-5}
- write test _before_ writing the tested code
- without the called unit the test fill fail
    - the called function does not exist
- write code, that makes the test pass
- improve the code quality
    - e.g., make it clear and clean
    - both the test and tested code

:::::::::
::::::::: {.column width="45%"}
![](figures/tdd.drawio.svg){width=350}

:::::::::
::::::::::::


## test-driven development -- fizzbuzz example

:::::::::::: {.columns}
::::::::: {.column width="55%"}
[fizzbuzz.py]{.text-smaller}

:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1 .width-100}
```python
```
:::
::: {.fragment .current-visible data-fragment-index=1 .width-100}
```python
def fizzbuzz():
    pass
```
:::
::: {.fragment .current-visible data-fragment-index=2 .width-100}
```python
def fizzbuzz(i):
    pass
```
:::
::: {.fragment .current-visible data-fragment-index=3 .width-100}
```python
def fizzbuzz(i):
    return "Fizz"
```
:::
::: {.fragment .current-visible data-fragment-index=4 .width-100}
```python
def fizzbuzz(i):
    return "Fizz"
```
:::
::: {.fragment .current-visible data-fragment-index=5 .width-100}
```python
def fizzbuzz(i):
    if i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
```
:::
::: {.fragment .current-visible data-fragment-index=6 .width-100}
```python
def fizzbuzz(i):
    if i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
```
:::
::: {.fragment .current-visible data-fragment-index=7 .width-100}
```python
def fizzbuzz(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
```
:::
::: {.fragment .current-visible data-fragment-index=8 .width-100}
```python
def fizzbuzz(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
```
:::
::: {.fragment .current-visible data-fragment-index=9 .width-100}
```python
def fizzbuzz(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)
```
:::
::::::
:::::::::
::::::::: {.column width="45%"}
[test_fizzbuzz.py]{.text-smaller}

:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=4 .width-100}
```python
from fizzbuzz import *

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
```
:::
::: {.fragment .current-visible data-fragment-index=4 .width-100}
```python
from fizzbuzz import *

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
```
:::
::: {.fragment .current-visible data-fragment-index=5 .width-100}
```python
from fizzbuzz import *

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
```
:::
::: {.fragment .current-visible data-fragment-index=6 .width-100}
```python
from fizzbuzz import *

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
```
:::
::: {.fragment .current-visible data-fragment-index=7 .width-100}
```python
from fizzbuzz import *

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
```
:::
::: {.fragment .current-visible data-fragment-index=8 .width-100}
```python
from fizzbuzz import *

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(17) == "17"
```
:::
::: {.fragment .current-visible data-fragment-index=9 .width-100}
```python
from fizzbuzz import *

def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(17) == "17"
```
:::
::::::
:::::::::
::::::::::::

:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
NameError: name 'fizzbuzz' is not defined
:::
::: {.fragment .current-visible data-fragment-index=1}
TypeError: fizzbuzz() takes 0 positional arguments but 1 was given
:::
::: {.fragment .current-visible data-fragment-index=2}
AssertionError: assert None == 'Fizz'
:::
::: {.fragment .current-visible data-fragment-index=3}
passed
:::
::: {.fragment .current-visible data-fragment-index=4}
AssertionError: assert 'Fizz' == 'Buzz' (5)
:::
::: {.fragment .current-visible data-fragment-index=5}
passed
:::
::: {.fragment .current-visible data-fragment-index=6}
AssertionError: assert 'Fizz' == 'FizzBuzz' (15)
:::
::: {.fragment .current-visible data-fragment-index=7}
passed
:::
::: {.fragment .current-visible data-fragment-index=8}
AssertionError: assert None == '17' (17)
:::
::: {.fragment .current-visible data-fragment-index=9}
passed

[there is not much to improve on the code, except that according to the PEP8 Python style guide the 'star import' is not allowed; it should be `import fizzbuzz`]{.text-smaller}
:::
::::::


# behaviour-driven development (BDD)

:::::::::::: {.columns}
::::::::: {.column width="55%" .mt-3}
- BDD is an extension of [TDD]{.tooltip title="test-driven development"}
- using BDD can help you to turn an idea for a requirement into implemented, **tested**, production-ready code
- BDD starts from a user story and focuses on adding the acceptance criteria
    - which can be turned into unit tests

:::::::::
::::::::: {.column width="45%"}
```
Title (one line describing the story)

Narrative:
As a [role]
I want [feature]
So that [benefit]

Acceptance Criteria: (presented as Scenarios)

Scenario 1: Title
Given [context]
  And [some more context]...
When  [event]
Then  [outcome]
  And [another outcome]...

Scenario 2: ...
```

:::::::::
::::::::::::

::: {.text-smaller}
taken from [@north2007what] by Daniel Terhorst-North | CC-BY 4.0
:::

::: notes
- the strict TDD does not allow more than one new test at a time
:::


## acceptance criteria

:::::::::::: {.columns}
::::::::: {.column width="55%" .mt-2}
- describes how a system should behave under certain circumstances
    - may originate from domain experts
- the 'rules' are written in natural language, but in a structured form
    - easy to discuss with non-developers
- based on the acceptance criteria multiple tests can be written

:::::::::
::::::::: {.column width="45%"}
```
Title (one line describing the story)

Narrative:
As a [role]
I want [feature]
So that [benefit]

Acceptance Criteria: (presented as Scenarios)

Scenario 1: Title
Given [context]
  And [some more context]...
When  [event]
Then  [outcome]
  And [another outcome]...

Scenario 2: ...
```

::: {.text-smaller}
taken from [@north2007what] by Daniel Terhorst-North | CC-BY 4.0
:::
:::::::::
::::::::::::



# test coverage

<!-- #F72388 -->


## when unit test are not more than a measure

:::::::::::: {.columns}
::::::::: {.column width="70%" .mt-4}
- zombie scrum: doing something without heart, without its essence
- if you write unit tests _just_ to increase the test coverage they loose its function

:::::::::
::::::::: {.column width="30%"}
![by Randall Munroe<br>[CC&nbsp;BY-NC&nbsp;2.5](https://creativecommons.org/licenses/by-nc/2.5/deed.en) | [source](https://xkcd.com/2899/)](figures/borrowed/xkcd/goodharts_law_2x.png){width=300}

:::::::::
::::::::::::


# legacy code

this chapter is based on the book _Working Efficiently with Legacy Code_ by Michael Feathers.


## what is legacy code?

> Code without tests is bad code.
> It doesn’t matter how well written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is.
> With tests, we can change the behavior of our code quickly and verifiably.
> Without them, we really don’t know if our code is getting better or worse.
>
> -- Michael Feathers, Working Effectively with Legacy Code: Preface [@feathers2004working]

<!--- [További definíciók](https://dzone.com/articles/defining-legacy-code)
- Legacy Code
    - [What are the key points of Working Effectively with Legacy Code?](http://programmers.stackexchange.com/questions/122014/what-are-the-key-points-of-working-effectively-with-legacy-code)-->


## the legacy code dilemma

> When we change code, we should have tests in place.
> To put tests in place, we often have to change code.
>
> -- Michael Feathers, Working Effectively with Legacy Code: Part I / Chapter 2 [@feathers2004working]


##  changing the software

|                  | add feature | fix a bug | refactor | optimize |
| ---------------- | ----------- | --------- | -------- | -------- |
| structure        | changes     | changes   | changes  |          |
| new funcionality | changes     |           |          |          |
| functionality    |             | changes   |          |          |
| resource usage   |             |           |          | changes  |

::: {.text-smaller .mt-4}
Michael Feathers, Working Effectively with Legacy Code: p1. pp 6. [@feathers2004working]
:::


# references

::: {#refs}
:::
