---
title: project assignment
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

# the project

An event organizer company entrusts your software development company to create a choreography designer software for drone shows.
They have just bought 512 drones and they want to be able to do smaller-scale drone shows on parties, birthdays, and weddings.

The software should be able to manage the position of every drone in a given space in respect of the time.
Every drone is capable of switch on RGB LEDs with a given light intensity.
The software should be able to manage not just the position, but the state (light) of the drone.

The software generates a trajectory for every drone that it will follow.

Your task is to design this software.


## drone show example

:::::::::::: {.columns}
::::::::: {.column width="60%"}
![Drone Show at Sydney (2023) by Leoxiong | [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.en)](../lectures/figures/borrowed/wikipedia/drone_show_at_sydney_2023.jpg)

:::::::::
::::::::: {.column width="40%" .text-smaller .mt-1}
from YouTube

- [Dragon Boat Show with 1500 drones in Shenzhen, China](https://www.youtube.com/watch?v=3G1KBu6H6BM)

:::::::::
::::::::::::


## choreography design in focus

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- the client company wants to design and operate the show
- the software has to focus on the choreography design, not the software running on the drone
- you can assume that there is a software from the drone manufacturer, which deals with the hardware level
    - it is an external "component" of the software system

:::::::::
::::::::: {.column width="40%"}
![](../lectures/figures/choreographer/viewport.drawio.svg)

:::::::::
::::::::::::

[How Drone Shows Work](https://www.youtube.com/watch?v=7fKfBb7x9WQ) by Julius Moorman
    

# contents -- outline

- introduction
    - what the software is -- practically the project assignment
    - team members -- students working on the assignment
- stakeholder identification
- methodology
- detailed requirements
    - functional requirements
    - non-functional requirements
- diagrams and models
- prioritization of requirements
- constraints and assumptions
- acceptance criteria
- appendices
- version history and approvals


## diagrams

:::::::::::: {.columns}
::::::::: {.column width="70%"}
- user stories
    - user story maps
    - with BDD-style acceptance criteria
- flowcharts
- first 3 level of C4
- also static and dynamic models of the software
    - 4th level / UML
- UI mockups

:::::::::
::::::::: {.column width="30%"}
![](../lectures/figures/publicdomainvectors/paperboard-flowchart.svg){height=300}

:::::::::
::::::::::::


## diagrams details

> overview first, zoom and filter, then details on demand
>
> -- Ben Shneiderman

::: {.mt-2}
- create a **user story map** in details for one role's set of features
    - for example the choreography design
- you don't have to detail every single role
    - but give an overview of the system
    - illustrate the every roles and the connections between them

:::

    
## work in agile methodology

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- imagine how you would use a software like this
    - what functions would you need
- identify dependencies between the functions / modules
- plan sprints with usable increments
- deadline: **10 December 2025** (week 13)
    - when the team also presents the design as a presentation
- practical classes are workshops
    - possible feedback from the instructor
- **NO CODING**

:::::::::
::::::::: {.column width="35%"}
![](../lectures/figures/publicdomainvectors/business-ideas-development.svg)

:::::::::
::::::::::::


# suggested software for

- the document: [Google Docs](https://docs.google.com/docs)
- user story map: [Google Drawings](https://docs.google.com/drawings)
- flowchart: [Google Drawings](https://docs.google.com/drawings)
- team management: [Trello](https://trello.com/)
- UML: [draw.io](https://app.diagrams.net/)
- C4: [Google Drawings](https://docs.google.com/drawings)
    - [create C4 diagrams in draw.io](https://www.drawio.com/blog/c4-modelling)


# submission

- you have to submit the main design document
- you may indicate who was responsible for each part
- including every diagram
    - please keep every version of the diagrams and attach them to the submission
        - I would like to see the evolution of your design
- and the presentation

you have to submit these by 10 December 2025 via Moodle,<br>when you also present your work

it is enough to upload it by one person from each team

# presentation

- the presentation should contain the purpose of the software
    - practically the project assignment
    - but with your interpretation
- team members
    - maybe with responsibilities
- the introduction of your design
    - from high level to the low level (according to C4)
    - describe the overall design
    - focusing on the interactions between your components
    - detail at least one of the component to the class level
    - attach UI mockups

    
## presentation

- you may separate the presentation by target audience
    - for the customer almost as if you wanted "sell" the software and introduce it from the user's perspective
        - C4 system context, use case, user story flows with UI mockups and explanation
    - and a more technical part focusing on the internal structures
        - zoom into the system as C4 modelling propagates
        - detail the interfaces and the environments where a software will operate
