#!/usr/bin/env python3

import rospy
import rospy
from geometry_msgs.msg import Twist

def move_robot():
    # ROS düğümünü başlat
    rospy.init_node('move_robot', anonymous=True)

    # /cmd_vel konusuna mesaj yayınlamak için Publisher oluştur
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Twist mesajı oluştur
    vel_msg = Twist()

    # Mesajın hız değerlerini ayarla
    vel_msg.linear.x = 0.5  # İleri doğru hız
    vel_msg.angular.z = 0.2  # Saat yönünde dönüş

    # Yayınlama oranını ayarla
    rate = rospy.Rate(10)  # 10 Hz

    # Sürekli döngü
    while not rospy.is_shutdown():
        # Mesajı yayınla
        velocity_publisher.publish(vel_msg)
        rospy.loginfo(f"Robot is moving: Linear={vel_msg.linear.x}, Angular={vel_msg.angular.z}")
        rate.sleep()

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
