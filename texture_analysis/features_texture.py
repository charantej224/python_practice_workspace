import json
import cv2
import os

annotations = "/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/instances_val2017.json"
images = "/home/charan/Documents/research/deep_lite/current_work/val2017"

image_name = "000000289343.jpg"
image_id = "289343"
x_min = 473.07
y_max = 395.93
width, height = 38.65, 28.67
x_max, y_min = round(x_min + width), round(y_max + height)
x_min, y_max = round(x_min), round(y_max)

image_path = os.path.join(images, image_name)

image = cv2.imread(image_path)
# cv2.imshow("original", image)
# cv2.waitKey(0)
print(x_min, y_min, x_max, y_max)
cropped = image[y_max:y_min, x_min:x_max]
image = cv2.rectangle(image, (x_min, y_max), (x_max, y_min), (255, 0, 0), 2)
cv2.imshow("plotting", image)
cv2.imwrite("original.png", image)
# cv2.waitKey(0)

cv2.imshow("cropped", cropped)
cv2.imwrite("cropped.png", cropped)
# cv2.waitKey(0)

# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
# from PIL import Image
#
# # Display the image
# plt.imshow(Image.open(image_path))
#
# # Add the patch to the Axes
# plt.gca().add_patch(Rectangle((x_min, y_max), width, height, linewidth=1, edgecolor='r', facecolor='none'))
# plt.show()
