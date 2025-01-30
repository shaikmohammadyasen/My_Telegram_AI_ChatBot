import cv2
import pytesseract
from PIL import Image
import PyPDF2
import numpy as np

# Function to process image files (OCR)
def process_image(image_path):
    try:
        # Load the image using OpenCV
        img = cv2.imread(image_path)
        
        # Convert the image to grayscale for better OCR accuracy
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding (you can adjust the parameters for better results)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        
        # Save the processed image for debugging (optional)
        processed_image_path = 'processed_image.jpg'
        cv2.imwrite(processed_image_path, thresh)
        
        # Use pytesseract to extract text from the processed image
        text = pytesseract.image_to_string(thresh)
        
        return text
    except Exception as e:
        return f"Error processing image: {e}"

# Function to process PDF files
def process_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            
            # Extract text from all pages
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        
        return text
    except Exception as e:
        return f"Error processing PDF: {e}"

# Example of using the functions
if __name__ == "__main__":
    # Example usage for image
    image_text = process_image('example_image.jpg')
    print("Extracted Text from Image:", image_text)
    
    # Example usage for PDF
    pdf_text = process_pdf('example_document.pdf')
    print("Extracted Text from PDF:", pdf_text)