import rospy
from std_msgs.msg import String

def callback(data):
    command = determine_robot_command(data.data)
    pub.publish(command)

def determine_robot_command(classification : String):
    # gestures = ['wave', 'push', 'squeeze', 'point', 'thumb_up']
    if classification == "wave":
        print("wave")
    elif classification == "push":
        print("point")
    elif classification == "squeeze":
        print("squeeze")
    elif classification == "point":
        print("point")
    elif classification == "thumb_up":
        print("thumb_up")

def listener():
    rospy.init_node('command_center', anonymous=True)
    rospy.Subscriber('classification_result', String, callback)
    global pub
    pub = rospy.Publisher('robot_command', String, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
