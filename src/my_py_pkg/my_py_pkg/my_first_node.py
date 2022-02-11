#from tokenize import Name
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hi Aj")

        self.counter1 = 0
        self.create_timer(0.5,self.timer_callback,)
    
    def timer_callback(self):
        self.counter1 += 1
        self.get_logger().info("Aj " + str(self.counter1))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == "__main__" :
    main()   