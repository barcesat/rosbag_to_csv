import csv
from pathlib import Path
from rosbags.highlevel import AnyReader

p = False

rosbag_path = 'imu record/good_imu_CB_prototype/rosbag2_2024_05_21-18_13_23/'

# Create a csv file to write to
with open(rosbag_path+'imu_data_av.csv', 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'angular_velocity_x', 'angular_velocity_y','angular_velocity_z','cov0','cov1','cov2','cov3','cov4','cov5','cov6','cov7','cov8']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # create reader instance and open for reading
    with AnyReader([Path(rosbag_path)]) as reader:
        connections = [x for x in reader.connections if x.topic == '/imu/data']
        for connection, timestamp, rawdata in reader.messages(connections=connections):
            msg = reader.deserialize(rawdata, connection.msgtype)
            if p:
                print(str(msg.header.stamp.sec) + '.' + str(msg.header.stamp.nanosec), msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z,  msg.angular_velocity_covariance[0],
                      msg.angular_velocity_covariance[1], msg.angular_velocity_covariance[2], msg.angular_velocity_covariance[3], msg.angular_velocity_covariance[4], msg.angular_velocity_covariance[5],
                      msg.angular_velocity_covariance[6], msg.angular_velocity_covariance[7], msg.angular_velocity_covariance[8])
            writer.writerow({'timestamp': str(msg.header.stamp.sec) + '.' + str(msg.header.stamp.nanosec),
                            'angular_velocity_x': msg.angular_velocity.x,
                            'angular_velocity_y':msg.angular_velocity.y,
                            'angular_velocity_z':msg.angular_velocity.z,
                            'cov0':msg.angular_velocity_covariance[0],
                            'cov1':msg.angular_velocity_covariance[1],
                            'cov2':msg.angular_velocity_covariance[2],
                            'cov3':msg.angular_velocity_covariance[3],
                            'cov4':msg.angular_velocity_covariance[4],
                            'cov5':msg.angular_velocity_covariance[5],
                            'cov6':msg.angular_velocity_covariance[6],
                            'cov7':msg.angular_velocity_covariance[7],
                            'cov8':msg.angular_velocity_covariance[8]
                             })