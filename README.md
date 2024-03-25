# Eye-and-Head-Controlled-Cursor-Grid-Blink-Activated-Interaction

This project uses eye and head movements to move a cursor on a grid. When you blink, it triggers actions on the grid, enabling users to navigate and interact with grid elements using natural eye and head motions.

## Required Dependencies

To run this project, you need to install the following dependencies:

- pygame
- opencv-python
- mediapipe==0.10.9
- numpy
- pyautogui


> [!TIP]
> You can clone the repository and install the requirements using the following commands: <br /> <br />
> `git clone https://github.com/Vageesh-Jayaraman/Eye-and-Head-Controlled-Cursor-Grid-Blink-Activated-Interaction.git`<br /> <br />
> `cd Eye-and-Head-Controlled-Cursor-Grid-Blink-Activated-Interaction`<br /><br />
> `pip install -r requirements.txt`<br />




## MediaPipe Face Mesh Points

![mediapipe_face_landmark_fullsize](https://github.com/Vageesh-Jayaraman/Eye-and-Head-Controlled-Cursor-Grid-Blink-Activated-Interaction/assets/143870355/c6f03d09-253e-4b1c-8a25-8127251c538a)
The project utilizes the following face mesh points:

- Left Eye: [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
- Right Eye: [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
- Left Iris: [474, 475, 476, 477]
- Right Iris: [469, 470, 471, 472]
- Left Eye Top: 159
- Left Eye Bottom: 145
- Right Eye Top: 386
- Right Eye Bottom: 374

## Working Video

![Working Video](working_video_placeholder.png)

## Usage

This project can be used for various applications, such as sending secret signals like Morse code using eye blinks and head movements.

## Improvements to be Made

One potential improvement is to incorporate gaze estimation for calibration, enhancing the accuracy of cursor control based on eye movements.
