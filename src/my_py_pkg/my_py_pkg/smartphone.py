#from tokenize import Name
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node):
    def __init__(self):
        super().__init__("smartphone")
        self.subscriber_ = self.create_subscription(String, "robot_news",self.callback_robot_news, 10)
        self.get_logger().info("Smartpone has been started.")

        # self.counter1 = 0
        # self.create_timer(0.5,self.timer_callback,)
    
    def callback_robot_news(self,msg):
        self.get_logger().info(msg.data)
    
    # def timer_callback(self):
    #     self.counter1 += 1
    #     self.get_logger().info("Aj " + str(self.counter1))

def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode()
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == "__main__" :
    main()   