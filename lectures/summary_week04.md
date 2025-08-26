---
title: week 4 summary 
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

# unified modeling language

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-4}
- UML 2.0 released in 2005
    - latest revision in 2017
- ISO/IEC 19501 standard
- designed to be a complete language of software modelling
- UML 2 has 14 diagrams in two categories: structure and behavior

::: {.fragment}
most software developer do not use UML (in a formal way), but hand drawn sketches which often include UML elements [@baltes2014sketches]
:::
:::::::::
::::::::: {.column width="40%"}
![](figures/uml/diagrams.svg)

:::::::::
::::::::::::


## use case diagram

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-5}
- depicts the interactions between system users (actors) and the system itself
- used to specify the functional requirements
- provides a high-level view
    - helping stakeholders to understand the system's functionality
- it's purpose is similar to the user story

:::::::::
::::::::: {.column width="40%"}
![](figures/social_media_platform/usecase_3.svg){width=300}

:::::::::
::::::::::::


## class diagram

:::::::::::: {.columns}
::::::::: {.column width="50%" .mt-5}
- describes the structure of a system by its classes
    - their attributes, methods, and the relationships among them 
- main building block of the object-oriented modeling

:::::::::
::::::::: {.column width="50%"}
![](figures/uml/class_example_2.svg){width=450}

:::::::::
::::::::::::


## object diagram

- special case of a class diagram
- graphical representation of the objects and their relationships<br>**at a specific moment in time**
- provides a snapshot of the system's structure
- does not show anything architecturally different to class diagram

![](figures/uml/object_class.svg){height=250}


## component diagram

- depicts the component structure and relations
- highlighting the interfaces

::: {.mt-2}
![](figures/uml/component.svg){height=275}
:::


## state diagram

:::::::::::: {.columns}
::::::::: {.column width="50%" .mt-5}
- a visual representation of the states a system or an object can be in
    also the transitions between those states
- models the dynamic behavior of the system, capturing how it responds to different events over time
- shows the system's life cycle

:::::::::
::::::::: {.column width="50%"}
![](figures/uml/stopwatch_state_commented.svg){width=350}

:::::::::
::::::::::::


## activity diagram

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-4}
- graphical representations of workflows
- similar to flowcharts
    - but uses UML notation
    - and can visualize parallel processing
    - has more features

:::::::::
::::::::: {.column width="20%"}
![flowchart](figures/uml/power.drawio.svg){height=300}
:::::::::
::::::::: {.column width="20%"}
![activity (UML)](figures/uml/activity.svg){height=300}
:::::::::
::::::::::::


## sequence diagram

:::::::::::: {.columns}
::::::::: {.column width="60%"}
![](figures/uml/sequence.svg)
:::::::::
::::::::: {.column width="40%" .mt-3}
- shows process interactions arranged in time sequence
- depicts the processes and objects involved and the sequence of messages exchanged
- instead of the inner parts of a system, message exchange between software systems can be depicted
:::::::::
::::::::::::


# what is the issue with UML?

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-4}
- closely connected with OOP
- propagates object-oriented modelling
    - however the design should not consider the implementation

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/paper-documents.svg){width=300}

:::::::::
::::::::::::

    
# C4 model

> overview first, zoom and filter, then details on demand
>
> -- Ben Shneiderman

- hierarchical set of software architecture diagrams
    - different levels of abstraction for different audience
- has four levels:
    - context, containers, components and code
- popularized by Simon Brown

::: {.text-smaller .mt-2}
this chapter is based on [c4model.com](https://c4model.com/)
:::


## level 1: system context diagram

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-2}
- shows how the software fits into the world
  - [who use it]{.text-smaller}
  - [what other software does it interacts]{.text-smaller}
- high level diagram
  - [technologies, protocols and other low-level details are not important]{.text-smaller}
- similar to use case diagram
- understandable for non-technical people

:::::::::
::::::::: {.column width="40%"}
![](figures/user_statistics/c4_system_context.drawio.svg){width=400}

::: {.text-smaller}
other possible users:

administrator, course planner
:::
:::::::::
::::::::::::


## level 2: container diagram

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="50%"}
- zooms into the software system
- shows the containers that make up that software system
  - [applications, data stores, microservices, etc.]{.text-smaller}
- technology decisions are also a key part of this diagram
  - [what database management system to use, e.g., PostgreSQL]{.text-smaller}
  - [what e-mail service to use, e.g., Mailchimp]{.text-smaller}
  - [what language to use]{.text-smaller}
  - [what UI framework to use]{.text-smaller}

:::::::::
::::::::: {.column width="50%"}
![](figures/user_statistics/c4_contianer.drawio.svg){width=400}
:::::::::
::::::::::::


## level 3: component diagram

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- decomposition of each container to identify the major structural building blocks and their interactions
- shows how a container is made up of a number of "components" 
  - what these components are, 
  - what they are responsibilities for, and
  - what also shows technology / implementation details
- roughly equivalent with the UML component diagram

:::::::::
::::::::: {.column width="40%"}
![the example shows the components of only one feature, so incomplete](figures/user_statistics/c4_component.excalidraw.svg){width=400}

:::::::::
::::::::::::


## level 4: code

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- optional level of detail 
- ideally this diagram would be automatically generated
- if you really want or need to, you can zoom into an individual component
  - but show only those attributes and methods that really needed for the storytelling
- UML class diagram can be used

:::::::::
::::::::: {.column width="40%"}
![this may be too much](figures/user_statistics/class_3.svg){width=400}

:::::::::
::::::::::::


# references

::: {#refs}
:::
