# samples가 360이어서 불필요한 /scan topic값 제외
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanFieldPrinter(Node):
    def __init__(self):
        super().__init__('scan_filter_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10
            )
        
    def listener_callback(self, msg: LaserScan):
        print(f"header.stamp.sec : {msg.header.stamp.sec}")
        print(f"header.stamp.nanosec : {msg.header.stamp.nanosec}")
        print(f"header.frame_id : {msg.header.frame_id}")
        print(f"angle_min : {msg.angle_min}")
        print(f"angle_max : {msg.angle_max}")
        print(f"angle_increment : {msg.angle_increment}")
        print(f"time_increment : {msg.time_increment}")
        print(f"scan_time : {msg.scan_time}")
        print(f"range_min : {msg.range_min}")
        print(f"range_max : {msg.range_max}")
        print('---------------------------')

def main(args=None):
    rclpy.init(args=args)
    node=ScanFieldPrinter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
