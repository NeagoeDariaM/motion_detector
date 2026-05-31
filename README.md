# motion_detector

This project identifies movement, and if it exists, pictures are taken every 3 seconds.
For this project I had to import cv2-for working with the camera, os-for working with files, imutils-for the frame in case of movement, time-to take the picture every 3 seconds.
The camera is opened, the image is resized and made black and white, then the difference is made to see if any movement has been made, and if so, a frame is made around what appeared and at the same time pictures are taken and saved in the folder.
When pressing the q key, the camera is turned off, and when pressing the s key, the picture is taken.
