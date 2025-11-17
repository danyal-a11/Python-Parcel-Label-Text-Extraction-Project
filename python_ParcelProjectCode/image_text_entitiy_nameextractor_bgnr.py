from paddleocr import PaddleOCR

# Step 1: Set the image path
image_path = ''  
# This tells the program where your parcel picture is. Update if the file is somewhere else.

# Step 2: Initialize PaddleOCR (rotated text detection included)
ocr = PaddleOCR(use_textline_orientation=True, lang='en')
# This sets up the OCR tool. 'use_textline_orientation=True' helps with sideways text on messy parcels.
# 'lang='en'' means it's looking for English words.

# Step 3: Run OCR on the image
result = ocr.predict(image_path)
# This tells the tool to read the image and save what it finds in 'result'.

# Step 4: Print detected text and confidence
print("Text detected by PaddleOCR:")
all_text = []  # This makes an empty list to hold all the words we find.
for res in result:  # This loops through each result (for one image, there's just one).
    result_dict = res.json  # This turns the result into a dictionary (a box of labeled info).
    # Now we grab the parts we need from the dictionary.
    rec_texts = result_dict['res']['rec_texts']  # List of words found, like ['FEI', 'WANG'].
    rec_scores = result_dict['res']['rec_scores']  # List of scores, like [0.94, 0.93].
    for i in range(len(rec_texts)):  # This loops through each word (i is the number, like 0, 1, 2...).
        text = rec_texts[i]  # Get the word at spot i.
        confidence = rec_scores[i]  # Get the score at spot i.
        print(f"- {text} (confidence: {confidence:.2f})")  # Print it nicely, like "- FEI (confidence: 0.94)".
        all_text.append(text)  # Add the word to our list.

# Step 5: Calculate and print the average confidence
# First, add up all the confidence scores.
total_confidence = sum(rec_scores)  # This adds every number in the rec_scores list together.
# Like if scores are 0.94 + 0.93 = 1.87.

# Next, count how many scores there are.
num_texts = len(rec_scores)  # This counts the items in the list, like 2 if there are two scores.

# Step 6: check if there are any texts (to avoid dividing by zero).
if num_texts > 0:  # This means: "If the count is more than zero..."
    average_confidence = total_confidence / num_texts  # Divide the total by the count to get the average.
    # Like 1.87 / 2 = 0.935.
    print(f"\nAverage confidence for the image: {average_confidence:.2f}")  # Print it nicely, with a blank line before.
    # The :.2f means show two numbers after the dot, like 0.94.
else:  # This means: "If there are no texts..."
    print("\nNo text detected, so no average confidence.")  # Print a message saying nothing was found.

# Step 7: Combine all detected text into one string
combined_text = ' '.join(all_text)  # This joins the words with spaces, like "FEI WANG".
print("\nCombined text output:")  # Print a heading with a blank line before it.
print(combined_text)  # Show the full string.

# Step 8: Use SpaCy to detect entities and names
import spacy    # Bring in the SpaCy library

# Load the most accurate English model (best for finding names properly)
nlp = spacy.load("en_core_web_trf") # nlp is now the "brain" that understands text

# Give your OCR text to SpaCy so it can analyse it
doc = nlp(combined_text)    # doc now holds all the  info SpaCy found


# Step 9: Print all entities found
print("All entities detected:")                   

# Go through every entity SpaCy found (people, companies, places, dates…)
for ent in doc.ents:
    # Print each one like: - John Smith (PERSON)
    print(f"- {ent.text} ({ent.label_})")


# Step 10: Print recipient PERSON(s)
# Make a list with only the PERSON names (usually the recipient)
person_entities = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

# If we found at least one person name
if person_entities:
    for name in person_entities:
        print(f"\nRecipient name: {name}")
else:
    print("\nNo recipient PERSON found.")