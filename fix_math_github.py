import re
from pathlib import Path

DIRS = [
    Path(__file__).parent / "notes",
    Path(r"C:/Users/Lenovo/.cursor/skills/notes"),
]


def fix_inline(match: re.Match) -> str:
    content = match.group(1).strip()
    if content.startswith("`") and content.endswith("`"):
        return match.group(0)
    return "$`" + content + "`$"


def fix_github_math(text: str) -> str:
    def repl_block(match: re.Match) -> str:
        body = match.group(1).strip("\n")
        return "\n```math\n" + body + "\n```\n"

    text = re.sub(r"\n\$\$\n([\s\S]*?)\n\$\$\n", repl_block, text)
    text = re.sub(r"(?<!\$)\$(?!\$)([^\$\n]+?)(?<!\$)\$(?!\$)", fix_inline, text)
    return text


def main() -> None:
    for d in DIRS:
        if not d.exists():
            print("missing", d)
            continue
        for path in sorted(d.glob("*.md")):
            if path.name == "SKILL.md":
                continue
            old = path.read_text(encoding="utf-8")
            new = fix_github_math(old)
            if new != old:
                path.write_text(new, encoding="utf-8", newline="\n")
                print("fixed:", path)


if __name__ == "__main__":
    main()
