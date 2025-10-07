---
title: Unified Modeling Language
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

# programming paradigms

- structural
- procedural
- object oriented
    - class-based
- functional

# structural

:::::::::::: {.columns}
::::::::: {.column width="20%" .mt-5}
- statement
- [condition]{.fragment data-fragment-index=1}
- [iteration]{.fragment data-fragment-index=2}

:::::::::
::::::::: {.column width="40%"}
:::::: {.r-stack .text-size-2}
::: {.fragment .fade-out data-fragment-index=1 .pre-width-100}
```python
a = 4.2
a = a * 10
```
:::
::: {.fragment .current-visible data-fragment-index=1 .pre-width-100}
```python
if a > 17
    a -= 5
else:
    a += 5
```
:::
::: {.fragment data-fragment-index=2 .pre-width-100}
<br>
```python
for i in range(10):
    print(i)
```

<br>

```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

:::

::::::
:::::::::
::::::::: {.column width="40%"}
:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
![](figures/flowchart_statement.drawio.svg)

:::
::: {.fragment .current-visible data-fragment-index=1}
![](figures/flowchart_condition.drawio.svg)
:::
::: {.fragment .current-visible data-fragment-index=2}
![](figures/flowchart_iteration.drawio.svg)
:::

::::::
:::::::::
::::::::::::


# procedural

<!-- :::::::::::: {.columns} -->
<!-- ::::::::: {.column width="70%"} -->
- extends structural with procedures
    - a.k.a. subroutines, methods, functions
- the two main concepts
    - modularity: organizing the parts of a program into separate modules
        - reusability
    - scoping
        - limit the scope of the variables

<!--:::::::::
::::::::: {.column width="30%"}
![](figures/flowchart_procedure.drawio.svg)

```python
def power(a, b):
    r = a
    for _ in range(b - 1):
        r *= r
    return r

a = 4.2
a = a * 10
power(a, 3)
```

:::::::::-->

## procedural - example

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/flowchart_procedure_2.drawio.svg)

:::::::::
::::::::: {.column width="50%" .mt-4 .text-size-2}
```python
def power(a, b):
    r = a
    for _ in range(b - 1):
        r *= r
    return r

a = 3
a = power(a, 3)
```

:::::::::
::::::::::::


# object oriented programming

- extends procedural programming with the concept of objects
- main properties of OOP
    1. abstraction
    2. encapsulation
    3. inheritance
    4. polymorphism

    
## 1. abstraction

<!-- Abstraction involves hiding the complex reality while exposing only the necessary parts. It allows programmers to focus on interactions at a higher level without needing to understand the intricate details of the implementation. This is achieved through abstract classes and interfaces, which define a contract for what methods an object must implement without specifying how they should be implemented -->

- hiding the complex reality while exposing only the necessary parts
- allows to focus on interactions at a higher level without needing to understand the details of the implementation
- *often* achieved through abstract classes and interfaces, which define a contract for what methods an object must implement without specifying how they should be implemented


## 2. encapsulation

<!--Encapsulation is the principle of bundling data (attributes) and methods (functions) that operate on that data into a single unit known as a class. This property restricts direct access to some of the object's components, which is a means of preventing unintended interference and misuse of the methods and data. By exposing only necessary parts of an object through public methods (getters and setters), encapsulation enhances security and integrity of the data-->

- bundling data (attributes) and methods (functions) that operate on that data into a single unit
- this property restricts direct access to some of the object's components
    - private, public, protected
- can preventing unintended interference and misuse of the methods and data
    - by exposing only the necessary parts of an object through public methods


## 3. inheritance

<!--Inheritance is a mechanism that allows one class (subclass or derived class) to inherit attributes and methods from another class (superclass or base class). This promotes code reusability, as common functionality can be defined in a base class and reused in derived classes.-->

- a mechanism that allows one class (subclass or derived class) to inherit attributes and methods from another class (superclass or base class)
- this is said to promote code reusability, as common functionality can be defined in a base class and reused in derived classes
- results hierarchical relationship which can foster modular design
    - also increases dependency

## class-based inheritance

- class-orientated, or class-based programming
    - inheritance via classes of objects,
    - instead of inheritance via the objects alone
- every object is defined by a class
    - which is like a definition or a blueprint
    - describes the structure and behavior of an object
- most common


## prototype based inheritance

> The object function untangles JavaScript's constructor pattern, achieving true prototypal inheritance.
> It takes an old object as a parameter and returns an empty new object that inherits from the old one.
> If we attempt to obtain a member from the new object, and it lacks that key, then the old object will supply the member.
> **Objects inherit from objects.**
> What could be more object oriented than that?
>
> [Douglas Crockford](http://crockford.com/javascript/prototypal.html)


## OO without inheritance

- Go does not support inheritance at all, though it is considered object-oriented
    - at least partially [[Go FAQ](https://go.dev/doc/faq#Is_Go_an_object-oriented_language)]
- Bjarne Stroustrup (author of C++) has stated that it is possible to do OOP without inheritance [@stroustrup2015object]


## 4. polymorphism

<!--Polymorphism allows objects to be treated as instances of their parent class, enabling a single interface to control access to different underlying forms (data types). There are two types of polymorphism: compile-time (method overloading) and runtime (method overriding). This property enables flexibility in code, allowing for methods to perform differently based on the object that invokes them. For instance, a method defined in a base class can be overridden in a derived class to provide specific behavior-->

- allows objects to be treated as instances of their parent class
- enables flexibility in code, allowing for methods to perform differently based on the object that invokes them
    - method defined in a base class can be overridden in a derived class to provide specific behavior


# some critics of OOP

::: {.wide-quote}
> object-oriented design is the roman numerals of computing
>
> -- Rob Pike, creator of Go programming language

:::

::: {.wide-quote .mt-1}
> The problem with object-oriented languages is they’ve got all this implicit environment that they carry around with them. You wanted a banana but what you got was a gorilla holding the banana and the entire jungle.
>
> -- Joe Armstrong, creator of Erlang programming language

:::

::: {.wide-quote .mt-1}
> Sometimes, the elegant implementation is just a function. Not a method. Not a class. Not a framework. Just a function.
>
> -- John Carmack, co-founder of id Software, lead programmer of Doom, Quake, etc.

:::

::: {.text-smaller}
more: [Object Oriented Programming is Inherently Harmful](https://harmful.cat-v.org/software/OO_programming/)
:::

## bounding together data and functions

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-2}
<!-- > Functions do things. They have inputs and outputs. The inputs and outputs are data structures, which get changed by the functions. -->

- methods change the state of the object
- introduces side effects
- makes harder to test

the increase function depends on the state of the object Something

how to reuse a function that has a hard dependency on an object state?

:::::::::
::::::::: {.column width="40%" .text-size-2}
```python
class Something:
    foo = 0
    
    def increase(self, by):
        self.foo += by
    
something = Something()
print(something.foo)  # 0
something.increase(2)
print(something.foo)  # 2
```

:::::::::
::::::::::::

## why OO got popular?

::: {.wide-quote}
> - Reason 1 - It was thought to be easy to learn.
> - Reason 2 - It was thought to make code reuse easier.
> - Reason 3 - It was hyped.
> - Reason 4 - It created a new software industry.
> 
> I see no evidence of 1 and 2. Reasons 3 and 4 seem to be the driving force behind the technology. If a language technology is so bad that it creates a new industry to solve problems of its own making then it must be a good idea for the guys who want to make money.
> 
> -- Joe Armstrong, creator of Erlang programming language

:::

::: {.text-smaller}
source: [Why OO Sucks by Joe Armstrong](https://harmful.cat-v.org/software/OO_programming/why_oo_sucks)
:::
    
# Unified Modeling Language

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-4}
- UML 2.0 released in 2005
    - latest revision in 2017
- ISO/IEC 19501 standard
- designed to be a complete language of software modelling
- UML 2 has 14 diagrams in two categories: structure and behavior

::: {.fragment}
most software developer do not use UML (in a formal way), but hand drawn sketches which often include UML elements [@baltes2014sketches]
:::
:::::::::
::::::::: {.column width="40%"}
![](figures/uml/diagrams.svg)

:::::::::
::::::::::::


# use case diagram

:::::::::::: {.columns}
::::::::: {.column width="55%"}
- depicts the interactions between system users (actors) and the system itself
- used to specify the functional requirements
- provides a high-level view
    - helping stakeholders to understand the system's functionality
- it's purpose is similar to the user story

:::::::::
::::::::: {.column width="45%"}
![](figures/uml/stopwatch_use_case.svg){width=275}

:::::::::
::::::::::::

## elements of the use case diagram

:::::::::::: {.columns}
::::::::: {.column width="40%"}
![](figures/uml/actor_note.svg)

:::::::::
::::::::: {.column width="50%"}
:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
![](figures/uml/usecase_extension.svg)
:::
::: {.fragment .current-visible data-fragment-index=1}
![](figures/uml/usecase_extension_example.svg)
:::
::: {.fragment data-fragment-index=2}
![](figures/uml/usecase_extension_example_boundary.svg)
:::
::::::

:::::::::
::::::::::::

<!--:::::::::::: {.columns}
::::::::: {.column width="40%"}
::: {.fragment data-fragment-index=3}
![](figures/uml/stereotype.svg){height=100}
:::
:::::::::
::::::::: {.column width="50%"}
stereotype (can be applied to actors as well) 
:::::::::
::::::::::::-->

## use case diagram - example

:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
![](figures/social_media_platform/usecase_1.svg){width=400}
:::
::: {.fragment .current-visible data-fragment-index=1}
![](figures/social_media_platform/usecase_2.svg){width=400}
:::
::: {.fragment .current-visible data-fragment-index=2}
![](figures/social_media_platform/usecase_3.svg){width=400}
:::
::::::

# class diagram

- describes the structure of a system by its classes
    - their attributes, methods, and the relationships among them 
- main building block of the object-oriented modeling

## (most common) elements of a class diagram

![](figures/uml/class.svg){height=350}

::: {.text-smaller}
based on PlantUML documentation
:::

## relations

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="50%"}
![[from Wikipedia](https://en.wikipedia.org/wiki/File:Uml_classes_en.svg) | CC BY-SA](figures/borrowed/class_relations.svg){height=450}

:::::::::
::::::::: {.column width="50%" .text-smaller .mt-5}
- association: structural relationship
    - allows one object instance to cause another to perform an action on its behalf
- realization: e.g., class implements a interface
- aggregation: "has a" relation
    - without life cycle control
- composition: stronger form of aggregation
    - where the aggregate controls the lifecycle of the elements
:::::::::
::::::::::::

::: notes
Aggregation can occur when a class is a collection or container of other classes, but the contained classes do not have a strong lifecycle dependency on the container. The contents of the container still exist when the container is destroyed. [@enwiki:1230720147]
:::

## class diagram - example

![](figures/uml/class_example.svg){height=450}


## class diagram - example

![](figures/uml/class_example_2.svg){height=450}


# object diagram

- special case of a class diagram
- graphical representation of the objects and their relationships<br>**at a specific moment in time**
- provides a snapshot of the system's structure
- does not show anything architecturally different to class diagram

![](figures/uml/object_class.svg){height=250}


<!--
## collections

![](figures/uml/object_collections.svg){height=350}
-->

# component diagram

- depicts the component structure and relations
- highlighting the interfaces

::: {.mt-2}
![](figures/uml/component.svg){height=275}
:::


# state diagram

- a visual representation of the states a system or an object can be in
    also the transitions between those states
- models the dynamic behavior of the system, capturing how it responds to different events over time
- shows the system's life cycle


## state diagram elements

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/uml/state.svg){width=400}
:::::::::
::::::::: {.column width="50%"}
![](figures/uml/substate.svg){width=300}
:::::::::
::::::::::::


## state diagram - example

:::::::::::: {.columns}
::::::::: {.column width="60%"}
![](figures/uml/stopwatch_state_commented.svg){width=350}
:::::::::
::::::::: {.column width="40%" .mt-4}
![](figures/borrowed/cronometro-mauro-olivo-01.svg){width=175}
:::::::::
::::::::::::

<!--
# activity diagram

- graphical representations of workflows
- similar to flowcharts
    - but uses UML notation
    - and can visualize parallel processing

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![](figures/uml/power.drawio.svg){height=300}
:::::::::
::::::::: {.column width="50%"}
![](figures/uml/activity.svg){height=300}
:::::::::
::::::::::::-->

# activity diagram

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-4}
- graphical representations of workflows
- similar to flowcharts
    - but uses UML notation
    - and can visualize parallel processing
    - has more features

:::::::::
::::::::: {.column width="20%"}
![flowchart](figures/uml/power.drawio.svg){height=300}
:::::::::
::::::::: {.column width="20%"}
![activity (UML)](figures/uml/activity.svg){height=300}
:::::::::
::::::::::::


## parallel processing

:::::::::::: {.columns}
::::::::: {.column width="50%"}
![fork with join](figures/uml/activity_join.svg){height=300}
:::::::::
::::::::: {.column width="50%"}
![fork with merge](figures/uml/activity_merge.svg){height=300}
:::::::::
::::::::::::

a join synchronizes two inflows (waits for the slower)


## merge after condition

![](figures/uml/activity_decision.svg)


## swimlanes

:::::::::::: {.columns}
::::::::: {.column width="65%" .mt-3}
- actions can be separated using "swimlanes"
- swimlanes can represent actors, components or other parts of the software system
:::::::::
::::::::: {.column width="35%"}
![](figures/uml/activity_swimlanes.svg){height=400}
:::::::::
::::::::::::


# sequence diagram

:::::::::::: {.columns}
::::::::: {.column width="60%"}
![](figures/uml/sequence.svg)
:::::::::
::::::::: {.column width="40%" .mt-3}
- shows process interactions arranged in time sequence
- depicts the processes and objects involved and the sequence of messages exchanged
- instead of the inner parts of a system, message exchange between software systems can be depicted
:::::::::
::::::::::::


# timing diagram

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- focuses on the chronological order of events, showing how different objects interact with each other over time
- especially useful in real-time systems and embedded systems
- more like for documentation rather than modelling

:::::::::
::::::::: {.column width="40%"}
:::::: {.r-stack}
::: {.fragment .fade-out data-fragment-index=1}
![](figures/uml/timing.svg)
:::
::: {.fragment .fade-in data-fragment-index=1}
![](figures/uml/timing_2.svg)
:::
::::::
:::::::::
::::::::::::

::: {.text-smaller}
source: [PlantUML documentation](https://plantuml.com/timing-diagram)
:::

# references

::: {#refs}
:::
