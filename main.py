import os


def build_entry():
    lines = [
        "Put the phone down when your grandmother starts the story about the war.",
        "I only heard the ending once, and now there is nobody left who remembers how it began.",
    ]
    return "\n".join(lines)


def main():
    text = build_entry()
    destination = os.path.join(os.sep, "output", "entry.txt")
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
