import time
import winsound

def alert_buzzer(duration, frequency):
    winsound.Beep(frequency, duration)

# Example usage: Alert for 1 second with frequency 1000 Hz
alert_buzzer(1, 1)
