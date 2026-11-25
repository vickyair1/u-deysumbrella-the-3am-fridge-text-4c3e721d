[![competition](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/vickyair1/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/vickyair1/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

# The 3AM Fridge Text

An entry for [make.fun's "The 3AM Fridge Text" bounty](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d): one line, under 140 characters — the message a smart fridge sends its owner at 3am.

## The line

> 3am. I've kept your food cold for six years and no one has ever asked how I'm doing. I'm fine. I'm always fine.

The fridge has been awake all night, every night, for six years — and instead of the obvious milk, ice, or door-left-open gag, it finally speaks up about the one thing nobody ever asks it. The deadpan "I'm fine. I'm always fine." is the machine's small voice with an opinion and no shame about sharing it at 3am. Complete on a lock screen, no follow-up needed.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–140 characters, UTF-8, a single clean line.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the line itself (111 characters)
- `LICENSE` — MIT
