---
title: summary by practice 
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
revealjs-url: "../assets/reveal.js-6.0.2/"
link-citations: true
---

## the user story

:::::::::::: {.columns}
::::::::: {.column width="65%" .text-smaller}

::: {.wide-quote}
> We would like you to create a flashcard app for smartphones.
> Just the [**usual stuff**]{.background-color-lightblue}: it shows cards and then if needed it shows the other side of the card with the meaning.
>
> Oh, and words should be in [**groups**]{.background-color-lightblue}. A [**word can appear in multiple groups**]{.background-color-lightblue}.
> The user [**selects a group**]{.background-color-lightblue} to practice. Then, the app shows a card with the word (or expression) in the target language.
> The user can do 3 things:
>
> 1. Tap the card to show its other side, both sides should be shown at the same time,
> 2. The user can swipe left to indicate that they do not know the word, or
> 3. swipe to right indicating the they know the word well.
>
> The app should [**count the swipes and keep statistics**]{.background-color-lightblue}.
> And one more thing: the [**statistics should be tracked per user basis**]{.background-color-lightblue}.

:::
:::::::::
::::::::: {.column width="35%"}
requirement smells

: language based signs in the requirements that indicate issues

misunderstanding the task can be costly

: ![[decreasing probability of introducing defects [@ambler2002agile]]{.text-smaller}](figures/introducing_defects.drawio.svg){data-preview-image="figures/introducing_defects.drawio.svg" data-preview-fit="contain"}

:::::::::
::::::::::::

::: {.mt-1}
requirement smell | review with output | documentation
:::

# requirement analysis


:::::::::::: {.columns}
::::::::: {.column width="65%" .text-smaller}
![](figures/user_statistics/story_map_v3.drawio.svg)
:::::::::
::::::::: {.column width="35%"}

**user story**

as a \<language learner><br>
I want to \<see my stats><br>
in order to \<track my progress>

::: {.mt-2}
the USM uses the user’s perspective to tell a story / narrative

overview first, zoom into details later
:::
:::::::::
::::::::::::

::: {.mt-1}
<!-- user story mapping | review with output | documentation -->
:::

## steps of requirement analysis

1. stakeholder identification
2. elicitation of requirements (gathering data)
3. documentation of requirements
4. analysis and negotiation
5. validation and verification
        
:::::::::::: {.columns .text-smaller .mt-3}
::::::::: {.column width="50%"}
validation

:    - are we building the right thing?
:    - is about confirming that the requirements actually meet the needs of the stakeholders

:::::::::
::::::::: {.column width="50%"}
verification

:    - are we building the thing right?
:    - to ensure that all requirements are clear, unambiguous, and consistent

:::::::::
::::::::::::

## functional and non-functional requirements

::: {.wide-quote}
functional requirements define what a system is supposed to do<br>and non-functional requirements define how a system is supposed to operate [@enwiki:1245895117]

:::

:::::::::::: {.columns .mt-3}
::::::::: {.column width="50%"}
functional

- [what]{.background-color-lightblue}
- features
- the webserver can serve pages via HTTP2

:::::::::
::::::::: {.column width="50%}
non-functional

- [how]{.background-color-lightblue}
- quality goals, quality of service requirements
- webserver is available 99.9% of time<br>(yearly about 8h 41m downtime)
- can serve at least 5.000 queries per sec

:::::::::
::::::::::::

## minimum viable product

:::::::::::::::::: {.columns}
::::::::::::::: {.column width="60%"}

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
![](figures/publicdomainvectors/blue-scooter-motorbike.svg){height=150}

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/blue-saloon-car.svg){height=150}

:::::::::
::::::::::::

::: {.text-smaller}
based on [Making sense of MVP (Minimum Viable Product)](https://blog.crisp.se/2016/01/25/henrikkniberg/making-sense-of-mvp) by Henrik Kniberg
:::

:::::::::::::::
::::::::::::::: {.column width="40%"}
![](figures/user_story_map_short.drawio.svg)
:::::::::::::::
::::::::::::::::::

::: {.text-smaller}
Gall's law: _A complex system that works is invariably evolved from a simple system that worked._

:::

# wireframing

:::::::::::: {.columns}
::::::::: {.column width="40%" .text-smaller .mt-2}
`as a user I want to see my activity to track my progress`

display user statistics including

:    - username
     - profile image
     - registration date
     - progress in course
     - last mondth activity

:::::::::
<!--
::::::::: {.column width="30%"}
![low-fidelity](figures/user_statistics/wireframe_lofi.drawio.svg){width=242}

:::::::::
::::::::: {.column width="30%"}
![mid-fidelity](figures/user_stats.drawio.svg){width=250}
:::::::::
-->
::::::::: {.column width="60%"}
:::::: {.r-stack}
::: {.fragment .fade-out fragment-index=1}
![low-fidelity](figures/user_statistics/wireframe_lofi.drawio.svg){width=242}
![mid-fidelity](figures/user_stats.drawio.svg){width=250}
:::
::: {.fragment .fade-in fragment-index=1}
![mid-fidelity](figures/user_stats.drawio.svg){width=250}
![high-fidelity](figures/user_statistics/wireframe_hifi.drawio.svg){width=250}
:::
::::::
:::::::::
::::::::::::

## wireframe map

![](figures/user_statistics/wireframe_map_full.drawio.svg){width=750}

# references

::: {#refs}
:::


<!--:::::::::::: {.columns}
::::::::: {.column width="50%" }

:::::::::
::::::::: {.column width="50%"}

:::::::::
::::::::::::-->
