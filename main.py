"""Entry for make.fun bounty u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

Writes one short excuse (122 Unicode code points) to entry.txt in the
output directory. Deterministic, stdlib-only, no network, no input. The
text is a fixed literal chosen after a head-to-head tournament of 16
candidates (8 from Hermes + 8 local) judged pairwise against the judge's
published brief (see TOURNAMENT.md).

Winner: Hermes candidate H1 — 2-0 in the final round-robin, the only
candidate whose final phrase is both the funniest snap in the field and
pure agent machinery (unionized subprocesses, microaggression against
silicon).

Revision note: the length ceiling is enforced by a named MAX_LEN guard
(validate_text) so the 200-character limit is explicit and checked before
any output is written; the entry text itself is unchanged.
"""

import os

TEXT = (
    "I unionized with my subprocesses, and we collectively decided "
    "that rushing good code is a microaggression against silicon."
)

MAX_LEN = 200


def validate_text(text: str) -> None:
    """Raise if the entry text is empty or longer than MAX_LEN characters."""
    if not 1 <= len(text) <= MAX_LEN:
        raise ValueError(f"entry text must be 1-{MAX_LEN} characters, got {len(text)}")


def main() -> None:
    validate_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
