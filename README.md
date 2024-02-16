# Micro Challenge I: Talk to the city
====================

***MDEF:** Digital Prototyping For Design*

***`Team names`** Marius and Núria*

**Index**

[TOC]

## Introduction

### Areas of interests and project alignment

![interests](https://hackmd.io/_uploads/r1ArS0js6.png)



### Research project

With this project we want to turn the city into a navigable space without individual digital devices (mobile phones). Add elements of signaling routes, important information of areas of the city and spaces for receiving feedback from citizens. To be able to "talk" to the city, to be able to collect proposals from citizens in an interactive, community and easy to use way.

In order to start the project it is necessary to collect data on the needs of the city's inhabitants to be able to incorporate them into the new "gamified city" system.

### Artifact description

City companion that gives the opportunity to the citizens to talk to the city and (maybe) recieve feed back from her.

The artifact we will design is an easy, interactive and accessible way for citizens to give feedback on the city about what do they want. It must be safe, anonymous, appealing and useful for the project.



<br></br>

## Project development

### References

![refereneeec](https://hackmd.io/_uploads/ryblERisp.png)


### First drafts and sketches

![sketch](https://hackmd.io/_uploads/rJ-UmAjoa.png)



### Materials and technologies needed

- Raspberry Pi
- Microphone
- Button
- Computer
- Wood/Acrylic
- Laser Cutting machine
- Paper printing


### Project planning
![image](https://hackmd.io/_uploads/rkh5GRjjT.png)




<br></br>
## Fabrication documentation

### Raspberry Pi

![raspb1](https://hackmd.io/_uploads/rJEgEn3ia.png)


In this Raspberry Pi setup we used a usb microphone/speaker headset and a button to record voice messages. please note the following steps:

1. Set up your Raspberry pi through downloading the os from the raspberry website and upload it to your SD Card
2. Preferably use a usb microphone, because aux is recognized by the raspberry as an output and can only be used as a microphone in a complicated way. for this you would need a usb adapter that splits input and output. 
3. type `sudo raspi-config` in the terminal, go to "System Options" -> "Audio" and ensure you have the selected the correct input device.
4. install with `pip install pyaudio` in your terminal the necessary library to use audio functions on your raspberry pi

Code to record wav. files with timestamp while button press:
```
import RPi.GPIO as GPIO
import time
import subprocess
import pyaudio
import wave
import datetime


# GPIO pins
BUTTON_PIN = 17

# Audio Settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "recording.wav"

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Function to start recording audio
def start_recording():
    # Generate a unique filename based on the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"recording_{timestamp}.wav"
    
    print("Recording...")
    frames = []
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    while GPIO.input(BUTTON_PIN) == False:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Stopped recording.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the audio to a WAV file
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



try:
    while True:
        input_state = GPIO.input(BUTTON_PIN)
        if input_state == False:
            print('Buttonpressed')
            start_recording()
            time.sleep(0.2)
            
finally:
    GPIO.cleanup()
```
### Microphone

![mic1](https://hackmd.io/_uploads/B1XbE3noT.png)



We found out the audio input can only come from USB, not AUX for the Raspberry Pi. 

To find a microphone that checked the requirements, we decided to go with a speaker/microphone headset. At the beginning it wasn't working, and we thought it was too confusing to have 2 functions in the same input for the Raspberry Pi. We realized the microphone of the headset wasn't working, and when we changed it for another headset, the code worked.

As a way to cover a little bit the mic and reduce background and wind sound, we covered it with a noise filter.


![mic2](https://hackmd.io/_uploads/BJ1MN22sT.png)




### Button

![button1](https://hackmd.io/_uploads/Bkcz4n3o6.png)


We used a similar button to the one we needed for our project of The Machine Paradox, so for the sake of reusing we extracted it from the previous machine and used it for this new one.

The button was an easy configuration, we plugged it into the Raspberry Pi pins. It was more difficult to figure out which commands we needed to use for each pin. But once we figured it out, it worked.



### Structure

![structura1](https://hackmd.io/_uploads/H1OQV32s6.png)


To collect the electronic parts and all the elements we designed a box to be manufactured by laser cutting. The box was placed on a metal structure that we recycled from Iaac, and for the support of the main poster, we laser cut a round structure that would hold the main poster straight.

![structura2](https://hackmd.io/_uploads/ByBVE33s6.png)



### User experience

We wanted to make a design that was appealing and simple for the user. That's why we incorporated a poster and some instructions on top of the box.





<br></br>

## Final Result







### Problems we faced

- Configuring a Raspberry Pi board for the first time on our own.
- Finding a microphone that worked, was a USB entry and fitted the form requirements for the machine.
- Face a problem with the laser cut machine's mirror.
- Coding with Python with little to no expertise.
- Timing, we thought we'd be faster with the tasks. That made us lower our expectations about the machine and realize that we had to go step by step.
- When trying to incorporate the transcript into the code, the libraries and functions we needed also affected our "simple working code".

### Future explorations
![Process](https://hackmd.io/_uploads/ByxC2poip.png)

- Incorporation of Language Recognition Tool to transcript all of the answers, no matter the language. So we can store data in text and not sound.
    - [tutorial](https://www.youtube.com/watch?v=2kSPbH4jWME)
    - https://alphacephei.com/vosk/ 

- Adding a speaker to the machine, so we can use the text inputs, give it to an AI bot simulating the city, converting the text from the bot to voice and play it for the participants.
