---
title: Scrum
author: Gergő Pintér
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
slideNumber: "true"
showSlideNumber: "print"
---

this presentation is based on The Scrum Guide (2020)<br>by Ken Schwaber and Jeff Sutherland [@schwaber2020scrum]

available from [scrumguides.org](https://scrumguides.org/) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

or download directly [from here](../resources/2020-Scrum-Guide-US.pdf)

# what is Scrum?

Scrum is a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems.

Scrum employs an iterative, incremental approach to optimize predictability and to control risk.
Scrum engages groups of people who collectively have all the skills and expertise to do the work and share or acquire such skills as needed.

## Scrum in a nutshell

::: {.text-smaller}
scrum requires a scrum master to foster an environment where:

1. a product owner orders the work for a complex problem into a product backlog
2. the scrum team turns a selection of the work into an increment of value during a sprint
3. the scrum team and its stakeholders inspect the results and adjust for the next sprint
4. repeat

:::

![](figures/scrum_sprint.drawio.png){height=300}

# Scrum team

- the Scrum team consists of
    - one scrum master, 
    - one product owner, 
    - and developers 
- there are no sub-teams or hierarchies

## size of a Scrum team

- small enough to remain nimble and large enough to complete work in a sprint
    - typically 10 or fewer people
    - smaller teams communicate better and are more productive
- if a team becomes too large, they should consider reorganizing into multiple cohesive scrum teams
    - each focused on the same product
    - therefore, they should share the same product goal, product backlog, and product owner


## SCRUM teams are cross-functional

![](figures/cross_functional.drawio.svg){width=500}

- the members have all the skills necessary to create value each sprint
- they are also self-managing, meaning they internally decide who does what, when, and how

## developers

## definition of done

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- checklist
- helps to track the progress of a task
     ![](figures/gitea_dod.png)
- a task is done, if every element of the checklist is done

:::::::::
::::::::: {.column width="50%"}
course definition of done:

- [x] attended the classes
- [x] homeworks completed
- [x] midterm exam passed
- [x] project work completed

:::::::::
::::::::::::

## product owner

## Scrum master



# team size

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/team_intercommunication_4.drawio.svg){width=350}
:::::::::
::::::::: {.column width="50%" .center-content}
::: {.fragment .text-size-5}
$\frac{4(4 − 1)}{2} = 6$
:::
:::::::::
::::::::::::

## team size

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/team_intercommunication_5.drawio.svg){width=350}
:::::::::
::::::::: {.column width="50%" .center-content}
:::::: {.r-stack}
::: {.text-size-5 .fragment .fade-out data-fragment-index="1"}
$\frac{5(5 − 1)}{2} = 10$
:::

::: {.fragment .text-size-5 data-fragment-index="1"}
$\frac{n(n − 1)}{2}$
:::
::::::
:::::::::
::::::::::::


## team size {visibility=hidden}

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/team_intercommunication_4.drawio.svg){width=350}
:::::::::
::::::::: {.column width="50%" .fragment}
![](figures/team_intercommunication_5.drawio.svg){width=350}
:::::::::
::::::::::::

# man-month

:::  {.text-size-3}
Man-month is a hypothetical unit of work representing the work done by one person in one month.
:::

# Brooks's law

> Adding manpower to a late software project makes it later.

. . .

Assigning more programmers to a project running behind schedule will make it even later.
This is because the **time required for the new programmers to learn about the project** and the **increased communication overhead** will consume an ever-increasing quantity of available time [@enwiki:1233664045].

::: notes
Furthermore, in many cases the new programmer cannot just learn about the project on their own, but someone should mentor them.
This may be considered as a part of the communication overhead, it is an important aspect.
:::

## what can be done?



# references

::: {#refs}
:::
