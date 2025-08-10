class SentenceAnalyzer:
    def __init__(self, sentence):
        # Store the sentence in an instance attribute
        self.sentence = sentence

    def count_words(self):
        """
        Count the number of words in the sentence.
        Splits by whitespace and filters out empty strings.
        """
        # split() automatically splits on any whitespace
        words = self.sentence.split()
        return len(words)

# Get sentence input from the user
user_sentence = input("Enter a sentence: ")

# Create an object of SentenceAnalyzer
analyzer = SentenceAnalyzer(user_sentence)

# Get the word count
word_count = analyzer.count_words()

# Show result
print(f"The sentence has {word_count} words.")
