import numpy as np
import cv2

def detect_noise(image, threshold=2.0):
    #Mengubah gambar menjadi grayscale (0 - 255)
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    # Menambaghkan padding pada gambar
    padded_image = np.pad(gray_image, pad_width=1, mode='constant', constant_values=0)
    
    # Mendapatkan nilai panjang (rows) dan lebar (cols) dari gambar
    rows, cols = gray_image.shape
    
    # Initialize the noise mask
    noise_mask = np.zeros_like(gray_image, dtype=bool)
    
    # Iterate over each pixel in the original image
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            # Extract the 3x3 neighborhood
            neighborhood = padded_image[i-1:i+2, j-1:j+2]
            
            # Calculate the local mean and variance
            local_mean = np.mean(neighborhood)
            local_variance = np.var(neighborhood)
            
            # Calculate the standard deviation
            local_std = np.sqrt(local_variance)
            
            # Get the pixel value
            pixel_value = gray_image[i-1, j-1]
            
            # Determine if the pixel is noise
            if abs(pixel_value - local_mean) > threshold * local_std:
                noise_mask[i-1, j-1] = True
    
    return noise_mask

# Example usage
image_path = 'D:\\GitHub\\PDP-Genap-2024\\codePython\\result-0.png'
image = cv2.imread(image_path)

noise_mask = detect_noise(image, threshold=2.0)