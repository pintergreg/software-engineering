---
title: software engineering
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
---

# schedule {visibility=hidden}

| week | date       | lecture                           | practical class    |
|-----:|:----------:|:---------------------------------:|:------------------:|
|    1 | 2024-09-10 | intro, software architecture      | SDLC               |
|    2 | 2024-09-17 | SCRUM                             | kanban             |
|    3 | 2024-09-24 | requirement analysis              | user story map     |
|    4 | 2024-10-01 | UML, C4                           | UML in practice    |
|    5 | 2024-10-08 | "communication", clean code       | case studies       |
|    6 | 2024-10-15 | legacy code, review               | "coding" example   |
|    7 | 2024-10-22 | testing, review                   | project assignment |
|    8 | 2024-10-29 | school holiday                    |                    |
|    9 | 2024-11-05 | dependency management             | VCS basics         |
|   10 | 2024-11-12 | CI, automatization, devops        | project workshop   |
|   11 | 2024-11-19 | project workshop                  | project workshop   |
|   12 | 2024-11-26 | summary, course feedback          | project workshop   |
|   13 | 2024-12-03 | midterm                           | project demo       |
|   14 | 2024-12-10 | no planned lecture                |                    |


# schedule {.exclude-header}

::: {.exclude}
| week | date       | lecture                           | practical class    |
|-----:|:----------:|:---------------------------------:|:------------------:|
|    1 | 2024-09-10 | intro, software architecture      | SDLC               |
|    2 | 2024-09-17 | SCRUM                             | kanban             |
|    3 | 2024-09-24 | requirement analysis              | user story map     |
|    4 | 2024-10-01 | UML, C4                           | UML in practice    |
|    5 | 2024-10-08 | "communication", clean code       | case studies       |
|    6 | 2024-10-15 | legacy code, review               | "coding" example   |
|    7 | 2024-10-22 | testing, review                   | project assignment |

:::

## schedule {.exclude-header}

::: {.exclude}
| week | date       | lecture                           | practical class    |
|-----:|:----------:|:---------------------------------:|:------------------:|
|    8 | 2024-10-29 | school holiday                    |                    |
|    9 | 2024-11-05 | dependency management             | VCS basics         |
|   10 | 2024-11-12 | CI, automatization, devops        | project workshop   |
|   11 | 2024-11-19 | project workshop                  | project workshop   |
|   12 | 2024-11-26 | summary, course feedback          | project workshop   |
|   13 | 2024-12-03 | midterm                           | project demo       |
|   14 | 2024-12-10 | no planned lecture                |                    |

:::

# materials {visibility=hidden .exclude}

- hangout, presentation website introduction

# tools

- diagram drawing: 
    - [draw.io](https://app.diagrams.net/)
    - [plantuml](https://plantuml.com/)
- whiteboard:
    - [excalidraw](https://excalidraw.com/)
- code hosting / task management
    - [GitHub](https://github.com/)
    
::: notes
:::
    
# program vs. software

:::::::::::: {.columns .fragment}
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
There is a metaphor saying that a program is like a recipe.

The computer follows the instructions of a program as the cook follows the instruction in a recipe.

Consequently programming is like creating a recipe.

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

It contains a loop going from 1 to 100 (ranges are not closed in Python, so 101 is excluded and the range step is 1 by default).
If the loop variable is dividable by 15, "FizzBuzz" is printed to the screen.
If it is only dividable by 3 "Fizz" is printed, if only by 5 "Buzz" is printed.
In any other cases the number id printed.


> Writing a computer program requires a nuanced understanding of the problem being solved by the computer program, pros and cons of various approaches, etc.
> It also requires the knowledge and expertise to describe those steps in a manner amenable to execution by a computer.
>
> [Jeff Rabinowitz](https://justabloginthepark.com/2016/01/09/how-programming-is-like-cooking/)

:::


# programming vs. software development

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/software_development.drawio.svg){width=400}

:::::::::
::::::::: {.column width="50%" .mt-5 .column-align-left}
::: {.fragment}
- does that mean a program is not 
    - planned
    - documented
    - tested
    - verified?
:::
::: {.fragment}
- the main difference is the formality of the process
    - which correlates the complexity of the project
:::

:::::::::
::::::::::::

::: notes
A program code is only a part of a software.
Programming is more or less a synonym to coding.

As a software is more than just the code, software development is more than just coding/programming.
The work is planned, documented, tested, verified, and framed by a process.

If programming is like creating a recipe, software development is more like running a restaurant.
One should come up with recipes, cook the food, but the restaurant also needs constant ingredient logistics and preparation, food serving, marketing, cleaning etc.

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
![[Wikimedia](https://commons.wikimedia.org/wiki/File:Sample_Floorplan.jpg) | public domain](figures/sample_floorplan.jpg)

:::::::::
::::::::::::

::: {.fragment .text-size-3}
maintenance?
:::

## software development *not* is like building a house

a software does not have to obey the laws of physics

- in software development you can start with the door of the second floor bathroom
- the size of a room can be changed during the construction -- even several times


# software development is like gardening

:::::::::::: {.columns .fragment}
::::::::: {.column width="55%"}
- a garden needs to be taken care of constantly
- without attention the garden will decay
<!-- - external factors like weather, pests, weeds can influence the garden -->
:::::::::
::::::::: {.column width="45%"}
- maintenance is part of software development
- software rots
<!-- - change in user requirements, but importantly the external dependencies such as frameworks, libraries, etc. can affect the software -->
:::::::::
::::::::::::

::: {.text-smaller .mt-5}
based on Software Architecture Metaphors by Lisa Stähli [@stahli2021software]
:::

::: notes
Another famous metaphor is the gardening.
The most important aspect of the gardening is that a garden needs to be taken care of constantly.
Without attention the garden will decay, which is also true for the software; the software can rot.

There are two types of software rot: dormant rot and active rot.
:::

## what is software rot?

::: {.wide-quote}
> Software rot (or software entropy) is the degradation, deterioration, or loss of the use or performance of software over time [@enwiki:1236668404]. 

:::

:::::::::::: {.columns .mt-2}
::::::::: {.column width="50%"}
**dormant rot**: the software in question is not changed, but as the environment evolves, it eventually becomes dysfunctional

:::::::::
::::::::: {.column width="50%" .fragment}
![Muni metro San Francisco<br>photo by [Albert](https://www.flickr.com/photos/24208255@N07/2751036689/) [CC BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/)](figures/borrowed/muni_metro.jpg)

:::::::::
::::::::::::

::: notes
Environment change can be either software or hardware.
The operating system, a software framework or even a hardware can be outdated to

The photo shows the San Fransico Muni metro, which still uses floppy disks to load its Automatic Train Control System every morning.
It is planned to replace by the end of the decade.
The system works without any problems, but the risk of failure is getting higher. [@harding2024san]

:::

## what is software rot? {.exclude-header}

:::::::::::: {.columns}
::::::::: {.column width="50%"}
**active rot**

- the software has undergone constant modifications but gradually loses its integrity
- the constant updates / bug fixing can lead to an evolution process,
    - which makes the program deviate from its original design, 
    - even introducing newer bugs

:::::::::
::::::::: {.column width="50%"}
![Randall Munroe | [CC BY-NC 2.5](https://creativecommons.org/licenses/by-nc/2.5/)](figures/borrowed/code_lifespan_2x.png)

:::::::::
::::::::::::

::: notes
It is said that nothing is more permanent than a temporary fix.
A quick fix often ignores the architectural design, not documented properly, thus contributes to the software rot.

A change in a production system should be properly planned in every possible details.
For example, because it can have side effects, or can affect the architecture.
Also, the documentation needs to be updated. Both documentations actually since there is a development documentation, that should contain information about the system for the developers and a user documentation (manual) for the operators of the system.

:::

## software development is like gardening - cont.

:::::::::::: {.columns}
::::::::: {.column width="55%"}
<!-- - a garden needs to be taken care of constantly -->
<!-- - without attention the garden will decay -->
- external factors like weather, pests, weeds can influence the garden
:::::::::
::::::::: {.column width="45%"}
<!-- - maintenance is part of software development -->
<!-- - software rots -->
- change in user requirements, and the external dependencies such as frameworks, libraries, etc. can affect the software
:::::::::
::::::::::::

::: {.text-smaller .mt-5}
based on Software Architecture Metaphors by Lisa Stähli [@stahli2021software]
:::

::: notes
Another similarity to gardening is that external factors can influence the software.
:::

## software development is like gardening - cont. {.exclude-header}

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- gardeners has a set of tools, selected for the characteristics of the garden and the gardener
- a beautiful garden is a piece of art
    - which can also serve a function, like producing vegetables / fruits
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

# software craftmanship

::: {.text-smaller}
As aspiring Software Craftsmen we are raising the bar of professional software development by practicing it and helping others learn the craft. Through this work we have come to value:
:::

- Not only working software, but also **well-crafted software**
- Not only responding to change, but also **steadily adding value**
- Not only individuals and interactions, but also **a community of professionals**
- Not only customer collaboration, but also **productive partnerships**

::: {.text-smaller .mt-4}
That is, in pursuit of the items on the left we have found the items on the right to be indispensable.
:::

::: {.text-size-1}
© 2009, the undersigned.
This statement may be freely copied in any form, but only in its entirety through this notice.
:::

::: notes
From [/manifesto.softwarecraftsmanship.org](https://manifesto.softwarecraftsmanship.org/).
:::

# software growth

24 million lines of code -- operational and support -- needed for the F-35 to be fully operational

::: notes

:::

## the more, the better?

> if we wish to count lines of code, we should not regard them as "lines produced" but as "lines spent"
>
> E. W. Dijkstra [EWD 1036](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD10xx/EWD1036.html)

::: {.fragment}
> Every line of code written comes at a price: maintenance. To avoid paying for a lot of code, we build reusable software. The problem with code re-use is that it gets in the way of changing your mind later on.
>
> tef - [Write code that is easy to delete, not easy to extend](https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to)

:::

::: notes
Some people may consider the code as the product.
In this regard, more lines of code means more product.
If you write more code you work better, which is not true.
You should work smarter, not harder.

As Dijkstra said, lines should considered an expense, which you want to minimize, not maximize.
More code means more plants in your garden to take care of.
It requires more resources, but at the same time it also increases complexity.
:::

## keep it simple

> A designer knows he has achieved perfection not when there is nothing left to add, but when there is nothing left to take away.
>
> -- [Antoine de Saint-Exupéry](https://en.wikiquote.org/wiki/Antoine_de_Saint_Exup%C3%A9ry)

::: {.fragment}
- KISS, an acronym for "Keep it simple, stupid!"
    - a variations: keep it stupidly simple
    - the term was popular in the 70s
:::

::: notes
<!-- According to Saint-Exupéry (who was the author of The Little Prince by the way) -->

The design, the code should be kept as simple as possible.
When you want to simplify a design, keep only those parts that are absolutely necessary to get the job done.
:::


## Linux 5.8 -- 800,000 new lines of code

::: {.text-smaller}
> [Linux Torvalds](https://lore.kernel.org/lkml/CAHk-=whfuea587g8rh2DeLFFGYxiVuh-bzq22osJwz3q4SOfmA@mail.gmail.com/): despite not really having any single thing that stands out... 5.8 looks to be one of our biggest releases of all time

:::

- how is it manageable?
    - process
    - version control
- each change must do only one thing
    - proper documentation
- changes cannot break the software
    - rigorous and automated testing
    
# version control

:::::::::::: {.columns}
::::::::: {.column width="55%"}
- version control (a.k.a. revision control) is system for recording and managing changes made in files
- commonly used to manage source code
    - however, it can be used to tracking changes to any kind of files
- people often employ their own version control system, without realising it
:::::::::
::::::::: {.column width="45%"}
![Simon Mutch | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)](figures/borrowed/custom_version_control.png)

:::::::::
::::::::::::

::: {.text-smaller .mt-3}
based on Simon Mutch's [Version Control materials](http://smutch.github.io/VersionControlTutorial/pages/0-intro.html)
:::

::: notes
[Simon Mutch | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en) | [source](https://gist.github.com/smutch/4951871)](figures/borrowed/vc-xkcd.jpg)

:::

## why you should use version control (for everything)

::: {.wide-quote}
> In practice, everything that has been created manually should be put in version control, including programs, original field observations, and the source files for papers.
>
> -- Best Practices for Scientific Computing; Wilson et al. 2012 ([arXiv:1210.0530](https://arxiv.org/abs/1210.0530))

:::

::: {.mt-5}
this presentation is under version control as well
:::

::: notes
Many services have some kind of version control built in. 
For example Google Docs or Microsoft Word also provides some level of version control.
:::

# project complexity

:::::: {.r-stack}
::: {.exclude}
![](figures/complex_projects.drawio.cropped_no_people.svg){width=55%}
:::
::: {.fragment}
![](figures/complex_projects.drawio.cropped.svg){width=55%}
:::
::::::

::: notes
:::

# what is software architecture?

> "Architecture" is a term that lots of people try to define, with little agreement. There are two common elements: One is the highest-level breakdown of a system into its parts; the other, decisions that are hard to change.
>
> -- Martin Fowler - Patterns of Enterprise Application Architecture

##

> In most successful software projects, the expert developers working on that project have a shared understanding of the system design. This **shared understanding** is called ‘architecture’. This understanding includes how the system is divided into components and how the components interact through interfaces. These components are usually composed of smaller components, but the architecture only includes the components  and interfaces that are understood by all the developers.
> 
> Ralph Johnson, XP mailing list

## 

> All architecture is design but not all design is architecture. Architecture represents the significant **design decisions** that shape a system, where significant is measured by cost of change.
>
> -- Grady Booch


# Topologies

[Introduction to Software Architecture](https://www.codeproject.com/Articles/1064240/Introduction-to-Software-Architecture)

## Layered Architechture

![](http://1.bp.blogspot.com/-TbA8p6DWYJc/Uc0zYwSG_iI/AAAAAAAAAag/cPytbL6oeM4/s800/layered.png)

- [Layered Architecture: Introduction](http://serena-yeoh.blogspot.com/2013/06/layered-architecture-for-net.html)
- [Layered Architecture: Component Interactions](http://serena-yeoh.blogspot.com/2014/01/layered-architecture-components.html)

## Message Bus Architecture

![](https://www.codeproject.com/KB/architecture/1064240/message-bus.gif)


## Server-Client Architecture

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Client-server-model.svg/1200px-Client-server-model.svg.png)

<!--# project management triangle

![](figures/quality_time_cost.drawio.svg){width=60%}

::: notes
:::-->

# references

::: {#refs}
:::
