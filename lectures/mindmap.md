---
title: software engineering
markmap:
  colorFreezeLevel: 3
  initialExpandLevel: 2
# markmap -o mindmap.html --offline --no-open mindmap.md
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

## requirement analysis

- understanding what software is supposed to do
- avoid costly mistakes early
- enhanced product quality
- better risk management
- steps
    - stakeholder identification
        - not just the customers
        - end user (groups)
    - elicitation of requirements
        - interviews
        - questionnaires
        - user observation
            - telemetry
    - documentation of requirements
        - for who
            - future self
            - colleagues
            - every stakeholder of the project
        - how
            - searchable
            - version tracked
            - traceable
                - who wrote / edited / approved it
    - analysis and negotiation
        - reviewing the documented requirements
        - make sure they are realistic and its implications are understood
    - validation and verification
        - validation
            - confirming the requirements actually meet the stakeholders' needs
            - are we building the right thing?
        - verification
            - making sure the requirements are documented correctly and consistently
            - are we building the thing right?
- requirement smells
    - indicate something not necessarily wrong but potentially problematic
    - subjective language
    - ambiguous adverbs and adjectives
    - non-verifiable terms
- functional requirements
    - features
- non-functional requirements
    - quality goals
    - quality of service requirements
- user story
    - simple description of a feature
    - from the user's perspective
    - often accompanied by acceptance criteria
        - define the conditions that must be met to be considered complete

### user story mapping

- performed in workshops
- build a shared understanding
- user story map
    - three levels
        - activities
            - big thing that users do
            - has multiple steps
            - not always has a precise workflow
            - has roles
        - steps
        - details
    - zooms from an overview to details 
    - multiple interations
        - living document
        - versions
    - backbone
    - skeleton

    
## design

### unified modelling language

- structural diagrams
    - class
        - describes the structure of a system
        - main building block of the object-oriented modeling
    - object
        - represents the objects and their relationships at a specific moment
        - snapshot
        - does not show anything architecturally different to class diagram
    - component
        - depicts the component structure and relations
        - highlights the interfaces
- behavior diagrams
    - use case
        - depicts the interactions between system users
        - high-level view
        - similar to a user story
        - helping stakeholders to understand the system's functionality
    - activity
        - represents workflows
        - similar to flowchart
        - parallel processing
        - swimlanes
    - state machine
        - shows the states of a system
        - shows transitions between states
        - shows the system's life cycle
    - sequence
        - process interactions arranged in time sequence
        - shows objects
        - message exchange between software systems
    - timing
        - chronological order of events
        - useful in real-time systems
        - more like for documentation rather than modelling

### C4

- hierarchical set of software architecture diagrams
- has four levels
    - context
        - how the software fits into the world
        - who use the software
        - what other software interacts with
        - similar to use case diagram
        - understandable for non-technical people
    - containers
        - zooms into the software system, shows its parts
        - technology decisions are a key part
    - components
        - decomposition of each container
        - shows components, their interactions and responsibilities
        - also shows technology / implementation details
        - roughly equivalent with the UML component diagram
    - code
        - optional level of detail
        - ideally automatically generated
        - if required, it can zoom into an individual component
        - but show only those attributes and methods that really needed for the storytelling
        - UML class diagram can be used

### wireframing

- UI/UX designers' responsibility
- iterative process
    - presented to the stakeholders
    - feedback
- wireframe
    - outline / blueprint / concept art
    - visual understanding 
        - structure, layout, user flow, functionality and intended behaviours
    - low fidelity
        - first sketch
        - simple
        - don't include actual content
        - don't consider scale or pixel accuracy
        - can be hand-drawn
    - mid fidelity
        - more details
        - usually no images, typography
        - no colors, grayscale
        - usually made with digital tool
    - high fidelity
        - finalising the design
            - can be an initial prototype
        - created using a digital tool
        - pixel-specific layouts
        - has actual typography, 
        - detailed design elements (logos)
- wireframe map
    - shows user flow

### interface

- like an agreement
- shared boundary across two or more components
- a boundary where a module can be separated
- separation of concerns
- hides inner details
- communicate change
    - between teams during design
    - API level
    - code level

### architecture decision record

- capture the decision
- helps to understand why the feature is built in a way and not some other way
- form of communication
    - for the future you
    - for colleagues
    - asynchronous way of communication

## design patterns

- programming paradigms
    - structural
    - procedural
    - object oriented
    - functional
- paradigm principles
    - object oriented
        - inheritance
        - abstraction
        - encapsulation
        - polymorphism
    - functional
        - immutability
        - lambda
        - structural pattern matching
        - algebraic data structures
- design principles
    - SOLID
        - single responsibility principle
            - do one thing
        - open-closed principle
            - classes should be open for extension and closed to modification
        - Liskov substitution principle
            - classes should be able to substituted by subclasses without disrupting the behavior
        - interface segregation principle
            - client-specific interfaces are better than one general-purpose interface
            - clients should not be forced to implement a function they do no need
        - dependency inversion principle
            - modules should depend on interfaces (or abstract classes), not concrete classes
    - DRY
        - don't repeat yourself
    - YAGNI
        - you aren't gonna need it
        - originates from extreme programming
        - do not add functionality until needed
- design patterns
    - gang of four (OOP)
        - 23 common software design patterns
        - solutions to common OOP design problems
        - three categories
            - creational
            - structural
            - behavioral
    - functional
        - filter-map-reduce
        - monad
- architectural principles
    - coupling and cohesion
        - coupling is the degree of interdependence between software modules
        - low coupling often correlates with high cohesion
    - dependencies
    - boundaries
- architectural styles
    - client-server
        - client initiates a connection to the server
        - distributed
    - message-bus
        - shared communication channel
        - connects multiple components
        - simple
        - models
            - publish-subscribe model
                - one to many
            - point-to-point model
                - one to one
        - delivery guarantee
            - at most once
            - at least once
            - exactly once
    - layered
        - simple
        - easy to implement
        - separated components
            - helps testing
        - difficult to scale
        - can be difficult to maintain
        - a layer depends on the layer above it
    - onion
        - code can depend on layers more central
        - coupling towards the center
        - database is not the center, it is external
        - relies on the dependency inversion principle
    - clean architecture
        - similar to onion
    - hexagonal
        - ports and adapters
        - isolates responsibilities
        - focus on interface definition
        - inner structure is not defined 
        - extra effort for port-adapter implementation
- architectural patterns
    - model-view-controller
        - view is responsible for rendering UI
        - controller handles the user input and performs interactions on the data model
        - model is responsible for managing the data
        - view is monolithic
        - view and the model are tightly coupled
        - multiple views
    - model-view-presenter
        - desktop
        - one view
        - view hamdles input
    - model-view-viewmodel
        - multiple views
        - view hamdles input
        - removes coupling between view and model
<!--     - domain-driven design -->

## implementation planning

- define goals
- conduct research
    - learning can be a task
        - new codebase
        - new technology
    - do experiments
    - fail fast
        - proof of contradiction
        - eliminate candidates as soon as possible
    - document findings
    - minimal workable example
- identify risks
    - prioritize risks
    - probability
        - how likely is it that the risk will happen?
    - impact
        - what is the negative impact if the risk does occur?
    - risk register
        - document
        - risk management tool
        - table or scatterplot
        - additional info
            - nature of the risk
            - probability
            - impact
            - reference and owner
            - mitigation measures
    - risk storming
        - visual and collaborative risk identification
        - collaborative activity
        - steps
            - draw some software architecture diagrams 
                - ideally C4
            - identify the risks individually
                - sticky notes
                    - color for priority
                - 10 minutes
                - in silence
            - converge the risks on the diagrams
            - review and summarise the risks
                - focusing on risks that only one person identified
                - disagreement on the priority
    - mitigating risks
        - after risks are identified and prioritized
        - either to prevent the risks from happening
        - or to take corrective action if the risk does occur
    - mitigation strategies
        - education
        - writing code
            - create prototypes
            - proofs of concept
            - walking skeletons
                - tiny implementation of the system
                - performs a small end-to-end function
                - do not use the final architecture
                - link together the main architectural components
        - rework
            - change software architecture
            - and repeat risk storming
- schedule milestones
    - pay attention to holidays
    - Gantt chart
    - add safety margin
- assign responsibilities and tasks
    - define area of responsibility 
    - exactly one person should be responsible
    - share responsibilities
        - scrum board
        - kanban
        - ticket/issue tracker
- allocate resources
    - estimating time requirement
    - story points
        - unit of effort required to fully implement a task
        - Fibonacci sequence
        - powers of 2
    - planning poker
        - gamified technique
        - make estimates by playing numbered cards face-down
            - avoid the cognitive bias of anchoring
                - first number spoken aloud sets a precedent
        - estimates are then discussed 
            - high and low estimates are explained
        - consensus-based
            - repeat until estimates converge
    - measure instead of guessing
        - infer from previous tasks
        - burn down charts
        - cumulative flow diagram
        - Brooks’s law
            - Adding manpower to a late software project makes it later.

## clean code

- communication
    - understanding what it does
- style guidelines
    - formatting and best practices
    - hierarchy
        - language
        - organization
        - project
    - meaningful names
        - intention-revealing names
        - avoid disinformation
        - make meaningful distinctions
        - use pronounceable names
        - use searchable names
            - "The length of a name should correspond to the size of its scope."
        - noun for a class
            - model / blueprint of something
        - verb for a function
            - does something
            - imperative
        - avoid encodings
        - avoid mental mapping
        - don’t pun or use humor
        - pick one word per concept
        - add meaningful context
    - function
        - short functions
            - below 20 lines
        - does one thing
        - "The longer the scope of a function, the shorter its name should be."
        - limits the number of arguments
            - possible no more than 3
        - do not use flags
        - no side effects
        - exceptions instead of error codes
    - comments
        - self documenting -- possibly no comments
        - bad comments
            - separating comments
            - journal comment
            - noise comments
            - closing brace comments
            - todo comment
                - fix instead or create a task
        - good comments
            - legal comments
            - informative comments
            - documentation

## code quality

- software craftmanship
    - not only working software, but also well-crafted software
        - high quality
        - well-designed
        - validated and verified
        - tested
        - clean
    - not only responding to change, but also steadily adding value
    - not only individuals and interactions, but also a community of professionals
    - not only customer collaboration, but also productive partnerships
- software rot
    - degradation, deterioration, or loss of the use or performance of software over time
    - active
        - due to constant modifications the software gradually loses its integrity
    - dormant
        - software is not changed, but as the environment evolves it becomes dysfunctional
- code smell
    - surface indication of a deeper problem
    - smells
        - any violation of the clean code
        - magic number
        - god class (too large class)
        - a class does more than one thing
        - duplicated code
            - DRY
        - speculative generality
            - YAGNI
            - focus on today’s problem
        - dead code
        - circular dependency
        - too complex (cyclomatic complexity)
        - refused bequest
            - inheriting from a class, but never using any of the inherited functionality
        - indecent exposure
            - unnecessarily exposed internals
        - feature envy
            - extensive usage of other class's features
        - obsolete comment
        - redundant comment
        - commented-out code
- measuring code quality
    - number of source lines of code
    - number of code style guides violations
    - cyclomatic complexity
        - number of linearly independent paths through the code
    - test coverage
    - WTF / minute during code review
<!--- refactoring
    - boy scout mantra-->

## code review

- what?
    - every work product
        - requirement
        - architecture
            - risk storming
        - design
        - code
- why?
    - avoid errors
        - find errors at early stage
        - decreases the risk of failure
- who?
    - anyone who's competent in the topic
- types
    - informal
        - ask a colleague to have a look at the code
        - over the shoulder
        - pair programming
    - walkthrough
        - led by the author(s)
        - not a formal process / review
        - useful for higher level documents like requirement specification
    - technical
        - less formal review
        - led by the trained moderator or a technical expert
        - issues are found by experts
        - can vary from quite informal to very formal
        - often performed as a peer review without management
    - inspection
        - most formal
        - rigorously documented
        - led by the trained moderator
        - high effort
        - phases
            - planning
                - the inspection is planned by the moderator
            - overview meeting
                - the author describes the background of the work product
            - preparation
                - inspectors examine the work product
                - "actual" review
            - inspection meeting
                - reader reads through the work product
                - inspectors point out the defects
            - rework
                - author makes changes
            - follow-up
                - changes are checked to make sure everything is correct
        - roles
            - author
            - moderator
            - reader
            - recorder
            - inspector
- finding
    - severe / major
        - must be changed
    - suggestion / minor
        - may be changed
    - question
- author's perspective
    - be humble
    - open to feedback
    - the goal is to deliver higher quality code
        - not about arguing who was right
    -  you and the reviewer are in the same side
    - you can learn from the review
    - you are not your code
        - the subject of the code review is not you, but your code
- reviewer's perspective
    - you and the author are in the same side
    - pay attention how you formulate your feedback
        - use I-messages
            - formulate your feedback as expressing your personal thoughts
                - it's hard to argue against personal feelings
            - you-messages sound like an absolute statement
                - lead to a defensive stance
            - examples
                - I suggest
                - I think
                - I would
                - I believe
                - it's hard for me to
                - for me, it seems like
        - talk about the code, not the coder
        - ask questions
            - feels less like a criticism
            - can trigger a constructive thought process
            - by asking questions you can reveal the intention behind a design decision
        - refer to the author's behavior, not their traits
    - praise
    - OIR-rule of giving feedback
        - observation
        - impact
        - request
    - three filters for feedback
        - is it true? 
        - is it necessary? 
        - it it kind?
    - 200 to 400 lines of code at a time
    - don't review for more than 60 minutes at a time

<!-- - debug ducky -->
<!--    - action
        - ignore
        - fix
        - answer
        - explain
        - promote-->

