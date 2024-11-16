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
        - shared communication channe
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
        - different terminology
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
