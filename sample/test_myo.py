import sys
sys.path.append('../lib/')

from myo import Myo
from print_pose_listener import PrintPoseListener
from CrazyFlie_listner import CrazyFlie_listner
from vibration_type import VibrationType

def main():
    print('Start Myo for Intel Edison or any Linux and Mac Complient Devices:')

    listener = PrintPoseListener()
    crazy_listner = CrazyFlie_listner()
    myo = Myo()

    try:
        myo.connect()
        myo.add_listener(listener)
        myo.add_listener(crazy_listner)
        myo.vibrate(VibrationType.SHORT)
        while True:
            myo.run()

    except KeyboardInterrupt:
        pass
    except ValueError as ex:
        print(ex)
    finally:
        myo.safely_disconnect()
        print('Finished.')

if __name__ == '__main__':
    main()
