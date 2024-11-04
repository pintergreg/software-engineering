---
title: testing
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

# legacy code

this chapter is based on the book _Working Efficiently with Legacy Code_ by Michael Feathers.


## what is legacy code?

> Code without tests is bad code.
> It doesn’t matter how well written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is.
> With tests, we can change the behavior of our code quickly and verifiably.
> Without them, we really don’t know if our code is getting better or worse.
>
> -- Feathers, M. (2004). Working Effectively with Legacy Code: Preface

<!--- [További definíciók](https://dzone.com/articles/defining-legacy-code)
- Legacy Code
    - [What are the key points of Working Effectively with Legacy Code?](http://programmers.stackexchange.com/questions/122014/what-are-the-key-points-of-working-effectively-with-legacy-code)-->


## the legacy code dilemma

> When we change code, we should have tests in place.
> To put tests in place, we often have to change code.
>
> -- Feathers, M. (2004). Working Effectively with Legacy Code: Part I / Chapter 2


##  changing the software

|                  | add feature | fix a bug | refactor | optimize |
| ---------------- | ----------- | --------- | -------- | -------- |
| structure        | changes     | changes   | changes  |          |
| new funcionality | changes     |           |          |          |
| functionality    |             | changes   |          |          |
| resource usage   |             |           |          | changes  |

::: {.text-smaller .mt-4}
Feathers, M. (2004). Working Effectively with Legacy Code: p1. pp 6. Prentice Hall Professional
:::
