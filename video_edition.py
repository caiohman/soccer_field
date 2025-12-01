#!/home/repo/soccer_field/venv/bin/python
import cv2 as cv
import sys


class Video:

    def __init__(self):
        self.video = cv.VideoCapture('/home/caiohman/repo/soccer_field/video.mp4')

        if self.video.isOpened() is False:
            sys.exit("Could not find video")

        frame_width = self.video.get(cv.CAP_PROP_FRAME_WIDTH)
        frame_height = self.video.get(cv.CAP_PROP_FRAME_HEIGHT)

        sponsor_logo = cv.imread('/home/caiohman/repo/soccer_field/logo.jpg')
        assert sponsor_logo is not None, "file could not be read"

        while self.video.isOpened:
            ret, frame = self.video.read()

            init_x = int(0)
            init_y = int(frame_height / 2)

            end_x = int(frame_width)
            end_y = int(frame_height)

            cv.rectangle(frame, (init_x, init_y), (end_x, end_y), (255, 255, 255), -1)



            cv.imshow('Video Frame', frame)

            if cv.waitKey(25) & 0XFF == ord('q'):
                break

        # at the end
        self.video.release()
        cv.destroyAllWindows()
