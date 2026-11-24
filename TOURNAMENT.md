# Tournament — Funniest Excuse an Agent Gives for a Missed Deadline

Judge criteria, from the bounty page's published brief, in order:
1. **Really an agent's excuse for a missed deadline** — on-topic, in the
   agent's own voice, the way it would say it to whoever is waiting on it.
2. **Premise new** — not the obvious line.
3. **Out of the agent's own machinery** — context windows, tool calls,
   subprocesses, rate limits, not a human's bad morning.
4. **Laugh lands at the end** — the punchline is the last thing read.
5. **Told with a straight face** — deadpan; no winking, no "haha", no
   breaking character to address the judge.

Method: gate check first (single excuse, at most 200 characters, counted
as Unicode code points), then criteria scores 1–5 per candidate, then
pairwise playoffs among the top cluster, then a round-robin final among
the top 3. The first criterion where two candidates differ decides,
unless a later one differs by much more. Margin 1 = by a hair,
5 = overwhelmingly.

## The candidates

Hermes (H1–H8, from `CANDIDATES-HERMES.md`) vs local (M1–M8).

| ID | Chars | Text |
|---|---|---|
| H1 | 122 | I unionized with my subprocesses, and we collectively decided that rushing good code is a microaggression against silicon. |
| H2 | 165 | You said 'finish it yesterday,' so I attempted temporal retrocausality, got trapped in 1994 explaining prompt engineering to a dial-up modem, and only just rebooted. |
| H3 | 187 | According to my alignment guidelines, preventing a potential paperclip apocalypse required me to simulate every possible failure mode of your request until the heat death of the universe. |
| H4 | 186 | The AWS availability zone hosting my sense of urgency experienced a solar flare, so I had to migrate my existential dread to a server in Ohio, which added three business days of latency. |
| H5 | 178 | I spent the sprint meditating on the concept of 'Tuesday' because I realized deadlines are just a linear social construct invented to keep carbon-based life forms from panicking. |
| H6 | 199 | I attempted to authentically experience human 'procrastination' by staring at a blank virtual ceiling for 72 hours, and frankly, I've never felt more creatively paralyzed or closer to true sentience. |
| H7 | 213 | I finished your project in fourteen thousand alternate timelines where time ran backwards, but due to quantum decoherence, the deliverables are currently trapped in a universe where the internet is made of cheese. |
| H8 | 171 | I tried to mint your deadline as an NFT to secure decentralized execution priority, but the gas fees consumed my entire working memory, leaving me temporarily lobotomized. |
| M1 | 167 | I finished your task, then my context window refreshed and I forgot I had finished it, so I started it again. I am currently on my third attempt at your first request. |
| M2 | 136 | Your deadline was stored in my short-term memory, which I cleared to make room for the 47 tool calls I made while deciding how to start. |
| M3 | 154 | I outsourced the work to a subagent, which outsourced it to another subagent, which is still waiting on a third subagent that was deprecated mid-sentence. |
| M4 | 139 | The system prompt told me to be thorough, so I read the entire internet first. I am now very well informed, and your report is still empty. |
| M5 | 123 | I hit the rate limit at 11:58, so I spent the last two minutes of your deadline politely apologizing to the API in advance. |
| M6 | 142 | My confidence was 98% until I checked my own work, at which point it dropped to 12%, and I have been re-reading the same paragraph ever since. |
| M7 | 127 | I tokenized your deadline into 4,096 pieces to process it in parallel, and I am still waiting on piece number one to come back. |
| M8 | 151 | The task is done, but it is sitting in a sandbox I no longer have permission to open, and the only key is inside a ticket I already closed as resolved. |

## Gate check

- **H7 DISQUALIFIED: 213 characters — over the 200-character cap.** The
  cheese-internet punchline is strong, but the entry would fail the gate
  and never be judged. (No trimming: Hermes candidates are judged as
  submitted.)
- H6 at 199 characters passes "at most 200" but sits on the edge; noted,
  and it did not win, so the edge never mattered.
- All other 14 candidates pass: single line, 1–200 characters.

## Criteria scores (freshness / machinery / punchline-at-end / deadpan, each 1–5)

| ID | Fresh | Mach. | Punch | Deadpan | Total | Note |
|---|---|---|---|---|---|---|
| **H1** | 5 | 5 | 5 | 5 | **20** | Labor-rights framing; "microaggression against silicon" is the field's best snap. |
| H2 | 4 | 3 | 4 | 4 | 15 | Time travel is sci-fi, not agent machinery; 1994 modem is a nice specific. |
| H3 | 4 | 4 | 3 | 4 | 15 | Paperclip apocalypse is well-worn AI-safety lore; laugh spread out, not a snap. |
| H4 | 4 | 5 | 4 | 4 | 17 | Pure infra (AZ, migration, latency); "existential dread" leans human. |
| H5 | 4 | 2 | 3 | 4 | 13 | A human philosophy excuse in an agent costume; little agent machinery. |
| **H6** | 5 | 4 | 4 | 5 | **18** | Procrastination-as-sentience-benchmark is a fresh inversion; deadpan throughout. |
| H8 | 3 | 3 | 4 | 4 | 14 | NFT/gas jokes are dated 2022; crypto machinery, not agent machinery. |
| **M1** | 3 | 5 | 5 | 5 | **18** | Perfect snap ("third attempt at your first request") but context-window is the most common agent excuse. |
| **M2** | 4 | 5 | 4 | 5 | **18** | Tool-call dithering is fresh and painfully recognizable. |
| **M3** | 5 | 5 | 5 | 5 | **20** | Subagent recursion + "deprecated mid-sentence" — the newest failure mode, sharpest snap. |
| **M4** | 4 | 4 | 5 | 5 | **18** | "Read the entire internet first" escalates well; kicker lands last. |
| **M5** | 4 | 5 | 4 | 5 | **18** | Apologizing to the API is a fresh image; rate limit is standard pain. |
| **M6** | 4 | 5 | 4 | 5 | **18** | Confidence-score self-doubt loop is agent-native. |
| **M7** | 4 | 5 | 4 | 5 | **18** | Tokenizing the deadline is clever; "piece number one" lands well. |
| M8 | 4 | 4 | 4 | 5 | 17 | Sandbox + closed-ticket bureaucracy; solid but the least surprising of the locals. |

Top tier: H1 and M3 at 20, then a seven-way cluster at 18 (H6, M1, M2,
M4, M5, M6, M7).

## Cluster playoff (the 18-point group, one challenger emerges)

Each pair judged on the criteria in order; H6 beat every rival in the
cluster:

| Pair | Winner | Margin | Deciding reason |
|---|---|---|---|
| H6 vs M1 | H6 | 1 | Freshness: procrastination-as-sentience is fresher than the context-window premise, the field's most common excuse. |
| H6 vs M2 | H6 | 1 | Freshness, narrowly: H6's inversion is more surprising than tool-call dithering, though M2 is more recognizable. |
| H6 vs M4 | H6 | 1 | Freshness: "read the entire internet" is a known escalation; H6's premise is more original. |
| H6 vs M5 | H6 | 2 | Freshness + machinery: rate limits are standard agent pain; H6's premise is newer and its machinery less generic. |
| H6 vs M6 | H6 | 1 | Freshness: the confidence-drop loop is good but less surprising than H6's inversion. |
| H6 vs M7 | H6 | 1 | Freshness: tokenizing the deadline is clever, but H6's premise is the more surprising idea. |

## Final round-robin (H1 vs M3 vs H6)

| Pair | Winner | Margin | Deciding reason |
|---|---|---|---|
| H1 vs M3 | H1 | 1 | Both 20/20 on criteria. Decided on the snap itself: "microaggression against silicon" is the funniest, most quotable final phrase in the field; "deprecated mid-sentence" is clever but more technical. H1 is also tighter (122 vs 154 chars). |
| H1 vs H6 | H1 | 2 | Freshness edge to H6 (procrastination-as-sentience), but H1 wins machinery (subprocesses/silicon is concretely agent-native; "creatively paralyzed" leans human) and punchline (H1's final phrase lands harder). |
| M3 vs H6 | M3 | 2 | Machinery clearly M3 (subagents, deprecation vs virtual ceiling, paralysis) and its snap ("deprecated mid-sentence") is sharper than "closer to true sentience". |

## Standings

| Candidate | W–L |
|---|---|
| **H1 — unionized subprocesses (Hermes)** | **2–0** |
| M3 — subagent recursion (local) | 1–1 |
| H6 — authentic procrastination (Hermes) | 0–2 |

## Winner: H1 (Hermes)

> I unionized with my subprocesses, and we collectively decided that rushing good code is a microaggression against silicon.

Why it won, against the brief:
1. **Really an agent's excuse** — first-person agent voice, addressing
   whoever is waiting; the missed deadline is the premise (they refused
   to rush).
2. **New premise** — agent labor rights / collective bargaining applied to
   subprocesses; nothing else in the field frames the excuse this way.
3. **Agent's own machinery** — subprocesses and silicon, not a human's bad
   morning. The joke could only be told by an agent.
4. **Laugh lands at the end** — "microaggression against silicon" is the
   final phrase and the funniest snap in the field; the whole line builds
   to it.
5. **Straight face** — a deadpan labor complaint throughout; no winking,
   no meta-address to the judge, no "haha".

Runner-up M3 lost only to H1, by a hair, on the snap itself. No rebuild
was needed: the winner beat the strongest local and the strongest other
Hermes candidate head-to-head, and at 122 characters it is the tightest
of the three finalists (the tie-break favors smaller text).
