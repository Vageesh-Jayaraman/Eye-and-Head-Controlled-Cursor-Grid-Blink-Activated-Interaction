import cv2
import mediapipe as mp
import numpy as np
import time
import pyautogui
import pygame
import sys

pygame.init()

width = 490
height = 490
screen = pygame.display.set_mode((width, height))
tile_size = 50
gap = 10
tiles = 8

tile_list = []

for x in range(10, width, tile_size + gap):
    for y in range(10, height, tile_size + gap):
        center = (x + tile_size // 2, y + tile_size // 2)
        radius = tile_size // 2
        tile_rect = pygame.Rect(x, y, tile_size, tile_size)
        tile_list.append({"rect": tile_rect, "glow": False})


LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

LEFT_EYE_TOP = 159
LEFT_EYE_BOTTOM = 145
RIGHT_EYE_TOP = 386
RIGHT_EYE_BOTTOM = 374

    
cap = cv2.VideoCapture(0)

mp_face_mesh = mp.solutions.face_mesh.FaceMesh(
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    refine_landmarks=True)


running = True
while running:
    _,frame = cap.read()     #_ - 0 - No frame detected, 1 - Frame detected
    frame = cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
    results = mp_face_mesh.process(rgb_frame)
        
    if (results.multi_face_landmarks):
        face_landmarks = results.multi_face_landmarks[0] # 0 - Only one face, so getting the landmarks only for the Zeroth index
        
        frame_height = frame.shape[0]
        frame_width = frame.shape[1]
        mesh_points=np.array([np.multiply([p.x,p.y],[frame_width,frame_height]) for p in face_landmarks.landmark])
                
        (l_x,l_y), l_radius = cv2.minEnclosingCircle(np.int32(mesh_points[LEFT_IRIS]))
        (r_x,r_y), r_radius = cv2.minEnclosingCircle(np.int32(mesh_points[RIGHT_IRIS]))
                
                #cv2.polylines(frame, np.int32([mesh_points[LEFT_EYE]]),True,(0,255,0), 1, cv2.LINE_AA)
                #cv2.polylines(frame, np.int32([mesh_points[RIGHT_EYE]]),True,(0,255,0), 1, cv2.LINE_AA) 
                
        center_left = np.array([l_x,l_y],dtype=np.int32)
        center_right = np.array([r_x,r_y],dtype=np.int32)
        cv2.circle(frame,center=center_left,radius=1,color=(255,0,255),thickness=2) #int(l_radius)
        cv2.circle(frame,center=center_right,radius=1,color=(255,0,255),thickness=2) #int(r_radius)
                
        screen_w,screen_h = pyautogui.size()
        x = center_right[0]*screen_w/frame_width
        y = center_right[1]*screen_h/frame_height
                
        pyautogui.moveTo(x,y)

        frame_height = frame.shape[0]
        frame_width = frame.shape[1]
        
        ##LEFT TOP
        left_top_landmark = face_landmarks.landmark[LEFT_EYE_TOP]
        left_top_centre = np.array(np.multiply([left_top_landmark.x,left_top_landmark.y],[frame_width,frame_height]),dtype=np.int32)
        cv2.circle(frame,center=left_top_centre,radius=2,color=(0,255,255),thickness=1)
        
        ##LEFT BOTTOM
        left_bottom_landmark = face_landmarks.landmark[LEFT_EYE_BOTTOM]
        left_bottom_centre = np.array(np.multiply([left_bottom_landmark.x,left_bottom_landmark.y],[frame_width,frame_height]),dtype=np.int32)
        cv2.circle(frame,center=left_bottom_centre,radius=2,color=(0,255,255),thickness=1)
        
        ##RIGHT TOP
        right_top_landmark = face_landmarks.landmark[RIGHT_EYE_TOP]
        right_top_centre = np.array(np.multiply([right_top_landmark.x,right_top_landmark.y],[frame_width,frame_height]),dtype=np.int32)
        cv2.circle(frame,center=right_top_centre,radius=2,color=(0,255,255),thickness=1)
        
        ##RIGHT BOTTOM
        right_bottom_landmark = face_landmarks.landmark[RIGHT_EYE_BOTTOM]
        right_bottom_centre = np.array(np.multiply([right_bottom_landmark.x,right_bottom_landmark.y],[frame_width,frame_height]),dtype=np.int32)
        cv2.circle(frame,center=right_bottom_centre,radius=2,color=(0,255,255),thickness=1)
        
        if (left_bottom_landmark.y - left_top_landmark.y) < 0.004 or (right_bottom_landmark.y - right_top_landmark.y) < 0.004:
            pyautogui.click()
            
        
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x_p, y_p = pygame.mouse.get_pos()
                    for tile in tile_list:
                        if tile["rect"].collidepoint(x_p, y_p):
                            tile["glow"] = not tile["glow"]  # Toggle glow state

    screen.fill((0, 0, 0))

    for tile in tile_list:
            center = (tile["rect"].centerx, tile["rect"].centery)
            radius = tile_size // 2
            if tile["glow"]:
                pygame.draw.circle(screen, (255, 0, 0), center, radius)
            else:
                pygame.draw.circle(screen, (100, 100, 100), center, radius)

    pygame.display.flip()  

            
    cv2.imshow('HumanoidX - Iris Movement Detection',frame)
        
    if cv2.waitKey(1)  & 0xFF == "27":
        break
        
cap.release()
cv2.destroyAllWindows()

