import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# inherit TestCase Class and create a new test class
username ='ADMIN'
access_key = ''
class PythonOrgSearch(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        # desired_caps = {
        #     'LT:Options': {
        #         "user": username,
        #         "accessKey": access_key,
        #         "build": "UnitTest-Selenium-Test",
        #         "platformName": "Windows 11",
        #         "selenium_version": "4.0.0"
        #     },
        #     "browserName": "Chrome",
        #     "browserVersion": "latest",
        # }

        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Remote(
        #     command_executor="command_executor="http://127.0.0.1:8000/admin/login/?next=/admin/"),
        #desired_capabilities=desired_caps)

    # Test case method. It should always start with test_
    def TEST_LOGIN(self):
        # get driver 
        print('batdau')
        driver = self.driver
        # get python.org using selenium
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        inputUserName = driver.find_element(By.NAME,value="username")
        print(inputUserName)
        inputUserName.send_keys("admin")
        time.sleep(5)

        password = driver.find_element(By.NAME,value="password")
        print(inputUserName)
        password.send_keys("thereshzed")
        time.sleep(5)

        password.send_keys(Keys.RETURN)
        print('111111111')
        # receive data
        # elem.send_keys(Keys.RETURN)
        # assert "No results found," not in driver.page_source

    #cleanup method called after every test performed
    #TH1 nhap username d,pass sai ---> KQ kỳ vọng login f
    #TH2 nhap username sai,pass d ---> login f
    #TH3 dung ca 2,               ---> login thanhcong----> vao duoc trang he thong
    #TH4 ko nhap ----> login f
    def tearDown(self):
        self.driver.close()
    def test_unit_login_3(self):
        # try:
        # get driver
        print('bat dau')
        driver = self.driver
        # get python.org using selenium
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        inputUserName = driver.find_element(By.NAME,value="username")

        inputUserName.send_keys("admin")
        # time.sleep(5)

        password = driver.find_element(By.NAME,value="password")

        password.send_keys("thereshzed")
        # time.sleep(5)

        password.send_keys(Keys.RETURN)

        time.sleep(10)
        actualTitle = driver.title
        print(actualTitle)
        # assert actualTitle ,"Site administration | Django site admin"
        assert(actualTitle == "Site administration | Django site admin")
        # assert 2 + 2 == 5, "Houston we've got a problem"

        # receive data 
        # elem.send_keys(Keys.RETURN)
        # assert "No result found." not in driver.page_source

# execute the script
if __name__=="__main__":
    unittest.main()
    