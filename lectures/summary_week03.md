---
title: week 3 summary 
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

# steps of requirement analysis

::: {.mt-2}
![based on [@krysik2023sdlc]](figures/requirement_analysis_steps.drawio.svg){height=75}

:::

## functional and non-functional requirements

:::::::::::: {.columns}
::::::::: {.column width="65%" .mt-4}
- functional requirements define<br>
  **what** a system is supposed to do
- non-functional requirements define<br>
  **how** a system is supposed to operate
    - e.g., legal requirements (GDPR)
  
<!--::: {.text-smaller}
source: [@enwiki:1245895117]
:::-->
:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/cogwheel.svg){height=250}

:::::::::
::::::::::::

# minimum viable product


:::::::::::: {.columns}
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/blue-saloon-car-wheels.svg){height=150}

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/blue-saloon-car-body.svg){height=150}

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/blue-saloon-car.svg){height=150}

:::::::::
::::::::::::

:::::::::::: {.columns}
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/children-bicycle.svg){height=150}

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/red-scooter-motorbike.svg){height=150}

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/blue-saloon-car.svg){height=150}

:::::::::
::::::::::::

::: {.text-smaller}
based on [Making sense of MVP (Minimum Viable Product)](https://blog.crisp.se/2016/01/25/henrikkniberg/making-sense-of-mvp) by Henrik Kniberg
:::

# what is a user story?

::: {}
- a popular tool in requirements analysis, particularly in agile software development methodologies
- simple description of a software feature
    - from the perspective of the end user or customer
- and are often accompanied by acceptance criteria (BDD),
    - which define the conditions that must be met to be considered complete
:::

::: {.mt-4}
as a `[type of user]`, I want to `[action/function]` in order to `[benefit/value]`

:::

# behaviour-driven development

:::::::::::: {.columns}
::::::::: {.column width="55%"}
- BDD starts from a user story and<br>focuses on adding acceptance criteria
- extends user stories how the software should react in some with scenarios (conditions)

:::::::::
::::::::: {.column width="45%"}
```
Title (one line describing the story)

Narrative:
As a [role]
I want [feature]
So that [benefit]

Acceptance Criteria:
(presented as Scenarios)

Scenario 1: Title
Given [context]
  And [some more context]...
When  [event]
Then  [outcome]
  And [another outcome]...

Scenario 2: ...
```

:::::::::
::::::::::::

# user story mapping

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- performed in workshops including 
    - users,
    - (UI) designers,
    - developers,
    - testers,
    - and stakeholders
- build a shared understanding of the product and a common language
- living document

:::::::::
::::::::: {.column width="50%"}
![](figures/user_story_map.drawio.svg)

:::::::::
::::::::::::

## user story mapping mistakes

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/usm_too_many_details.drawio.svg){height=450}

:::::::::
::::::::: {.column width="50%"}
:::::: {.r-stack}
::: {.fragment}
![](figures/usm_whole_story_first.drawio.svg){height=450}
:::
::: {.fragment}
![](figures/usm_whole_story_first_verbs.drawio.svg){height=450}
:::
::: {.fragment}
![](figures/usm_whole_story_first_extra.drawio.svg){height=450}
:::
::::::
:::::::::
::::::::::::

::: {.text-smaller}
more from Jeff Patton: [5 story mapping mistakes](https://jpattonassociates.com/5-story-mapping-mistakes/)
:::

# references

::: {#refs}
:::
