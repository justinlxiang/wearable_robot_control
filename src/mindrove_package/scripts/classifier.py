import rospy
from mindrove_package.msg import MindRoveData
from std_msgs.msg import String

from classifier import classify_data

def callback(data):
    classification = classify_data(data.data)
    pub.publish(classification)

def listener():
    rospy.init_node('classifier_node', anonymous=True)
    rospy.Subscriber('mindrove_data', MindRoveData, callback)
    global pub
    pub = rospy.Publisher('classification_result', String, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()