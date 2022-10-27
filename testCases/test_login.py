import pytest
from selenium import webdriver
from pageObjects.LoginPageObject import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_homePageTitle(self,setup):

        self.logger.info("************************* Test_001_Login *******************")
        self.logger.info("**************Verifying Home Page Title Test*****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**************Home Page Title Test Case passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.implicitly_wait(5)
            assert False
            self.logger.error("**************Home Page Title Test Case passed ****************")
        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("**************Verifying Login Test*****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************Login Test Passed *****************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.implicitly_wait(5)
            assert False
            self.logger.error("**************Login Test Failed *****************")
        self.driver.quit()






