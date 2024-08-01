---
title: Testing
author: Gergő Pintér
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
slideNumber: "true"
showSlideNumber: "print"
---

# test coverage

:::::::::::: {.columns}
::::::::: {.column width="50%"}
``` {.python}
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

:::::::::
::::::::::::


::: notes
:::

## test coverage

:::::::::::: {.columns}
::::::::: {.column width="50%"}
``` {.python line-numbers="4,7-8,10" data-highlight-background="#ef8a62"}
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
``` {.python}
def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
```
:::::::::
::::::::::::

::: {}
test coverage: 60%
:::

::: notes
:::

## test coverage {data-transition="none"}

:::::::::::: {.columns}
::::::::: {.column width="50%"}
``` {.python line-numbers="4,10" data-highlight-background="#ef8a62"}
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
``` {.python}
def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
```
:::::::::
::::::::::::

::: {}
test coverage: 80%
:::

::: notes
:::

## test coverage {data-transition="none"}

:::::::::::: {.columns}
::::::::: {.column width="50%"}
``` {.python line-numbers="10" data-highlight-background="#ef8a62"}
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
``` {.python}
def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
```
:::::::::
::::::::::::

::: {}
test coverage: 90%
:::

::: notes
:::

## test coverage {data-transition="none"}

:::::::::::: {.columns}
::::::::: {.column width="50%"}
``` {.python}
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
``` {.python}
def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(17) == "17"
```
:::::::::
::::::::::::

::: {}
test coverage: 100%
:::

::: notes
:::

# a

~~~~ {#mycode .haskell .numberLines startFrom="100"}
qsort []     = []
qsort (x:xs) = qsort (filter (< x) xs) ++ [x] ++
               qsort (filter (>= x) xs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
