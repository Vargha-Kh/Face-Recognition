import cv2
from datetime import datetime
import os
import time
from numpy.linalg import norm
import numpy as np


class AddingFace:
    def __init__(self, database_directory='/home/vargha/Desktop/database', full_name='vargha'):
        self.database_directory = database_directory
        self.full_name = full_name.lower()

    def saving_image(self, image_name, image):
        folders = os.listdir(self.database_directory)
        if self.full_name in folders:
            print('Folder already exists')
            cv2.imwrite(os.path.join(self.database_directory, self.full_name, image_name), image)
            print(
                f"Image saved successfully in {os.path.join(self.database_directory, self.full_name, image_name)} directory")
        else:
            os.makedirs(os.path.join(self.database_directory, self.full_name))
            print(f"Appending new person {self.full_name}")
            cv2.imwrite(os.path.join(self.database_directory, self.full_name, image_name), image)
            print(
                f"Image saved successfully in {os.path.join(self.database_directory, self.full_name, image_name)} directory")

    def brightness(self, img):
        return np.average(norm(img, axis=2)) / np.sqrt(3)

    def capturing_image(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Adding Face")

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to open the camera")
                break
            print("brightness: ", self.brightness(frame))
            display = frame.copy()
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(display, 'Press Space to capture image', (10, 10), font, 1, (255, 255, 255), 2, cv2.LINE_4)
            cv2.putText(display, 'Press q to exit', (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_4)
            cv2.imshow("Adding Face", display)
            k = cv2.waitKey(1)
            if k & 0xFF == ord('q'):
                # q key
                print("Exiting AddingFace...")
                break

            elif k % 256 == 32:
                # SPACE pressed
                print('Capturing face...')
                time.sleep(3)
                img_name = f"{self.full_name}_{datetime.now()}.jpg"
                self.saving_image(img_name, frame)

        cam.release()
        cv2.destroyAllWindows()
