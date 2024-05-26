import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt
import io

def analyze_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to RGB (pytesseract expects RGB)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(rgb_image)
    return extracted_text

def segment_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    sure_bg = cv2.dilate(closing, kernel, iterations=3)
    
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    _, markers = cv2.connectedComponents(sure_fg)
    
    markers = markers + 1
    markers[unknown == 0] = 0
    
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]
    
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.savefig('segmented_image.png')  # Save segmented image
    plt.close()

def main(image_path):
    # Analyze image and extract text
    extracted_text = analyze_image(image_path)
    
    # Segment image
    segment_image(image_path)
    
    # Write extracted text and embed image into HTML file
    with open('output.html', 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Image Analysis Report</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<h1>Extracted Text</h1>\n')
        f.write('<p>' + extracted_text.replace('\n', '<br>') + '</p>\n')
        f.write('<h1>Segmented Image</h1>\n')
        f.write('<img src="segmented_image.png" alt="Segmented Image">\n')
        f.write('</body>\n')
        f.write('</html>\n')

# Example :
# main('/home/nitin1053/Documents/ml/Screenshot from 2023-01-08 00-59-31.png')

main('/path of your image.png')

