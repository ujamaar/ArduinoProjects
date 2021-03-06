import Tkinter
import serial
import time
import datetime
import os, errno
ser = serial.Serial(11,115200) #ArduinoMega is on COM12 port

#If above doesn't work, try these:
#ser = serial.Serial('/dev/ttyS1',115200) #this one works with Arduino Due
#ser = serial.Serial('/dev/ttyACM1',115200)
#ser = serial.Serial('/dev/ttyUSB1',115200)
#ser = serial.Serial('com1',115200)
#ser = serial.Serial('COM1',115200)

#create a new window
window = Tkinter.Tk()
#set the window title
window.title("Mouse Virtual Reality Experiment")


mouse_label = Tkinter.Label(window, text="Mouse ID:")#create a label widget
mouse = Tkinter.Entry(window, width=7) #create a text entry widget
mouse.insert(0,"x") #insert default value for the mouse entry
mouse_label.grid(row=0, column=0)
mouse.grid		(row=0, column=1)

reward_size_label = Tkinter.Label(window, text="Reward size(ms):")
reward_size = Tkinter.Entry(window, width=7)
reward_size.insert(0,"30")
reward_size_label.grid(row=1, column=0)
reward_size.grid	  (row=1, column=1)

licks_per_reward_label = Tkinter.Label(window, text="Licks/reward:")
licks_per_reward = Tkinter.Entry(window, width=7)
licks_per_reward.insert(0,"2")
licks_per_reward_label.grid(row=2, column=0)
licks_per_reward.grid	   (row=2, column=1)

reward_window_label = Tkinter.Label(window, text="Reward window(s):")
reward_window = Tkinter.Entry(window, bg = 'light green', width=7)
reward_window.insert(0,"2")
reward_window_label.grid(row=3, column=0)
reward_window.grid		(row=3, column=1)

track_label = Tkinter.Label(window, text="Virtual track(mm):")
track = Tkinter.Entry(window, bg = 'light blue', width=7)
track.insert(0,"2000")
track_label.grid(row=4, column=0)
track.grid		(row=4, column=1)

recording_duration_label = Tkinter.Label(window, text="Recording duration(s):")
recording_duration = Tkinter.Entry(window, fg = 'blue', width=7)
recording_duration.insert(0,"2400")
recording_duration_label.grid(row=5, column=0)
recording_duration.grid		 (row=5, column=1)

blank_label = Tkinter.Label(window, width=7).grid(row=6)
#############################################################################

envA_initial_drop_label = Tkinter.Label(window, text="Initial drop(ms):")
envA_initial_drop = Tkinter.Entry(window, width=5)
envA_initial_drop.insert(0,"30")
envA_initial_drop_label.grid(row=7, column=0)
envA_initial_drop.grid		(row=7, column=1)

envA_max_lap_count_label = Tkinter.Label(window, text="Max laps:")
envA_max_lap_count = Tkinter.Entry(window, width=5)
envA_max_lap_count.insert(0,"1")
envA_max_lap_count_label.grid(row=8, column=0)
envA_max_lap_count.grid		 (row=8, column=1)

envA_odor1_label = Tkinter.Label(window, text="envA_odor1:")
envA_odor1 = Tkinter.Entry(window, fg = 'red', width=5)
envA_odor1.insert(0,"1")
envA_odor1_label.grid(row=9, column=0)
envA_odor1.grid		 (row=9, column=1)

envA_odor2_label = Tkinter.Label(window, text="envA_odor2:")
envA_odor2 = Tkinter.Entry(window, fg = 'red', width=5)
envA_odor2.insert(0,"2")
envA_odor2_label.grid(row=10, column=0)
envA_odor2.grid		 (row=10, column=1)

envA_odor3_label = Tkinter.Label(window, text="envA_odor3:")
envA_odor3 = Tkinter.Entry(window, fg = 'red', width=5)
envA_odor3.insert(0,"3")
envA_odor3_label.grid(row=11, column=0)
envA_odor3.grid		 (row=11, column=1)

blank_label = Tkinter.Label(window, width=5).grid(row=13)
############################################################################

envB_initial_drop_label = Tkinter.Label(window, text="Initial drop(ms):")
envB_initial_drop = Tkinter.Entry(window, width=5)
envB_initial_drop.insert(0,"0")
envB_initial_drop_label.grid(row=14, column=0)
envB_initial_drop.grid		(row=14, column=1)

envB_max_lap_count_label = Tkinter.Label(window, text="Max laps:")
envB_max_lap_count = Tkinter.Entry(window, width=5)
envB_max_lap_count.insert(0,"0")
envB_max_lap_count_label.grid(row=15, column=0)
envB_max_lap_count.grid		 (row=15, column=1)

envB_odor1_label = Tkinter.Label(window, text="envB_odor1:")
envB_odor1 = Tkinter.Entry(window, fg = 'red', width=5)
envB_odor1.insert(0,"0")
envB_odor1_label.grid(row=16, column=0)
envB_odor1.grid		 (row=16, column=1)

envB_odor2_label = Tkinter.Label(window, text="envB_odor2:")
envB_odor2 = Tkinter.Entry(window, fg = 'red', width=5)
envB_odor2.insert(0,"0")
envB_odor2_label.grid(row=17, column=0)
envB_odor2.grid		 (row=17, column=1)

envB_odor3_label = Tkinter.Label(window, text="envB_odor3:")
envB_odor3 = Tkinter.Entry(window, fg = 'red', width=5)
envB_odor3.insert(0,"0")
envB_odor3_label.grid(row=18, column=0)
envB_odor3.grid		 (row=18, column=1)

blank_label = Tkinter.Label(window, width=5).grid(row=19)

random_sequence_label = Tkinter.Label(window, text="Random odor sequence:")
random_sequence = Tkinter.Entry(window, fg = 'blue', width=5)
random_sequence.insert(0,"0")
random_sequence_label.grid(row=20, column=0)
random_sequence.grid	  (row=20, column=1)

# random_sequence = Tkinter.StringVar()
# Tkinter.Checkbutton(window, text="Randomize env sequence", variable=random_sequence,onvalue = 1, offvalue = 0,indicatoron=1).grid(row=22)

#############################################################################
#############################################################################

envC_initial_drop_label = Tkinter.Label(window, text="Initial drop(ms):")
envC_initial_drop = Tkinter.Entry(window, width=5)
envC_initial_drop.insert(0,"0")
envC_initial_drop_label.grid(row=7, column=2)
envC_initial_drop.grid		(row=7, column=3)

envC_max_lap_count_label = Tkinter.Label(window, text="Max laps:")
envC_max_lap_count = Tkinter.Entry(window, width=5)
envC_max_lap_count.insert(0,"0")
envC_max_lap_count_label.grid(row=8, column=2)
envC_max_lap_count.grid		 (row=8, column=3)

envC_odor1_label = Tkinter.Label(window, text="envC_odor1:")
envC_odor1 = Tkinter.Entry(window, fg = 'red', width=5)
envC_odor1.insert(0,"0")
envC_odor1_label.grid(row=9, column=2)
envC_odor1.grid		 (row=9, column=3)

envC_odor2_label = Tkinter.Label(window, text="envC_odor2:")
envC_odor2 = Tkinter.Entry(window, fg = 'red', width=5)
envC_odor2.insert(0,"0")
envC_odor2_label.grid(row=10, column=2)
envC_odor2.grid		 (row=10, column=3)

envC_odor3_label = Tkinter.Label(window, text="envC_odor3:")
envC_odor3 = Tkinter.Entry(window, fg = 'red', width=5)
envC_odor3.insert(0,"0")
envC_odor3_label.grid(row=11, column=2)
envC_odor3.grid		 (row=11, column=3)

blank_label = Tkinter.Label(window, width=5).grid(row=13,column=2)
############################################################################

envD_initial_drop_label = Tkinter.Label(window, text="Initial drop(ms):")
envD_initial_drop = Tkinter.Entry(window, width=5)
envD_initial_drop.insert(0,"0")
envD_initial_drop_label.grid(row=14, column=2)
envD_initial_drop.grid		(row=14, column=3)

envD_max_lap_count_label = Tkinter.Label(window, text="Max laps:")
envD_max_lap_count = Tkinter.Entry(window, width=5)
envD_max_lap_count.insert(0,"0")
envD_max_lap_count_label.grid(row=15, column=2)
envD_max_lap_count.grid		 (row=15, column=3)

envD_odor1_label = Tkinter.Label(window, text="envD_odor1:")
envD_odor1 = Tkinter.Entry(window, fg = 'red', width=5)
envD_odor1.insert(0,"0")
envD_odor1_label.grid(row=16, column=2)
envD_odor1.grid		 (row=16, column=3)

envD_odor2_label = Tkinter.Label(window, text="envD_odor2:")
envD_odor2 = Tkinter.Entry(window, fg = 'red', width=5)
envD_odor2.insert(0,"0")
envD_odor2_label.grid(row=17, column=2)
envD_odor2.grid		 (row=17, column=3)

envD_odor3_label = Tkinter.Label(window, text="envD_odor3:")
envD_odor3 = Tkinter.Entry(window, fg = 'red', width=5)
envD_odor3.insert(0,"0")
envD_odor3_label.grid(row=18, column=2)
envD_odor3.grid		 (row=18, column=3)

blank_label = Tkinter.Label(window, width=5).grid(row=19,column=2)
#############################################################################


#############################################################################
def arduinoParameters():
	parameters = [mouse.get(), 					
				  reward_size.get(),
				  licks_per_reward.get(),
				  reward_window.get(),
				  track.get(),
				  recording_duration.get(),
				  
				  envA_initial_drop.get(),
				  envA_max_lap_count.get(),
				  envA_odor1.get(),
				  envA_odor2.get(),
				  envA_odor3.get(),
				  
				  envB_initial_drop.get(),
				  envB_max_lap_count.get(),
				  envB_odor1.get(),
				  envB_odor2.get(),
				  envB_odor3.get(),

				  envC_initial_drop.get(),
				  envC_max_lap_count.get(),
				  envC_odor1.get(),
				  envC_odor2.get(),
				  envC_odor3.get(),
				  
				  envD_initial_drop.get(),
				  envD_max_lap_count.get(),
				  envD_odor1.get(),
				  envD_odor2.get(),
				  envD_odor3.get(),				  
				  		  
				  random_sequence.get()]			  
				  
	return parameters

def num(s):
    try:
        return int(s)
    except ValueError:
        return -1
	return
	
def timeStamp(fname, fmt='{fname}_%Y_%m_%d_%Hh_%Mm_%Ss'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

def dir_timeStamp(fmt='%Y_%m_%d'):
    return datetime.datetime.now().strftime(fmt)

def main():
	
	fyle = arduinoParameters()
	filename = timeStamp(fyle[0])
	filename = filename + "_behavior.csv"
	print 'Name of this file is: ' + filename
	
	#create a .csv file inside a folder for each mouse to save incoming data from the arduino
	dir_path = 'C:/Users/axel/Desktop/Recordings/' + fyle[0] + '/' + fyle[0] + '_' + dir_timeStamp()
	filename = dir_path + '/' + filename
	if dir_path:
		if not os.path.isdir(dir_path):
			os.makedirs(dir_path)
		dataLog = open(filename, "a+")
	
	#record the detailed conditions of each trial
	trial_details = ('Mouse_name,'+ fyle[0] +
					',Reward_size,'+ fyle[1] + 
					',Licks_per_reward,'+ fyle[2]+
					',Reward_window,'+ fyle[3]+
					',Track_length,'+ fyle[4]+
					',Recording_duration,'+ fyle[5]+
					',envA_initial_drop,'+ fyle[6]+
					',envA_max_number_of_laps,'+ fyle[7]+
					',envA_odor1,'+ fyle[8]+
					',envA_odor2,'+ fyle[9]+
					',envA_odor3,'+ fyle[10]+
					',envB_initial_drop,'+ fyle[11]+
					',envB_max_number_of_laps,'+ fyle[12]+
					',envB_odor1,'+ fyle[13]+
					',envB_odor2,'+ fyle[14]+
					',envB_odor3,'+ fyle[15]+
					',envC_initial_drop,'+ fyle[16]+
					',envC_max_number_of_laps,'+ fyle[17]+
					',envC_odor1,'+ fyle[18]+
					',envC_odor2,'+ fyle[19]+
					',envC_odor3,'+ fyle[20]+
					',envD_initial_drop,'+ fyle[21]+
					',envD_max_number_of_laps,'+ fyle[22]+
					',envD_odor1,'+ fyle[23]+
					',envD_odor2,'+ fyle[24]+
					',envD_odor3,'+ fyle[25]+
					',Random_sequence,'+ fyle[26]+
					'\n')	
	dataLog.write(trial_details)
	
	#this header assigns the labels for each column of the saved data
	header = 'TTLtotalCount,Time,Valve,LickCount,RewardCount,InitialDropCount,RewardWindow,Distance,TotalDistance,LapCount,Environment\n'
	print header.rstrip('\n')
	dataLog.write(header)
	
	#this tells the arduino to start sending data and also provides parameter values
	arduino_parameters = '1'
	for n in range(1,len(fyle)):
		arduino_parameters = arduino_parameters +',' + fyle[n]
	print arduino_parameters
	ser.write(arduino_parameters) 
	
	#now receive and save data, one line per loop
	while True:
		
		currentInput = ser.readline().rstrip('\n')		#rstrip('\n') removes blank lines
		restart_cue = num(currentInput)
		if (restart_cue == 8128):
			print 'End of trial \n'
			break
		print currentInput
		dataLog.write(currentInput)
	dataLog.close()

#create a button widget
click_button = Tkinter.Button(window, text="Start", command = main)
click_button.grid(row=24)

# myGUI = guiMaker()
#draw the window, and start the 'application'
window.mainloop()