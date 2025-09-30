---
title: user story mapping example
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

- customer is a language association
- has textbooks and workbooks for learning a minority language
- wants our company to develop a flashcard application, which will help people to learn the language

## the user story {visibility=hidden}

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

# had another meeting to clarify the task

- which platform?
    - Android and iOS (tablets should be supported)
    - at least 5 years old devices should be supported
- offline app, no subscription plans, one-time payment via the store
- no ~~passive-aggressive~~ urging in a form of push notifications
- how the words are groupped?
    - by chapters of the textbook
    - the customer provides a wordlist (with meaning) for each chapter
- user will not be able to add new words
- one interface language is enough
    - the majority language of the country
- logo of the language association should appear on the main screen

## had another meeting to clarify the task

- high-constrast theme is a good idea besides the light/dark ones
    - no need for additional themes
    - font size settings is a good idea
- the customer wants a learning mode, which just goes through the word of the chapter (groups)
- and a practicing mode, which selects words randomly from every group
    - words with more left-swipe should appear more frequent
- users should be able to check the statistics
    - streak
    - progress bar (learnt words / total)
        - if a word was swiped left, three right swipes needed to consider it learnt
    - which days they learned in the last month, how many cards they've learnt
- the customer was interested in the audio feature for the cards, but *currently* not needed, maybe in a future release

# offline application

![offline application, a simple case](../lectures/figures/simple_case.drawio.svg)

## customer provides the word database

![standardizing input](../lectures/figures/etl.drawio.svg)

# user story mapping

:::::::::::: {.columns}
::::::::: {.column width="50%" .mt-3}
- let's draw a user story map
- [open textusm](https://app.textusm.com/)

:::::::::
::::::::: {.column width="50%"}
![](../lectures/figures/user_story_map.drawio.svg)

:::::::::
::::::::::::


