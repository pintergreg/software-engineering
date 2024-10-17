---
title: clean code
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

# software design and architecture stack

![based on Khalil Stemmel's figure [@stemmler2019how]](figures/the_software_design_and_architecture_stack_generalized.drawio.svg){height=475}


# hierarchy in style guides

:::::::::::: {.columns}
::::::::: {.column width="55"}
- language level:
    - Python: [PEP 8](https://peps.python.org/pep-0008/) or [pep8.org](https://pep8.org/)
    - Ruby: [Ruby Style Guide](https://rubystyle.guide/)
    - Rust [The Rust Style Guide](https://doc.rust-lang.org/beta/style-guide/index.html)
    - etc.
- organization level:
    - [Google Style Guides](https://google.github.io/styleguide/)
        - [C# at Google Style Guide](https://google.github.io/styleguide/csharp-style.html)
        - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
        - [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)

::: {.fragment}
not just style guides, also best practices
:::
:::::::::
::::::::: {.column width="45%"}
![](figures/style_hierarchy.drawio.svg){width=300}

:::::::::
::::::::::::


# write idiomatic code

:::::::::::: {.columns}
::::::::: {.column width="70"}
::: {.text-align-left}
- a prog. language implements a prog. paradigm
- a paradigm defines a certain "way" of writing code
    - using different abstractions / building blocks
    - promoting a given concept
:::
::: {.fragment .text-align-left}
- some languages implements multiple paradigms
:::
::: {.fragment .text-align-left}
- and languages have their own way of doing things
    - languages have pros and cons
    - for a given problem
:::
:::::::::
::::::::: {.column width="30%"}
![](figures/publicdomainvectors/rural-road-with-signpost.svg){width=250}

:::::::::
::::::::::::

::: {.fragment .mt-3}
just as in the case of natural languages, you ought to use a language properly
:::


## write idiomatic code

:::::::::::: {.columns .column-gapless}
::::::::: {.column width="55"}
```javascript
for (i = 0; i < 10; i++) {
    console.log(i);
}
```

::: {.fragment data-fragment-index="5"}
```javascript
[...Array(10).keys()].forEach(i => {
    console.log(i);
});
```

:::
:::::::::
::::::::: {.column width="20%"}
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

::: {.fragment data-fragment-index="1"}
```python
for i in range(10):
    print(i)
```

:::
:::::::::
::::::::: {.column width="25%"}
::: {.fragment data-fragment-index="2"}
```ruby
for i in 0..9 do
   puts i
end
```

:::
::: {.fragment data-fragment-index="3"}
```ruby
(0..9).each do |i|
    puts i
end
```

:::
::: {.fragment data-fragment-index="4"}
```ruby
(0..9).each {|i| puts i}
```

:::
:::::::::
::::::::::::


