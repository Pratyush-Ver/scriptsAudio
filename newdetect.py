import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime
import os
import time
 
path = "C://Users//praty//Desktop//work//scriptsAudio//rec" 

# Data to be written
payload = {
"deviceId":"SN0001",
"deviceType":"standalone",
"timeStamp":"dd/mm/yyyy_hh:mm:ss",
"recTimeStamp":"dd/mm/yyyy_hh:mm:ss",
"recFileName":"xyz.wav",
"gpsLat":"11.5N",
"gpsLong":"88.4E",
"recDuration":"10",
"recSamplingRate":"48000",
"recFormat":"wav",
"detectionCount":"11",
"onsetThreshold":"0.01",
"peakTimeStamp":[],
"peakMagnitude":[]
}

def build_payload(onset_detects,onset_detects_values,filename):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%YT%H-%M-%S")
    payload["timeStamp"]=dt_string
    payload["recFileName"]=filename
    payload["recTimeStamp"]=filename.split("_")[1]
    payload["recDuration"]=recDuration
    payload["recSamplingRate"]=recSamplingRate
    payload["recFormat"]=recFormat
    payload["detectionCount"]=len(onset_detects)
    payload["onsetThreshold"]=threshold
    payload["peakTimeStamp"]=onset_detects
    payload["peakMagnitude"]=onset_detects_values
    json_write(payload)

# Writing to sample.json
def json_write(payload):
    json_object = json.dumps(payload, indent=4)
    with open("detections.json", "a") as outfile:
        outfile.write(json_object)

def filecheck():
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")
    #print(dir_list)
    if len(dir_list)==0:
        return False, dir_list
    else:
        return True, dir_list

#sampling rate is variable

# Get the list of all files and directories
#function for file list
#return true if files detected with list else return false
#once file is processed, delete 

#filename="rec_2023-06-10T14-37-00.wav"
recDuration="20"
recSamplingRate="48000"
recFormat="wav"

#x=list(range(1,220161))
while 1:
    flag, dir_list=filecheck()
    #logic for waiting until new files are generated
    if flag==False:
        print("No files... Sleeping...")
        time.sleep(30)
    else:
        #dir_list=filecheck()
        for file in dir_list:
            # Load audio file
            audio_file = file
            y_init, sr_init = librosa.load(audio_file)
            print("Files found! sr is ",sr_init)
            #print("y is",y_init)
            # Plot waveform of amplitude vs time
            #plt.figure(figsize=(14, 5))
            #fig, ax = plt.subplots(nrows=3, sharex=True)

            # librosa.display.waveshow(y_init, sr=sr_init, ax=ax[0])
            # ax[0].set(title='Envelope view, mono')
            # ax[0].label_outer()

            # plt.plot(y_init,x)
            # plt.show

            # Set loudness threshold
            threshold = 0.05

            # Find timestamps when the sound goes over the threshold
            onset_frames = librosa.onset.onset_detect(y=y_init, sr=sr_init)
            onset_times = librosa.frames_to_time(onset_frames, sr=sr_init)
            #print(y_init.shape)
            #print("onset times are ",onset_times,type(onset_times))
            onset_detects=[]
            onset_detects_values=[]
            # Print timestamps when the sound goes over the threshold
            for onset_time in onset_times:
                if int(onset_time * sr_init) < len(y_init) and y_init[int(onset_time * sr_init)] > threshold:
                    #print(onset_time)
                    onset_detects.append(str(onset_time))
                    onset_detects_values.append(str(y_init[int(onset_time * sr_init)]))
            print("detected time are",onset_detects)
            print("detected values are",onset_detects_values)
            build_payload(onset_detects,onset_detects_values,file)
        