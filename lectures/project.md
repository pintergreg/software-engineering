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
revealjs-url: "../assets/reveal.js-5.1.0/"
---

# the project

An event organizer company entrusts your software development company to create a drone show choreography designer software.
They have just bought 256 drones and they want to be able to do smaller-scale drone shows on parties, birthdays and weddings.

The software should be able to manage the position of every drone in a given space in respect of the time.
Every drone is capable of switch on RGB LEDs with a given light intensity.
The software should be able to manage not just the position, but the state (light) of the drone.

The software generates a trajectory for every drone that it will follow.

Your task is to design this software.


## drone show example

[Dragon Boat Show with 1500 drones in Shenzhen, China](https://www.youtube.com/watch?v=3G1KBu6H6BM)


# contents

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
    - UML
- UI mockups

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/paperboard-flowchart.svg){height=300}

:::::::::
::::::::::::


## diagrams details

- create a user story map in details for one role's set of features
    - for example the choreography design
- you don't have to detail every single role
    - but give an overview of the system
    - illustrate the every roles and the connections between them

> overview first, zoom and filter, then details on demand
>
> -- Ben Shneiderman

    
## work in agile methodology

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- imagine how you would use a software like this
    - what functions would you need
- identify dependencies between the functions / modules
- plan sprints with usable increments
- deadline: 2024-12-03 (week 13)
    - when the team also presents the design as a presentation
- practical classes are workshops
    - possible feedback from the instructor
- **NO CODING**

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/business-ideas-development.svg)

:::::::::
::::::::::::


# suggested software for

- the document: [Google Docs](https://docs.google.com/docs)
- user story map: [Google Drawings](https://docs.google.com/drawings)
- flowchart: [Google Drawings](https://docs.google.com/drawings)
- team management: [Trello](https://trello.com/)
- UML: [draw.io](https://app.diagrams.net/)
- C4: [Google Drawings](https://docs.google.com/drawings)
