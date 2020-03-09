# #!/usr/bin/env python
# """Simple Selenium WebDriver test that uses TestChameleon Selenium"""

# # import unittest
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class PythonPytestSimpleTest():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    command_executor="http://127.0.0.1:8080/wd/hub", desired_capabilities=chrome_options.to_capabilities()
#     """A simple Selenium example test with Python and pytest."""

#     # def setUp(self):
#     #     """Setup before test."""
#     #     # capas = DesiredCapabilities.FIREFOX
#     #     # self.driver = webdriver.Remote(desired_capabilities=capas)

    def test_title():
        print "wilsonn"
#         """Test the title of our demo page."""
#         self.driver.get("https://demo.testchameleon.com/")
#         assert "Gentellela Alela!" in self.driver.title

    def tearDown():
        print "smth"
#         """Cleanup after test."""
#         self.driver.quit()


# if __name__ == "__main__":
#     unittest.main()
