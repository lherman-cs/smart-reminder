import tensorflow as tf
import cv2 as cv


class Model:

    def __init__(self):
        with tf.gfile.FastGFile('model/frozen_inference_graph.pb', 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())

        self.sess = tf.Session()
        self.sess.graph.as_default()
        tf.import_graph_def(graph_def, name='')

    def __del__(self):
        self.sess.close()

    def is_person(self, img):
        sess = self.sess

        inp = cv.resize(img, (300, 300))
        inp = inp[:, :, [2, 1, 0]]  # BGR2RGB

        # Run the model
        out = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                        sess.graph.get_tensor_by_name('detection_scores:0'),
                        sess.graph.get_tensor_by_name('detection_classes:0')],
                       feed_dict={'image_tensor:0': inp.reshape(1, inp.shape[0], inp.shape[1], 3)})

        num_detections = int(out[0][0])
        for i in range(num_detections):
            classId = int(out[2][0][i])
            score = float(out[1][0][i])
            if score > 0.3 and classId == 1:
                return True

        return False
