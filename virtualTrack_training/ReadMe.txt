This Arduino sketch and python GUI are for running behavior as well as imaging experiments in a virtual reality context. To generate the virtual track in our experiments we use a spherical treadmill that can spin on one axis. A mouse is head-fixed as it sits on top of the Styrofoam sphere. The mouse is trained to run in head-fixed state on the sphere.

The Arduino sketch is written to run with Arduino Mega (http://arduino.cc/en/Main/arduinoBoardMega ).It should run well with Arduino Due too, because the pin layout on both boards are practically same for our purposes. A rotary encoder, connected to analogue pin#10 (A10) on the Arduino, reads the movement of the spinning sphere.

The Arduino controls eight solenoid valves(digital pins 22, 24, 26, 28, 30, 32, 34 and 36). The valve connected to pin#36 is for delivering water reward to the mouse through the lick port. The other 7 valves control airflow to deliver desired odors to the mouse.

Digital pin#40 is set up to send out an imaging trigger to the microscope (in our case, an Inscopix scope: http://www.inscopix.com/ ) to start recording images. Similarly, digital pin#44 receives a signal from the scope each time an image frame is captured.

An MPR121 capacitative touch sensor (https://www.sparkfun.com/products/9695 ) is connected to digital pin#13. It serves as a very reliable lick sensor to register mouse licks. However, it requires some fairly complicated integration with the Arduino sketch. The lickport.cpp and parameter_definitions.h files are solely to run this lick sensor. You will probably never have to go back to these files once you get the lick sensor working.

MPR121-breakout-v3 touch sensor is connected to the arduino with 5 wires:
1. GND - connected to arduino ground
2. SDA - arduino SDA (pin#20)
3. SCL - arduino SCL (pin#21)
4. IRQ - digital pin#13
5. 3.3V - 3.3V supply pin on arduino

Electrode pin#0 on the touch sensor is connected to the metal lick port. (any of the 12 electrode pins should work just as fine)


##############################################################################################################

Here are the general steps for running the whole program:

1. First load the Arduino sketch named virtualTrack.ino (make sure to choose the right board and Serial port before attempting to load the sketch).
	   
2. Then open the GUI window named virtualTrack_GUI.py (runs with 32-bit Python 2.7, not sure about other versions). You might need to install the serial library if your version of python doesn't have it already.

3. In the GUI, set the parameters as needed. Once you hit start, the program will begin to save the collected data in a .csv file in the designated folder (currently set to create a folder named 'Recordings' on the Desktop to save this file).

###############################################################################################################

 

Best wishes !!


nj2292@columbia.edu
November 24, 2014
