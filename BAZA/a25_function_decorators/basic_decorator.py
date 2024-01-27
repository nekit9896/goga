import webbrowser
from time import sleep


def validator(func):
    def wrapper(url):  # вложенная функция - обертка
        if "https://" in url:
            sleep(3)
            func(url)
        else:
            return print("неверный url")

    return wrapper


@validator
def web_browser1(url):
    webbrowser.open(url)


web_browser1("https://itproger.com")
