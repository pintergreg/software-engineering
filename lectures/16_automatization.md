---
title: automatization
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

# interruption


# continuous integration


## build script

example: [build script](https://github.com/pintergreg/software-engineering/blob/main/.github/workflows/main.yaml){target="_blank"} of the course website


# continuous deployment


# versioning


## semantic versioning

:::::::::::: {.columns .column-gaplexss}
::::::::: {.column width="50%"}
![](figures/semver.drawio.svg){width=500}

:::::::::
::::::::: {.column width="50%" .text-medium .mt-3}
- **alpha**: incomplete feature-wise, external release is uncommon for proprietary software
    - whitebox testing

- **beta**: the software is feature-complete but contains several known or unknown bugs
    - blackbox testing

- **rc**: release candidate, final touches
    - highest level testing
:::::::::
::::::::::::

::: {.mt-1}
1. **major** version when you make incompatible [API]{.tooltip title="application programming interface"} changes
    - [a way of communicating changes]{.text-smaller}
2. **minor** version when you add functionality in a backward compatible manner
3. **patch** version when you make backward compatible bug fixes

::: {.text-smaller}
additional labels for pre-release and build metadata are available as extensions to the `major.minor.patch` format | from [semver.org](https://semver.org)
:::
:::

::: notes
optional reading: [Why I don't like SemVer anymore](https://snarky.ca/why-i-dont-like-semver/)
:::


## calendar versioning

- "*CalVer* is a versioning convention based on your project's release calendar, instead of arbitrary numbers."
- YYYY.MINOR.MICRO
- [calver.org](https://calver.org)


## ZeroVer: 0-based versioning

- "Your software's major version should never exceed the first and most important number in computing: zero."
- e.g.: **0.4.1**
- [0ver.org](https://0ver.org)


## Fibonacci releases

| version | type           | release date   | delta |
|:-------:|----------------|----------------|------:|
| 6.1.0   | Release        | Tue 2024-06-18 | 0     |
| 6.1.1   | Bugfix Release | Tue 2024-06-25 | 1     |
| 6.1.2   | Bugfix Release | Tue 2024-07-02 | 1     |
| 6.1.3   | Bugfix Release | Tue 2024-07-16 | 2     |
| 6.1.4   | Bugfix Release | Tue 2024-08-06 | 3     |
| 6.1.5   | Bugfix Release | Tue 2024-09-10 | 5     |

table: KDE / Plasma 6.1 series [release schedule](https://community.kde.org/Schedules/Plasma_6)


# references

::: {#refs}
:::
