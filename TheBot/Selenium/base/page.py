# Universal behaviors of a WebPage

class BasePage(object):
    url = None

    def __init__(self, driver) -> None:
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()
