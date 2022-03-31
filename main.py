import rotatescreen as r
import time
screen = r.get_primary_display()
for i in range(21):
    time.sleep(0.2)
    screen.rotate_to(i*90%360)