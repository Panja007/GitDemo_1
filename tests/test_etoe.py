import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.checkoutPage import CheckOutPage
from POM.confirmPage import ConfirmPage
from POM.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_endToEnd(self):
        # Functional Testing:
        log = self.getLogger()

        homepage =HomePage(self.driver)

        checkOut = homepage.getShop()
        # all the products are displayed so grab the all products in to one list and do the further operations

        productList = checkOut.getProductList()

        assert len(productList) == 4
        log.info("Products Displayed"+str(len(productList)))
        for product in productList:
            productName = product.find_element_by_xpath("div[1]/h4/a")
            if productName.text == "iphone X":
                log.info("Selected Product"+"iphone X")
                product.find_element_by_xpath("div[2]/button").click()
        checkOut.getPrimaryButton().click()
        # next page product and selected product validation

        assert "iphone X" == checkOut.getConfirmProductName().text
        log.info("the product in checkout page is"+checkOut.getConfirmProductName().text)
        confirm = checkOut.getSuccessButton()
        confirm.getCountryKey().send_keys("ind")
        log.info("send keys"+"ind")
        self.verifyLinkPresence("//a[text()='India']")


        confirm.getCountryName().click()

        log.info("contry name India clicked")
        confirm.getCheckBox().click()
        confirm.getBtnSuccess().click()
        assert "Successtretret!" in confirm.getSuccessAlert().text
        log.info("success text displayed as " +confirm.getSuccessAlert().text)
        self.driver.get_screenshot_as_file("screen.png")




