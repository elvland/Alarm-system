import threading
import winsound
import cv2 as cv
import imutils
import pygame



cap = cv.VideoCapture(0,cv.CAP_DSHOW)


cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

# Create starting frame from the camera & turn it into black and white frames
_, start_frames = cap.read()
start_frames = imutils.resize(start_frames, width=500)
start_frames = cv.cvtColor(start_frames, cv.COLOR_BGR2GRAY)
start_frames = cv.GaussianBlur(start_frames, (21, 21), 0)

# alarm parameters
alarm: bool = False
alarm_mode: bool = False
alarm_counter: int = 0


# Alarm function which triggers swhen alarm occurs
alarmPlaying = False  # Flag to track if the alarm is currently playing

def beep_alarm():
    global alarm, alarmPlaying
    # Annoying alarm sound
    # for i in range(7):
    #     if not alarm_mode:
    #         break
    #     print("alarm")
    #     winsound.Beep(2500, 1000)

    #FANCY ALARM SOUND
    if not alarmPlaying:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('rumble.mp3')
        pygame.mixer.music.play()
        alarmPlaying = True
    pygame.time.delay(1000)  # Delay for (1 second)
    alarm = False




while True:
    # new frame for each iteration
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    # Calculate the difference between the current frame and the previous frame
    if alarm_mode:
        frame_bw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_bw = cv.GaussianBlur(frame_bw, (5, 5), 0)

        differance = cv.absdiff(start_frames, frame_bw)
        threshold = cv.threshold(differance, 25, 255, cv.THRESH_BINARY)[1]
        start_frames = frame_bw

        if threshold.sum() > 8000:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv.imshow("CAM", threshold)

    else:
        cv.imshow("cam", frame)

    # If threshold has been crossed 20 times, trigger the alarm
    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()

    key_pressed = cv.waitKey(30)
    # Manually trigger and reset alarm parameters
    if key_pressed == ord('t'):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key_pressed == ord('q'):
        alarm_mode = False
        break

cap.release()
cv.destroyAllWindows()
