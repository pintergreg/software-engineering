---
title: Scrum
author: Gergő Pintér
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
slideNumber: "true"
showSlideNumber: "print"
---

this presentation is based on The Scrum Guide (2020)<br>by Ken Schwaber and Jeff Sutherland [@schwaber2020scrum]

available from [scrumguides.org](https://scrumguides.org/) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

or download directly [from here](../resources/2020-Scrum-Guide-US.pdf)

# what is scrum?

Scrum is a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems.

Scrum employs an iterative, incremental approach to optimize predictability and to control risk.
Scrum engages groups of people who collectively have all the skills and expertise to do the work and share or acquire such skills as needed.

## scrum in a nutshell

::: {.text-smaller}
scrum requires a scrum master to foster an environment where:

1. a product owner orders the work for a complex problem into a product backlog
2. the scrum team turns a selection of the work into an increment of value during a sprint
3. the scrum team and its stakeholders inspect the results and adjust for the next sprint
4. repeat

:::

![](figures/scrum_sprint.drawio.svg){height=300}

# scrum team

- the Scrum team consists of
    - one scrum master, 
    - one product owner, 
    - and developers 
- there are no sub-teams or hierarchies

## size of a scrum team

- small enough to remain nimble and large enough to complete work in a sprint
    - typically 10 or fewer people
    - smaller teams communicate better and are more productive
- if a team becomes too large, they should consider reorganizing into multiple cohesive scrum teams
    - each focused on the same product
    - therefore, they should share the same product goal, product backlog, and product owner


## scrum teams are cross-functional

![](figures/cross_functional.drawio.svg){width=500}

- the members have all the skills necessary to create value each sprint
- they are also self-managing, meaning they internally decide who does what, when, and how

## developers

- committed to creating any aspect of a usable increment each sprint
- the specific skills needed by the developers are often broad and will vary with the domain of work
- developers are accountable for
    - creating a plan for the sprint, the sprint backlog,
    - instilling quality by adhering to a definition of done,
    - adapting their plan each day toward the sprint goal, and
    - holding each other accountable as professionals


## definition of done

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- checklist
- defines steps to complete the task
- helps to track the progress of a task
     ![](figures/gitea_dod.png)
- a task is done, if every element of the checklist is done

:::::::::
::::::::: {.column width="50%"}
course definition of done:

- [x] attended all classes
- [x] homeworks completed
- [x] midterm exam passed
- [x] project work completed

:::::::::
::::::::::::

## product owner

- accountable for maximizing the value of the product resulting from the work of the scrum team
- also accountable for effective product backlog management, which includes:
    - developing and explicitly communicating the product goal,
    - creating and clearly communicating product backlog items,
    - ordering product backlog items, and
    - ensuring that the product backlog is transparent, visible and understood

The product owner may do the above work or may delegate the responsibility to others. Regardless, the product owner remains accountable.

## scrum master

- accountable for 
    - establishing scrum as defined in the Scrum Guide
        - by helping everyone understand the theory and practice, both within the scrum team and the organization
    - for the scrum team's effectiveness
        - by enabling the scrum team to improve its practices, within the scrum framework

::: notes
You can watch a parody about a the scrum master role: [Scrum Master - Funny movie about The Power of Scrum](https://www.youtube.com/watch?v=P6v-I9VvTq4) (5m 23s)
:::

## scrum master serves the scrum team

- coaching the team members in self-management and cross-functionality,
- helping the scrum team focus on creating high-value increments that meet the definition of done,
- causing the removal of impediments to the scrum team's progress, and
- ensuring that all scrum events take place and are positive, productive, and kept within the timebox

## scrum master serves the product owner

- helping find techniques for effective product goal definition and product backlog management,
- helping the scrum team understand the need for clear and concise product backlog items,
- helping establish empirical product planning for a complex environment, and
- facilitating stakeholder collaboration as requested or needed

## scrum master serves the organization

- leading, training, and coaching the organization in its scrum adoption,
- planning and advising scrum implementations within the organization,
- helping employees and stakeholders understand and enact an empirical approach for complex work, and
- removing barriers between stakeholders and scrum teams


# scrum events

:::::::::::: {.columns}
::::::::: {.column width="40%"}
- sprint
- sprint planning
- daily scrum
- sprint review
- sprint retrospective

:::::::::
::::::::: {.column width="60%"}

![](figures/scrum_events.drawio.svg)
:::::::::
::::::::::::

::: notes
Besides people there are events in scrum.
:::

# sprint

> Sprints are the heartbeat of Scrum, where ideas are turned into value.

- fixed length events (maximum one month) to create consistency
- a new sprint starts immediately after the end of the previous

## during the sprint

- no changes are made that would endanger the sprint goal,
- quality does not decrease,
- the Product Backlog is refined as needed, and
- scope may be clarified and renegotiated with the product owner as more is learned

##

- a sprint could be cancelled if the sprint goal becomes obsolete
- only the Product Owner has the authority to cancel the sprint

# sprint planning

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

::: {.fragment}
Assigning more programmers to a project running behind schedule will make it even later.
This is because the **time required for the new programmers to learn about the project** and the **increased communication overhead** will consume an ever-increasing quantity of available time [@enwiki:1233664045].
:::

::: notes
Furthermore, in many cases the new programmer cannot just learn about the project on their own, but someone should mentor them.
This may be considered as a part of the communication overhead, it is an important aspect.
:::

## what can be done?



# references

::: {#refs}
:::
