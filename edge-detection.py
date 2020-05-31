import cv2

image = cv2.imread('images/frostmourne.jpg', 0)

sobel_x = cv2.Sobel(image, -1, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, -1, 0, 1, ksize=5)

subplot(1, 2, 1)
imshow(image, cmap ='gray')
title('Original')

subplot(1, 2, 2)
imshow(sobel_y, cmap ='gray')
title('Edge detection')

show()