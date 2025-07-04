import random

def getWords(filename):
    try:
        with open(filename, "r") as file:
            words = [line.strip() for line in file if line.strip()]
        return tuple(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ()

def generateSentence(articles, nouns, verbs, prepositions):
    return " ".join([
        random.choice(articles),
        random.choice(nouns),
        random.choice(verbs),
        random.choice(prepositions),
        random.choice(articles),
        random.choice(nouns)
    ]) + "."

def main():
    articles = getWords("articles.txt")
    nouns = getWords("nouns.txt")
    verbs = getWords("verbs.txt")
    prepositions = getWords("prepositions.txt")

    # Check if any tuple is empty (missing file or no content)
    if not all([articles, nouns, verbs, prepositions]):
        print("One or more vocabulary files are missing or empty.")
        return

    for _ in range(5):
        sentence = generateSentence(articles, nouns, verbs, prepositions)
        print(sentence.capitalize())

if __name__ == "__main__":
    main()
