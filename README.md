# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/oponopon31/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/oponopon31/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

One fortune-cookie line, 117 characters, for a software developer:

> The TODO you leave will outlive your time here, so write it kindly, as a note to the stranger who finishes your work.

The line fits the brief because it is one short balanced fortune sentence
about a truth every developer knows — TODO comments outlive their authors —
and it turns that truth once: the comment is not a chore for later but a
note to a stranger, so kindness to the next reader is the fortune's quiet
twist.

## How to run

```sh
python3 main.py
```

This validates the line (1–120 characters, a single line, no leading or
trailing whitespace), writes it to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`, falling back to the
current directory), then re-reads the file and verifies the bytes match
with a SHA-256 digest, printing the character count and the digest.
