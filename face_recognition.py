from add_face import AddingFace
from deepface import DeepFace
import sys

if __name__ == '__main__':

    while True:
        print(" ************ main menu ************")
        print('1. Add a new face')
        print('2. Recognize a face')
        print('3. Exit')

        database_path = '/home/vargha/Desktop/database'

        try:
            menu_item = int(input('Choose the menu item: '))
            if menu_item == 1:
                full_name = input("Enter the full name: ")
                database_path = input("Enter the database path: ") or database_path
                new_face = AddingFace(database_path, full_name)
                new_face.capturing_image()
            elif menu_item == 2:
                DeepFace.stream(db_path=database_path, detector_backend='ssd', model_name='Facenet512',
                                distance_metric="cosine", enable_face_analysis=False, time_threshold=2,
                                frame_threshold=2, source=0)
                # if output:
                #     print("Face detected, Welcome")
            elif menu_item == 3:
                print("Exiting...")
                sys.exit()
            else:
                raise ValueError

        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            print("Invalid input. Please enter a number.")
