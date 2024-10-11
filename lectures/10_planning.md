---
title: implementation planning
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

# implementation planning

1. define goals
    - practically done with requirement analysis 
2. conduct research
    - partially done at the requirement elicitation phase
3. map out risks
4. schedule milestones
5. assign responsibilities and tasks
6. allocate resources

::: {.text-smaller}
based on [What is an implementation plan? 6 steps to create one](https://asana.com/resources/implementation-plan) [@asana2024what]
:::


# conduct research

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- during the requirement analysis some data was already collected
    - regarding functional and non-functional requirements
    - interviews, questionnaires, telemetry, etc.
- some research may be needed to select the tools and frameworks during the implementation
    - do some experiments with different libraries

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/chemist-conducting-experiments.svg){height=300}
:::::::::
::::::::::::


## experiments


## fail fast


## minimal working example

eliminate variables

https://stackoverflow.com/help/minimal-reproducible-example


# identify risks


## risk register


## Rust-GCC example

| Risk | Impact<br>(1-3) | Likelihood<br>(0-10) | Risk<br>(I * L) | Mitigation |
|-----------|---:|---:|---:|----------------|
| Rust Language Changes | 2 | 7 | 14 | Target a specific Rustc version |
| Missing GCC 13 upstream window | 1 | 6 | 6 | Merge in GCC 14 and be proactive about reviews |

::: {.text-smaller}
source: [Rust-GCC / Reporting](https://github.com/Rust-GCC/Reporting/blob/main/2022/2022-04-11-report.org)
:::


# risk storming

- visual and collaborative risk identification technique
- created by Simon Brown
    - author of C4 model

1. draw some software architecture diagrams
    - to show what you're planning to build or change, ideally at different levels of abstraction
    - ideally C4
2. identify the risks individually 
    - gather people in front of the diagrams, 
    - ask them to identify what they personally perceive to be risky
    - write a summary of each risk on a separate sticky note,
    - colour coded to represent low, medium, and high priority risks
    - timebox this exercise (e.g. 10 minutes), 
    - do it in silence

::: {.text-smaller}
this chapter is based on [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


# schedule milestones

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- visualize project milestones
    - Gantt chart
- keep the entire team posted
- pay attention to holidays
    - multiple countries in the case of an international team
- things won't go as planned, so
    - add safety margin (wiggle room)
    - e.g., an extra week before deadline for fixing bugs

:::::::::
::::::::: {.column width="40%"}
![Gantt chart from [Wikipedia](https://commons.wikimedia.org/wiki/File:GanttChartAnatomy.svg) <br> public domain](figures/borrowed/GanttChartAnatomy.svg)

:::::::::
::::::::::::


# assign responsibilities and tasks

- every task you want to make done should have exactly one person responsible
    - no responsible
- define area of responsibility
    - a task (in scrum terminology) should have definition of done, which specifies it
- everyone needs to know what other people are responsible for
    - scrum/kanban board can visualize it
    - issue/ticket trackers can also work
- at the end of a sprint planning, every task in the sprint backlog should have an assignee

:::{.text-smaller}
source: [@paquet2019when]
:::


# allocate resources: man-month

::: {.text-size-2 .mt-5}
Man-month is a hypothetical unit of work representing the work done by one person in one month.
:::

-- Fred Brooks: The Mythical Man-Month [@brooks1974mythical]


## estimating time requirement of a task

- scrum (and agile in general) does not say anything about *how* to estimate time
- seemingly simple task can be difficult

Brooks' law says that it is impossible to measure useful work in man-months.


## poker planning

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- is a consensus-based, gamified technique for estimation (in agile)
- members of the group make estimates by playing numbered cards face-down to the table, instead of speaking them aloud
- estimates are then discussed and high and low estimates are explained
    - repeat until estimates converge
- by hiding the figures, the group can avoid the cognitive bias of anchoring
    - where the first number spoken aloud sets a precedent for subsequent estimates

:::::::::
::::::::: {.column width="40%"}
![by [Hkniberg ](https://en.wikipedia.org/wiki/File:CrispPlanningPokerDeck.jpg) | public domain](figures/borrowed/CrispPlanningPokerDeck.jpg)

::: {.text-smaller .mt-1}
optional cards

:    - ? means *unsure*
     - &#9749; mean "I need a break"
<!--- card values: 0, ½, 1, 2, 3, 5, 8, 13, 20, 40, 100, and optionally a ? (unsure)
- Fibonacci sequence: 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89-->
:::
:::::::::
::::::::::::

::: {.text-smaller}
source: [@enwiki:1243064642]
:::


## Brooks's law

> Adding manpower to a late software project makes it later.

::: {.fragment}
Assigning more programmers to a project running behind schedule will make it even later.
This is because the **time required for the new programmers to learn about the project** and the **increased communication overhead** will consume an ever-increasing quantity of available time [@enwiki:1233664045].
:::

::: notes
Furthermore, in many cases the new programmer cannot just learn about the project on their own, but someone should mentor them.
This may be considered as a part of the communication overhead, it is an important aspect.
:::

<!-- ## what can be done? -->



# quality - time - cost

![](figures/quality_time_cost.drawio.svg){height=375}


# references

::: {#refs}
:::
