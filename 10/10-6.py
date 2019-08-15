import tensorflow as tf
import cv2

img_add_list = []
img_label_list = []
with open("train_list.csv") as fid:
    for image in fid.readlines():
        img_add_list.append(image.strip().split(",")[0])
        img_label_list.append(image.strip().split(",")[1])

img = tf.image.convert_image_dtype(tf.image.decode_jpeg(tf.read_file('jpg\\image_0000.jpg'),channels = 1),dtype = tf.float32)
print(img)