"""Fortune Cookie Wisdom for Developers.

One original fortune-cookie line for a software developer, written to
entry.txt. The line turns a familiar truth of a developer's day — the
TODO comment left behind in code — into a fortune: what you leave in the
code outlasts your time on the team, so leave it kindly.
"""

import hashlib
import os
import sys

# One original fortune-cookie line for a developer (117 characters).
LINE = (
    "The TODO you leave will outlive your time here, so write it kindly, "
    "as a note to the stranger who finishes your work."
)

MAX_CHARS = 120


def resolve_output_dir() -> str:
    """Output directory: MAKEFUN_OUTPUT_DIR, else /output, else cwd."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.getcwd()


def validate(line: str) -> None:
    """Check the line meets the gate: 1-120 chars, one line, no stray space."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the 120 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")


def main() -> int:
    validate(LINE)

    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)

    # Re-read the file and verify the bytes match what was written.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise ValueError("entry.txt bytes do not match the line")
    # Byte-level gate check: the file must hold exactly the line, with no
    # line break and no stray leading or trailing whitespace.
    if b"\n" in written or b"\r" in written:
        raise ValueError("entry.txt must not contain a line break")
    if written != written.strip():
        raise ValueError("entry.txt must not have leading or trailing whitespace")
    written.decode("utf-8")  # confirm the file is valid UTF-8 text

    digest = hashlib.sha256(written).hexdigest()
    print(f"characters: {len(LINE)}")
    print(f"sha256: {digest}")
    print(f"wrote: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
