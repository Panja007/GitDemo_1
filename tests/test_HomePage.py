import pytest
from selenium.webdriver.support.select import Select

from POM.Registration import Registration
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        registration =Registration(self.driver)

        registration.getName().send_keys(getData["firstname"])
        log.info("First Name is" + getData["firstname"])
        registration.getEmail().send_keys(getData["lastname"])
        registration.getPassword().send_keys("academy")
        self.driver.find_element_by_id("exampleCheck1").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        self.selectGender(registration.getDropdown(),getData["gender"])
        SuccessText = self.driver.find_element_by_class_name("alert-success").text
        assert "Success" in SuccessText
        self.driver.refresh()
        print("first repository")
        print("first repository2")
        print("first repository3")

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self,request):
        return request.param

