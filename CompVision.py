import cv2
import numpy as np

def add_license_plate_annotation(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise Exception("Could not read the input image")

    # Get image dimensions
    height, width = img.shape[:2]

    # This is to adjust values for better license plate coverage
    x = int(width * 0.1)  
    y = int(height * 0.15)  
    w = int(width * 0.67)   
    h = int(height * 0.82)   

    # Draw green rectangle
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)

    # This is to deal with text
    text = "RAH972U"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 5
    font_color = (0, 255, 0)  

    # Get text size
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)

    # Position text in top right corner with padding
    text_x = width - text_width - 20
    text_y = text_height + 60
    padding = 10

    overlay = img.copy()
    cv2.rectangle(overlay, 
                 (text_x - padding, text_y - text_height - padding),
                 (text_x + text_width + padding, text_y + padding),
                 (0, 0, 0),  
                 -1)  
    
    # Apply the overlay with transparency
    alpha = 0.3 
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

    # Add text
    cv2.putText(img, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

    # Show the image
    cv2.imshow("Updated image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    cv2.imwrite(output_path, img)
    print(f"Image saved successfully to {output_path}")

try:
    # Process the image
    add_license_plate_annotation("assignment-001-given.png", "assignment-001-result.jpg")
except Exception as e:
    print(f"Error processing image: {str(e)}")