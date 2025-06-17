def main():
    text = input("Text: ").strip()
    words = text.lower().split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    longest_word_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{longest_word_length}} : {word_counts[word]}")


if __name__ == "__main__":
    main()
