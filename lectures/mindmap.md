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

### extreme programming

- advocates frequent releases in short development cycles
- intended to improve productivity
- introduced checkpoints when new requirements can be adopted
- features
    - programming in pairs
    - doing extensive code review
    - unit testing of all code
    - not programming features until they are actually needed
    - flat management structure
- considered a type of agile software development

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
- user story mapping
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
    - KISS
        - keep it stupidly simple
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

## testing

### unit testing

- unit
    - smallest testable part of a program
    - a single behaviour exhibited by the system under test
    - often, but not always a method
- unit test
    - piece of code that tests a unit
    - AAA(A) Rule
        - arrange
            - set up the testing environment 
            - handle dependencies
        - act
            - call the tested unit 
        - assert
            - compare expected vs. actual
        - (annihilate)
            - free resource
            - automatic in modern languages
- should be fast
    - whole unit test suite should be able to run in milliseconds
    - immediate feedback
    - slow elements should be mocked
- safety net

### mocking

- test doubles
    - dummy
        - simplest, most primitive type of test double
        - null
    - stub
        - provides static input
    - spy
        - similar to stub
        - gives back values according to the caller
    - fake
        - more complex implementations
        - resembles a production implementation
        - not a complete production implementation
    - mock
        - dynamically created by a mock library
        - can behave like a dummy, a stub, or a spy

### test-driven development

- write test before writing the tested code
- TDD cycle
    - red
        - write a test that fails
        - test only one thing at a time
        - should be very simple
        - increase the complexity continuously
    - green
        - make it pass
        - use the possible simplest code
            - can be ugly
        - other tests should also pass
    - refactor
        - improve code quality
        - code level
            - style guide
            - best practices
        - architecture level
            - design patterns, principles
        - part of day-to-day programming
            - campground rule
                - leave the code better than you found it
- "As the tests get more specific, the code gets more generic."
- transformation priority premise
    - preventing getting stuck
- coding kata
    - simple programming task, that is meant to practised over and over again
- turning experiments into test
    
### behaviour-driven development

- is an extension of TDD
- can help to turn a requirement into implemented, tested, production-ready code
- adding the acceptance criteria to a user story
    - which can be turned into unit tests
- acceptance criteria
    - describes system behavior under certain circumstances 
    - written in natural language, but in a structured form

### acceptance test-driven development

- extends TDD and BDD
- focuses on the acceptance criteria of the whole system
    - instead of a unit
- writing acceptance tests before coding

### readme driven development

- document how a user would use the software
- before writing any code or tests

### test coverage

- the percentage of the code lines ‘protected’ or covered by tests
- test the edge cases
    - interval boundaries
    - requirements
    - defining of done
    - acceptance criteria

### testing approaches

- blackbox testing
    - testing the functionality without knowing the inner structure
- whitebox testing
    - testing the internal structure as opposed to its functionality
    - often associated to unit testing
- smoke testing
    - subset of test cases covering the most important functionality
    - verifing that the code is testable before sent to the test team
- rubber duck debugging
    - explaining the code, line by line, to a rubber duck
    - explaining something can provide a deeper understanding
    - articulating a problem in natural language

### legacy code

- avoid, rewrite
- what is legacy code
    - old, inherited code
    - difﬁcult-to-change code that we don't understand
    - spaghetti code
    - rotten
    - code without tests
        - cannot know whether code gets better or worse after change
- legacy code dilemma
    - can't change the code without adding tests
    - have to change the code to add tests
- legacy code change algorithm
    - steps
        - identify change points
        - find test points
        - break dependencies
            - e.g., misspelled function name
        - write tests
        - make changes and refactor
    - when?
        - not for the sake of refactoring
        - along with other changes
        - leave the code cleaner than you found it
    - how?
        - in stall, safe steps
        - use the IDE features
        - sensing
        - separation
        - mocking
- seam
    - a place in the code that you can insert a modification in behavior
    - change the behaviour without changing the code
    - types
        - object seam
            - using inheritance 
        - linker seam
        - preprocessor
- reason of change
    - add feature
        - adds new functionality
    - fix bug
        - changes structure
        - changes functionality
    - refactor
        - changes structure
    - optimize
        - changes resource usage
- technical debt
    - implied cost of future reworking because a solution prioritized short-term solution over long-term design

## automatization

- what?
    - every repetitive tasks
    - style guide compliance
    - code smell finding
    - code quality measurement
    - review
    - building
    - testing
    - deployment
- why?
    - workload reduction
    - developers could focus on non-automatable tasks
- editor level
    - linter
        - like a spell checker
        - gives immediate feedback on syntax errors, styling issues or bad practices
        - can detect some code smells
    - auto formatting
        - reformat the source code
        - usually triggered by saving the file
    - configuration
    - personal preference

### continuous integration and deployment

- emerged from extreme programming
- an agile approach
- gives immediate feedback
    - merge branches
    - build the software
    - do testing on the software
    - analyze the code
    - generate reports
        - feedback to stakeholders
        - decreases interruption
- build script
    - not only for building the software
    - running tests
    - generating reports 
        - test coverage
        - static code analysis
        - release
            - identified by a version number
                - often seen as an arbitrary number
                - pre-releases
                    - alpha
                        - incomplete
                        - whitebox testing
                    - beta
                        - feature-complete
                        - contains bugs
                        - mostly blackbox testing
                    - release candidate
                        - final touches 
                        - highest level of testing
                - semantic versioning
                    - major
                        - incompatible API changes
                    - minor
                        - add functionality in a backward compatible manner
                    - patch
                        - backward compatible bug fix
                - calendar versioning
                    - based on release date
                    - YYYY.MINOR.PATCH
                    - YYYY.MM.MINOR.PATCH
        - packaging the software
        - deploying
    - trigger
        - push
        - pull request
        - scheduled / time based
            - nightly build
                - building a the latest version of a software, on a daily basis
                - a full build with tests could take hours on a large software
        - manual
- deployment strategies
    - blue-green
        - two servers
            - one for production
            - one for internal manual testing
            - cost
        - after testing the servers are swaped
    - shadow
        - two servers
            - cost
        - testing the performance and stability requirements
            - traffic channeled through the shadow server 
    - canary
        - incremental deployment
        - allows to test updates in live environment
            - on small groups of users before deploying to many users
        - may involve telemetry
    - A/B testing
        - similar to canary deployment
        - two versions of updates in small set of users to identify which version perform better
- devops
    - collaboration
        - software **dev**elopers
            - writes (unit) tests
        - IT **op**eration**s**
            - maintains build script and CI/CD server
    - agile mindset and set of principles
        - collaboration and communication
        - continuous improvement
        - automation of the SDLC
        - short feedback loops
    - relies on automatization, CI and CD
- automatized review
    - using CI environment
    - do static code analysis
    - run test suite
    - generate review report from the findings
    - not to replace human reviewing

### interruption

- greatest "enemy" of a developer
- takes time to understand the code
- context switching is expensive
- define small tasks during the sprint planning
    - e.g., 1 hour 
    - one uninterrupted 2-hour session in a day
- average lost time per major interruption is 23 minutes
- unplanned interruption
    - someone asks about something or to do something 
    - wear headphones
    - notification in advance
- planned interruption
    - meeting
    - wrongly placed meeting can be worse than an unplanned interruption
    - schedule small, easy tasks before meeting
- mitigation
    - time blocking 
    - time batching
    - prioritize tasks
    - tackle the biggest task first in the morning
    - turn off notifications
    - asynchronous communication

## version control

- file sharing issue
    - lock-modify-unlock
        - locks edited file
        - one developer can edit a file at the same time
    - copy-modify-merge
        - checks if file was changes
        - compares and merges
- centralized
    - one remote repository
    - limited working copy
- distributed
    - full local repository
        - serves as backup
    - compares the local repository to the remote
- feature branching
    - each developed feature has its own branch
    - merged to the mainline after completion
    - multiple different branching strategies
        - to maintain multiple versions of the software
- when to make a commit?
    - when you completed a unit of work
    - when you have changes you may want to undo
- how to write the commit message?
    1. Separate subject from body with a blank line
    2. Limit the subject line to 50 characters
    3. **Capitalize the subject line**
    4. **Do not end the subject line with a period**
    5. **Use the imperative mood in the subject line**
    6. Wrap the body at 72 characters
        - least important
    7. **Explain what and why not how**
    8. **Reference the issue!**

<!--
- structure
    - version tracking
        - best practices
            - syncronize often
            - small changes
            - merge often
            - independent tasks-->
