import tensorflow as tf
import numpy as np
a_data = 0.55
b_data = [58]
c_data = np.array([[1,4,5,6],[7,5,7,3]])
c = c_data.astype(np.uint8)
c_raw = c.tostring()

example = tf.train.Example(
    features = tf.train.Features(
        feature = {
            'a':tf.train.Feature(
                float_list = tf.train.FloatList(value = [a_data]) #方括号表示列表
            ),
            'b':tf.train.Feature(
                int64_list = tf.train.Int64List(value = b_data)#b_data本身就是列表
            ),
            'c':tf.train.Feature(
                bytes_list = tf.train.BytesList(value = [c_raw])#c_raw被转化为byte格式
            )
        }
    )
)