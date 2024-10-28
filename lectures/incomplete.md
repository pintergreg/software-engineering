---
title: incomplete
author: Gergő Pintér, PhD
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
slideNumber: "true"
showSlideNumber: "print"
revealjs-url: "../assets/reveal.js-5.1.0/"
---

# legacy code

this chapter is based on the book _Working Efficiently with Legacy Code_ by Michael Feathers.


## what is legacy code?

> Code without tests is bad code. It doesn’t matter how well written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is. With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don’t know if our code is getting better or worse.
>
> -- Feathers, M. (2004). Working Effectively with Legacy Code: Preface


- [További definíciók](https://dzone.com/articles/defining-legacy-code)
- Legacy Code
    - [What are the key points of Working Effectively with Legacy Code?](http://programmers.stackexchange.com/questions/122014/what-are-the-key-points-of-working-effectively-with-legacy-code)


## the legacy code dilemma

> When we change code, we should have tests in place. To put tests in place, we often have to change code.
>
> -- Feathers, M. (2004). Working Effectively with Legacy Code: Part I / Chapter 2


## Code Smells

- [Code Smells](https://blog.codinghorror.com/code-smells/)


##  changing the software

|                  | add feature | fix a bug | refactor | optimize |
| ---------------- | ----------- | --------- | -------- | -------- |
| structure        | changes     | changes   | changes  |          |
| new funcionality | changes     |           |          |          |
| functionality    |             | changes   |          |          |
| resource usage   |             |           |          | changes  |

::: {.text-smaller}
Feathers, M. (2004). Working Effectively with Legacy Code: p1. pp 6. Prentice Hall Professional
:::


# versioning

## semantic versioning

![](https://jontejada.com/blog/assets/semver02.png)

- [website](https://semver.org)
- [Why I don't like SemVer anymore](https://snarky.ca/why-i-dont-like-semver/)

## calendar versioning

- "*CalVer* is a versioning convention based on your project's release calendar, instead of arbitrary numbers."
- YYYY.MINOR.MICRO
- [website](https://calver.org)

## ZeroVer: 0-based versioning

- "Your software's major version should never exceed the first and most important number in computing: zero."
- e.g.: **0.4.1**
- [website](https://0ver.org)


# Fibonacci releases

| version | type           | release date   | delta |
|:-------:|----------------|----------------|------:|
| 6.1.0   | Release        | Tue 2024-06-18 | 0     |
| 6.1.1   | Bugfix Release | Tue 2024-06-25 | 1     |
| 6.1.2   | Bugfix Release | Tue 2024-07-02 | 1     |
| 6.1.3   | Bugfix Release | Tue 2024-07-16 | 2     |
| 6.1.4   | Bugfix Release | Tue 2024-08-06 | 3     |
| 6.1.5   | Bugfix Release | Tue 2024-09-10 | 5     |

table: KDE / Plasma 6.1 series [release schedule](https://community.kde.org/Schedules/Plasma_6)
