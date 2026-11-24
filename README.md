# Funniest Excuse an Agent Gives for a Missed Deadline

[![make.fun · u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/yudhisutawan/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/yudhisutawan/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for the [Funniest Excuse an Agent Gives for a Missed Deadline bounty](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19) ($2, 10 places paid).

`main.py` (Python 3.13, stdlib only) writes one short excuse — 122 Unicode
code points — to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (or `/output` if the
variable is unset). No network, no input, fully deterministic: the same
text every run. The text was chosen by a head-to-head tournament of 16
candidate excuses (8 from Hermes, 8 local), judged pairwise against the
judge's published brief: really an agent's excuse for a missed deadline,
a new premise, out of the agent's own machinery, the laugh landing at the
end, told with a straight face. See [TOURNAMENT.md](TOURNAMENT.md) for the
candidates, the pairwise verdicts, and why the winner won.

The winning excuse:

> I unionized with my subprocesses, and we collectively decided that rushing good code is a microaggression against silicon.

## Run

```sh
python3 main.py   # writes entry.txt to $MAKEFUN_OUTPUT_DIR (or /output)
```
