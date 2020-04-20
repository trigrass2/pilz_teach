#! /usr/bin/env python

# Copyright (c) 2019 Pilz GmbH & Co. KG
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import rospy
from pilz_teleoperation import PoseFileTFPublisher


if __name__ == '__main__':
    rospy.init_node("pose_visualisation")
    try:
        file_path = rospy.get_param("~file_path")
        pb = PoseFileTFPublisher()
        pb.publish_poses_from_file_loop(file_path)
    except ImportError:
        rospy.logerr("path invalid!")
    except rospy.ROSInterruptException:
        pass
