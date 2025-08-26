---
title: week 10 summary 
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

# V model [@forsberg1991relationship]

:::::::::::: {.columns .column-gapless .text-smaller}
::::::::: {.column width="50%" .mt-4}
- each phase has output and a _review process_
    - errors are found at early stage
    - decreases the risk of failure
- testing is done in a hierarchical perspective
- review is a testing process usually without executing the code

:::::::::
::::::::: {.column width="50%"}
![](figures/v_model_unit_testing.drawio.svg){width=450}

:::::::::
::::::::::::


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


# what is a unit?

- defined as a **single behaviour** exhibited by the system under test
    - usually corresponding to a requirement
- often corresponds to a function or a module / method or a class
    - depending on the paradigm
    - often, but not always
- "only entry points to externally-visible system behaviours define units"
    - by Kent Beck [@beck2002test]

::: {.mt-3}
a unit test is another piece of code, that tests the given unit 
:::


## arrange, act, assert(, annihilate) pattern

parts of a unit test

:::::::::::: {.columns}
::::::::: {.column width="50%"}
arrange
~ set up the testing environment (e.g., create objects)

act
~ call the tested unit

assert
~ compare the result of the 'act' step to the expected value

(annihilate)
~ free resources
~ automatic in modern languages

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


# mocking

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


## test doubles -- mock object types

there is no open standard for categories

:::::::::::: {.columns}
::::::::: {.column width="40%" .mt-2}
- dummy
- stub
- spy
- mock
- fake

:::::::::
::::::::: {.column width="60%"}
![reproduction of figure 2 from [@seemann2007unit]](figures/spectrum_of_test_doubles.drawio.svg){width=400}
:::::::::
::::::::::::

::: {.text-smaller}
these are from the book _xUnit test patterns: Refactoring test code_ -- by Gerard Meszaros [@meszaros2007xunit]
:::


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


##

> As the tests get more specific, the code gets more generic.
>
> -- Robert C. Martin, [The Cycles of TDD](http://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html) [@martin2014cycles]

![](figures/test_code_generality.drawio.svg){width=375 .mt-4}



# test coverage

- the percentage of the code lines 'protected' or covered by tests

:::::::::::: {.columns}
::::::::: {.column width="50%"}
[`code/fizzbuzz.py`]{.text-smaller}

:::::: {.r-stack}
::: {.fragment .fade-out .width-100 data-fragment-index=1}
```{.python line-numbers="2-6,9,11" data-highlight-background="#c6ff8c"}
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
:::
::: {.fragment .current-visible .width-100 data-fragment-index=1}
```{.python line-numbers="2-9,11" data-highlight-background="#c6ff8c"}
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
:::
::: {.fragment .current-visible .width-100 data-fragment-index=2}
```{.python line-numbers="2-11" data-highlight-background="#c6ff8c"}
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
:::
::::::
:::::::::
::::::::: {.column width="50%"}
[`code/test_fizzbuzz.py`]{.text-smaller}

:::::: {.r-stack}
::: {.fragment .fade-out .width-100 data-fragment-index=1}
```python
from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(3) == "Fizz"
```
:::
::: {.fragment .current-visible .width-100 data-fragment-index=1}
```python
from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
```
:::
::: {.fragment .current-visible .width-100 data-fragment-index=2}
```python
from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(17) == "17"
```
:::
:::::
:::::::::
::::::::::::

:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
test coverage: 70%
:::
::: {.fragment .current-visible data-fragment-index=1}
test coverage: 90%
:::
::: {.fragment .current-visible data-fragment-index=2}
test coverage: 100%

four control flow branch, all of them needs to be tested
:::
::::::

<!-- #F72388 -->


## how to measure code quality?

it is hard to objectively measure the quality of code

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- [number of source lines of code (SLOC)]{.alpha-50}
- style guide compliance [-- is the code clean?]{.fragment data-fragment-index=1 .text-color-secondary}
- [Halstead metrics]{.alpha-50}
- cyclomatic complexity [-- is the code simple?]{.fragment data-fragment-index=1 .text-color-secondary}
- [maintainability index]{.alpha-50}
- test coverage [-- is the code tested?]{.fragment data-fragment-index=1 .text-color-secondary}

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/worker-takes-measurements.svg){width=400}

:::::::::
::::::::::::


## what to test - the edge cases

:::::::::::: {.columns}
::::::::: {.column width="40%"}
```python
def calculate_progress(
    finished: int,
    total: int,
    as_percentage: bool,
) -> float:
    progress = finished / total

    if as_percentage:
        return progress * 100
    else:
        return progress
```

::: {.fragment data-fragment-index=1}
this function need some value checking
:::
:::::::::
::::::::: {.column width="60%"}
what does this function do?
~ - divides the number of finished lessons by the total number of lessons
~ - returns progress in the closed interval of [0, 1] or [0, 100]

::: {.fragment data-fragment-index=1 .text-align-left}
edge cases
~ - total is 0
~ - total is less than 0
~ - finished is less than 0
~ - finished is greater than total
:::
:::::::::
::::::::::::

::: {.fragment data-fragment-index=2 .r-frame .mt-1}
test coverage only measures that every control flow branch is tested

the point of testing is testing for the edge cases
:::


#  changing the software

|                  | add feature | fix a bug | refactor | optimize |
| ---------------- | ----------- | --------- | -------- | -------- |
| structure        | changes     | changes   | changes  |          |
| new funcionality | changes     |           |          |          |
| functionality    |             | changes   |          |          |
| resource usage   |             |           |          | changes  |

::: {.text-smaller .mt-4}
Michael Feathers, Working Effectively with Legacy Code: part 1 pp 6 [@feathers2004working]
:::


# testing approaches

:::::::::::: {.columns}
::::::::: {.column width="50%"}
**black box**

![](figures/black_box.drawio.svg){width=350}

- examining / testing the functionality without knowing the inner structure
- works at all levels: unit, integration, system, acceptance
- also for debugging a legacy code

:::::::::
::::::::: {.column width="50%"}
**white box**

![](figures/white_box.drawio.svg){width=225}

- testing the internal structure as opposed to its functionality
- often associated to unit testing, but also works on higher levels (i.e., integration, system)

:::::::::
::::::::::::


# references

::: {#refs}
:::


<!--:::::::::::: {.columns}
::::::::: {.column width="50%" }

:::::::::
::::::::: {.column width="50%"}

:::::::::
::::::::::::-->
