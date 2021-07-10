import time
from plyer import notification
if __name__ == '__main__':
    notification.notify(
        title="Drink Water",
        app_icon="1.ico",
        message="Drink Water Daily",
        timeout=5
    )
    time.sleep(60*60)




