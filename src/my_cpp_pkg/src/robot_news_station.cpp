#include "rclcpp/rclcpp.hpp"

class RobotNewsStationNode : public rclcpp::Node {
public:
    RobotNewsStationNode(): Node("robor_news_stations")
    {
    }

private:
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}  