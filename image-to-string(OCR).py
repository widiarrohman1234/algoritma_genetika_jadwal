from PIL import Image
import pytesseract

# Load the uploaded image
image_path = 'jadwal_S2_SM1_PENS.png'
image = Image.open(image_path)

# Use OCR to extract text from the image
extracted_text = pytesseract.image_to_string(image)

print(extracted_text)