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

# what to automatize?

:::::::::::: {.columns}
::::::::: {.column width="60%" .text-align-left}
::: {.r-fit-text}
everything
:::

more precisely, **repetitve tasks** | scripting: writing relatively short and simple code to automatize an otherwise manual process


:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/robotic-arm-assembles-a-puzzle.svg){width=300}

:::::::::
::::::::::::


## in a software development context

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-2}
- style guide compliance
- code smell finding
- code quality measurement
- review
- building
- testing
- deployment

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/robotic-arm-assembles-a-puzzle.svg){width=300}

:::::::::
::::::::::::


## linting

:::::::::::: {.columns}
::::::::: {.column width="75%"}
- a linter in modern editors behaves like a spell checker in a word processor
    - gives immediate feedback on syntax errors, styling issues or bad practices
- can detect some code smells
- traditionally linters were developed for languages, then linter plugins for editors
    - so language support in editors were not evident
    - Language Server Protocol (LSP) was developed (originally at Microsoft), providing a common interface for linters

:::::::::
::::::::: {.column width="25%"}
![](figures/publicdomainvectors/app-development-concept.svg){width=300}

:::::::::
::::::::::::


## auto formatting

- there are automatic code formatters for more and more languages
    - that can reformat the source code to align with the style guide
- usually triggered by saving the file
- usually configurable to align with organization / project specific rules
- some examples:
    - Python: [ruff](https://docs.astral.sh/ruff/formatter/) (among others)
    - Ruby: [rubocop](https://rubocop.org/)
    - Go: [gofmt](https://pkg.go.dev/cmd/gofmt)
    

## well configured editor

:::::::::::: {.columns}
::::::::: {.column width="75%"}
- can help keeping the feedback loop fast
    - auto formatter
    - linter
    - running test
- decrease cost
    - immediate feedback
    - less refactoring (later), less review finding
    - developers can focus on non-automatable tasks

:::::::::
::::::::: {.column width="25%" .mt-2}
![](figures/publicdomainvectors/programming-language.svg){width=300}

:::::::::
::::::::::::

::: {.fragment .mt-3}
importance of personal preferences!
:::

::: notes
that is why I previously said that trust in your IDE
:::


# version control systems

:::::::::::: {.columns}
::::::::: {.column width="55%" .mt-2}
- scrum development team
- multiple task on the sprint backlog
- developers start to work on different tasks
    - the time to complete a task varies
- work items need to be merged to the common code base / repository
- version control systems are used to solve this issue
:::::::::

::::::::: {.column width="40%"}
![](figures/publicdomainvectors/scrum-task-board.svg){width=150}

:::::::::::: {.columns}
::::::::: {.column width="33%"}
![](figures/publicdomainvectors/developer-at-work.svg){width=150}

:::::::::
::::::::: {.column width="33%"}
![](figures/publicdomainvectors/workplace-rpogrammer.svg){width=150}

:::::::::
::::::::: {.column width="33%"}
![](figures/publicdomainvectors/programming-vector.svg){width=150}

:::::::::
::::::::::::
:::::::::
::::::::::::


# interruption

:::::::::::: {.columns}
::::::::: {.column width="33%"}
![](figures/borrowed/ProgrammerInterrupted.webp){style="width: 300px; height: 430px; object-fit: cover; object-position: 100% 0;"}

:::::::::
::::::::: {.column width="33%" .fragment}
![](figures/borrowed/ProgrammerInterrupted.webp){style="width: 300px; height: 323px; object-fit: cover; object-position: 100% -430px;"}

:::::::::
::::::::: {.column width="33%" .fragment}
![](figures/borrowed/ProgrammerInterrupted.webp){style="width: 300px; height: 350px; object-fit: cover; object-position: 100% -751px;"}

:::::::::
::::::::::::


## interruption

- the greatest "enemy" of a developer is interruption
- the code is one thing, the logic behind it is another
    - takes time to understand
- context switching is costly
    - switching between tasks
    - that is why it is advisable to define small tasks during the sprint planning
        - 1--4 hours, but ideally closer to 1
        - preventing interruption
<!--     - [also withing a OS / CPU]{.text-smaller} -->


## the cost of interruption

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-3}
- according to a study, the average lost time per major interruption is **23 minutes** [@mark2008cost]
    - for developers, it could be far worse
- "getting back to the exact state of mind you were at right before an interruption is nearly impossible" [@to2018cost]
- planned and unplanned interruptions

:::::::::
::::::::: {.column width="40%"}
![&#169; [Ash Lamb](https://ashlamb.com/)<br>used with the author's permission](figures/borrowed/quick_call.jpg){width=350}

:::::::::
::::::::::::

::: {.text-smaller}
source: [The Cost of Interruption for Software Developers](https://www.brightdevelopers.com/the-cost-of-interruption-for-software-developers/) -- by Steven To [@to2018cost]
:::


## planned and unplanned interruptions

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="50%"}
**unplanned**

- someone asks about something or to do something
    - usually a small task
        - informal review, advice, etc.
- mitigation
    - wear headphones (in open offices)
    - notify in advance
:::::::::
::::::::: {.column width="50%" .fragment}
**planned**

- meetings, including standup
- standup is usually the first thing in a workday, not to divide the work time until lunch
- a wrongly placed meeting can be even worse than an unplanned interruption
    - [you have to keep in mind that you have a meeting, cannot start anyting serious]{.text-smaller}
- mitigation
    - [schedule small, easy tasks before meeting]{.text-smaller}
:::::::::
::::::::::::

::: {.text-smaller}
source: [The Cost of Interruption for Software Developers](https://www.brightdevelopers.com/the-cost-of-interruption-for-software-developers/) -- by Steven To [@to2018cost]
:::


# continuous integration


## build script

example: [build script](https://github.com/pintergreg/software-engineering/blob/main/.github/workflows/main.yaml){target="_blank"} of the course website


# continuous deployment


# versioning

- a software is identified by a version number


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

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/calver.drawio.svg){width=450}

:::::::::
::::::::: {.column width="50%" .mt-4}
format examples:

- YYYY.MINOR.PATCH
    - [micro is used instead of patch]{.text-smaller}
- YYYY.MM.MINOR.PATCH
:::::::::
::::::::::::

"*CalVer* is a versioning convention based on your project's release calendar, instead of arbitrary numbers." | [calver.org](https://calver.org)


## ZeroVer: 0-based versioning

"Your software's major version should never exceed the first and most important number in computing: zero." | [0ver.org](https://0ver.org)

- e.g.: **0.4.1**
- popular among open source software projects
    - [some may reach 1.0.0 eventually]{.text-smaller}

::: {.text-smaller .mt-2}
[[semver]{.tooltip title="semantic versioning"}](https://semver.org): "If your software is being used in production, it should probably already be 1.0.0." 
:::


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
