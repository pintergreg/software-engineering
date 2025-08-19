---
title: Kanban
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

this presentation is based on The Kanban Guide (2020) by Daniel S. Vacanti

available from [kanbanguides.org](https://kanbanguides.org) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

or download directly [from here](../resources/Kanban-Guide-2020-12.pdf)

# what is kanban?

:::::::::::: {.columns}
::::::::: {.column width="50%"}
> Kanban is a strategy for optimizing the flow of value through a process that uses a visual, pull-based system

:::::::::
::::::::: {.column width="50%"}
![](figures/kanban.drawio.svg)

:::::::::
::::::::::::

## principles of kanban

:::::::::::: {.columns}
::::::::: {.column width="70%"}
1. defining and visualizing a workflow
2. actively managing items in a workflow
3. improving a workflow

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/scrum-task-board.svg)

:::::::::
::::::::::::

::: notes
These Kanban practices are collectively called a Kanban system.
Those who participate in the value delivery of a Kanban system are called Kanban system members.
:::

# defining and visualizing the workflow

:::::::::::: {.columns}
::::::::: {.column width="60%" .column-align-left}
::: {}
- definition of workflow (DoW)
    - the visualization of the DoW is called a Kanban board
    - states (columns)
    - conditions when to move an item between columns

:::
::: {.fragment data-fragment-index="1"}
- a definition of the individual units of value that are moving through the workflow
    - referred to as work items (or items)

:::
:::::::::
::::::::: {.column width="40%"}
![](figures/job_hunting_kanban_item.drawio.svg){.fragment data-fragment-index="1"}

:::::::::
::::::::::::

## defining and visualizing the workflow

:::::::::::: {.columns}
::::::::: {.column width="60%" .column-align-left}
- a definition for when work items are started and finished within the workflow
    - a workflow may have more than one started or finished points

:::::::::
::::::::: {.column width="40%"}
![](figures/job_hunting_kanban_finish.drawio.svg)

:::::::::
::::::::::::

## defining and visualizing the workflow

:::::::::::: {.columns}
::::::::: {.column width="60%" .column-align-left}
- one or more defined states between the started to finished
    - item between start and finish point are considered work in progress (WIP)
- a definition of how WIP will be controlled from started to finished
- explicit policies about how work items can flow through each state

:::::::::
::::::::: {.column width="40%"}
![](figures/job_hunting_kanban_transitions.drawio.svg)

:::::::::
::::::::::::

# Service Level Expectation

:::::::::::: {.columns}
::::::::: {.column width="50%" .column-align-left}
- a service level expectation (SLE)
    - which is a forecast of how long it **should** take a work item to flow from started to finished
- the SLE itself has two parts: a period of elapsed time and a probability associated with that period
    - e.g., 85% of work items will be finished in eight days or less

:::::::::
::::::::: {.column width="50%"}
![](figures/job_hunting_kanban_transitions_2.drawio.svg)

:::::::::
::::::::::::

## Service Level Expectation

:::::::::::: {.columns}
::::::::: {.column width="50%" .column-align-left}
- the SLE should be based on historical cycle time
    - and once calculated, should be visualized on the Kanban board
    - if historical cycle time data does not exist, a best guess will do until there is enough historical data

:::::::::
::::::::: {.column width="50%"}
![](figures/job_hunting_kanban_transitions_2.drawio.svg)

:::::::::
::::::::::::

# improving the Workflow

- it is common practice to review the DoW from time to time to discuss and implement any
changes needed
    - e.g., need a new column for a new state
- not necessary to wait for a formal meeting at a regular cadence to make these changes

# kanban measures

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- WIP: number of work items started but not finished
- throughput: number of work items finished per unit of time
    - Note the measurement of throughput is the exact count of work items
- work item age: elapsed time from when a work item started
- cycle time: time between when a work item started and finished
:::::::::
::::::::: {.column width="40%"}
![](figures/cdf.svg)

:::::::::
::::::::::::

::: notes
Visualizing these metrics using charts is recommended.
It does not matter what kind of charts are used as long as they enable a shared understanding of the Kanban system's current health and performance.
:::

# Toyota's six rules [@enwiki:1239509091]

:::::::::::: {.columns}
::::::::: {.column width="70%"}
1. Each process issues requests (kanban) to its suppliers when it consumes its supplies.
2. Each process produces according to the quantity and sequence of incoming requests.
3. No items are made or transported without a request.
4. The request associated with an item is always attached to it.
5. Processes must not send out defective items, to ensure that the finished products will be defect-free.
6. Limiting the number of pending requests makes the process more sensitive and reveals inefficiencies.

:::::::::
::::::::: {.column width="30%"}
![Kanban card together with the bag of bolts](figures/borrowed/080527-F-0000A-001.JPG)

:::::::::
::::::::::::

# scrumban

SCRUM and kanBAN can coexist

:::::::::::: {.columns}
::::::::: {.column width="50%"}
Scrum contributes to scrumban:

- sprints
- daily standups
- retrospectives

:::::::::
::::::::: {.column width="50%"}
Kanban contributes to scrumban:

- board
- cards
- work-in-progress limits

:::::::::
::::::::::::

# references

::: refs
:::
