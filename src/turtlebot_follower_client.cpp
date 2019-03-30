#include "ros/ros.h"
#include <turtlebot_msgs/SetFollowState.h>
#include <cstdlib>
using namespace std;
int main(int argc,char** argv)
{
    ros::init(argc,argv,"turtlebot_follower_client");
    ros::NodeHandle n;
    ros::ServiceClient client=n.serviceClient<turtlebot_msgs::SetFollowState>("/turtlebot_follower/change_state");
    turtlebot_msgs::SetFollowState order;
    char com=' ';
    while (com!='q')
    {
    cout<<"Next command:"<<endl;
    cin>>com;
    if(com=='w')
    {
        order.request.state=1;
    }
    else if(com=='s')
    {
        order.request.state=0;
    }
    if (client.call(order))
    {
    ROS_INFO("Succeed to call the service!");
    }
    else
    {
    ROS_ERROR("Failed to call the service!");
    return 1;
    }

    }
return 0;

}
