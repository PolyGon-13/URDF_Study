# /scan 토픽에서 유효한 intensites와 ranges 값만 뽑아내기
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class ScanFilterNode(Node):
    def __init__(self):
        super().__init__('ranges_intensities_filter')
        self.subscription=self.create_subscription(
            LaserScan, # 메시지 타입
            '/scan', # /scan 이라는 토픽 구독
            self.scan_callback, # 콜백함수
            10 # 큐사이즈
        )

    def scan_callback(self,msg):
        valid_ranges=[r for r in msg.ranges if not math.isinf(r) and not math.isnan(r)]
        valid_intensities=[i for i in msg.intensities if i>0.0]

        self.get_logger().info(f'Valid Ranges ({len(valid_ranges)}): {valid_ranges[:10]}...')
        self.get_logger().info(f'Valid Intensities ({len(valid_intensities)}): {valid_intensities[:10]}...')

def main(args=None):
    rclpy.init(args=args) # ROS2 시스템 초기화
    node=ScanFilterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()