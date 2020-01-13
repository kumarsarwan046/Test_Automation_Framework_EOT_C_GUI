import pytest
@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path= "C:/Users/kruthi.p/PycharmProjects/Test_Automation_Framework/drivers/chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()