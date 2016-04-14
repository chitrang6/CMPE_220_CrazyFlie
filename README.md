# Myo4Intel Edsion

    This is the library for the communication between Myo- ARM band and the Intel Edison Board. You must connect the BLE dongle provided by the Thalmic Labs to Intel Ediosn. After connection the BLE, dongle tou need to run the print_pose_listner.py and then run the test_myo.py to test the Myo Arm Band.You can peroform different gesture to test the Myo ARM Band.

## Pre-requirements for your Myo device
- Firmware version 1.3.1448 or higher
- It is necessary to calibrate your Myo device using the official software.
- Use the Myo dongle bluetooth

## Requirements
- python >=2.6
- pySerial
- enum34

## Execute Sample
The Myo dongle bluetooth must be connected.

- Open the console "terminal" 
- Go to sample folder in the project
- Execute this command:
  
  ```
  python test_myo.py
  ```
