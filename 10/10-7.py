import tensorflow as tf
import cv2
img_add_list = []
img_label_list = []

with open("train_list.csv") as fid:
    for image in fid.readlines():
        img_add_list.append(image.strip().split(",")[0])
        img_label_list.append(image.strip().split(",")[1])

def get_image(image_path):
    return tf.image.convert_image_dtype(
        tf.image.decode_jpeg(
            tf.read_file(image_path),channels = 1
        ),dtype = tf.uint8
    )

img = get_image('jpg\\image_0001.jpg')
sess = tf.Session()
cv2Img = sess.run(img)
cv2.imshow("image",cv2Img)
cv2.waitKey()