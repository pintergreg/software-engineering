---
title: code review
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

:::::::::::: {.columns}
::::::::: {.column width="30%" .text-size-2 .mt-2}
- informal
- walkthrough
- technical
- inspection

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/impossible-geometric-shapes.svg){width=250}

:::::::::
::::::::::::


## informal

- asking a colleague to have a look at the code
    - they express their opinion and that's all
    - no documentation
    - no process
- pair programming is also a kind of constant informal review


## walkthrough

- not a formal process / review
- led by the author(s)
- the author(s) guide the participants through the work product to achieve a common understanding and to gather feedback
- useful for higher level documents like requirement specification
    - e.g., risk storming, sprint review
    
::: {.text-smaller}
source: [What is Walkthrough in software testing?](http://tryqa.com/what-is-walkthrough-in-software-testing/) [@tryqa_walkthrough]
:::


## technical

- less formal review
- led by the trained moderator or a technical expert
- often performed as a peer review without management participation
- issues are found by experts (e.g., architects, designers)
- technical reviews can vary from quite informal to very formal
    
::: {.text-smaller}
source: [What is Technical review in software testing?](http://tryqa.com/what-is-technical-review-in-software-testing/) [@tryqa_technical]
:::


## (Fagan) inspection [@enwiki:1060854286]

:::::::::::: {.columns .column-gaplessx}
::::::::: {.column width="85%" .text-smaller}
<!--::: {.text-align-left .text-smaller}
- most formal review process
- led by the trained moderators
    - [ends the process if exit criteria is met]{.text-smaller}

:::-->
process phases
~ - **planning**: the inspection is planned by the moderator
~ - **overview meeting**: the author describes the background of the [WP]{.tooltip title="work product"}
~ - **preparation**: each inspector examines the work product to identify possible defects
~ - **inspection meeting**: reader reads through the work product, part by part and the inspectors point out the defects
~ - **rework**: the author makes changes to the work product according to the action plans from the inspection meeting
~ - **follow-up**: the changes are checked to make sure everything is correct

::: {.text-smallers}
roles
~ - **author**: created the work product being inspected
~ - **moderator**: the leader of the inspection, who plans and coordinates it
~ - **reader**: reads through the documents, while the other inspectors then point out defects
~ - **recorder**: documents the defects that are found during the inspection
~ - **inspector**: examines the work product to identify possible defects

:::

:::::::::
::::::::: {.column width="15%"}
![](figures/fagan_inspection.svg){width=150}

:::::::::
::::::::::::


## review types by formality -- summary

|type       |formality     |led by                           |effort  |documentation                            |
|:---------:|:------------:|:-------------------------------:|:------:|:---------------------------------------:|
|informal   |not formal    |noone                            |minimal |undocumented                             |
|walkthrough|not formal[^1]|authors                          |very low|normal, fault-finding                    |
|technical  |less formal   |trained moderator, not the author|moderate|more detailed                            |
|inspection |most formal   |trained moderator                |high    |thorough; based on standards, checklists |

[^1]:
Sometimes it can be somewhat formal.


# code review  -- author's perspective

:::::::::::: {.columns}
::::::::: {.column width="63%"}
- be humble
- open to feedback
- the goal is to deliver higher quality code, not about arguing who was right
    - you and the reviewer are in the same side
- you and the reviewer are not only talking about the code,
    - you are exchanging best practices and experiences
- you can learn from the review

:::::::::
::::::::: {.column width="37%"}
![](figures/publicdomainvectors/programmer-at-laptop.svg){width=300}

:::::::::
::::::::::::

::: {.text-smaller}
based on: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## you are not your code

:::::::::::: {.columns}
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/programmer-at-laptop.svg){width=300}

:::::::::
::::::::: {.column width="20%" .mt-5}
![](figures/not_equal.drawio.svg){width=150}

:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/programming-language.svg){width=300}

:::::::::
::::::::::::

::: {.r-fit-text}
the subject of the code review is not you, but your code
:::

::: {.text-smaller}
based on: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


# code review  -- reviewer's perspective

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-3}
- pay attention to the way you are formulating your feedback
    - phrasing is crucial for your feedback to be accepted
- you and the author are in the same side
- the goal is to deliver higher quality code, not about arguing who was right

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/detective.svg){width=300}

:::::::::
::::::::::::

::: {.text-smaller}
source: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## use I-messages

:::::::::::: {.columns}
::::::::: {.column width="50%"}
formulate your feedback as expressing your personal thoughts

::: {.text-smaller}
- I suggest
- I think
- I would
- I believe
- it's hard for me to
- for me, it seems like

:::

it's hard to argue against personal feelings since they are subjective

:::::::::
::::::::: {.column width="50%" .mt-2}

- You-messages sound like an absolute statement
- which will lead to a defensive stance
- the author would argue with the reviewer instead of thinking about a change
- so the author will be less open for the feedback

:::::::::
::::::::::::

::: {.text-smaller}
source: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## talk about the code, not the coder

:::::::::::: {.columns}
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/programming-language.svg){width=225}

:::::::::
::::::::: {.column width="30%"}
:::::: {.r-stack}
![](figures/publicdomainvectors/programmer-at-laptop.svg){width=225}

![](figures/cross.drawio.svg){width=225}
::::::
:::::::::
::::::::::::

::: {}
wrong
~ you hard-coded the total number of lessons into the query, which is wrong

right
~ the total number of lessons is hard-coded into the query, which may raise issues later
:::

::: {.text-smaller}
based on: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## ask questions

:::::::::::: {.columns}
::::::::: {.column width="75%"}
- asking questions feels less like a criticism as the author can answer the question
    - it can trigger a thought process which can lead to accepting the feedback
    - or the author can come up with a better solution
- by asking questions you can reveal the intention behind a certain design decision
    - there may be a good reason for it
    
:::::::::
::::::::: {.column width="25%"}
![](figures/publicdomainvectors/question-mark-color.svg){width=150}

:::::::::
::::::::::::

::: {.text-smaller}
source: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## refer to the author's behavior, not their traits

wrong
~ You are sloppy when it comes to following the style guide.
~ Can't you just configure your [IDE]{.tooltip title="integrated development environment"} properly?

right
~ I believe that you should pay more attention to the style guide.
~ Try to enable the auto-formatting in your [IDE]{.tooltip title="integrated development environment"}.

::: {.fragment .wide-quote .mt-3}
- usually  it's not required to talk about the author at all in a code review
- use I-messages, talk about the code or ask questions
:::

::: {.text-smaller}
based on: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## OIR-rule of giving feedback

Observation
~ Describe your observations in an objective and neutral way. Refer to the behavior if you have to talk about the author. Using an I-message is often useful here.
~ [e.g., "This method has 100 lines."]{.text-smaller}

Impact
~ Explain the impact that the observation has on you. Use I-messages.
~ [e.g., "This makes it hard for me to grasp the essential logic of this method."]{.text-smaller}

Request
~ Use an I-message to express your wish or proposal.
~ [e.g., "I suggest extracting the low-level-details into subroutines and give them expressive names."]{.text-smaller}

::: {.text-smaller}
source: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## three filters for feedback

always ask yourself, if your feedback is true, necessary and kind

[(from April Wensel [@wensel2018compassionate] via [@hauer2018code])]{.text-smaller}

- is it true?
    - [avoid statements assuming an absolute truth]{.text-smaller}
    - [avoid the words "right", "wrong", "never", "always" and "should"]{.text-smaller}
    - [refer to your opinion instead]{.text-smaller}
- is it necessary?
    - [does the ~~demanded~~ requested change make the reviewed code better]{.text-smaller}
- it it kind?

::: {.text-smaller}
source: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## praise

- don't forget to express your appreciation if you have reviewed good code
- praising doesn't hurt you but will motivate the author
- however, be specific and separate the prasie from the criticism

::: {.text-smaller}
based on: [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) [@hauer2018code]
:::


## looks good to me

::: {.text-align-left}
- it's okay to say: "Everything is good!"
- no code change request is a valid outcome of a code review
    - you don't have to find something in the code
- a code can be not just okay, but worth to learn from it

:::

::: {.fragment .text-align-left}
- however, when a reviewer too often says LGTM, it becomes fishy
    - especially if the review code turns out to be problematic later regardless the positive feedback

:::


# a review process

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="60%"}
![](figures/proc3.png){width=500}

:::::::::
::::::::: {.column width="40%" .mt-5 .text-smaller}
- is it understandable (clear)
- is it clean (no code smells)
- does it match the task?
- does it fulfill the task?
    - every [DoD]{.tooltip title="Definition of Done"} point covered?
- is it possible to improve?
:::::::::
::::::::::::


#

:::::::::::: {.columns}
::::::::: {.column width="60%" .text-smaller}
```c
#include <stdio.h>
main()
{
    int a,b,c;
    int count = 1;
    for (b=c=10;a="- FIGURE?, UMKC,XYZHello Folks,\
    TFy!QJu ROo TNn(ROo)SLq SLq ULo+\
    UHs UJq TNn*RPn/QPbEWS_JSWQAIJO^\
    NBELPeHBFHT}TnALVlBLOFAkHFOuFETp\
    HCStHAUFAgcEAelclcn^r^r\\tZvYxXy\
    T|S~Pn SPm SOn TNn ULo0ULo#ULo-W\
    Hq!WFs XDt!" [b+++21]; )
    for(; a-- > 64 ; )
    putchar ( ++c=='Z' ? c = c/ 9:33^b&1);
    return 0;
}
```

::: {.fragment data-fragment-index=1}
via [How does this code generate the map of India?](https://stackoverflow.com/questions/3533348/how-does-this-code-generate-the-map-of-india)
:::

:::::::::
::::::::: {.column width="40%" .text-smaller .fragment data-fragment-index=1}
![](figures/india.png)

:::::::::
::::::::::::

##

:::::::::::: {.columns}
::::::::: {.column width="60%" .text-smaller}
```c
#include "stdio.h"
int main (void) {
    int a=10, b=0, c=10;
    char* bits ="TFy!QJu ROo TNn(ROo)SLq SLq ULo+UHs UJq TNn*R\
    Pn/QPbEWS_JSWQAIJO^NBELPeHBFHT}TnALVlBLOFAkHFOuFETpHCStHAU\
    FAgcEAelclcn^r^r\\tZvYxXyT|S~Pn SPm SOn TNn ULo0ULo#ULo-WH\
    q!WFs XDt!";
    a = bits[b];
    while (a != 0) {
        a = bits[b];
        b++;
        while (a > 64) {
            a--;
            if (++c == 'Z') {
                c /= 9;
                putchar(c);
            } else {
                putchar(33 ^ (b & 0x01));
            }
        }
    }
    return 0;
}
```

::: {}
[a less obfuscated version](https://stackoverflow.com/a/3533420/4737417) (with explanation)<br>by [bta](https://stackoverflow.com/users/79566/bta) CC&nbsp;BY-SA&nbsp;2.5
:::

:::::::::
::::::::: {.column width="40%" .text-smaller}
![](figures/india_cleaner.png)

:::::::::
::::::::::::


# references

::: {#refs}
:::
