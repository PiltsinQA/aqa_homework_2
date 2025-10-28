# Домашняя работа
1. Зарегистрировать аккаунт на https://github.com
2. Создать новый проект для домашнего задания https://github.com/new
3. Изменить тест на поиск в google
4. Добавьте тест на открытия страницы github.com

**ответ на домашнюю работу**

```# добавил библиотеки что бы работало
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

```

4. Исправить ошибки в коде (PEP8, PEP20)
```print("Hello, README!")


Text = """Lorem Ipsum - это текст-'рыба', часто используемый в печати и вэб-дизайне.
         Lorem Ipsum является стандартной рыбой для текстов на латинице с начала XVI века.
         В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов,
         используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил
         без заметных изменений пять веков, но и перешагнул в электронный дизайн.
         Его популяризации в новое время послужили публикация листов Letraset
         с образцами Lorem Ipsum в 60-х годах и, в более недавнее время,
         программы электронной вёрстки типа Aldus PageMaker,
         в шаблонах которых используется Lorem Ipsum."""


def add(a, b):
    return a + b


def greet(name):
    print("Привет," + name)


NUMS = [1, 2, 3, 4, 5]

greet("мир")


print(add(2, 2))


```
