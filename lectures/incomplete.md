---
title: incomplete
author: Gergő Pintér, PhD
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
slideNumber: "true"
showSlideNumber: "print"
revealjs-url: "../assets/reveal.js-5.2.1/"
link-citations: true
---

# types

- [types vs. tests](https://www.destroyallsoftware.com/talks/ideology)
    - video ~21 min
- [I don't need types](https://dmerej.info/blog/post/trying-mypy/)
    - blogposzt a típusosságról

# Karpathy-inspired claude code guidelines

| principle | addresses               |
|-----------|-------------------------|
| think before coding   | wrong assumptions, hidden confusion,<br>missing tradeoffs |
| simplicity first      | overcomplication, bloated abstractions                    |
| surgical changes      | orthogonal edits, touching code you shouldn't             |
| goal-driven execution | leverage through tests-first, verifiable success criteria |

::: {}
source: [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
:::

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

::: {.text-smaller}
source: [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
:::

::: {.r-frame .mt-2}
Explicit is better than implicit.
:::

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

::: {.text-smaller}
source: [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
:::

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

::: {.text-smaller}
source: [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
:::

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:

- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

::: {.text-smaller}
source: [Karpathy-Inspired Claude Code Guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
:::

# Rob Pike's 5 rules of programming

1. You can't tell where a program is going to spend its time. Bottlenecks occur in surprising places, so don't try to second guess and put in a speed hack until you've proven that's where the bottleneck is.
2. Measure. Don't tune for speed until you've measured, and even then don't unless one part of the code overwhelms the rest.

Pike's rules 1 and 2 restate Donald Knuth's famous statement ["Premature optimization is the root of all evil."]{.background-color-lightblue}

::: {.mt-2}
> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%.
>
> -- Donald Knuth, 1974 [@knuth1974structured]

:::


## Rob Pike's 5 rules of programming

3. Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants. Until you know that n is frequently going to be big, don't get fancy. (Even if n does get big, use Rule 2 first.)
4. Fancy algorithms are buggier than simple ones, and they're much harder to implement. Use simple algorithms as well as simple data structures.

Ken Thompson rephrased Pike's rules 3 and 4 as "When in doubt, use brute force.".

Rules 3 and 4 are instances of the design philosophy [KISS]{.tooltip title="keep it stupidly simple"}.


## Rob Pike's 5 rules of programming

5. Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. Data structures, not algorithms, are central to programming.

Rule 5 was previously stated by Fred Brooks in The Mythical Man-Month. Rule 5 is often shortened to "write stupid code that uses smart objects". 

::: {.wide-quote .mt-2}
> I will, in fact, claim that the difference between a bad programmer and a good one is whether he considers his code or his data structures more important. Bad programmers worry about the code. [Good programmers worry about data structures and their relationships.]{.background-color-lightblue}
>
> -- Linus Torvalds 

:::

# references

::: #refs
:::
