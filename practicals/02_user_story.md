---
title: sample task
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
revealjs-url: "../assets/reveal.js-5.2.1/"
---

# sample task -- flashcard application

The prepresentative of a language association entrusts your software development company to create a flashcard application, which will help people to learn a minority language.
The task is to design this software.

## the user story

::: {.wide-quote}
> We would like you to create a flashcard app for smartphones.
> Just the usual stuff: it shows cards and then if needed it shows the other side of the card with the meaning.
>
> Oh, and words should be in groups. A word can appear in multiple groups.
> The user selects a group to practice. Then, the app shows a card with the word (or expression) in the target language.
> The user can do 3 things:
>
> 1. Tap the card to show its other side, both sides should be shown at the same time,
> 2. The use can swipe left to indicate that they do not know the word, or
> 3. swipe to right indicating the they know the word well.
>
> The app should count the swipes and keep statistics.
> And one more thing: the statistics should be tracked per user basis.

:::
<!-- A word with more left swipes should appear more often. -->

# requirements analysis

:::::::::::: {.columns}
::::::::: {.column width="70%" .mt-4}
- starts with understanding the task
    - read, reread, and reflect on it
- collect every detail, specifically the ambiguous parts
- take notes, maybe draw

:::::::::
::::::::: {.column width="30%"}
![](../lectures/figures/mental_map.drawio.svg)

:::::::::
::::::::::::


## why do requirements analysis?

one reason is

![the rising costs of finding and fixing defects<br>based on Figure 3.4 of [@ambler2002agile] (Ambler, 2002)](../lectures/figures/cost_of_fixing.drawio.svg)

## why do requirements analysis well?

misunderstanding the task can cost a lot

![the decreasing probability of introducing defects<br>based on Figure 3.3 of [@ambler2002agile] (Ambler, 2002)](../lectures/figures/introducing_defects.drawio.svg)


## the user story

:::::: {.r-stack} 
::: {.wide-quote .fragment .fade-out data-fragment-index=1}
> We would like you to create a flashcard app for smartphones.
> Just the usual stuff: it shows cards and then if needed it shows the other side of the card with the meaning.
>
> Oh, and words should be in groups. A word can appear in multiple groups.
> The user selects a group to practice. Then, the app shows a card with the word (or expression) in the target language.
> The user can do 3 things:
>
> 1. Tap the card to show its other side, both sides should be shown at the same time,
> 2. The use can swipe left to indicate that they do not know the word, or
> 3. swipe to right indicating the they know the word well.
>
> The app should count the swipes and keep statistics.
> And one more thing: the statistics should be tracked per user basis.

:::
::: {.wide-quote .fragment .current-visible data-fragment-index=1}
> We would like you to create a flashcard app for smartphones.
> Just the [**usual stuff**]{.background-color-lightblue}: it shows cards and then if needed it shows the other side of the card with the meaning.
>
> Oh, and words should be in [**groups**]{.background-color-lightblue}. A [**word can appear in multiple groups**]{.background-color-lightblue}.
> The user [**selects a group**]{.background-color-lightblue} to practice. Then, the app shows a card with the word (or expression) in the target language.
> The user can do 3 things:
>
> 1. Tap the card to show its other side, both sides should be shown at the same time,
> 2. The use can swipe left to indicate that they do not know the word, or
> 3. swipe to right indicating the they know the word well.
>
> The app should [**count the swipes and keep statistics**]{.background-color-lightblue}.
> And one more thing: the [**statistics should be tracked per user basis**]{.background-color-lightblue}.

:::
<!-- > A [**word with more left swipes should appear more often**]{.background-color-lightblue}. -->
::::::

# let's collect the requirements

::: {.r-fit-text .mt-3}
[open PlantUML editor](https://editor.plantuml.com/uml/SoWkIImgAKygvYfEJin9LJ3YAixEp5CeoYzEvUBILaZBIIpEI4uiIb58B2ZWud98pKi1gGK0)

with a Work Breakdown Structure (WBS) diagram skeleton

:::

# questions

- "per user basis"
    - might indicate user management
        - create, read, update, and delete (CRUD)
        - log in, log out
    - or it can be completely offline
- "user selects a group"
    - is this action starts the "game"
- it is not mentioned explicitly, but cards management is possible required
    - CRUD
    - sort into group
    - remove from group
    - "word can appear in multiple group"
        - one to many connection!
- "keeps statistics"
    - for what purpose? only to display it, or for the repetition mechanics?
        
## additional questions

- which platforms should be supported?
- what does 'per user basis' mean?
- who and how creates the cards?
- what is the teaching language?
    - only one language supported?
- does the front side of a card contain only a word/expression?
    - any additional info like word class
- does the back side of a card contain only a meaning?
    - any additional comments or connected words
- price of the application?
    - subscription model / one time payment / free

# possible architecture

![offline application, a simple case](../lectures/figures/simple_case.drawio.svg)

## evaluation

- simple
    - it can contain advanced features like detailed statistics for the user, but it is stored on the device
    - telemetry is possible to add if the customer require some statistics above what the app store provide
- the application package contains everything
    - including the word database
- does not depend on internet collection

::: {.text-color-secondary .mt-2}
these are just some considerations, the customer needs to decide
:::

# possible architecture 2

![service-based application, a more complicated case](../lectures/figures/complicated_case.drawio.svg)

## evaluation

- more complicated, it consists of two different software
    - the server need to run constantly otherwise the application may be unusable
        - depends on the implementation
- can support subscription model
    - needs payment handling, which complicates things further
- the application package can still contain the word database
    - but the available word packages can be controlled based on the subscription plan
- it may depend on internet collection
    - for authentication/authorization
    - for account syncronization
    - *subscription* 

::: {.text-color-secondary .mt-2}
these are just some considerations, the customer needs to decide
:::

# think over every possibility

- it is acceptable to provide alternatives for the customer
    - they often don't even know what they want
- to provide the alternatives, you have to think them over
    - it is also necessary for the price estimation

# references

::: {#refs .text-smaller}
:::
