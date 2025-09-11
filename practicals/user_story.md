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
> The app should count the swipes and keep statistics. A word with more left swipes should appear more often.
> And one more thing: the statistics should be tracked per user basis.

:::

# requirements analysis

- starts with understanding the task
    - read, reread, and reflect on it
- collect every detail, specifically the ambiguous parts
- take notes, maybe draw

## the user story

::: {.wide-quote}
> We would like you to create a flashcard app for smartphones.
> Just the **usual stuff**: it shows cards and then if needed it shows the other side of the card with the meaning.
>
> Oh, and words should be in **groups**. A **word can appear in multiple groups**.
> The user **selects a group** to practice. Then, the app shows a card with the word (or expression) in the target language.
> The user can do 3 things:
>
> 1. Tap the card to show its other side, both sides should be shown at the same time,
> 2. The use can swipe left to indicate that they do not know the word, or
> 3. swipe to right indicating the they know the word well.
>
> The app should **count the swipes and keep statistics**. A **word with more left swipes should appear more often**.
> And one more thing: the **statistics should be tracked per user basis**.

:::

# requirements

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

## questions

- which platforms should be supported?
- what does 'per user basis' mean?
- who and how creates the cards?
- what is the teaching language?
    - only one language supported?
- does the front side of a card contain only a word/expression?
    - any additional info like word class
- does the back side of a card contain only a meaning?
    - any additional comments or connected words

# possible architecture

![offline application, a simple case](../lectures/figures/simple_case.drawio.svg)

## possible architecture 2

![service-based application, a more complex case](../lectures/figures/complicated_case.drawio.svg)
