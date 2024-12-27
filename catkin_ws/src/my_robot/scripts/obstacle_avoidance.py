#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(scan):
    # LIDAR verilerini işleyerek robotun etrafındaki mesafeleri hesapla
    regions = {
        'front': min(min(scan.ranges[0:10] + scan.ranges[-10:]), 10),
        'left': min(min(scan.ranges[30:60]), 10),
        'right': min(min(scan.ranges[-60:-30]), 10),
    }

    rospy.loginfo(f"Regions: {regions}")  # LIDAR verilerini logla

    move = Twist()

    # Engellerden kaçınma mantığı
    if regions['front'] < 1.0:  # Önünde engel varsa
        move.linear.x = 0.0
        move.angular.z = 0.3  # Sağa dön
    elif regions['left'] < 1.0:  # Solunda engel varsa
        move.linear.x = 0.1
        move.angular.z = -0.3  # Sağa yönel
    elif regions['right'] < 1.0:  # Sağında engel varsa
        move.linear.x = 0.1
        move.angular.z = 0.3  # Sola yönel
    else:  # Engel yoksa düz ilerle
        move.linear.x = 0.5
        move.angular.z = 0.0

    pub.publish(move)

if __name__ == '__main__':
    rospy.init_node('obstacle_avoidance')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()
