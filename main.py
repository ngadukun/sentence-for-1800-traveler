"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes the sentence to output/entry.txt. Every word in it was already
in use before 1800. Python stdlib only, no network, deterministic.
"""

from pathlib import Path

ENTRY = (
    "Picture every printing press, letter, and library on Earth bound by "
    "invisible cords, so a question asked at breakfast in London is "
    "answered by a stranger across the sea before supper."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"


MAX_CHARS = 200  # the brief caps the sentence at 200 characters

# Words coined after 1800 that would mean nothing to the traveler.
TOO_NEW = {"internet", "computer", "online", "website", "email", "phone",
           "electric", "digital", "screen", "data", "network", "app"}


def check_entry(text: str) -> str:
    """Return the sentence unchanged, or raise if it breaks the brief."""
    if len(text) > MAX_CHARS:
        raise ValueError(f"sentence is {len(text)} chars, over the {MAX_CHARS} cap")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("the entry must be exactly one sentence")
    words = {w.strip(".,;:!?").lower() for w in text.split()}
    modern = words & TOO_NEW
    if modern:
        raise ValueError(f"words a traveler from 1800 would not know: {modern}")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
