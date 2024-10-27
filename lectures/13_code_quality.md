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

# WTF per minute

![own drawing based on [Glen Lipka's](https://commadot.com/wtf-per-minute/)](figures/wtf_per_minute.drawio.svg){width=725}


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
:::
::::::


#

https://mvineetsharma.medium.com/analyzing-software-code-maintainability-index-9765896c80f9
https://radon.readthedocs.io/en/latest/intro.html#halstead-metrics


# references

::: {#refs}
:::
