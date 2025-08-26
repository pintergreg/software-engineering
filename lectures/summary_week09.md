---
title: week 9 summary 
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

# code quality

::: {.text-align-left}
agile
~ working software over comprehensive documentation

:::

::: {.mt-1 .text-align-left}
software craftmanship
~ not only working software, but also well-crafted software 

:::

:::::::::::: {.columns .mt-1}
::::::::: {.column width="70%" .text-align-left}
well-crafted
~ - high quality
~ - well-designed
~ - validated and verified
~ - tested
~ - code is clean, easy to understand and maintain

:::::::::
::::::::::::


# code smell

> a code smell is a surface indication that usually corresponds to a deeper problem
>
> -- Martin Flower [@fowler2006code]


:::::::::::: {.columns .mt-3}
::::::::: {.column width="40%" .text-smaller}
software rot is the degradation, deterioration, or loss of the use or performance of software over time [@enwiki:1236668404]
:::::::::
::::::::: {.column width="40%" .text-smaller}
**requirement smell**: signs in the requirements that are not necessarily wrong but could be problematic [@femmer2017rapid]

:::::::::
::::::::::::


## clean clode violations as code smells

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- long method
- long parameter list
- naming
    - notation in names
    - inconsistent names
    - uncommunicative names
- comments
- large class
    - possibly do more than one thing
- a function / class does more than one thing
:::::::::
::::::::: {.column width="50%"}
- magic number
- duplicated code
- speculative generality
- dead code
- too complexity comditions
- feature envy
- bad comment
    - obsolete, redundant (noise), commented-out code
:::::::::
::::::::::::

::: {.text-smaller}
source: [@atwood2006code],  [@martin2009clean]
:::


# how to measure code quality?

it is hard to objectively measure the quality of code

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- [number of source lines of code (SLOC)]{.alpha-50}
- style guide compliance [-- is the code clean?]{.fragment data-fragment-index=1 .text-color-secondary}
- [Halstead metrics]{.alpha-50}
- cyclomatic complexity [-- is the code simple?]{.fragment data-fragment-index=1 .text-color-secondary}
- [maintainability index]{.alpha-50}
- test coverage [-- is the code tested?]{.fragment data-fragment-index=1 .text-color-secondary}

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/worker-takes-measurements.svg){width=400}

:::::::::
::::::::::::


## cyclomatic comlexity

- developed by Thomas J. McCabe in 1976
- quantitative measure of the number of linearly independent paths through the source code
- computed using the control-flow graph of the program

defined as:

$$ M = E - N + 2P $$

::: {.text-smaller}
- E: the number of edges of the graph
- N: the number of nodes of the graph
- P: the number of connected components
    - for a single method, P always equals 1
:::


## cyclomatic comlexity -- example

:::::::::::: {.columns}
::::::::: {.column width="40%"}
```python
def calculate_progress(
    finished: int,
    total: int,
    as_percentage: bool,
    foo: bool
) -> float:
    progress = finished / total

    if as_percentage and foo:
        return progress * 100
    else:
        return progress
```

:::::::::
::::::::: {.column width="40%"}
::: {.text-smaller}
activity diagram
:::
![](figures/progress_foo.svg){width=300}

:::::::::
::::::::: {.column width="20%"}
::: {.text-smaller}
control flow
:::
![](figures/progress_foo_2.drawio.svg){width=300}

:::::::::
::::::::::::

::: {}
$$ CC = E - N + 2 $$
$$ CC = 7 - 6 + 2 $$
$$ CC = 3 $$
:::


# WTF per minute

![own drawing based on [Glen Lipka's](https://commadot.com/wtf-per-minute/)](figures/wtf_per_minute.drawio.svg){width=725}


# V model [@forsberg1991relationship]

:::::::::::: {.columns}
::::::::: {.column width="50%" .mt-3}
- each phase has output and a _review process_
    - errors are found at early stage
    - decreases the risk of failure
- testing is done in a hierarchical perspective

:::::::::
::::::::: {.column width="50%"}
:::::: {.r-stack}
![based on [guru99.com's image](https://www.guru99.com/images/6-2015/052715_0904_GuidetoSDLC3.png)](figures/v_model.drawio.svg){width=500}
::::::
:::::::::
::::::::::::


## requirement analysis review

:::::::::::: {.columns}
::::::::: {.column width="40%"}
![user story map](figures/user_statistics/story_map.drawio.svg){width=400}

::: {.text-smaller .mt-3}
- can be discussed / reviewed
- even with a customer representative

:::
:::::::::
::::::::: {.column width="15%" .mt-5}
![](figures/double_arrow.drawio.svg){width=100}

:::::::::
::::::::: {.column width="45%"}
![user story "reviewed" in an issue tracker](figures/user_statistics/user_story_review_2.png){width=400}

:::::::::
::::::::::::


## architecture review

:::::::::::: {.columns}
::::::::: {.column width="40%"}
![C4 diagrams as the output of the high level design](figures/user_statistics/c4_component.excalidraw.svg){width=400}

:::::::::
::::::::: {.column width="15%" .mt-5}
![](figures/double_arrow.drawio.svg){width=100}

:::::::::
::::::::: {.column width="40%"}
![risk storming as a review process](figures/user_statistics/risk_storming.excalidraw.svg){width=400}

:::::::::
::::::::::::


## code review

:::::::::::: {.columns}
::::::::: {.column width="50%"}
```python
def query_progress(user_id:int) -> float:
    # establish connection
    con= sqlite3.connect("data.db")
    # build query
    progress_query = f"""
    SELECT
        lesson / 50.0 AS progress
    FROM activity
    WHERE
        user_id = {user_id} AND
        result = 'success'
    ORDER BY
        lesson DESC
    LIMIT 1
    ;
    """
    # execute query
    res =con.execute(progress_query)
    progress=res.fetchone()[0]
    return progress
```

:::::::::
::::::::: {.column width="50%" .mt-4}
- does not respect style guide
- does 3 things
    - establish DB connection
    - build query
    - execute query
- contains separation comments
- hard coded divisor
    - magic number
:::::::::
::::::::::::


##

::: {.r-fit-text}
every work product can and _should_ be reviewed
:::


# review types by formality

|type       |formality     |led by                           |effort  |documentation                           |
|:---------:|:------------:|:-------------------------------:|:------:|:--------------------------------------:|
|informal   |not formal    |noone                            |minimal |undocumented                            |
|walkthrough|not formal[^1]|authors                          |very low|normal, fault-finding                   |
|technical  |less formal   |trained moderator, not the author|moderate|more detailed                           |
|inspection |most formal   |trained moderator                |high    |thorough; based on standards, checklists|


[^1]:
Sometimes it can be somewhat formal.


# review -- author's perspective

- be humble
    - mind that everybody's code can be improved
    - you are not perfect, accept that you will make mistakes
- open to feedback
- you are not your code
- the goal is to deliver higher quality code, not about arguing who was right
    - you and the reviewer are in the same side
- you and the reviewer are not only talking about the code,
    - you are exchanging best practices and experiences
- you can learn from the review

::: {.text-smaller}
source: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


# review -- reviewer's perspective

- use I-messages
- talk about the code, not the coder
- ask questions instead of making statements
- refer to the behavior, not the traits of the author
- accept that there are different solutions
- respect and trust the author
- mind the OIR-rule of giving feedback
    - [observation, impact, request]{.text-smaller}
- before giving feedback, ask yourself:
    - [is it true? (opinion != truth)]{.text-smaller}
    - [is it necessary? (avoid nagging, focus on the current work product)]{.text-smaller}
    - [is it kind? (no shaming)]{.text-smaller}
- be humble; you are not perfect and you can also improve
- it's fine to say: Everything is good!
- don't forget to praise

::: {.text-smaller}
source: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


# references

::: {#refs}
:::


<!--:::::::::::: {.columns}
::::::::: {.column width="50%" }

:::::::::
::::::::: {.column width="50%"}

:::::::::
::::::::::::-->
