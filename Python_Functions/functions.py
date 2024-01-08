def normalize_text(text):
    """Normalize text from letter cases point of view."""
    return text.lower()

def fix_misspelling(text):
    """Fix misspelling "iZ" with correct "is"."""
    return text.replace("iz", "is")

def count_whitespace(text):
    """Count the number of whitespace characters."""
    return sum(1 for char in text if char.isspace())

def create_additional_sentence(text):
    """Create one more sentence with the last words of each existing sentence."""
    sentences = text.split('.')
    last_words = [sentence.split()[-1] for sentence in sentences if sentence.strip()]
    additional_sentence = " ".join(last_words) + "."
    return additional_sentence

def display_results(normalized_text, whitespace_count, additional_sentence):
    """Display the results."""
    print("Normalized Text:", normalized_text)
    print("Number of Whitespace Characters:", whitespace_count)
    print("Final Paragraph:", normalized_text + " " + additional_sentence)

# Provided text
homework_text = "tHis iz your homeWork, copy these Text to variable. You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

# Refactor the code using functional approach with decomposition
normalized_text = normalize_text(homework_text)
fixed_text = fix_misspelling(normalized_text)
whitespace_count = count_whitespace(fixed_text)
additional_sentence = create_additional_sentence(homework_text)

# Display the results
display_results(fixed_text, whitespace_count, additional_sentence)
