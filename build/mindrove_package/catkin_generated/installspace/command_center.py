import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sound_play.libsoundplay import SoundClient

def callback(msg):
    classification = msg.data
    if classification == "wave":
        send_goal(1.0, 2.0, 0.0, 1.0)  # Example coordinates
    elif classification == "push":
        send_goal(-1.0, 0.0, 0.0, 1.0)  # Move out of the way
    elif classification == "squeeze":
        change_lights(255, 0, 0)  # Change lights to red
    elif classification == "point":
        play_sound('/path/to/sound/file.wav')  # Play a sound
    elif classification == "thumb_up":
        play_sound('/path/to/sound/file.wav')  # Play a sound

def send_goal(x, y, z, w):
    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = z
    goal.pose.orientation.w = w
    goal_pub.publish(goal)

def change_lights(r, g, b):
    rospy.wait_for_service('/mm1/led/set_strip_color')
    try:
        set_strip_color = rospy.ServiceProxy('/mm1/led/set_strip_color', rospy.SetStripColor)
        set_strip_color(0, r, g, b)  # Left strip
        set_strip_color(1, r, g, b)  # Right strip
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def play_sound(file_path):
    soundhandle = SoundClient()
    rospy.sleep(1)
    soundhandle.playWave(file_path)

def listener():
    rospy.init_node('command_center', anonymous=True)
    rospy.Subscriber('classification_result', String, callback)
    global pub, goal_pub
    pub = rospy.Publisher('robot_command', String, queue_size=10)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
