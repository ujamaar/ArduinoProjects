import Tkinter
import serial
import time
import datetime
import os, errno
ser = serial.Serial(11,115200) #ArduinoMega is on COM11 port
#ser = serial.Serial('/dev/ttyS4',115200)

#create a new window
window = Tkinter.Tk()
#set the window title
window.title("Training a mouse to run on a ball")


mouse_label = Tkinter.Label(window, text="Mouse").grid(row=0) #create a label widget
mouse = Tkinter.Entry(window) #create a text entry widget
mouse.insert(0,"x") #insert default value for the mouse entry

reward_size_label = Tkinter.Label(window, text="Reward size(ms):").grid(row=1)
reward_size = Tkinter.Entry(window)
reward_size.insert(0,"30")

licks_per_reward_label = Tkinter.Label(window, text="Licks per reward:").grid(row=2)
licks_per_reward = Tkinter.Entry(window)
licks_per_reward.insert(0,"2")

initial_drop_label = Tkinter.Label(window, text="Initial drop size(ms):").grid(row=3)
initial_drop = Tkinter.Entry(window)
initial_drop.insert(0,"30")

reward_window_label = Tkinter.Label(window, text="Reward window(s):").grid(row=4)
reward_window = Tkinter.Entry(window)
reward_window.insert(0,"10")

track_label = Tkinter.Label(window, text="Track length(mm):").grid(row=5)
track = Tkinter.Entry(window, bg = 'light green')
track.insert(0,"1000")

recording_duration_label = Tkinter.Label(window, text="Recording duration(s):").grid(row=6)
recording_duration = Tkinter.Entry(window)
recording_duration.insert(0,"60")

#arrange the entry fields in a grid layout
mouse.grid(row=0, column=1)
reward_size.grid(row=1, column=1)
licks_per_reward.grid(row=2, column=1)
initial_drop.grid(row=3, column=1)
reward_window.grid(row=4, column=1)
track.grid(row=5, column=1)
recording_duration.grid(row=6, column=1)	


##########################################################################

def arduinoParameters():
	parameters = [mouse.get(), 					#0
				  reward_size.get(), 			#1
				  licks_per_reward.get(), 		#2
				  initial_drop.get(), 			#3
				  recording_duration.get(),		#4
				  reward_window.get(), 			#5
				  track.get()]					#6
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
					',Initial_drop,'+ fyle[3]+
					',Recording_duration,'+ fyle[4]+
					',Reward_window,'+ fyle[5]+
					',Track_length,'+ fyle[6]+
					'\n')	
	dataLog.write(trial_details)
	
	#this header assigns the labels for each column of the saved data
	header = 'Time,Valve,Lick,LickCount,Reward,RewardCount,Distance,TotalDistance,RewardWindow,InitialDrop,InitialDropCount,ImagingTrigger,TTLpulse,TTLtotalCount,LickRate,LapCount\n'
	print header.rstrip('\n')
	dataLog.write(header)
	
	#this tells the arduino to start sending data and also provides parameter values
	arduino_parameters = ('1,'+ 
						  fyle[1]+','+ 
						  fyle[2]+','+ 
						  fyle[3]+','+ 
						  fyle[4]+','+ 
						  fyle[5]+','+ 
						  fyle[6])
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
click_button.grid(row=9,column=1)

# myGUI = guiMaker()
#draw the window, and start the 'application'
window.mainloop()