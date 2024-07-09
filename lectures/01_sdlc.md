---
title: Software Development Life Cycle
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

![based on [guru99.com's image](https://www.guru99.com/images/6-2015/052715_0904_GuidetoSDLC3.png)](figures/v_model.drawio.svg){width=750}

::: notes
The *unit testing* will be discussed later in the testing chapter. For now it is enough to know that it is a tool to test the lower level part of the software.
:::

# incremental

# the agile manifesto

> We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value:
>
> - **Individuals and interactions** over processes and tools
> - **Working software** over comprehensive documentation
> - **Customer collaboration over** contract negotiation
> - **Responding to change over** following a plan
>
> That is, while there is value in the items on the right, we value the items on the left more.
>
> <cite>[forrás](https://www.agilealliance.org/agile101/the-agile-manifesto/)</cite>

## subway map to agile practices

![](borrowed/subway_map_to_agile_practices.svg)

## agile vs. waterfall

| agile       | waterfall  |
|:-----------:|:----------:|
| incremental | sequential |
| phases repeated | phases completed exactly once |
| flexible    | rigid      |
| allows changes during the development | no change once the development started |

# SCRUM

# kanban

:::::::::::: {.columns}
::::::::: {.column width="45%"}
![simple kanban board<br>by [Jeff Lasovski](https://commons.wikimedia.org/wiki/File:Simple-kanban-board-.jpg) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)](figures/simple_kanban_board.jpg){width=700}
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
The word "*kanban*" roughly means board in Japanese.
Kanban is a general technique, you can use it for household chores, for job applications (e.g., backlog, application sent, interview, done, declined)
:::

# scrumban

- SCRUM and kanban can coexist

# references
