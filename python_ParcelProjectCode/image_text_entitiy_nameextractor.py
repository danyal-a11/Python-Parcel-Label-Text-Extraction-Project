from paddleocr import PaddleOCR

# Step 1: Set the image path
image_path = ''  

# Step 2: Initialize PaddleOCR (rotated text detection included)
ocr = PaddleOCR(use_textline_orientation=True, lang='en')

# Step 3: Run OCR on the image
result = ocr.predict(image_path)

# Step 4: Print detected text and confidence
print("Text detected by PaddleOCR:")
all_text = []  
for res in result:  
    result_dict = res.json  
    rec_texts = result_dict['res']['rec_texts']  
    rec_scores = result_dict['res']['rec_scores']  
    for i in range(len(rec_texts)):  
        text = rec_texts[i]  
        confidence = rec_scores[i]  
        print(f"- {text} (confidence: {confidence:.2f})")  
        all_text.append(text)  

# Step 5: Calculate and print the average confidence
total_confidence = sum(rec_scores)  
num_texts = len(rec_scores)  

# Step 6: check if there are any texts (to avoid dividing by zero).
if num_texts > 0:  
    average_confidence = total_confidence / num_texts  
    print(f"\nAverage confidence for the image: {average_confidence:.2f}")  
else:  
    print("\nNo text detected, so no average confidence.")  

# Step 7: Combine all detected text into one string
combined_text = ' '.join(all_text)  
print("\nCombined text output:")  
print(combined_text)  

# Step 8: Use SpaCy to detect entities and names
import spacy

nlp = spacy.load("en_core_web_trf")
doc = nlp(combined_text)

# Step 9: Print all entities found
print("All entities detected:")
for ent in doc.ents:
    print(f"- {ent.text} ({ent.label_})")

# Step 10: Print recipient PERSON(s)
person_entities = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
if person_entities:
    for name in person_entities:
        print(f"\nRecipient name: {name}")
else:
    print("\nNo recipient PERSON found.")