import os
import time
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

edge_options = Options()
edge_driver_path = os.path.join(os.getcwd(), "msedgedriver.exe")
edge_service = Service(edge_driver_path)
edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Edge(edge_driver_path, options=edge_options)

artist = "Young+Fathers"
album = "Heavy+Heavy"
driver.get(f'https://www.albumoftheyear.org/search/?q={artist}+{album}')
time.sleep(1)

first_album = driver.find_element(By.CLASS_NAME, "albumBlock")
first_album.click()
time.sleep(1)

score_field = driver.find_element(By.ID, "value")
score_field.send_keys("85")

rate_btn = driver.find_element(By.ID, "rate")
rate_btn.click()

# msedge.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\EdgeProfile"