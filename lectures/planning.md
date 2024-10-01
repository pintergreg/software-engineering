---
title: Planning
author: Gergő Pintér, PhD
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
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
based on [What is an implementation plan? 6 steps to create one](https://asana.com/resources/implementation-plan)
:::


# conduct research

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- during the requirement analysis some data was already collected
    - regarding functional and non-functional requirements
- some research may be needed to select the tools and frameworks during the implementation
    - do some experiments with different libraries

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/chemist-conducting-experiments.svg){height=300}
:::::::::
::::::::::::

# identify risks


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

<!-- ## what can be done? -->





