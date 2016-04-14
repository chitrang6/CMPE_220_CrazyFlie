import sys
sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType
import time

try:
    import zmq
except ImportError as e:
    raise Exception("ZMQ library probably not installed ({})".format(e))

context = zmq.Context()
sender = context.socket(zmq.PUSH)
bind_addr = "tcp://127.0.0.1:{}".format(1024 + 188)
sender.connect(bind_addr)

cmdmess = {
    "version": 1,
    "ctrl": {
        "roll": 0.0,
        "pitch": 0.0,
        "yaw": 0.0,
        "thrust": 30
    }
}

print("starting to send control commands!")


class CrazyFlie_listner(DeviceListener):
    def on_pose(self, pose):
        context = zmq.Context()
        sender = context.socket(zmq.PUSH)
        bind_addr = "tcp://127.0.0.1:{}".format(1024 + 188)
        sender.connect(bind_addr)
        cmdmess = {
   			 "version": 1,
    		"ctrl": {
       	 "roll": 0.0,
       	 "pitch": 0.0,
       	 "yaw": 0.0,
       	 "thrust": 30
   		 }
		}
        print("Starting to send control commands!")
        # Unlocking thrust protection
        cmdmess["ctrl"]["thrust"] = 0
        sender.send_json(cmdmess)
        pose_type = PoseType(pose)
        print(pose_type.name)
        if pose_type.name == 'DOUBLE_TAP':
            cmdmess["ctrl"]["thrust"] = (5500 ) / 100.0
            sender.send_json(cmdmess)
            time.sleep(0.01)
            print('Hi  ')
        elif pose_type.name == 'WAVE_IN':
            print('Hi  ')
            cmdmess["ctrl"]["thrust"] = ( 7500 ) / 100.0
            sender.send_json(cmdmess)
            time.sleep(0.01)
        else:
            cmdmess["ctrl"]["thrust"] = 0
            sender.send_json(cmdmess)
