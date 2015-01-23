This is a visualizer for the Piksi RTK solution written in Python/PyOpenGL.

#Dependencies
Python dependencies are contained in `requirements.txt`. You can install these via:

    $ pip install -r requirements.txt

You'll also need to build the Piksi firmware, which builds the files which define the Piksi firmware messages, which are a dependency of the visualizer. You'll need to have installed the [piksi_firmware](https://github.com/swift-nav/piksi_firmware) toolchain first.

    $ git submodule update --init --recursive
    $ cd piksi_firmware; make; cd ..

#Running the visualizer
Enter the below, where `/dev/tty.usbserial1234` is your Piksi's virtual com port.

    $ ./visualizer.py -p /dev/tty.usbserial1234
