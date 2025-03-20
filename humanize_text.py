from transformers import pipeline

# Load the T5 model for paraphrasing
paraphraser = pipeline("text2text-generation", model="t5-small")

def humanize_text(text):
    """
    Takes input text and rewrites it in a human-like way.
    """
    # Generate paraphrased text from the model
    response = paraphraser(f"paraphrase: {text}", max_length=100, do_sample=True)
    
    # Print the raw response for debugging
    print("Raw Response: ", response)
    
    # Get the generated text
    humanized_text = response[0]['generated_text']
    
    # Clean the response by removing the "paraphrase: " part if it's present
    if humanized_text.lower().startswith("paraphrase:"):
        humanized_text = humanized_text[len("paraphrase: "):]
    
    # Remove any leading/trailing spaces and return the cleaned text
    return humanized_text.strip()

