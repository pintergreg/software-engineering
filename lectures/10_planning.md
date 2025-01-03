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


## learning could be a task

:::::::::::: {.columns}
::::::::: {.column width="50%" .mt-4}
- you may need to work a technology / framework / language that you are not familiar with
- or you just have to learn a new codebase
- calculate with learning during the planning

:::::::::
::::::::: {.column width="50%"}
![](figures/complex_projects.drawio.cropped_no_people.svg){height=400}

:::::::::
::::::::::::


## experiments

<!--:::::::::::: {.columns}
::::::::: {.column width="77%"}-->
- sometimes the task requires a step that you don't want to implement (again) but use an existing framework instead
    - e.g., crop a profile picture to a standard size, while keeping the face in focus
- then you may want to search for a suitable framework and do some research about how to use it


<!-- - this may help to measure the  -->
<!--:::::::::
::::::::: {.column width="23%"}
![](figures/cropping.drawio.svg){width=250}

:::::::::
::::::::::::-->

<!-- - do not invent the wheel again, use an existing framework / method -->


## fail fast

~ indirect proof, proof of contradiction

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- the requirements are known
- try to eliminate candidates as soon as possible
    - unmaintained
    - cannot handle certain file formats
    - target language / version is not supported
- then move on the next one
- document findings (~ decision records)

:::::::::
::::::::: {.column width="40%"}
![screenshot of [leblancfg/autocrop](https://github.com/leblancfg/autocrop) GitHub project page](figures/autocrop.png){width=300}

:::::::::
::::::::::::

::: notes
https://en.wikipedia.org/wiki/Fail_fast_(business)
:::


## minimal workable example

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- when you have a promising candidate, write code to try it out in practice
- start new project<br>(for every candidate / experiment)
    - simple, clean
    - no interference, side effects
    - eliminate unknown variables
- document research findings (~ decision records)

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/developer-at-work.svg){width=250}
:::::::::
::::::::::::

::: {.text-smaller}
Stackoverflow guideline on [How to create a Minimal, Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example)
:::


# identify risks

a risk is a possibility that something bad can happen

- there is risk inherent with building any piece of software
- whether you're building a completely new greenfield project,
- or adding a new feature to an existing codebase
    - other parts cease to work
    - the new feature alienate users
    - data loss

::: {.text-smaller}
based on [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


## prioritize risks

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- often difficult to prioritise which risks you should take care of 
- one way to do this is to map risks to a matrix
- where you evaluate 
    - the probability: how likely is it that the risk will happen?
    - and the impact: what is the negative impact if the risk does occur?

:::::::::
::::::::: {.column width="40%"}
![](figures/borrowed/quantifying-risk-1.png){width=350}

:::::::::
::::::::::::

::: {.text-smaller}
from [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


## risk register

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="65%"}
- a risk register is a document used as a risk management tool 
- contains all identified risks with additional information
    - e.g., nature of the risk, probability, impact, reference and owner, mitigation measures
- it can be displayed as a table or as a scatterplot

:::::::::
::::::::: {.column width="35%"}
![by [Hou710](https://en.wikipedia.org/wiki/File:Hou710_RiskLog.svg) | [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.en) ](figures/borrowed/Risk Log - Party Example.svg){width=300}

:::::::::
::::::::::::

::: {.text-smaller .mt-4}
source [Wikipedia](https://en.wikipedia.org/wiki/Risk_register) [@enwiki:1245973868]
:::

<!--
## risk register - table

:::::::::::: {.columns}
::::::::: {.column width="40%"}
**common columns**

- category
- name
- responsible
- probability
- impact
- mitigation
- action by
- action when

:::::::::
::::::::: {.column width="60%"}
instance Toyota's risk register listed reputation risks caused by Prius' malfunctions but the company failed to take action
:::::::::
::::::::::::-->


## Rust-GCC example

common columns in table-based risk registers:
~ category, name, responsible, probability, impact, mitigation, action by, action when

::: {.mt-3}

| Risk | Impact<br>(1-3) | Likelihood<br>(0-10) | Risk<br>(I * L) | Mitigation |
|-----------|---:|---:|---:|----------------|
| Rust Language Changes | 2 | 7 | 14 | Target a specific Rustc version |
| Missing GCC 13 upstream window | 1 | 6 | 6 | Merge in GCC 14 and be proactive about reviews |

:::

::: {.text-smaller}
source: [Rust-GCC / Reporting](https://github.com/Rust-GCC/Reporting/blob/main/2022/2022-04-11-report.org)
:::


## risk storming

:::::::::::: {.columns}
::::::::: {.column width="70%"}
- visual and collaborative risk identification technique
- created by Simon Brown
    - author of C4 model
- motivation: often only one person evaluated risks
    - ~ four eyes see more than two
- risk evaluation should be collaborative activity

:::::::::
::::::::: {.column width="30%"}
![](figures/borrowed/risk-storming-1.png){width=250}

:::::::::
::::::::::::

::: {.text-smaller}
this chapter is based on [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::
    
## steps of risk storming

1. draw some software architecture diagrams
    - to show what you're planning to build, at different levels of abstraction
    - ideally C4
2. identify the risks individually 
    - gather people in front of the diagrams, 
    - ask them to identify what they personally perceive to be risky
    - write a summary of each risk on a separate sticky note,
    - colour coded to represent low, medium, and high priority risks
    - timebox this exercise (e.g. 10 minutes), 
    - do it in silence

::: {.text-smaller}
from [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::
    

## steps of risk storming

:::::::::::: {.columns}
::::::::: {.column width="60%"}
3. converge the risks on the diagrams
    - ask everyone to place their sticky notes onto the diagrams,
    - sticking them in close to the area where the risk has been identified
4. review and summarise the risks
    - review and summarise the output,
    - especially focusing on risks that only one person identified,
    - or risks where multiple people disgree on the priority

:::::::::
::::::::: {.column width="40%"}
![](figures/borrowed/risk-storming-2-cropped.png){width=250}

:::::::::
::::::::::::

::: {.text-smaller}
from [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


## mitigating risks

- risks are identified
    - and prioritized
- come up with mitigation strategies
    - either to prevent the risks from happening
    - or to take corrective action if the risk does occur
- focus on the highest priority ones first
<!--- mitigation strategies the are applicable depending upon the type of risk, including: 
    - education
    - writing code
    - re-work-->

::: {.text-smaller}
from [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


## mitigation strategies

- education
    - train the team, 
    - or hire new team members in areas where you lack experience
- writing code
    - create prototypes, proofs of concept, walking skeletons, etc. to mitigate technical risks by proving that something does or doesn't work
- re-work
    - change software architecture to remove or reduce the probability/impact of identified risks
        - e.g. removing single points of failure, 
    - upon change you should re-run the risk-storming process

::: {.text-smaller}
from [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


## walking skeleton

:::::::::::: {.columns}
::::::::: {.column width="70%"}

> A Walking Skeleton is a tiny implementation of the system that performs a small end-to-end function. It need not use the final architecture, but it should link together the main architectural components. The architecture and the functionality can then evolve in parallel.
>
> -- Alistair Cockburn

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/skeleton.svg){width=275}

:::::::::
::::::::::::

::: {.text-smaller}
it is a pattern intended to kick-start test driven development (later in the course)

via [wiki.c2.com](https://wiki.c2.com/?WalkingSkeleton)
:::


## risk storming example

![](figures/user_statistics/risk_storming.excalidraw.svg){height=550}


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

## ninety–ninety rule

> The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time.
>
> -- Tom Cargill, Bell Labs

::: {.text-smaller}
source: [@bentley1985programming]
:::

<!-- ![](figures/borrowed/estimating_time_2x.png){height=300} -->


# assign responsibilities and tasks

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- every task you want to make done should have exactly one person responsible
    - no assignee -- no one will do it
    - more than one -- "I though the other one was doing it"
- define area of responsibility
    - a task (as in scrum) should have definition of done, which specifies it
- everyone needs to know what other people are responsible for
    - scrum/kanban board can visualize it
    - issue/ticket trackers can also work

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/scrum-task-board.svg){width=250}

at the end of a sprint planning, every task in the sprint backlog should have an assignee

:::::::::
::::::::::::

:::{.text-smaller}
source: [@paquet2019when]
:::


## dependencies

:::::::::::: {.columns}
::::::::: {.column width="50%"}
:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
![](figures/team_dependency_1.drawio.svg){width=450}
:::
::: {.fragment .fade-in data-fragment-index=1}
![](figures/team_dependency_2.drawio.svg){width=450}
:::
::::::
:::::::::
::::::::: {.column width="50%" .fragment data-fragment-index=2}
![](figures/borrowed/CouplingVsCohesion.svg){width=350}

:::::::::
::::::::::::


# allocate resources

- resource is anything that is available with limits
    - money, time, personnel, equipment, etc.

![](figures/quality_time_cost.drawio.svg){height=250}


## man-month

::: {.text-size-2 .mt-1}
Man-month is a hypothetical unit of work representing the work done by one person in one month.
:::

-- Fred Brooks: The Mythical Man-Month [@brooks1974mythical]

::: {.fragment}
![how developers spend their time -- based on 295 responses | own figure based on data from [@grams2019how]](figures/how_developers_spend_time.svg){height=300}
:::


## estimating time requirement of a task

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- scrum (and agile in general) does not say anything about *how* to estimate (time)
- story points are often used instead
    - (relative) unit of effort required to fully implement a product backlog item
    - e.g., 1--5,
    - Fibonacci: 1, 2, 3, 5, 8, 13...
    - powers of 2: 1, 2, 4, 8, 16, 32...
:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/time-management.svg){width=250}

:::::::::
::::::::::::

::: {.text-smaller}
"Story points reward team members for solving problems based on difficulty, not time spent. This keeps team members focused on shipping value, not spending time [@radiganstory]."
:::


## planning poker

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- is a consensus-based, gamified technique for estimation (in agile)
- product owner reads the user story
- members of the group make estimates by playing numbered cards face-down to the table, instead of speaking them aloud
- estimates are then discussed and high and low estimates are explained
    - repeat until estimates converge
- by hiding the figures, the group can avoid the cognitive bias of anchoring
    - [where the first number spoken aloud sets a precedent for subsequent estimates]{.text-smaller}

:::::::::
::::::::: {.column width="40%"}
![by [Hkniberg ](https://en.wikipedia.org/wiki/File:CrispPlanningPokerDeck.jpg) | public domain](figures/borrowed/CrispPlanningPokerDeck.jpg)

::: {.text-smaller .mt-1}
zero: done | tiny: ½ |
easy: 1, 2, 3 |
medium: 5, 8, 13 |
large: 20, 40 | very&nbsp;large: 100 | &infin;: huge

optional cards

:    - ? means *unsure*
     - &#9749; means "I need a break"
<!--- card values: 0, ½, 1, 2, 3, 5, 8, 13, 20, 40, 100, and optionally a ? (unsure)
- Fibonacci sequence: 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89-->
:::
:::::::::
::::::::::::

::: {.text-smaller}
source: [@enwiki:1243064642]
:::


## estimation is guessing

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- many developers do not like to estimate
- seemingly simple task can turn out to be difficult
    - some difficulties are hard to foresee
    - bad architectural decision
        - ["Architecture is the decisions that you wish you could get right early in a project." -- Ralph Johnson]{.text-smaller}
- make educated guesses instead
    - measure
        - [burn down charts, cumulative flow diagram]{.text-smaller}
    - infer from previous tasks

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/thimbles-game.svg){width=250}

:::::::::
::::::::::::


## Brooks's law

> Adding manpower to a late software project makes it later.

:::::::::::: {.columns .column-gapless .fragment}
::::::::: {.column width="72%"}
Assigning more programmers to a project running behind schedule will make it even later.
This is because the **time required for the new programmers to learn about the project** and the **increased communication overhead** will consume an ever-increasing quantity of available time [@enwiki:1233664045].

:::::::::
::::::::: {.column width="28%"}
![](figures/communication_overhead_eq.svg){width=200}

:::::::::
::::::::::::

::: notes
Furthermore, in many cases the new programmer cannot just learn about the project on their own, but someone should mentor them.
This may be considered as a part of the communication overhead, it is an important aspect.
:::

<!-- ## what can be done? -->
<!-- Brooks' law says that it is impossible to measure useful work in man-months. -->


# references

::: {#refs}
:::
