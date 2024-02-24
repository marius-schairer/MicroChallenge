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
