---
title: incomplete
author: Gergő Pintér, PhD
date: gergo.pinter@uni-corvinus.hu
lang: en-US
title-slide-attributes:
    data-background-color: "#181d37"
slideNumber: "true"
showSlideNumber: "print"
revealjs-url: "../assets/reveal.js-5.1.0/"
---

# versioning

## semantic versioning

![](https://jontejada.com/blog/assets/semver02.png)

- [website](https://semver.org)
- [Why I don't like SemVer anymore](https://snarky.ca/why-i-dont-like-semver/)

## calendar versioning

- "*CalVer* is a versioning convention based on your project's release calendar, instead of arbitrary numbers."
- YYYY.MINOR.MICRO
- [website](https://calver.org)

## ZeroVer: 0-based versioning

- "Your software's major version should never exceed the first and most important number in computing: zero."
- e.g.: **0.4.1**
- [website](https://0ver.org)


# Fibonacci releases

| version | type           | release date   | delta |
|:-------:|----------------|----------------|------:|
| 6.1.0   | Release        | Tue 2024-06-18 | 0     |
| 6.1.1   | Bugfix Release | Tue 2024-06-25 | 1     |
| 6.1.2   | Bugfix Release | Tue 2024-07-02 | 1     |
| 6.1.3   | Bugfix Release | Tue 2024-07-16 | 2     |
| 6.1.4   | Bugfix Release | Tue 2024-08-06 | 3     |
| 6.1.5   | Bugfix Release | Tue 2024-09-10 | 5     |

table: KDE / Plasma 6.1 series [release schedule](https://community.kde.org/Schedules/Plasma_6)

# types

- [types vs. tests](https://www.destroyallsoftware.com/talks/ideology)
    - video ~21 min
- [I don't need types](https://dmerej.info/blog/post/trying-mypy/)
    - blogposzt a típusosságról
