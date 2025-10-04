"""
Text Analyzer Module
Performs simple text analysis: total length, uppercase, digits, and special characters.
"""

class TextAnalyzer:
    """Analyze text for length, uppercase letters, digits, and special characters."""

    def __init__(self, text):
        self.text = str(text)

    def analyze(self):
        """Return a dictionary of text statistics."""
        return {
            "total_length": len(self.text),
            "uppercase_count": sum(ch.isupper() for ch in self.text),
            "digit_count": sum(ch.isdigit() for ch in self.text),
            "special_char_count": sum(not ch.isalnum() for ch in self.text),
        }


if __name__ == "__main__":
    sample = TextAnalyzer("Hello123!!!")
    print(sample.analyze())
