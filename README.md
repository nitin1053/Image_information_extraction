

PROJECT_NAME="Image Analysis Project"
DESCRIPTION="This project utilizes Tesseract OCR and OpenCV to perform text extraction and image segmentation on an input image."
AUTHOR="Nitin Jha"



## Installation
### Prerequisites
- Python 3
- Tesseract OCR
- OpenCV
- pytesseract

### Installation Steps
1. Install Tesseract OCR:
   \`\`\`sh
   sudo apt-get update
   sudo apt-get install tesseract-ocr
   \`\`\`

2. Install Python libraries:
   \`\`\`sh
   pip install opencv-python pytesseract
   \`\`\`

## Usage
1. Clone the repository:
   \`\`\`sh
   git clone <repository-url>
   cd <repository-name>
   \`\`\`

2. Run the main script:
   \`\`\`sh
   python image_analysis.py
   \`\`\`

## Project Structure
- **image_analysis.py**: Python script for text extraction and image segmentation.
- **segmented_image.png**: Output image with segmented visual elements.
- **output.html**: HTML file containing extracted text and embedded image.



EOF

echo "README.md generated successfully!"
