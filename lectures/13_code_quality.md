---
title: code quality
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

#

::: {.text-align-left}
agile
~ working software over comprehensive documentation

:::

::: {.mt-2 .text-align-left}
software craftmanship
~ not only working software, but also well-crafted software 

:::

:::::::::::: {.columns .mt-2  .fragment height=240}
::::::::: {.column width="70%" .text-align-left}
::: {.text-align-left}
well-crafted
~    - high quality
     - well-designed
     - validated and verified
     - tested
     - code is clean, easy to understand, **maintain**

:::
:::::::::
::::::::: {.column width="30%"}

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

##

- long method
- long parameter list
- naming
    - notation in names
    - inconsistent names
    - uncommunicative names
- comments
- large class
    - possible do more than on thing
- duplicated code
- conditional complexity
- dead code
- speculative generality
- temporary field

code smells between classes

Alternative Classes with Different Interfaces

Data Class

Data Clumps

Refused Bequest

Indecent Exposure

Feature Envy




## some code smells

:::::::::::: {.columns}
::::::::: {.column width="60%" .mt-5}
this section is based on the book *Clean Code* (chapter 17) by Robert C. Martin [@martin2009clean]

with own examples

:::::::::
::::::::: {.column width="40%"}
![by Thomas Nast via [Wikipedia](https://commons.wikimedia.org/wiki/File:Smell_of_Tammany.png)<br>public domain](figures/borrowed/762px-Smell_of_Tammany.png){height=300}

:::::::::
::::::::::::


## obsolete comment

version *n-1* (OOP)

```python
# increase class attribute
def increase(self, by):
    self.foo += by
```

version *n* (FP)

```python
# increase class attribute
def increase(what, by):
    return what + by
```

::: {.mt-5}
these are actually noise comments, so they are bad in the first place
:::


## redundant comment

```python
# creates an empty dataframe
def create_empty_dataframe(start_week, end_week):
```

::: {.mt-5}
redundant as it does not give new information, a form of noise comment
:::

## commented-out code

```python
def increase(what, by):
    # print(what, by)
    return what + by
```

not needed, just remove it

::: {.fragment}
```python
class Something:
    foo = 0
    
    def increase(self, by):
        self.foo += by
    
    def decrease(self, by):
        self.foo -= by
    
    # def mutiply(self, by):
    #     self.foo *= by
```

the version tracker will preserve it, if you might meed it sometime in the future
:::


## dead function, dead code

## duplication

## feature envy

## magic numbers

magic number is an unexplained constant in the code

```python
def calculate_circle_area(r: float) -> float:
    return r * r * 3.141592
```

::: {.fragment}
```python
PI = 3.141592

def calculate_circle_area(r: float) -> float:
    return r * r * PI
```
:::

::: {.fragment}
```python
import math


def calculate_circle_area(r: float) -> float:
    return r * r * math.pi
```
:::


## structure over convention

Enforce design decisions with structure over convention. Naming conventions are good,
but they are inferior to structures that force compliance. For example, switch/cases with
nicely named enumerations are inferior to base classes with abstract methods. No one is
forced to implement the switch/case statement the same way each time; but the base
classes do enforce that concrete classes have all abstract methods implemented.

G29: Avoid Negative Conditionals
Negatives are just a bit harder to understand than positives. So, when possible, condition-
als should be expressed as positives. For example:
if (buffer.shouldCompact())
is preferable to
if (!buffer.shouldNotCompact())


Functions Should Do One Thing

Encapsulate Boundary Conditions

```python
if level + 1 < length:
    do_somthing(foo, bar, level + 1)
```
    
```python
next_level = level + 1
if next_level < length:
    do_somthing(foo, bar, next_level)
```


# denoting blocks

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="50"}
```javascript
for (i = 0; i < 10; i++) {
    console.log(i);
}
```
```javascript
for (i = 0; i < 10; i++)
    console.log(i);

```
```javascript
var a = 0;
for (i = 0; i < 10; i++)
    a++;
    console.log(i);

```

:::::::::
::::::::: {.column width="25%"}

::: {.fragment data-fragment-index="1"}
```python
for i in range(10):
    print(i)
```
```python
a = 0
for i in range(10):
    a += 1
    print(i)
```

:::
:::::::::
::::::::: {.column width="25%"}
::: {.fragment data-fragment-index="2"}
<!--```ruby
a = 0
for i in 0..9 do
   a += 1
   puts i
end
```
```ruby
a = 0
for i in 0..9 {
   a += 1
   puts i
}
```-->
```go
package main
 
import (
    "fmt"
)
 
func main() {
    for i:=0; i<10; i++ {
        fmt.Println(i)
    }
}
```

```rust
fn main() {
    for i in 0..9 {
        println!("{}", i);
    }
}
```
:::

:::::::::
::::::::::::


## what could go wrong?

:::::: {.fragment}
::: {.text-smaller}
parts from [sslKeyExchange.c](https://opensource.apple.com/source/Security/Security-55471/libsecurity_ssl/lib/sslKeyExchange.c?txt)
:::

```c {.numberLines startFrom="623"}
if ((err = ReadyHash(&SSLHashSHA1, &hashCtx)) != 0)
    goto fail;
if ((err = SSLHashSHA1.update(&hashCtx, &clientRandom)) != 0)
    goto fail;
if ((err = SSLHashSHA1.update(&hashCtx, &serverRandom)) != 0)
    goto fail;
if ((err = SSLHashSHA1.update(&hashCtx, &signedParams)) != 0)
    goto fail;
    goto fail;
if ((err = SSLHashSHA1.final(&hashCtx, &hashOut)) != 0)
    goto fail;
```

```c {.numberLines startFrom="647"}
fail:
    SSLFreeBuffer(&signedHashes);
    SSLFreeBuffer(&hashCtx);
    return err;
```

::: {.fragment}
more about Apple's "goto fail" fiasco (2014): [@wheeler2014apple], [@migues2014understanding]

false blame on `goto`, could be prevented by review and testing
:::
::::::


# how to measure code quality?

it is hard to objectively measure the quality of code

:::::::::::: {.columns}
::::::::: {.column width="60%"}
- number of source lines of code (SLOC)
    - more code, more (potential) issues
- aligns well with code style guides
- Halstead metrics
- cyclomatic complexity
- maintainability index
- test coverage [(later)]{.text-color-lightblue}

:::::::::
::::::::: {.column width="40%"}
![](figures/publicdomainvectors/worker-takes-measurements.svg){width=400}

:::::::::
::::::::::::


# Halstead metrics

Halstead's goal was to identify measurable properties of software, and the relations between them [@radon].

:::::::::::: {.columns .text-smaller}
::::::::: {.column width="50%"}
statistically computed numbers:

- $\eta_1$ = the number of distinct operators
- $\eta_2$ = the number of distinct operands
- $N_1$ = the total number of operators
- $N_2$ = the total number of operands

:::::::::
::::::::: {.column width="50%"}
some of the measures:

- program vocabulary: $\eta = \eta_1 + \eta_2$
- program length: $N = N_1 + N_2$
- calculated program length: $\widehat{N} = \eta_1 log_2{\eta_1} + \eta2 log_2{\eta_2}$
- volume: $V = N log_2{\eta}$
- difficulty: $D = \frac{\eta_1}{2} \cdot \frac{N_2}{\eta_2}$
- effort: $E = D \cdot V$

:::::::::
::::::::::::

<!-- https://radon.readthedocs.io/en/latest/intro.html#halstead-metrics -->


# cyclomatic comlexity

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
    as_percentage: bool
) -> float:
    progress = finished / total

    if as_percentage:
        return progress * 100
    else:
        return progress
```

:::::::::
::::::::: {.column width="30%"}
::: {.text-smaller}
activity diagram
:::

![](figures/user_statistics/progress_activity.svg){width=300}

:::::::::
::::::::: {.column width="20%" .fragment data-fragment-index=1}
::: {.text-smaller}
control flow
:::
![](figures/progress_control_flow_2.drawio.svg){width=300}

:::::::::
::::::::::::

::: {.fragment data-fragment-index=1}
$$ CC = E - N + 2 $$
$$ CC = 4 - 4 + 2 $$
$$ CC = 2 $$
:::


## cyclomatic comlexity -- 2nd example

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


## Python statements' effects on cyclomatic complexity

::: {.text-smaller}
|construct|effect|reasoning|
|-------|--|----------------------|
|if              |+1|An if statement is a single decision.                                             |
|elif            |+1|The elif statement adds another decision.                                         |
|else            |+0|The else statement does not cause a new decision. The decision is at the if.      |
|for             |+1|There is a decision at the start of the loop.                                     |
|while           |+1|There is a decision at the while statement.                                       |
|except          |+1|Each except branch adds a new conditional path of execution.                      |
|finally         |+0|The finally block is unconditionally executed.                                    |
|with            |+1|The with statement roughly corresponds to a try/except block.                     |
|boolean operator|+1|Every boolean operator (and, or) adds a decision point.                           |

:::

::: {.text-smaller}
source: Radon [documentation](https://radon.readthedocs.io/en/latest/index.html) [@radon]
:::

<!--|assert          |+1|The assert statement internally roughly equals a conditional statement.           |
|comprehension   |+1|A list/set/dict comprehension of generator expression is equivalent to a for loop.|-->


## interpretation of cyclomatic complexity -- Radon

|CC score|rank|risk         |
|--------|----|-------------|
|   1 - 5|   A|low - simple block                     |
|  6 - 10|   B|low - well structured and stable block |
| 11 - 20|   C|moderate - slightly complex block      |
| 21 - 30|   D|more than moderate - more complex block|
| 31 - 40|   E|high - complex block, alarming         |
| 41+    |   F|very high - error-prone, unstable block|

::: {.text-smaller}
source: Radon [documentation](https://radon.readthedocs.io/en/latest/index.html) [@radon]
:::


# maintainability index

original [@coleman1994using]:
~ $$ MI = 171 - 5.2 \ln{V} - 0.23G - 16.2\ln{L} $$

Visual Studio derivate:
~ $$ MI = max\left[0,100 \frac{171 - 5.2 \ln{V} - 0.23G - 16.2\ln{L}}{171}\right] $$

::: {.text-smaller .mt-2}
:::::::::::: {.columns .column-gapless}
::::::::: {.column width="40%" .mt-2}
- V: the Halstead volume
- G: the total cyclomatic complexity
- L: the number of source lines of code

:::::::::
::::::::: {.column width="30%" .text-size-1}

|score  |maintainability|
|:-----:|:-------------:|
|0-10   |low       |
|10-20  |moderate  |
|20+    |high      |

Table: Visual Studio

:::::::::
::::::::: {.column width="30%" .text-size-1}
|score |maintainability|
|:----:|:-------------:|
|  0–10|low            |
| 10–20|moderate       |
| 20–30|good           |
| 30–40|very good      |
|40–100|excellent      |

Table: based on [@sharma2024analyzing]

:::::::::
::::::::::::
:::

::: {.text-smaller .mt-2 .fragment}
**issues**: ease of computation, language independence, understandability, explainability [@heitlager2007practical]

read more in [Think Twice Before Using the "Maintainability Index"](https://avandeursen.com/2014/08/29/think-twice-before-using-the-maintainability-index/) [@vandeursen2014think]
:::


## maintainability index -- example

```python
def calculate_progress(finished: int, total: int, as_percentage: bool) -> float:
    progress = finished / total

    if as_percentage:
        return progress * 100
    else:
        return progress


def calculate_progress_2(
    finished: int, total: int, as_percentage: bool, foo: bool
) -> float:
    progress = finished / total

    if as_percentage and foo:
        return progress * 100
    else:
        return progress
```

- maintainability index for a script containing the code above is **63.71**
- calculated with Radon


# go report

- **gofmt**: style guide
- go_vet: reports suspicious constructs (Go specific)
- ineffassign: detects ineffectual assignments in Go code
- **gocyclo**: cyclomatic complexity
- license: checks whether your project has a LICENSE file
- misspell: finds commonly misspelled English words

![](figures/go report_ A+.svg){width=150}

[Go Report Card for Gitea](https://goreportcard.com/report/code.gitea.io/gitea)


<!--GoFmt: 0.30
GoLint: 0.10
go_vet: 0.30
GoCyclo: 0.10
IneffAssign: 0.10
Misspell: 0.05
Staticcheck: 0.15
ErrCehck: 0.15
Licence: 0.00-->


# code chunk permanence in a codebase 

<!--:::::::::::: {.columns}
::::::::: {.column width="50%"}

:::::::::
::::::::: {.column width="50%"}

:::::::::
::::::::::::-->

![Linux codebase -- from the [Hercules](https://github.com/src-d/hercules) (Git history analyser) documentation](https://raw.githubusercontent.com/src-d/hercules/refs/heads/master/doc/linux.png){width=400}

::: {.mt-2}
- there was no need to change it, presumably it was written well in the first place
- multiple changes in a short period indicate problems during software development [@nagappan2010change]
:::


# WTF per minute

![own drawing based on [Glen Lipka's](https://commadot.com/wtf-per-minute/)](figures/wtf_per_minute.drawio.svg){width=725}


# references

::: {#refs}
:::
