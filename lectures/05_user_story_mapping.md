---
title: user story mapping
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

# the problem

- the backlog difficult to prioritize 
    - identify dependencies
    - already at this point the tasks need detailed understanding
- the backlog is one dimensional
    - priority


# user story map

![](figures/user_story_map.drawio.svg)

::: notes
- two dimensional
- consists of three elements
    1. activities
    2. steps
    3. details
:::


## activity

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- is sort of a big thing that people do 
- that has lots of steps,
- and doesn't always have a precise workflow

activities are still user stories with roles

:::::::::
::::::::: {.column width="50%" .text-size-2}
```
As a social media platform user
I want to follow users
so I can keep up with their posts.
```

:::::::::
::::::::::::

::: notes
An activity is close to an epic in the scrum literature.
:::


## user task

:::::::::::: {.columns}
::::::::: {.column width="55%"}
- in agile a "task" refers to the things that *developers* do
    - to finish user stories
- user story mapping considers the *user*,
    - so a user task is what a user needs to do to complete an activity

:::::::::
::::::::: {.column width="45%"}
for example (follow a user)

:   1. search for user
    2. add user to followed list

:::::::::
::::::::::::

<!--## details

search for user

:   - type username
    - browse the result lists
    - click to the "follow" button-->

## 

![from "Quickstart Guide to User Story Mapping" by Eben Halford | CC BY-SA 2.5](figures/borrowed/split_restaurant_bill.jpg){width=80%}
    

# user story mapping

- popularized by Jeff Patton
    - [original blog post](https://jpattonassociates.com/the-new-backlog/)
    - User Story Mapping, O'Reilly, 2014, ISBN-13: 978-1491904909
- performed in workshops including 
    - users,
    - (UI) designers,
    - developers,
    - testers,
    - and stakeholders
- build a shared understanding of the product and a common language


## user story map as a document

- not final, not set in stone
- it is possible and encouraged to adjust<br>as the more knowledge is acquired about the software
    - versioning
- you are free to move notes up and down
    - change the role (activity &#8596; user task)


# backbone, skeleton, ribs

![](figures/user_story_map_bones.drawio.svg)


## iterations

![](figures/user_story_map_increments.drawio.svg)


# social media platform - example

![](figures/social_media_platform/usm_sign_up.drawio.svg)


# user story mapping mistakes

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
