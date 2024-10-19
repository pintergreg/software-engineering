---
title: week 6 summary 
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

# interface is an agreement

:::::::::::: {.columns}
::::::::: {.column width="55%" .mt-4}
- how a module / component will work
- so as long as the agreement is complied the components do not need to know about the internal structure/work of the other components
    - separation of concerns
    - single responsibility principle
    - the other component can be replaced, mocked

:::::::::
::::::::: {.column width="45%"}
![](figures/publicdomainvectors/business-handshake-hands.svg){width=500}
:::::::::
::::::::::::


# interface changes should be communicated

:::::::::::: {.columns .mt-4}
::::::::: {.column width="65%"}
::: {.align-left}
- during design / development
    - change can be necessary / allowed, but communicate towards the impacted teams
    - diagrams show inner dependencies

:::
::: {.align-left .fragment}
- services announce API deprecations
- so as library / framework developers
    - can be a source of new issues even if downstream code is not changed

:::
:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/policeman-screams-into-a-megaphone.svg){width=225}

:::::::::
::::::::::::


## API versions

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/user_statistics/interface_versions.svg){width=475}

:::::::::
::::::::: {.column width="50%"}
![](figures/user_statistics/interface_versions_gantt.svg){width=375}

:::::::::
::::::::::::

::: {.text-smaller}
`https://developers.facebook.com/v21.0/me?fields=id,name`
:::

```python
def unary_union(self):
    warnings.warn(
        "The 'unary_union' attribute is deprecated, "
        "use the 'union_all' method instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return self.union_all()
```


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


## learning could be a task

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-1}
- you may need to work a technology / framework / language that you are not familiar with
- that may require research
    - fail fast
    - document findings
        - minimal workable example
- or you just have to learn a new codebase
- calculate with learning during the planning

:::::::::
::::::::: {.column width="40%"}
![](figures/complex_projects.drawio.cropped_no_people.svg){height=400}

:::::::::
::::::::::::


# identify and prioritize risks

a risk is a possibility that something bad can happen

- there is risk inherent with building any piece of software
- whether you're building a completely new greenfield project,
- or adding a new feature to an existing codebase
    - other parts cease to work
    - the new feature alienate users
    - data loss
- often difficult to prioritise which risks you should take care of
    - the probability: how likely is it that the risk will happen?
    - and the impact: what is the negative impact if the risk does occur?

::: {.text-smaller}
based on [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


## risk storming

:::::::::::: {.columns}
::::::::: {.column width="70%" .mt-4}
- visual and collaborative risk identification technique
- created by Simon Brown (author of C4 model)
- motivation: often only one person evaluated risks
- risk evaluation should be collaborative activity

:::::::::
::::::::: {.column width="30%"}
![](figures/user_statistics/risk_storming.excalidraw.svg){width=300}

:::::::::
::::::::::::

::: {.text-smaller}
based on [riskstorming.com](https://riskstorming.com/) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
:::


## risk register

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="65%"}
- a risk register is a document used as a risk management tool 
- contains all identified risks with additional information
    - category, name, responsible, probability, impact, mitigation, action by, action when
- it can be displayed as a table or as a scatterplot

:::::::::
::::::::: {.column width="35%"}
![by [Hou710](https://en.wikipedia.org/wiki/File:Hou710_RiskLog.svg) | [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.en) ](figures/borrowed/Risk Log - Party Example.svg){width=300}

:::::::::
::::::::::::

::: {.text-smaller .mt-3}

| Risk | Impact<br>(1-3) | Likelihood<br>(0-10) | Risk<br>(I * L) | Mitigation |
|-----------|---:|---:|---:|----------------|
| Rust Language Changes | 2 | 7 | 14 | Target a specific Rustc version |
| Missing GCC 13 upstream window | 1 | 6 | 6 | Merge in GCC 14 and be proactive about reviews |

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


# allocate resources

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
![planning poker by [Hkniberg ](https://en.wikipedia.org/wiki/File:CrispPlanningPokerDeck.jpg) <br> public domain](figures/borrowed/CrispPlanningPokerDeck.jpg)

:::::::::
::::::::::::

::: {.text-smaller}
"Story points reward team members for solving problems based on difficulty, not time spent. This keeps team members focused on shipping value, not spending time [@radiganstory]."
:::


## estimation is guessing

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- many developers do not like to estimate
- seemingly simple task can turn out to be difficult
    - some difficulties are hard to foresee
    - bad architectural decision
        - ["Adding manpower to a late software project makes it later." -- Fred Brooks]{.text-smaller}
- make educated guesses instead
    - measure
        - [burn down charts, cumulative flow diagram]{.text-smaller}
    - infer from previous tasks

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/thimbles-game.svg){width=250}

:::::::::
::::::::::::

# references

::: {#refs}
:::
