<!-- code quality:4 -->
### What does the "Boy Scout Rule" or "campground rule" mean in clean code?  

1. [ ] Avoid leaving any code incomplete  
2. [ ] Always write detailed comments for each function  
3. [x] Leave the code cleaner than you found it  
4. [ ] Refactor only when necessary for production  

### What is the "long method" code smell?  

1. [x] A method that is too long and performs multiple unrelated tasks  
2. [ ] A method that is deprecated and no longer in use  
3. [ ] A method with poor naming conventions  
4. [ ] A method that contains nested loops  

### What is software rot in software development?  

1. [x] The gradual deterioration of software quality over time due to lack of maintenance or changes in its environment  
2. [ ] The physical degradation of hardware components  
3. [ ] A planned process of deprecating old software features  
4. [ ] A temporary issue caused by unstable internet connections  

### What is spaghetti code?

1. [x] Code with a disorganized and tangled structure that is difficult to understand  
2. [ ] Code written in a functional programming paradigm  
3. [ ] Code that strictly follows design patterns  
4. [ ] Code that is intentionally obfuscated for security purposes  

<!-- automatization:4 -->
### What is a linter in software development?  

1. [x] A tool that analyzes code for potential errors, style issues, and best practices  
2. [ ] A tool used to run automated tests  
3. [ ] A tool for deploying code to production  
4. [ ] A tool to measure code execution time  

### What is the "fail-fast" principle in CI/CD?  

1. [ ] Avoiding testing until the end of the project  
2. [ ] Prioritizing tasks based on sprint planning  
3. [x] Quickly identifying and addressing issues in the pipeline to reduce delays  
4. [ ] Releasing incomplete features to production  

### How can interruptions impact the productivity of software developers?  

1. [ ] They improve focus and increase the speed of development  
2. [ ] They provide an opportunity to refactor code  
3. [x] They can lead to context switching, reducing focus and efficiency  
4. [ ] They help developers learn new techniques  

### What is a key advantage of the copy-modify-merge strategy over lock-modify-unlock?  

1. [ ] It prevents developers from accidentally making changes to the same file  
2. [ ] It ensures that only one developer works on a file at any time  
3. [x] It allows multiple developers to work on the same file simultaneously without blocking each other  
4. [ ] It simplifies the process of merging code changes automatically  

<!-- design:10 -->
### Which stakeholders benefit most from wireframe maps?

1. [ ] Marketing teams focusing on branding  
2. [ ] End users testing the final product  
3. [x] Designers, developers, and UX teams ensuring smooth navigation  
4. [ ] System administrators managing server-side workflows  

### Which diagram in UML shows the flow of activities in a process or system?

1. [ ] Use case diagram  
2. [ ] Sequence diagram  
3. [ ] Deployment diagram  
4. [x] Activity diagram  

### When should an Architecture Decision Record be created?

1. [ ] Only at the beginning of a project  
2. [x] Whenever a significant architectural decision is made  
3. [ ] After the system is deployed  
4. [ ] At the end of each sprint during retrospectives

### What type of diagram would you use to describe a microservice's internal structure?

1. [ ] Context diagram  
2. [ ] Container diagram  
3. [x] Component diagram  
4. [ ] Code diagram  

### Which of the following is a key benefit of the C4 model?

1. [ ] It provides a single view of the system architecture  
2. [x] It combines high-level and detailed perspectives of a system  
3. [ ] It eliminates the need for developer documentation  
4. [ ] It focuses exclusively on code-level diagrams  

### Which UML diagram is most similar in purpose to a flowchart?

1. [ ] Class diagram
2. [ ] Deployment diagram
3. [x] Activity diagram
4. [ ] Use case diagram

### What notation style is most commonly used in C4 diagrams?

1. [ ] UML diagrams  
2. [ ] Text-based markdown with ASCII art  
3. [x] Simple boxes and lines with explanatory annotations  
4. [ ] Gantt charts  

### How does the C4 model differ from UML in terms of its purpose?  

1. [x] The C4 model focuses on high-level system architecture visualization, while UML provides detailed design for software components.  
2. [ ] The C4 model is only for business processes, while UML is for technical designs.  
3. [ ] The C4 model emphasizes testing workflows, while UML focuses on development methodologies.  
4. [ ] Both serve the same purpose and are interchangeable.  

### What does the Component diagram NOT include?

1. [ ] Relationships between components within a container  
2. [ ] Interactions with external containers  
3. [x] Deployment configuration details  
4. [ ] The responsibilities of each component  

### Which UML diagram is used to model finite state machines?

1. [ ] Sequence diagram  
2. [ ] Activity diagram  
3. [x] State diagram  
4. [ ] Class diagram  

<!-- design_patterns:4 -->

### What role does the View play in all three architectural patterns (MVC, MVP, and MVVM)?  

1. [ ] The View processes business logic and updates the Model  
2. [ ] The View serves as a communication bridge between the other components  
3. [x] The View is responsible for displaying information to the user  
4. [ ] The View manages data storage and retrieval  

### What is an example of poor cohesion in software design?  

1. [x] A class handling unrelated responsibilities like UI and database logic  
2. [ ] A class with only one method  
3. [ ] A class that implements an interface  
4. [ ] A class reused across multiple projects  

### What does the "Interface Segregation Principle" in SOLID recommend?  

1. [ ] A single interface should have all necessary methods for any client  
2. [x] Interfaces should be small and client-specific  
3. [ ] All classes must implement a common interface  
4. [ ] Interfaces should only be used for polymorphism  

### Which architectural style promotes using the same core application logic for different user interfaces, such as web, mobile, and API?  

1. [ ] Client-server  
2. [ ] Layered architecture  
3. [x] Hexagonal architecture  
4. [ ] Message-bus  

<!-- requirement_analysis:10 -->
### What is not a requirement elicitation technique?

1. [ ] user observation (telemetry)
2. [ ] interview
3. [ ] questionnaire
4. [x] risk register

### What is a poorly prioritized requirement an example of?

1. [ ] A functional requirement  
2. [x] A requirement smell  
3. [ ] A non-functional requirement  
4. [ ] An acceptance criterion  

### Who is typically responsible for writing user stories?

1. [ ] The development team only  
2. [ ] The design team only  
3. [x] The product owner, with input from stakeholders and the development team  
4. [ ] The QA team  

### How does user story mapping aid in Agile development?

1. [ ] By replacing daily stand-up meetings  
2. [x] By providing a shared understanding of user needs and priorities  
3. [ ] By defining sprint lengths  
4. [ ] By enforcing strict deadlines  

### Which of the following is NOT a component of a user story map?

1. [ ] User activities  
2. [ ] User tasks  
3. [ ] User stories  
4. [x] Database schemas  

### What does traceability in requirements refer to?

1. [x] The ability to track changes back to requirements
2. [ ] Documenting requirements in chronological order  
3. [ ] Eliminating non-functional requirements  
4. [ ] Writing user stories without dependencies  

### What is the importance of documenting functional requirements?

1. [ ] To avoid designing the user interface  
2. [ ] To finalize the project's timeline  
3. [x] To ensure developers understand what the system must do  
4. [ ] To define the marketing strategy  

### What should you do if new requirements emerge during story mapping?

1. [ ] Start the mapping process over from scratch  
2. [ ] Ignore the new requirements to avoid delays  
3. [x] Integrate the new requirements into the map and reassess priorities  
4. [ ] Postpone the mapping session until all requirements are fixed  

### What is a key challenge in user story mapping?

1. [ ] Ensuring code quality  
2. [x] Balancing stakeholder priorities and technical feasibility  
3. [ ] Automating testing processes  
4. [ ] Writing test scripts  

### What is the "backbone" in a user story map?

1. [x] The high-level user activities (or main steps) in the user journey  
2. [ ] The detailed technical requirements of the product  
3. [ ] The summary of all user stories in the project  
4. [ ] The underlying system architecture  

<!-- planning:4 -->
### When is Planning Poker typically performed in Scrum?  

1. [ ] During the daily stand-up meeting  
2. [ ] At the sprint review  
3. [x] During sprint planning sessions  
4. [ ] At the retrospective meeting  

### What is the primary focus when assessing risks during a risk storming session?  

1. [ ] Choosing technologies to mitigate the risks  
2. [ ] Prioritizing high-value features  
3. [x] Evaluating the impact and likelihood of each risk  
4. [ ] Conducting detailed root cause analysis  

### How often should risk storming be conducted in a project?  

1. [ ] Only at the start of the project  
2. [x] Regularly throughout the project lifecycle to reassess risks  
3. [ ] After the deployment phase  
4. [ ] Only when a major incident occurs  

### Why do Scrum teams use story points instead of hours for estimation?  

1. [x] To focus on relative effort and complexity rather than exact time estimates  
2. [ ] To replace the need for sprint planning sessions  
3. [ ] To make project deadlines more flexible  
4. [ ] To simplify team communication  

<!-- testing.md:4 -->

### What is a "test suite"?  

1. [ ] A tool used for debugging code  
2. [ ] A collection of user interface tests  
3. [x] A collection of test cases designed to test a particular application or module  
4. [ ] A series of manual test scripts  

### What is the role of mocks in unit testing?  

1. [ ] To generate performance metrics  
2. [x] To simulate external dependencies or objects for testing purposes  
3. [ ] To create complex test cases  
4. [ ] To automate the generation of test reports  

### What is a key difference between a walkthrough and an inspection?  

1. [ ] Walkthroughs are formal, while inspections are informal  
2. [x] Walkthroughs are led by the author, while inspections involve a moderator and formal defect logging  
3. [ ] Walkthroughs focus on defect detection, while inspections are for knowledge sharing  
4. [ ] Walkthroughs are only for code, while inspections cover all documents  

### Which of the following is a defining characteristic of a technical review?  

1. [ ] It is led by the author of the document  
2. [ ] It focuses on brainstorming rather than defect detection  
3. [x] It is conducted by peers with expertise in the technical domain of the work being reviewed  
4. [ ] It does not involve any predefined roles  

<!-- sdlc:10 -->
### What is true about the Definition of Done?

1. [ ] it is a list of risks that must be avoided to complete the sprint
2. [ ] it is a long text that describes the importance of the product increment
3. [ ] it is a software development process that must be followed in order to deliver a software
4. [x] it is a checklist

### What is the optimal size of a scrum team?

1. [ ] at most 5 people
2. [x] 3 to 9 people
3. [ ] 10-20 people
4. [ ] there is no limit, the more the merrier

### Who is responsible for creating the Product Backlog?

1. [ ] Scrum Master  
2. [x] Product Owner  
3. [ ] Development Team  
4. [ ] Stakeholders  

### How does Kanban differ from Scrum in its approach to work?

1. [ ] Kanban uses iterations, while Scrum has a continuous flow of tasks  
2. [x] Kanban focuses on flow, while Scrum emphasizes time-boxed sprints  
3. [ ] Kanban is team-based, while Scrum is individual-focused  
4. [ ] Kanban requires fixed sprint goals, unlike Scrum  

### In Kanban, what is a "Work In Progress (WIP) limit"?

1. [ ] The maximum number of team members allowed on a project  
2. [ ] The total number of tasks that can be completed in a day  
3. [x] The maximum number of tasks allowed in a workflow state at a time  
4. [ ] The budget allocated for ongoing projects  

### What is the Agile Manifesto’s priority?

1. [ ] Following a detailed plan  
2. [x] Delivering valuable software early and continuously  
3. [ ] Writing comprehensive documentation  
4. [ ] Rigid adherence to initial requirements  

### Which life cycle model is most suitable for projects with unclear requirements?

1. [ ] Waterfall model  
2. [ ] V-model  
3. [x] Iterative model  
4. [ ] Sequential model  

### What does the "V" in the V-model represent?

1. [ ] Verification and Validation  
2. [x] The relationship between development and testing phases  
3. [ ] Visual representation of tasks  
4. [ ] Velocity of task completion  

### What is the purpose of a daily stand-up in Scrum?

1. [ ] To review completed project phases  
2. [x] To discuss progress, obstacles, and plans for the day  
3. [ ] To approve user stories  
4. [ ] To finalize documentation  

### What is backlog grooming in Scrum?

1. [ ] Removing outdated code from the project  
2. [x] Refining and prioritizing items in the product backlog  
3. [ ] Assigning tasks to team members  
4. [ ] Writing new user stories for the next sprint  
