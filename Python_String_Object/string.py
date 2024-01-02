# Provided text
homework_text = "tHis iz your homeWork, copy these Text to variable. You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

# Normalize from letter cases point of view
normalized_text = homework_text.lower()

# Fix misspelling "iZ"
normalized_text = normalized_text.replace("iz", "is")

# Calculate the number of whitespace characters
whitespace_count = sum(1 for char in normalized_text if char.isspace())

# Display the results
print("Normalized Text:", normalized_text)
print("Number of Whitespace Characters:", whitespace_count)

# Create one more sentence with the last words of each existing sentence
sentences = homework_text.split('.')
last_words = [sentence.split()[-1] for sentence in sentences if sentence.strip()]
additional_sentence = " ".join(last_words) + "."

# Add the additional sentence to the end of the paragraph
normalized_text += " " + additional_sentence

# Display the final paragraph
print("Final Paragraph:", normalized_text)
