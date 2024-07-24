from scipy.signal import butter, lfilter
import numpy as np

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def extract_features(emg_data, imu_data, fs=1000):
    emg_filtered = butter_bandpass_filter(emg_data.values, 20, 450, fs, order=4)

    # Calculate time-domain features for each EMG channel
    features = []
    for channel in range(emg_filtered.shape[1]):
        channel_data = emg_filtered[:, channel]
        mav = np.mean(np.abs(channel_data))
        rms = np.sqrt(np.mean(channel_data ** 2))
        wl = np.sum(np.abs(np.diff(channel_data)))
        zc = np.sum(np.abs(np.diff(np.sign(channel_data)))) / 2
        ssc = np.sum(np.abs(np.diff(np.sign(np.diff(channel_data))))) / 2
        iemg = np.sum(np.abs(channel_data))
        features.extend([mav, rms, wl, zc, ssc, iemg])

    # Calculate IMU features
    for sensor in ['Gyro', 'Accel']:
        for axis in ['0', '1', '2']:
            channel_data = imu_data[f'{sensor}_{axis}'].values
            mav = np.mean(np.abs(channel_data))
            rms = np.sqrt(np.mean(channel_data ** 2))
            wl = np.sum(np.abs(np.diff(channel_data)))
            zc = np.sum(np.abs(np.diff(np.sign(channel_data)))) / 2
            ssc = np.sum(np.abs(np.diff(np.sign(np.diff(channel_data))))) / 2
            
            max_value = np.max(channel_data)
            min_value = np.min(channel_data)
            range_value = max_value-min_value
            std_value = np.std(channel_data)
            mean = np.mean(channel_data)
            skew_gyro = np.mean((channel_data - mean) ** 3) / (std_value ** 3)
            kurt_gyro = np.mean((channel_data - mean) ** 4) / (std_value ** 4)
            
            features.extend([mav, rms, wl, zc, ssc, mean, std_value, max_value, min_value, range_value, skew_gyro, kurt_gyro])

    features_array =  np.array(features)
    
    # Check for NaN values
    if np.isnan(features_array).any():
        print("NaN values found in features")
        nan_indices = np.where(np.isnan(features_array))
        print("NaN indices:", nan_indices)
        print("NaN values:", features_array[nan_indices])
    
    return features_array