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
> -- Feathers, M. (2004). Working Effectively with Legacy Code: Preface

<!--- [További definíciók](https://dzone.com/articles/defining-legacy-code)
- Legacy Code
    - [What are the key points of Working Effectively with Legacy Code?](http://programmers.stackexchange.com/questions/122014/what-are-the-key-points-of-working-effectively-with-legacy-code)-->


## the legacy code dilemma

> When we change code, we should have tests in place.
> To put tests in place, we often have to change code.
>
> -- Feathers, M. (2004). Working Effectively with Legacy Code: Part I / Chapter 2


##  changing the software

|                  | add feature | fix a bug | refactor | optimize |
| ---------------- | ----------- | --------- | -------- | -------- |
| structure        | changes     | changes   | changes  |          |
| new funcionality | changes     |           |          |          |
| functionality    |             | changes   |          |          |
| resource usage   |             |           |          | changes  |

::: {.text-smaller .mt-4}
Feathers, M. (2004). Working Effectively with Legacy Code: p1. pp 6. Prentice Hall Professional
:::
