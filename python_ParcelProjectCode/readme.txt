The goal of this project is to extract text from parcel label jpeg images, find the 
recepients name so that it can be matched with names in an existing database, and then
send an email out to the recepient telling them their parcel has arrived, it is ready
to collect.

So far I have completed the code to extract text out of images and extract entities and names.

For the text extraction PaddleOCR has worked well giving high confidence levels of <.90 in the text.

What is PaddelOCR?
PaddleOCR is an open-source Character Recognition (OCR) system developed by Baidu, built upon the PaddlePaddle
deep learning framework. It is designed to be lightweight, efficient, and practical for various real-world 
OCR applications.

note: It should be known that paddle OCR did not work on apple silicone(M1,M2,etc). the code would get stuck 
when it needed to process the image. I used an M1 chip, I can not say for the other M series chips.
A windows pc should work fine for processing images. 
note: processing multiple images(<100) on older hardware could take longer.     

After extracting the text spaCy is used and the en_core_web_trf model is used to detect entities
such as names, organizations, locations etc. 
The model was not able to extract names from all the images i tried to process. 
So tweaking is needed.

What is spaCy?
spaCy is a free, open-source Python libray for industrial-strength Natural Language Processing (NLP).
It is designed for production use and helps developers build applications that process and "understand"
large volumes of text efficiently.

What is en_core_web_trf?
It is a specific language model package for SpaCy that leverages transformer architecture to provide
better accuracy.

Code Steps 
Step 1: Set the image path
Step 2: Initialize PaddleOCR (rotated text detection included)
Step 3: Run OCR on the image
Step 4: Print detected text and confidence
Step 5: Calculate and print the average confidence
Step 6: check if there are any texts (to avoid dividing by zero)
Step 7: Combine all detected text into one string
Step 8: Use SpaCy to detect entities and names
Step 9: Print all entities found
Step 10: Print recipient PERSON(s)

How to use the code?
Line 4 add your image path 

File information:
image_text_extrtactor.py 
Only includes the text extractor.

image_text_entitiy_nameextrtactor.py 
Includes both text entity, name extractror.

Files with 'bgnr' include explainations for each line of code for beginners new to python.

note: Unable to extract names from all the parcel label images i used so tweaks are needed with the 
spaCy model being used. 

note:image_text_extractor.py could even be used to extract text from documents etc. It doesnt only have to be 
a parcel label.

