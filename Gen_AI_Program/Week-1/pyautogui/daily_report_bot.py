
import pyautogui
import time
from datetime import datetime

print("Daily Report Automation...")

time.sleep(3)

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
PROFILE_COORD  = (624, 597)
pyautogui.moveTo(PROFILE_COORD, duration=1)
pyautogui.click()
time.sleep(2)

pyautogui.hotkey("ctrl", "t")
website = "https://www.accuweather.com/en/de/berlin/10178/weather-forecast/178087"

pyautogui.write(website)
pyautogui.press("enter")

HEADER_START = (575, 182)
pyautogui.moveTo(HEADER_START, duration=1)
pyautogui.click()
time.sleep(3)

HEADER_END = (718, 190)
pyautogui.dragTo(
   HEADER_END,
    duration=0.5,
    button="left"
)

pyautogui.hotkey("ctrl", "c")

time.sleep(2)

pyautogui.hotkey("win", "r")

time.sleep(1)

pyautogui.write("notepad")

pyautogui.press("enter")

time.sleep(3)

pyautogui.hotkey("ctrl", "n")

time.sleep(2)

current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

time.sleep(2)

pyautogui.write("**** Daily Weather Report **** ")
time.sleep(2)
pyautogui.press("enter")
pyautogui.press("enter")


pyautogui.write("Date & Time :")

pyautogui.press("enter")

pyautogui.write(current_datetime, interval=0.03)

pyautogui.press("enter")
pyautogui.press("enter")

pyautogui.write("Weather :")

pyautogui.press("enter")

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")
pyautogui.press("enter")

pyautogui.write("Comment :")
pyautogui.press("enter")

pyautogui.write("Cloudy Day")

pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(1)
pyautogui.write("**** End of Report  ***** ")
time.sleep(1)
pyautogui.hotkey("ctrl", "shift","s")
time.sleep(2)

filename = f"weather_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

pyautogui.write(filename, interval=0.02)

pyautogui.press("enter")
time.sleep(2)


screenshot = pyautogui.screenshot()

screenshot.save("daily_weather_report.png")
