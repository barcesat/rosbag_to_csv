import csv
from pathlib import Path
from rosbags.highlevel import AnyReader

p = False

rosbag_path = 'imu record/good_imu_CB_prototype/rosbag2_2024_05_21-18_13_23/'

# Create a csv file to write to
with open(rosbag_path+'imu_data_temp.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'temperature']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # create reader instance and open for reading
    with AnyReader([Path(rosbag_path)]) as reader:
        connections = [x for x in reader.connections if x.topic == '/temperature']
        for connection, timestamp, rawdata in reader.messages(connections=connections):
            msg = reader.deserialize(rawdata, connection.msgtype)
            if p:
                print(str(msg.header.stamp.sec) + '.' + str(msg.header.stamp.nanosec), msg.temperature)
            writer.writerow({'timestamp': str(msg.header.stamp.sec) + '.' + str(msg.header.stamp.nanosec),
                            'temperature': msg.temperature,
                             })