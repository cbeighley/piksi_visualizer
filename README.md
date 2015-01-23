This is a visualizer for the Piksi RTK solution written in Python/PyOpenGL.

#Dependencies
Python dependencies (not including the [piksi_firmware](https://github.com/swift-nav/piksi_firmware) Python dependencies) are contained in `requirements.txt`. You can install these via:

    $ pip install -r requirements.txt
    
See the [piksi_firmware](https://github.com/swift-nav/piksi_firmware) Github page for piksi_firmware dependencies.

#Running the visualizer
After cloning this repo, enter the piksi_firmware directory and enter the following. You'll need to have installed the piksi_firmware toolchain first.

    $ cd piksi_firmware
    $ git submodule init
    $ git submodule update
    $ make
    $ cd ..

You can then run the visualizer.

    $ ./visualizer.py -p /dev/tty.usbserial1234
