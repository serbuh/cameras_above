from ast import If
import cv2
from multiprocessing import Process
import time

#to use this resolution you should uncomment 31 line ("frame = ...")
IMAGE_RES = (900,900)

NINJA1_ID = 'UOXBGL'
NINJA1_IP = '192.168.0.233'


NINJA2_ID = 'TGASLM'
NINJA2_IP = '192.168.0.76'

NINJA3_ID = 'VSYAJL'
NINJA3_IP = '192.168.0.79'

NINJA4_ID = 'IGXJVS'
NINJA4_IP = '192.168.0.55'

#This function shows the stream of one EZVIZ camera
#Input: cameraID(written on the camera), cameraIP(can be found in router`s settings)

def showStream(cameraID: str, cameraIP: str):
    stream = "rtsp://admin:{id}@{ip}:554/H.264".format(id=cameraID, ip = cameraIP)
    vcap = cv2.VideoCapture(stream)
    start = time.time()
    while(True):
        ret, frame = vcap.read()

        # uncomment this line to resize frame
        # frame = cv2.resize(frame, IMAGE_RES)
        cv2.imshow(cameraID, frame)
		#close the window by pressing 'q' on it
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
			
    vcap.release()
    cv2.destroyAllWindows()
    


def main():
    camera_threads = [Process(target = showStream, args=(NINJA1_ID, NINJA1_IP)),
                    Process(target = showStream, args=(NINJA2_ID,NINJA2_IP)),
                    Process(target = showStream, args=(NINJA3_ID,NINJA3_IP)),
                    Process(target = showStream, args=(NINJA4_ID,NINJA4_IP))]

    for camera in camera_threads:
        camera.start() # start the threads 

    for camera in camera_threads:
        camera.join() # wait until end

if __name__ == "__main__":
    main()

