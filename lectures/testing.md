---
title: Testing
author: Gergő Pintér
date: gergo.pinter@uni-corvinus.hu
title-slide-attributes:
    data-background-color: "#181d37"
    data-background-image: assets/corvinus_neti_white.svg
    data-background-size: 23vw
    data-background-position: 1.25rem calc(100% - 1.25rem)
slideNumber: "true"
showSlideNumber: "print"
---

# test coverage

:::::::::::: {.columns}
::::::::: {.column width="50%"}
:::::: {.r-stack2}
::: {}
``` {#foo .python .numberLinesxs line-numbers="4,7-8,10" data-highlight-background="#ef8a62"}
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
:::::: {.r-stack2}
::: {.fragment data-fragment-index=1 .current-visible}
``` {.python}
def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
```
:::
::: {.fragment data-fragment-index=2 .current-visible}
``` {.python}
def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
```
:::
::::::
:::::::::
::::::::::::

:::::: {.r-stack}
::: {data-fragment-index=1 .current-visible}
test coverage: 60%
:::
::: {data-fragment-index=1 .current-visible}
test coverage: 80%
:::
::::::

::: notes
:::

## a

~~~~ {#mycode .haskell .numberLines startFrom="100"}
qsort []     = []
qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++
               qsort (filter (>= x) xs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
