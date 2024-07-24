import rospy
from mindrove_package.msg import MindRoveData
import numpy as np
import mindrove
from mindrove.board_shim import BoardIds, BoardShim, MindRoveInputParams

def publisher():
    rospy.init_node('mindrove_publisher', anonymous=True)
    pub = rospy.Publisher('mindrove_data', MindRoveData, queue_size=1)
    BoardShim.enable_dev_board_logger()
    board_id = BoardIds.MINDROVE_WIFI_BOARD.value
    params = MindRoveInputParams()
    board = BoardShim(BoardIds.MINDROVE_WIFI_BOARD, params)
    board.prepare_session()
    board.start_stream()
    emg_channels = BoardShim.get_emg_channels(BoardIds.MINDROVE_WIFI_BOARD)
    gyro_channels = BoardShim.get_gyro_channels(BoardIds.MINDROVE_WIFI_BOARD)
    accel_channels = BoardShim.get_accel_channels(BoardIds.MINDROVE_WIFI_BOARD)
    sampling_rate = BoardShim.get_sampling_rate(board_id)
    # sampling_period = 1 / sampling_rate

    rate = rospy.Rate(sampling_rate)
    while not rospy.is_shutdown():
        data = board.get_current_board_data(1000)
        if data.shape[1] < 1000:
            continue
            
        emg_data = data[emg_channels]
        gyro_data = data[gyro_channels]
        accel_data = data[accel_channels]

        msg = MindRoveData()
        msg.data = np.transpose(np.vstack((emg_data, gyro_data, accel_data))).flatten().tolist()
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass