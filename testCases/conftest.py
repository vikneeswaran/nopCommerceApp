import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        serv_obj_chrome = Service("C:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome ( service=serv_obj_chrome )
        print ( "********Launching Chrome Browser**************" )

    elif browser == "firefox":
        serv_obj_ff = Service("C:\\SeleniumDrivers\\geckodriver-v0.31.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox ( service=serv_obj_ff )
        print ( "**************Launching FF browser************" )
    else:
        serv_obj_edge = Service("C:\\SeleniumDrivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj_edge)
        print ( "**************Launching Edge browser************" )
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
#def pytest_configure(config):
#    config._metadata['Project Name'] = 'nop Commerce'
#    config._metadata['Module Name'] = 'Customers'
#    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
