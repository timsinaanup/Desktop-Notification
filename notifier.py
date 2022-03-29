from plyer import notification
from time import sleep

while True:
    notification.notify(
        title="Hey There🙋️",
        message="Have a nice day 😁 😊 ",
        timeout=10,
)
    sleep(3000)  #this 300 indicates that this loop will run in each 300 sec i.e:3000/60= 50min