<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alarm System</title>
</head>
<body>
  <h1>Alarm System</h1>
  <p>This project implements a simple alarm system using Python and various libraries such as OpenCV, Pygame, and threading. The system monitors a video feed from a camera and triggers an alarm when certain conditions are met.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Motion Detection:</strong> The system detects motion in the video feed using background subtraction and thresholding techniques.</li>
    <li><strong>Alarm Triggering:</strong> When motion is detected, the system triggers an alarm to alert the user.</li>
    <li><strong>Customizable Alarm Sound:</strong> Users can choose their own alarm sound to be played when motion is detected.</li>
    <li><strong>Manual Control:</strong> Users can manually control the alarm system by toggling between alarm modes and resetting the alarm counter.</li>
  </ul>

  <h2>Getting Started</h2>
  <h3>Prerequisites</h3>
  <ul>
    <li>Python 3.x</li>
    <li>OpenCV (`cv2`)</li>
    <li>Pygame</li>
    <li>`winsound` (for Windows only)</li>
  </ul>

  
  <h2>Usage</h2>
  <ol>
    <li>Run the Python script:</li>
    <code>python alarm_system.py</code>
    <li>Press 't' to toggle alarm mode.</li>
    <li>Press 'q' to quit the application.</li>
  </ol>


</body>
</html>
