import rospy
from std_msgs.msg import String

def callback(data):
    command = determine_robot_command(data.data)
    pub.publish(command)

def determine_robot_command(classification : String):
    return

def listener():
    rospy.init_node('command_center', anonymous=True)
    rospy.Subscriber('classification_result', String, callback)
    global pub
    pub = rospy.Publisher('robot_command', String, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
