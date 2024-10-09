---
title: interfaces
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

![hexagonal arcitectural pattern (a.k.a. ports & adapters)](figures/hexagonal_interface.drawio.svg){width=700}

an interface is a shared boundary across which two or more separate components of a computer system [@enwiki:1244878409]

# NASA lost a 327 Million Dollar Mission

NASA and Lockheed Martin mixed up units for the Mars Climate Orbiter

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-1}
- spacecraft sent values back to Earth in **Newton seconds**
- the software in the ground station read those results as **pound seconds**
    - the guidance and navigation teams was off by a factor of 4.45 times
- this led to a miscalculated trajectory, which doomed the probe and the mission

:::::::::
::::::::: {.column width="40%"}
![rendering of the Mars Climate Orbiter [by NASA/JPL/Corby Waste via [Wikipedia](https://en.wikipedia.org/wiki/File:Mars_Climate_Orbiter_2.jpg) [@enwiki:1248652445]]{.text-small}](figures/borrowed/Mars_Climate_Orbiter_2.jpg)
:::::::::
::::::::::::

::: {.text-smaller}
based on [@dodd2020metric], read the [full story](https://everydayastronaut.com/mars-climate-orbiter/) written by Tim Dodd
:::


# references

::: {#refs}
:::
