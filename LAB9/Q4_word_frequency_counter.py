# Q4. Word Frequency Counter using a Dictionary


def clean_text(paragraph):
    """Convert to lowercase and remove punctuation without importing a library."""
    cleaned = ""
    for character in paragraph.lower():
        if character.isalnum() or character.isspace():
            cleaned += character
        else:
            cleaned += " "
    return cleaned


def main():
    paragraph = input("Enter a paragraph: ")
    words = clean_text(paragraph).split()

    if not words:
        print("No words were entered. Nothing to count.")
        return

    # Count each word using dict.get().
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord counts:")
    for word in sorted(frequency):
        print(f"{word}: {frequency[word]}")

    try:
        n = int(input("\nEnter N to display top N words: "))
        if n < 0:
            print("N cannot be negative. Using 0.")
            n = 0
    except ValueError:
        print("Invalid N. Using 0.")
        n = 0

    # Sort by frequency descending, then alphabetically for ties.
    top_words = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
    print(f"\nTop {n} words:")
    for word, count in top_words[:n]:
        print(f"{word} ({count})")

    single_words = sorted([word for word, count in frequency.items() if count == 1])
    print("\nWords appearing exactly once:", single_words)

    # Invert word -> frequency into frequency -> sorted list of words.
    inverted = {}
    for word, count in frequency.items():
        inverted.setdefault(count, []).append(word)
    for word_list in inverted.values():
        word_list.sort()
    print("\nInverted dictionary:", dict(sorted(inverted.items())))

    # Group unique words according to their length.
    by_length = {}
    for word in frequency:
        by_length.setdefault(len(word), []).append(word)
    for word_list in by_length.values():
        word_list.sort()
    print("\nWords grouped by length:", dict(sorted(by_length.items())))

    search_word = input("\nEnter a word to search: ").lower().strip()
    search_word = clean_text(search_word).strip()
    # A search phrase with spaces is treated as one exact key and will not match.
    if search_word in frequency:
        print(f"'{search_word}' appears {frequency[search_word]} time(s).")
    else:
        print("Word not found.")


if __name__ == "__main__":
    main()
