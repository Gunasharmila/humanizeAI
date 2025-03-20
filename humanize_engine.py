# Import the humanize_text function from the other file
from humanize_text import humanize_text

# You can define additional transformations if needed
def humanize_text_advanced(text):
    # Call the previously defined humanize_text function to paraphrase
    humanized = humanize_text(text)  # Paraphrase first
    # You can add other steps to enhance text further here
    return humanized

# Test the functions
if __name__ == "__main__":
    text = "AI-generated content is often predictable and lacks human touch."
    print("Original Text: ", text)
    print("Humanized Text: ", humanize_text_advanced(text))
