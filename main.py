import time
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    yield driver
    driver.quit()

def test_drag_and_drop_positive(driver):

    #switch to the iframe
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    #item to drag
    item = driver.find_element(By.XPATH, "//div[@id='draggable']")

    #drop area
    drop_area = driver.find_element(By.XPATH,"//div[@id='droppable']")

    #perform drag and drop
    actions = ActionChains(driver)
    actions.drag_and_drop(item, drop_area).perform()

    time.sleep(2)

    assert drop_area.text == "Dropped!"


def test_drag_and_drop_negative(driver):
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    drop_area = driver.find_element(By.XPATH, "//div[@id='droppable']")
    assert drop_area.text == "Dropped!"

