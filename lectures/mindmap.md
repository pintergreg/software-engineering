---
title: software engineering
markmap:
  colorFreezeLevel: 3
  initialExpandLevel: 2
# markmap -o mindmap.html --offline --no-open  mindmap.md
---

## SDLC

### waterfall 

- earliest SDLC model
- progress flows in one direction
- not iterative, not flexible
- linear, sequential phases
- later it was extended with feedback loops

### V Model

- rigid model
- each phase has output and a review process
    - errors are found at early stage
    - decreases the risk of failure
- large to small: testing is done in a hierarchical perspective

### iterative model

- software is built incrementally
    - with each iteration adding new features or refining existing ones
- possible to get feedback after each iteration
- can be rigid within an iteration

### agile

#### manifesto

- individuals and interactions over processes and tools
- working software over comprehensive documentation
- customer collaboration over contract negotiation
- responding to change over following a plan

#### scrum

- roles
    - scrum master
        - developer representative
        - responsible for the scrum team’s effectiveness
        - impediment handler
        - ensures calm and uninterrupted working
    - product owner
        - customer representative
        - creates product backlog
        - prioritizes items in product backlog
        - responsible for maximizing the value of the product
    - developer team
        - optimally 3 to 9 people
        - self-organizing
        - cross-functional
- epic
    - user story
        - task
- events
    - sprint planning
        - initiates the sprint
        - max 8 hours for a four-week sprint
        - defining sprint goal
    - sprint
        - 1-4 week long
        - considered a short project
        - turns backlog items into increments
        - includes daily scrum
    - daily standup
        - a.k.a. daily scrum
        - 3 questions
        - timebox: 15 minutes
        - always on the same time and at the same place
        - standing up
    - backlog grooming
        - refinement of user story dod
            - smart goals
        - effort estimation
    - sprint review
        - a.k.a. demo
        - scrum team presents the their work to the stakeholders
        - increment is evaluated
        - max 4 hours for a four-week sprint
    - retrospective
        - concludes the sprint
        - max 3 hours for a four-week sprint
        - retrospective starfish
            - start
            - stop
            - more
            - less
            - continue
- artifacts
    - sprint backlog
    - product backlog
    - sprint goal
    - definition of done
    - burndown chart
    - board

#### kanban

- pull-based system
- uses a visual workflow
- uses columns for states of the product
- continuous flow (not iterative)
- no roles, no events
- pick top right task
- encourages to improve the workflow

#### extreme programming

- frequent releases, short development cycles
- intended to improve productivity and
- introduce checkpoints for customer requirements
- features
    - pair programming
    - doing extensive code review
    - unit testing of all code
    - not programming features until they are actually needed
    - flat management structure
