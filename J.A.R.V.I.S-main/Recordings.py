import datetime
from PIL import ImageGrab
import numpy as np 
import cv2
import pyaudio
import wave
import subprocess
import msvcrt
import pyautogui

def Record_Option(option):
    
    audio = pyaudio.PyAudio()
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')    
    VideoFile_name = f'E:\\JARVIS\\Recorded\\Screen\\VideoFile-{time_stamp}.mp4'
    AudioFile_name = f'E:\\JARVIS\\Recorded\\Audio\\AudioFile-{time_stamp}.wav'
    OutputFileName = f'E:\\JARVIS\\Recorded\\SCREENRECORDED\\VideoFile-{time_stamp}.mp4'
    frames=[]
    stream = audio.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)
    if "screen recording" in option:
        ScreenRecording(audio,VideoFile_name,AudioFile_name,OutputFileName,frames,stream)
    elif "voice recording" in option:
        VoiceRecording(stream,frames,AudioFile_name,audio)

def ScreenRecording(audio,VideoFile_name,AudioFile_name,OutputFileName,frames,stream):
    print("Screen Recording has been started")
    print("press the key 'q' to exit stop screen recording")

    width, height= pyautogui.size()

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(VideoFile_name, fourcc, 20.0, (width, height))

    while True:
        img = ImageGrab.grab(bbox=(0,0,width,height))
        image_np = np.array(img) 
        VoiceCapture(stream,frames)
        Final_img = cv2.cvtColor(image_np,cv2.COLOR_BGR2RGB) 
        cv2.imshow('Screen Recorder',Final_img) 
        captured_video.write(Final_img)
        VoiceCapture(stream,frames)
        
        if cv2.waitKey(10) == ord('q'):
            stream.stop_stream()
            stream.close()
            audio.terminate()
            break
    
    VoiceEnd(AudioFile_name,audio,frames)
    cv2.destroyAllWindows()
    captured_video.release()

    cmd = f"ffmpeg -i {VideoFile_name} -i {AudioFile_name} -c:v copy -c:a aac {OutputFileName}"
    subprocess.call(cmd, shell=True)
    print("screen Recording has been ended")

def VoiceCapture(stream,frames):
    date = stream.read(1024) 
    frames.append(date)

def VoiceEnd(AudioFile_name,audio,frames):
    soundFile = wave.open(AudioFile_name,"wb")
    soundFile.setnchannels(1)
    soundFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    soundFile.setframerate(44100)
    soundFile.writeframes(b''.join(frames))
    soundFile.close()

def VoiceRecording(stream,frames,AudioFile_name,audio):
    print("voice Recording has been started")
    print("press the key 'q' to exit stop voice recording")
    while True:
        VoiceCapture(stream,frames)
        
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == ord('q'):
                break


    stream.stop_stream()
    stream.close()
    audio.terminate()

    VoiceEnd(AudioFile_name,audio,frames)
    print("voice Recording has been ended")

