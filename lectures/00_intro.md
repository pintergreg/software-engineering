---
title: software engineering
author: Gergő Pintér
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
    data-background-image: assets/corvinus_neti_white.svg
    data-background-size: 23vw
    data-background-position: 1.25rem calc(100% - 1.25rem)
slideNumber: "true"
showSlideNumber: "print"
---

# schedule

| week | date       | lecture                          | practical class |
|-----:|:----------:|:--------------------------------:|:---------------:|
|    1 | 2024-09-10 | software development life cycles | SCRUM           |
|    2 | 2024-09-17 | software architecture            |
|    3 | 2024-09-24 | 
|    4 | 2024-10-01 |
|    5 | 2024-10-08 |
|    6 | 2024-10-15 |
|    7 | 2024-10-22 | 
|    9 | 2024-11-05 | 
|   10 | 2024-11-12 | 
|   11 | 2024-11-19 | 
|   12 | 2024-11-26 | 
|   13 | 2024-12-03 | 

# materials

- hangout, presentation website introduction
- also, moodle?


# program vs. software

:::::::::::: {.columns}
::::::::: {.column width="75%"}
> A computer program is a sequence or set of instructions in a programming language for a computer to execute.
> It is one component of software, which also includes documentation and other intangible components.
>
> ISO/IEC 2382:2015 via Wikipedia [@enwiki:1233276268]

:::::::::
::::::::: {.column width="25%"}
![](figures/program_software_product.drawio.svg)

:::::::::
::::::::::::


## program is like a recipe

:::::::::::: {.columns}
::::::::: {.column width="50%"}
There is an metaphor saying that a program is like a recipe.

The computer follows the instructions of a program as the cook follows the instruction in a recipe.

Consequently programming is like a creating a recipe.

:::::::::
::::::::: {.column width="50%" .fragment}

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("" + "FizzBuzz")
    elif i % 3 == 0:
        print("" + "Fizz")
    elif i % 5 == 0:
        print("" + "Buzz")
    else:
        print(i)
```

:::::::::
::::::::::::

::: notes
It is easy to read this code snippet and figure out what it does, but constructing an algorithm might be more complicated.

> Writing a computer program requires a nuanced understanding of the problem being solved by the computer program, pros and cons of various approaches, etc.
> It also requires the knowledge and expertise to describe those steps in a manner amenable to execution by a computer.
>
> [Jeff Rabinowitz](https://justabloginthepark.com/2016/01/09/how-programming-is-like-cooking/)
:::


# software development is like building a house

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- the software development is often compared to house building
    - which is more like a sequential process
- after the planning (including building permit, budget, etc.), the foundation is built first, then walls and the roof
    - these phases cannot be swapped
- after the construction is finished, the contractor leaves the site
:::::::::
::::::::: {.column width="35%"}
![<span class="text-smaller">[Wikimedia](https://commons.wikimedia.org/wiki/File:Sample_Floorplan.jpg) | public domain </span>](figures/sample_floorplan.jpg)

:::::::::
::::::::::::

::: {.fragment .text-size-3}
maintenance?
:::

## software development *not* is like building a house

- in software development you can start with the door of the second floor bathroom
- the size of a room can be changed during the construction -- even several times

. . .

a software does not have to obey the laws of physics


# software development is like gardening

:::::::::::: {.columns}
::::::::: {.column width="55%"}
- a garden needs to be taken care of constantly
- without attention the garden will decay
<!--     - and the code rots -->
- external factors like weather, pests, weeds can influence the garden
:::::::::
::::::::: {.column width="45%"}
- maintenance is part of software development
- code rots
- change in user requirements, but importantly the external dependencies such as frameworks, libraries, etc. can affect the software
:::::::::
::::::::::::

::: {.text-smaller}
based on Software Architecture Metaphors by Lisa Stähli [@stahli2021software]
:::

::: notes
Another famous metaphor is the gardening.
The most important aspect of the gardening is that a garden needs to be taken care of constantly.
:::

## software development is like gardening II

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- gardeners has a set of tools, selected for the characteristics of the garden and the gardener
- a beautiful garden is a piece of art
    - which can serve a function, like producing vegetables or fruits
:::::::::
::::::::: {.column width="50%"}
- software developer also uses tools chosen according to the environment and type of software 
<!--     -  e.g., to automate processes -->
- software is a piece of art, e.g., the UI has to be not just functional, but aesthetic and ergonomic
    - software code/design is also a piece of art; see software craftmanship (later)
:::::::::
::::::::::::

::: {.text-smaller}
based on Software Architecture Metaphors by Lisa Stähli [@stahli2021software]
:::

# references
