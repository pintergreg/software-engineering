---
title: week 5 summary 
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


# gang of four (GoF) design patterns

- GoF: Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
- 23 common software design patterns
    - published in "Design Patterns: Elements of Reusable Object-Oriented Software" (1994) [@gamma1994design]
- provides solutions to common design problems
- categorized into three main groups
    1. creational
    2. structural
    3. behavioral

::: {.text-smaller}
read about the design patterns in details, for example at [refactoring.guru](https://refactoring.guru/design-patterns/catalog)
:::


## GoF design patterns in functional programming

| OO pattern        | FP pattern |
|-------------------|------------|
| factory pattern   | function   |
| strategy pattern  | function   |
| decorator pattern | function   |
| visitor pattern   | function   |
| ...               | ...        |

Peter Norvig [demonstrated](http://www.norvig.com/design-patterns/) that 16 out of the 23 patterns are simplified or eliminated by language features in Lisp or Dylan (1998) [@norvig1998design]

[more about](https://fsharpforfunandprofit.com/fppatterns/) it from Scott Wlaschin [@wlaschin2014functional]


# SOLID principles

[SOLID is a mnemonic acronym for five design principles intended to make object-oriented designs more understandable, flexible, and maintainable [@enwiki:1237710587]]{.text-smaller}

single responsibility principle
~ [a class should do one thing and therefore it should have only a single reason to change]{.text-smaller}

open-closed principle
~ [classes should be open for extension and closed to modification]{.text-smaller}

Liskov substitution principle
~ [if class A is a subtype of class B, B should be able to replaced with A without disrupting the behavior of the program]{.text-smaller}

interface segregation principle
~ [many client-specific interfaces are better than one general-purpose interface. Clients should not be forced to implement a function they do no need.]{.text-smaller}

dependency inversion principle
~ [modules should depend upon interfaces or abstract classes, not concrete classes. It's an inversion because implementations depend upon abstractions and not the other way round]{.text-smaller}

::: {.text-smaller}
based on [@millington2019solid], [@oloruntoba2024solid]
:::


# coupling

:::::::::::: {.columns}
::::::::: {.column width="55%" .mt-5}
- the degree of interdependence between software modules
- coupling is usually contrasted with cohesion
    - low coupling often correlates with high cohesion, and vice versa
:::::::::
::::::::: {.column width="45%"}
![from [Wikimedia](https://commons.wikimedia.org/wiki/File:CouplingVsCohesion.svg) | public domain](figures/borrowed/CouplingVsCohesion.svg)
:::::::::
::::::::::::

::: {.text-smaller .mt-2}
source [Wikipedia](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) [@enwiki:1245630908]
:::


# architectural styles / topologies

:::::::::::: {.columns}
::::::::: {.column width="33%"}
![](figures/server_client.drawio.svg){width=250}

![](figures/message_bus.drawio.svg){width=250}

:::::::::
::::::::: {.column width="33%"}
![](figures/layered_4.drawio.svg){width=200}

:::::::::
::::::::: {.column width="33%"}
![](figures/onion.drawio.svg){width=250}

![](figures/hexagonal_extend.drawio.svg){width=250}

:::::::::
::::::::::::


# architectural patterns

:::::::::::: {.columns}
::::::::: {.column width="30%"}
![MVC](figures/mvc.drawio.svg){width=300}

:::{.text-smaller}
ASP.NET, Django (Python), Ruby on Rails, Laravel (PHP)
:::
:::::::::
::::::::: {.column width="30%"}
![MVP](figures/mvp.drawio.svg){width=300}

:::{.text-smaller}
Windows Forms, Java Swing
:::
:::::::::
::::::::: {.column width="30%"}
![MVVM](figures/mvvm.drawio.svg){width=300}

:::{.text-smaller}
WPF, AngularJS
:::
:::::::::
::::::::::::

::: {.text-smaller .mt-2}
- view is responsible for rendering UI
- controller responds to the user input (in MVC) and performs interactions on the data model
- model is responsible for managing the data
:::


# references

::: {#refs}
:::
