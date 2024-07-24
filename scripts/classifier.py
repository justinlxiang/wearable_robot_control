import joblib
import mindrove_package.utils as utils
import numpy as np
import pandas as pd
import rospy
import sklearn
from std_msgs.msg import String

from mindrove_package.msg import MindRoveData


def classify_data(input):
    gestures = ["wave", "push", "squeeze", "point", "thumb_up"]
    classification = gestures[int(model.predict([input])[0])]
    return classification


def detect_trigger(input):
    outputs = ["yes", "no"]
    classification = outputs[int(trigger_model.predict([input])[0])]
    return classification


def callback(msg):
    if publish:
        if publish_counter == 1000:
            data = np.array(msg.data)
            data = data.reshape(1000, 14)
            emg_data = data[:, :8]
            imu_data = data[:, 8:]
            emg_df = pd.DataFrame(emg_data, columns=[f"EMG_{i}" for i in range(8)])
            imu_df = pd.DataFrame(
                imu_data,
                columns=[f"Gyro_{i}" for i in range(3)]
                + [f"Accel_{i}" for i in range(3)],
            )
            features = utils.extract_features(emg_df, imu_df)

            classification = classify_data(features)
            publish = False
            publish_counter = 0
            pub.publish(classification)
        else:
            publish_counter += 1
    else:
        data = np.array(msg.data)
        data = data.reshape(1000, 14)
        emg_data = data[:, :8]
        imu_data = data[:, 8:]
        emg_df = pd.DataFrame(emg_data, columns=[f"EMG_{i}" for i in range(8)])
        imu_df = pd.DataFrame(
            imu_data,
            columns=[f"Gyro_{i}" for i in range(3)] + [f"Accel_{i}" for i in range(3)],
        )
        features = utils.extract_features(emg_df, imu_df)

        classification = detect_trigger(features)

        if classification == "yes":
            publish = True


def listener():
    rospy.init_node("classifier_node", anonymous=True)
    rospy.Subscriber("mindrove_data", MindRoveData, callback)
    global pub
    pub = rospy.Publisher("classification_result", String, queue_size=10)

    model_path = rospy.get_param("~model_path")
    trigger_model_path = rospy.get_param("~trigger_model_path")

    # Load the Random Forest model
    global model, trigger_model
    model = joblib.load(model_path)
    trigger_model = joblib.load(trigger_model_path)

    global publish, publish_counter
    publish = False
    publish_counter = 0

    rospy.spin()


if __name__ == "__main__":
    listener()
