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
