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


## file sharing issue

:::::::::::: {.columns}
::::::::: {.column width="25%"}
![read the same file](figures/vcs_read.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![make changes](figures/vcs_change.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![Arthur writes first](figures/vcs_write.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![Ford overwrites with his version](figures/vcs_overwrite.drawio.svg){width=200}

:::::::::
::::::::::::

::: {.text-smaller}
the figures are based on Figure 2.2 of the [TortoiseSVN documentation](https://tortoisesvn.net/docs/release/TortoiseSVN_en/help-onepage.html)
:::


## lock-modify-unlock solution

:::::::::::: {.columns}
::::::::: {.column width="25%"}
![lock before read](figures/vcs_lock.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![cannot read while locked](figures/vcs_locked.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![writes and unlock](figures/vcs_unlock.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![Ford locks and reads](figures/vcs_relock.drawio.svg){width=200}

:::::::::
::::::::::::

::: {.text-align-left .mt-3 .fragment}
one developer can edit a file at the same time -- not very effective
:::

::: {.text-smaller}
the figures are based on Figure 2.3 of the [TortoiseSVN documentation](https://tortoisesvn.net/docs/release/TortoiseSVN_en/help-onepage.html)
:::


## copy-modify-merge solution

:::::::::::: {.columns}
::::::::: {.column width="25%"}
![lock before read](figures/vcs_read.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![make changes](figures/vcs_change.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![Arthur writes first](figures/vcs_write.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![Ford cannot write due to the change](figures/vcs_cannotwrite.drawio.svg){width=200}

:::::::::
::::::::::::

::: {.text-smaller}
the figures are based on Figure 2.4 of the [TortoiseSVN documentation](https://tortoisesvn.net/docs/release/TortoiseSVN_en/help-onepage.html)
:::


## copy-modify-merge solution #2

:::::::::::: {.columns}
::::::::: {.column width="25%"}
![compare the latest to his own](figures/vcs_compare.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![merged the changes](figures/vcs_merged.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![publish merged](figures/vcs_publish_merged.drawio.svg){width=200}

:::::::::
::::::::: {.column width="25%"}
![changes shared](figures/vcs_changes_shared.drawio.svg){width=200}

:::::::::
::::::::::::

::: {.text-align-left .mt-3 .fragment}
example: **git**, mercurial
:::

::: {.text-smaller}
the figures are based on Figure 2.5 of the [TortoiseSVN documentation](https://tortoisesvn.net/docs/release/TortoiseSVN_en/help-onepage.html)
:::


## centralized vs. distributed version control system

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![centralized](figures/vcs_centralized.drawio.svg){width=400}

::: {.text-align-left .text-smaller .mt-3}
example: subversion
:::
:::::::::
::::::::: {.column width="50%"}
![distributed](figures/vcs_distributed.drawio.svg){width=400}

::: {.text-align-left .text-smaller .mt-3}
example: **git**, mercurial
:::
:::::::::
::::::::::::

::: {.text-smaller}
the figures are based on [Version control concepts and best practices](https://homes.cs.washington.edu/~mernst/advice/version-control.html) - by Michael Ernst [@ernst2012version]
:::


# continuous integration (CI)

<!--:::::::::::: {.columns}
::::::::: {.column width="70%"}-->
![](figures/ci.drawio.svg){width=625}

<!--:::::::::
::::::::: {.column width="30%" .text-smaller}
- extreme programming
- agile
- immediate feedback

:::::::::
::::::::::::-->


## continuous integration environment

![](figures/ci_environment.drawio.svg){width=700}

::: notes
What happens here is that the developer pushes a change to the version control server, which can  be(depends on the configuration) a trigger.
Based on the trigger the CI environment start a runner.
A runner can be, for example, a linux instance running in a virtual machine or in a container.
In the newly started environment, the changes are fetched.
Considering git as a version control system, fetching means clone and checkout operations.
As the CI environment is "empty", in a sense that it does not contain any of the software code, the code repository has to be cloned every time.
Then, the right version, defined by the trigger should be selected using the `git checkout` command.
After the software version to be tested is available, the build script should be executed.
Optionally with static code analysis, tests, and so on, then the reports are generated.

If the build or the tests did not succeed a notification is sent to the developer(s), and any other stakeholder who are subscribed.
If the build (and tests) succeeded, notification are usually only sent if the previous build failed, preventing unnecessary noise.
:::


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

example: [build script](https://github.com/pintergreg/software-engineering/blob/main/.github/workflows/main.yaml){target="_blank"} of the course website


## scheduled build

![](figures/ci_environment_schedule.drawio.svg){width=700}

::: notes
The trigger can be also be a scheduler, so a build / test running can be executed without explicit change of a new push.
:::


## nightly build

:::::::::::: {.columns}
::::::::: {.column width="50%" .mt-2}
- scheduled build during night time
- typically includes a smoke test
- building a the latest version of a software, on a daily basis
- originally scheduled to night time because for large software a full build (with all tests) could take hours

:::::::::
::::::::: {.column width="50%"}
![](figures/publicdomainvectors/city-night-landscape.svg){width=300}

:::::::::
::::::::::::

::: notes
also known as daily build
:::


# continuous deployment

:::::::::::: {.columns}
::::::::: {.column width="65%" .mt-2}
- continuous integration ensures everyone integrates their code to the mainline [@fowler2024continuous]
- "Continuous Deployment means the product is automatically released to production whenever it passes all the automated tests in the deployment pipeline." -- Martin Fowler [@fowler2024continuous]

:::::::::
::::::::: {.column width="35%"}
![](figures/publicdomainvectors/industrial-conveyor-belt.svg){width=300}

:::::::::
::::::::::::


## continuous deployment environment

![](figures/cd_environment_schedule.drawio.svg){width=700}

- extension of a continuous integration environment
- deployment is another stage in the _build script_
- same triggers as in a [CI]{.tooltip title="continuous integration"} environment (not just the scheduler)


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


## devops

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="55%"}
- software [dev]{.text-color-secondary}elopment + IT [op]{.text-color-secondary}eration[s]{.text-color-secondary}
    - [collaboration]{.text-smaller}
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


# what tools to use?

:::::::::::: {.columns}
::::::::: {.column width="75%"}
::: {.text-smaller}
- [CI]{.tooltip title="continuous integration"} and [CD]{.tooltip title="continuous deployment"} became a fundamental part of software development
    - got integrated into services like GitHub, GitLab, BitBucket, JetBrains Space
- some solutions:
    - Jenkins
        - open source, self hosted
    - GitHub Actions
        - integrated to code hosting, free options
        - example: [course repository](https://github.com/pintergreg/software-engineering/actions)
    - GitLab Pipelines
        - integrated to code hosting, free options
    - Travis CI
        - free for open source projects
    - Circle CI
        - free options
:::
:::::::::
::::::::: {.column width="25%"}
![Jenkins](figures/borrowed/Jenkins_logo.svg){width=75}

![GitHub Actions](figures/borrowed/Font_Awesome_5_brands_github.svg){height=60}

![GitLab Pipelines](figures/borrowed/GitLab_icon.svg){height=50}

:::::::::
::::::::::::

::: {.text-small .mt-2}
- [Jenkins logo](https://commons.wikimedia.org/wiki/File:Jenkins_logo.svg) -- The Jenkins project [http://jenkins-ci.org/](http://jenkins-ci.org/) | [CC&nbsp;BY-SA](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
- [GitHub icon](https://commons.wikimedia.org/wiki/File:GitLab_icon.svg) -- Font Awesome Free 5.4.1 by \@fontawesome - [https://fontawesome.com](https://fontawesome.com) | [CC&nbsp;BY](https://creativecommons.org/licenses/by/4.0/deed.en)
- [GitLab icon](https://commons.wikimedia.org/wiki/File:GitLab_icon.svg) by 292Jacob | [CC&nbsp;BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.en)
:::


# automatized review

:::::::::::: {.columns}
::::::::: {.column width="65%" .mt-2}
- using [CI]{.tooltip title="continuous integration"} environment
- do static code analysis
    - analyzing the code without execution
    - searching for syntax errors, styling issues, bad practices or code smells
- run test suite
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


## automatized review -- example

- [CI]{.tooltip title="continuous integration"} services integrated into the code hosting / developer platforms
- code changes can ba annotated by automatized review findings
    -  [usually at a pull request level]{.text-smaller}
- a bit slower feedback than running static analysis or test locally

::: {.mt-3}
![source: [go-gitea/gitea at GitHub, pull request #31768](https://github.com/go-gitea/gitea/pull/31768/files)](figures/github_automated_review.png){width=850}
:::


## vulnerability alerts

:::::::::::: {.columns}
::::::::: {.column width="65%" .mt-1}
- Common Vulnerabilities and Exposures (CVE)
    - a dictionary of common names (i.e., CVE Identifiers) for publicly known information security vulnerabilities [@enwiki:1256072917]
    - Apple's "goto fail" issue is officially called CVE-2014-1266
- GitHub [Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
    - uses package manager
    - e.g., cargo (Rust), npm (JS), nuget (C#), maven (Java), pip (Python)
    - checks dependencies for vulnerabilities

:::::::::
::::::::: {.column width="35%" .text-smaller}
```toml
[tool.poetry.dependencies]
python = "^3.12"
numpy = "^1.26.3"
pandas = "^2.2"
geopandas = "^1.0"
networkx = "^3.2.1"
osmnx = "^1.6.0"
matplotlib = "^3.8.2"
seaborn = "^0.13.0"
contextily = "^1.3.0"
opencv-python = "^4.9.0"
pyaml = "^23.9.7"
pyogrio = "^0.7"
pyarrow = "^15.0.0"
scipy = "^1.12.0"
haversine = "^2.8.1"
mapclassify = "^2.6.1"
openpyxl = "^3.1.2"
ecomplexity = "^0.5.2"
structlog = "^24.1.0"
h3 = "^3.7.7"
pandarallel = "^1.6.5"
jinja2 = "^3.1.4"
tabulate = "^0.9.0"
```
::: {.text-smaller}
Python dependencies managed by poetry
:::
:::::::::
::::::::::::

::: notes
GitLab also has a similar solution
:::


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


# release versioning

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- a software release is identified by a version number
- often seen as an arbitrary number

::: {.text-smaller .mt-5}
pre-releases

- **alpha**: incomplete feature-wise, external release is uncommon for proprietary software
    - whitebox testing

- **beta**: the software is feature-complete but contains several known or unknown bugs
    - blackbox testing

- **rc**: release candidate, final touches
    - highest level testing
:::
:::::::::
::::::::: {.column width="51%" .text-smaller}
:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
![](figures/publicdomainvectors/businessman-running-to-finish.svg){width=300}
:::
::: {.fragment data-fragment-index=1}
- odd number for development (4.1), even for stable (4.2)
- Chromium: 131.0.6778.69
- after GNOME 3.38, the "3." was dropped and GNOME 40 vas released
    - [Java 1.6, 1.7, ~~1.8~~, 8, 9, 10...]{.text-smaller}
- Linux 5.19, 6.0
    - ["So, as is hopefully clear to everybody, the major version number change is more about me running out of fingers and toes than it is about any big fundamental changes." -- [Linux Torvalds](https://lkml.iu.edu/hypermail/linux/kernel/2210.0/00685.html)]{.text-smaller}
- since version 3, TeX has used an idiosyncratic version numbering system [@enwiki:1253226188]
    - [where updates have been indicated by adding an extra digit at the end of the decimal, so that the version number asymptotically approaches π]{.text-smaller}
    - [last version is 3.141592653 (released in 2021)]{.text-smaller}
:::
::::::
:::::::::
::::::::::::


## semantic versioning

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/semver.drawio.svg){width=500}

:::::::::
<!--::::::::: {.column width="50%" .text-medium .mt-3}
- **alpha**: incomplete feature-wise, external release is uncommon for proprietary software
    - whitebox testing

- **beta**: the software is feature-complete but contains several known or unknown bugs
    - blackbox testing

- **rc**: release candidate, final touches
    - highest level testing
:::::::::-->
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
