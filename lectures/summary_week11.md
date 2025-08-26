---
title: week 11 summary 
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

# what to automatize?

:::::::::::: {.columns}
::::::::: {.column width="60%" .text-align-left}
*repetitve tasks* of

- style guide compliance
- code smell finding
- code quality measurement
- review
- building
- testing
- deployment

::: {.text-smaller}
scripting: writing relatively short and simple code to automatize an otherwise manual process
:::
:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/robotic-arm-assembles-a-puzzle.svg){width=300}

:::::::::
::::::::::::


# local automatization based on the code editor

:::::::::::: {.columns .text-smaller}
::::::::: {.column width="50%" }
**linting**

- a linter in modern editors behaves like a spell checker in a word processor
    - gives immediate feedback on syntax errors, styling issues or bad practices
- can detect some code smells
:::::::::
::::::::: {.column width="50%"}
**code formatting**

- reformat the source code to align with the style guide
- there are code formatters for many languages
- usually triggered by saving the file

:::::::::
::::::::::::

:::::::::::: {.columns .mt-2}
::::::::: {.column width="75%" .mt-2}
- needs a well configured editor (personal preferences)
- can help keeping the feedback loop fast
- decrease cost
- developers can focus on non-automatable tasks
:::::::::
::::::::: {.column width="25%"}
![](figures/publicdomainvectors/programming-language.svg){width=250}
:::::::::
::::::::::::


# continuous integration (CI)

::: {.text-smaller}
> Continuous Integration is a software development practice where each member of a team merges their changes into a codebase together with their colleagues changes at least daily. 
>
> -- Martin Fowler [@fowler2024continuous]

:::

:::::::::::: {.columns}
::::::::: {.column width="50%" }
::: {.text-smaller}
- emerged from extreme programming
- considered an agile approach
- gives immediate feedback
    - the integration (merging) will fail if two branches are not compatible
    - and build the integrated software
- also gives opportunity to do testing on the built software...
:::
:::::::::
::::::::: {.column width="50%"}
![feature branching](figures/branching.svg){width=625}
:::::::::
::::::::::::


## continuous integration environment

![](figures/ci_environment.drawio.svg){width=700}

- scheduled build
- nightly build: scheduled build during night time because for large software a full build (with all tests) could take hours


## build script

:::::::::::: {.columns}
::::::::: {.column width="65%" .mt-4}
- traditionally called build script
- responsible not only for building the software
- but also for running tests, generating reports
    - code coverage
- and even for packaging the software

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/robotic-arm-assembles-a-puzzle.svg){width=300}

:::::::::
::::::::::::


# continuous deployment (CD)

![](figures/cd_environment_schedule.drawio.svg){width=700}

::: {.text-smaller}
- "Continuous Deployment means the product is automatically released to production whenever it passes all the automated tests in the deployment pipeline." -- Martin Fowler [@fowler2024continuous]
- CD environment extension of a [CI]{.tooltip title="continuous integration"} environment
    - triggers are the same
    - deployment is another stage in the _build script_
:::


## blue–green deployment [@enwiki:1249842339]

![](figures/blue_green_deployment_v2.drawio.svg){width=700}

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="70%"}
::: {.text-smaller}
- two servers are maintained ("blue" and "green")
    - [expensive]{.text-smaller}
- at a given time, only one server is handling public request
- the other can be accessed only from a private network
- changes applied to the non-live server and verified
- when verified, the non-live server is swapped with the live server
:::
:::::::::
::::::::: {.column width="30%"}
![](figures/test_pyramid_manual.drawio.svg){width=200 .no-margin}

:::::::::
::::::::::::


## shadow deployment

![](figures/shadow_deployment.drawio.svg){width=650}

- two servers are maintained ("live" and "shadow")
- for testing the performance and stability requirements
    - on success, the release can be deployed to the live server as well
- specialized strategy, complex and (relatively) expensive to set up


## canary deployment

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- deployment in an incremental fashion
- starts with a small number of users
- and continues until 100% is reached
- allows to test updates in live environment
    - on small groups of users
    - before deploying to many users
    - may involve telemetry
:::::::::
::::::::: {.column width="40%"}
![](figures/canary_deployment.drawio.svg){width=400}

:::::::::
::::::::::::

::: {.fragment .mt-2}
**A/B testing** is more of a testing approach than a deployment technique, but it works similarly to canary deployment.
It involves reviewing two versions of updates in small set of users to identify which version perform better. [@kazim2023what]
:::


# devops

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="55%"}
- software [dev]{.text-color-secondary}elopment + IT [op]{.text-color-secondary}eration[s]{.text-color-secondary}
    - [collaboration]{.text-smaller}
- who is responsible for what?
- agile mindset, set of principles [@gitlab2022four]
    - [automation of the [SDLC]{.tooltip title="software development lifecycle"}]{.text-smaller}
    - [collaboration and communication]{.text-smaller}
    - [continuous improvement]{.text-smaller}
    - [focus on user needs with short feedback loops]{.text-smaller}
- relies on automatization, [CI]{.tooltip title="continuous integration"} and [CD]{.tooltip title="continuous deployment"}
- to build, test and release better software
    - [frequently, reliably, rapidly]{.text-smaller}

:::::::::
::::::::: {.column width="45%"}
![by [Kharnagy](https://commons.wikimedia.org/wiki/File:Devops-toolchain.svg) | [CC&nbsp;BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.en)](figures/borrowed/Devops-toolchain.svg){width=400}

:::::::::
::::::::::::

::: {.text-smaller .mt-2}
further reading: [11 DevOps Principles and Practices to Master: Pro Advice](https://roadmap.sh/devops/principles) - by Fernando Doglio
:::

# automatized review

:::::::::::: {.columns}
::::::::: {.column width="65%" .mt-2}
- using [CI]{.tooltip title="continuous integration"} environment
- do static code analysis
    - [analyzing the code without execution]{.text-smaller}
    - [searching for syntax errors, styling issues, bad practices or code smells]{.text-smaller}
- run test suite
- vulnerability alerts
    - [uses package manager's dependency info to checks for vulnerabilities ([CVE]{.tooltip title="Common Vulnerabilities and Exposures"}) among dependencies]{.text-smaller}
- generate review report from the findings

::: {.fragment .mt-2}
::: {.text-color-secondary}
should not replace human reviewing
:::
::: {.text-smaller}
just decrease the work by automatizing trivial tasks 
:::
:::
:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/machine-learning.svg){width=300}

:::::::::
::::::::::::


# semantic versioning

:::::::::::: {.columns}
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


## the cost of interruption

:::::::::::: {.columns}
::::::::: {.column width="65%"}
- the greatest "enemy" of a developer is interruption
    - ["getting back to the exact state of mind you were at right before an interruption is nearly impossible" [@to2018cost]]{.text-smaller}
- according to a study, the average lost time per major interruption is **23 minutes** [@mark2008cost]
    - [for developers, it could be worse]{.text-smaller}
    - [according to another study it is at least 15 minutes [@parnin2013programmer]]{.text-smaller}
- define small tasks during the sprint planning to preventing interruption
    - [1--4 hours, but ideally closer to 1]{.text-smaller}
    - [a programmer probably get one uninterrupted 2-hour session in a day [@parnin2013programmer]]{.text-smaller}

:::::::::
::::::::: {.column width="35%"}
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


## techniques to minimize context switching

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="50%"}
- time blocking
    - divide workday into blocks
- time batching
    - do similar tasks in a batch
- prioritize tasks
- tackle the biggest task first in the morning
- turn off notifications
- adopt asynchronous communication
    - e-mail, documentation, [ADR]{.tooltip title="architecture decision record"}

::: {.text-smaller}
source: [The high price of context switching for developers & ways to avoid it](https://pacohq.com/blog/guide/the-high-price-of-context-switching-for-developers/) [@pande2021high]
:::

:::::::::
::::::::: {.column width="50%"}
![ideal, very bad, much better schedule](figures/time_blocking.drawio.svg){width=400}
:::::::::
::::::::::::

# references

::: {#refs}
:::


<!--:::::::::::: {.columns}
::::::::: {.column width="50%" }

:::::::::
::::::::: {.column width="50%"}

:::::::::
::::::::::::-->
