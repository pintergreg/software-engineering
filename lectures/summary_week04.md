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
revealjs-url: "../assets/reveal.js-5.1.0/"
---

# what is the issue with UML?

- closely connected with OOP
- propagates object-oriented modelling
    - however the design should not consider the implementation

    
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
::::::::: {.column width="50%" .mt-4}
- shows how the software fits into the world
  - [who use it]{.text-smaller}
  - [what other software does it interacts]{.text-smaller}
- high diagram
  - [technologies, protocols and other low-level details are not important]{.text-smaller}
- similar to use case diagram
- understandable for non-technical people
:::::::::
::::::::: {.column width="50%"}
![](figures/user_statistics/c4_system_context.drawio.svg){width=400}
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
::::::::: {.column width="50%"}


:::::::::
::::::::: {.column width="50%"}
![](figures/user_statistics/c4_component.excalidraw.svg){width=400}
:::::::::
::::::::::::


## level 4: code


# references

::: {#refs}
:::
