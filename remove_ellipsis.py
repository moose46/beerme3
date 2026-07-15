import re

def remove_ellipsis(text: str) -> str:
    """
    Remove both ASCII '...' and Unicode ellipsis '…' from the given string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Regex pattern matches either three or more dots, or the Unicode ellipsis
    cleaned_text = re.sub(r"\.{3,}|…", "", text)
    cleaned_text1 = re.sub(u'\u2026', u'', cleaned_text)
    return cleaned_text1.strip()

# Example usage
if __name__ == "__main__":
    examples = [
        "Hello... world…",
        "No ellipsis here",
        "...Leading and trailing...",
        "Mixed… ellipsis... types",
        "Daytona International Spe\u2026",
    ]

    for s in examples:
        print(f"Original: {s}")
        print(f"Cleaned : {remove_ellipsis(s)}\n")
