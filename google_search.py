# добавил библиотеки что бы работало
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    # opts.add_argument("--headless=new") #закоментил потому что хочу увидеть как откр. браузер
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_selenium_web_google(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url


def test_selenium_web_github(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title
    assert driver.current_url == url
