---
title: Software Development Life Cycle
author: Gergő Pintér
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

# content

- software development life cycle
- waterfal
- V model
- incremental
- agile
    - SCRUM
- kanban

# waterfall model

![](figures/waterfall.svg){width=750}

::: notes
- earliest SDLC model
- the origin of the name is that the progress flows in one direction, downwards like a waterfall
- not iterative, not flexible
- linear, sequential phases
:::

## criticism

- Clients may not know exactly what their requirements are before they see working software and so change their requirements, leading to redesign, redevelopment, and retesting, and increased costs. [@parnas1986rational]
In most cases the people who comission the building of the a software system do not know exactly what they want and are unable to tell us all they know.

## modified waterfall model

![based on Figure 4. of [@royce1970managing]](figures/waterfall_modified.svg){width=750}


# V model [@forsberg1991relationship]

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- still rigid
- each phase has output and a review process
    - errors are found at early stage
    - decreases the risk of failure
- large to small: testing is done in a hierarchical perspective

:::::::::
::::::::: {.column width="50%"}
:::::: {.r-stack}
![based on [guru99.com's image](https://www.guru99.com/images/6-2015/052715_0904_GuidetoSDLC3.png)](figures/v_model.drawio.svg){width=500}
::::::
:::::::::
::::::::::::

::: notes
The *unit testing* will be discussed later in the testing chapter. For now it is enough to know that it is a tool to test the lower level part of the software.
:::

# iterative model

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- software is built incrementally,
    - with each iteration adding new features or refining existing ones
- possible to get feedback after each iteration
- can be rigid within an iteration

:::::::::
::::::::: {.column width="50%"}
:::::: {.r-stack}
![](figures/iterative.drawio.svg){width=500}
::::::
:::::::::
::::::::::::


# agile model

:::::::::::: {.columns}
::::::::: {.column width="50%"}
- continuous collaboration and fast response to change, while the iterative model takes a more gradual approach, building up the final product over multiple iterations
- scrum is an agile methodology

:::::::::
::::::::: {.column width="50%"}
:::::: {.r-stack}
![](figures/agile.drawio.svg){width=500}
::::::
:::::::::
::::::::::::


# the agile manifesto

> We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value:
>
> - **Individuals and interactions** over processes and tools
> - **Working software** over comprehensive documentation
> - **Customer collaboration** over contract negotiation
> - **Responding to change** over following a plan
>
> That is, while there is value in the items on the right, we value the items on the left more.

[agilemanifesto.org](https://agilemanifesto.org/)

. . .

[Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html)

::: notes
- The agile does not mean a specific methodology, so SCRUM is not the only agile approach (the course will cover SCRUM later), and agile is not the only approach.
<!-- - Processes and protocols are established with good reason, but they cannot be more important than people. -->
- The documentation is still important, the course will cover later what and how should be documented, but the point is no matter how much documentation you have, if the software does not work as expected.
- In the business world, contracts are important, especially contract violations and the penalty clauses, but customers should be treated as a partner, and collaborative communication should come first, before giving more jobs to the lawyers.
- Planing is import (even having a plan B is often advisable), but the world is in constant change, so flexibility is required. Compared to the waterfall, which requires you to follow the initial plan, agile allows changes during the development. Remember, programming is more like gardening.

There are also twelve principles behind the Agile Manifesto, that provides some more detailed interpretation for the values. 
:::

## 1. Principle behind the Agile Manifesto

> Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.

. . .

> Release early. Release often. And listen to your customers.
>
> Eric S. Raymond: The Cathedral and the Bazaar (1997)

::: notes
The "release early, release often mantra" is quite widespread, but I rarely see the "listen to your customers" part.
One of the main principle of agile is to collaborate with the customer, who should be involved into the development. Show them the software as soon as possible and ask for feedback.
Feedback means there will be change requests.
:::

## 2. Principle behind the Agile Manifesto

> Welcome changing requirements, even late in development. <span class=".fragment">Agile processes harness change for the customer's competitive advantage.<span>
>
> <cite>[Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html)</cite>

::: notes
A feedback is something that represent value, so change requests should be welcomed.
Satisfing the customer is good for the business.
:::

## 3. Principle behind the Agile Manifesto

> Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.

::: notes
This is a significant seep-up compared to the waterfall, where it could even take years while the customer sees something in action.
And if you consider this as a users' perspective, small changes are easier to adapt, than drastic restructurings which are comparable to learn a completely new software.
:::

## 4. Principle behind the Agile Manifesto

> Business people and developers must work together daily throughout the project.

::: notes
Polarization is not good.
There should not be sides, business people and developers must not consider the other foes.
They work together for the same goal.
:::

## 5. Principle behind the Agile Manifesto

> Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done.

## 6. Principle behind the Agile Manifesto

> The most efficient and effective method of conveying information to and within a development team is face-to-face conversation.

::: notes
While it is not untrue. I consider it outdated from some aspect.
:::

## 7. Principle behind the Agile Manifesto

> Working software is the primary measure of progress.

::: notes
:::

## 8. Principle behind the Agile Manifesto

> Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely.

::: notes
:::

## 9. Principle behind the Agile Manifesto

> Continuous attention to technical excellence and good design enhances agility.

::: notes
:::

## 10. Principle behind the Agile Manifesto

> Simplicity--the art of maximizing the amount of work not done--is essential.

::: notes
:::

## 11. Principle behind the Agile Manifesto

> The best architectures, requirements, and designs emerge from self-organizing teams.

::: notes
:::

## 12. Principle behind the Agile Manifesto

> At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.

::: notes
:::

# manifesto for software craftsmanship

::: {.wide-quote}
> As aspiring Software Craftsmen we are raising the bar of professional software development by practicing it and helping others learn the craft. Through this work we have come to value:
>
> - Not only working software, but also **well-crafted software**
> - Not only responding to change, but also **steadily adding value**
> - Not only individuals and interactions, but also **a community of professionals**
> - Not only customer collaboration, but also **productive partnerships**
>
> That is, in pursuit of the items on the left we have found the items on the right to be indispensable.

:::

::: notes
This reads like an answer to the agile manifesto.
The working software is good, but should well-crafted, which aligns with the ninth agile principle: "Continuous attention to technical excellence and good design enhances agility."
<!-- Accepting change requests is okay, but the change should improve the software. -->
:::

<!--## subway map to agile practices

![](borrowed/subway_map_to_agile_practices.svg)-->

## agile vs. waterfall

| agile                                 | waterfall                              |
|:-------------------------------------:|:--------------------------------------:|
| incremental                           | sequential                             |
| phases repeated                       | phases completed exactly once          |
| flexible                              | rigid                                  |
| allows changes during the development | no change once the development started |

## agile vs. waterfall

Can waterfall work? Yes, it can, if the customer exactly knows what they want and can express it in technical terms.

Although usually the customer does not know what they want, so agile usually work better.

# SCRUM

![](figures/scrum_sprint.drawio.svg)

# kanban

:::::::::::: {.columns}
::::::::: {.column width="45%"}
![simple kanban board<br>by [Jeff Lasovski](https://commons.wikimedia.org/wiki/File:Simple-kanban-board-.jpg) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)](figures/borrowed/simple_kanban_board.jpg){width=700}
:::::::::
::::::::: {.column width="55%"}
- notes move from left to right
- order denote priority
- allways process the right- and topmost one to finish it ASAP
- tool-dependent but a note can indicate:
    - who's responsible
    - how much effort to do it
    - etc.

:::::::::
::::::::::::

::: notes
The word "*kanban*" roughly means board in Japanese (signboard or billboard, actually).

:::

## kanban for job hunting

![](figures/job_hunting_kanban.drawio.svg)

::: notes
Kanban is a general technique, you can use it for household chores, for job applications (e.g., backlog, application sent, interview, done, declined).
A whiteboard can be used or there a many different software for the task.
Some general examples are:
- Trello (https://trello.com/),
   - free and paid plans
- Taiga (https://taiga.io/).
   - open source, self-hosted, cloud based free and paid plans
- WeKan (https://wekan.github.io/)
   - open source, self-hosted
:::

## kanban in software development

![](figures/kanban.drawio.svg)

::: notes
Kanban is widespread in software development.
The major code hosting solutions (GitHub, GitLab, Bitbucket, Gitea) all have some board functionalities.
:::

# SCUM + kanban = scrumban

- SCRUM and kanban can coexist
- quite new methodology

# references
