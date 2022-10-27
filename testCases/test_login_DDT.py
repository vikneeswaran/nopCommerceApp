import time

import pytest
from selenium import webdriver
from pageObjects.LoginPageObject import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutils

class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path ="C:\\Users\\Admin\\PycharmProjects\\nopCommerceApp\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self,setup):
        self.logger.info("**********Test_002_DDT_Login*****")
        self.logger.info("**************Verifying Login Test*****************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)

        self.lp = LoginPage(self.driver)

        self.rows = XLutils.getRowCount(self.path,'Sheet1')
        print("No. of Rows in an Excel",self.rows)

        lst_status = [] #empty list variable to put the results
        for r in range(2,self.rows+1):
            self.user = XLutils.readData(self.path,'Sheet1',r,1)
            self.password = XLutils.readData(self.path,'Sheet1',r,2)
            self.exp = XLutils.readData(self.path,'Sheet1',r,3)


            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**************Login Test Passed *****************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp=="Fail":
                    self.logger.info("**************Login Test Failed *****************")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
                    self.driver.implicitly_wait(5)
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**************Login Test Failed*****************")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
                    self.driver.implicitly_wait ( 5 )
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("**************Login Test Passed *****************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
           self.logger.info("********Login DDT Test is Passed*****")
           self.driver.close()
           assert True

        else:
           self.logger.info("********login DDT Testing Failed*******")
           self.driver.close()
           assert False

        print(lst_status)

        self.logger.info("***********End 0f Login Testing******")
        self.logger.info("*****End of DDT Testing*****")
        self.driver.quit()






