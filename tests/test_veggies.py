import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckoutPage import CheckoutPage
from utility.BaseClass import BaseClass


class TestTwo(BaseClass):
    def test_veggies(self):

        list = []
        list2 = []
        list1 = []

        # driver.implicitly_wait(7)
        checkoutPage =CheckoutPage(self.driver)
        checkoutPage.getSearchItem().send_keys("al")
        time.sleep(5)
        selectedItems = checkoutPage.getSelectedItems()
        #assert len(selectedItems) == 3
        cartItems = checkoutPage.getCartItems()

        for cartItem in cartItems:
            list.append(cartItem.find_element_by_xpath("parent::div/parent::div/h4").text)
            cartItem.click()
        print(list)

        self.driver.find_element_by_css_selector("img[alt='Cart']").click()
        addCartItems = self.driver.find_elements_by_xpath("//div[@class='cart-preview active']/div/div/ul/li/div[1]/p[1]")
        for addCartItem in addCartItems:
            list1.append(addCartItem.text)
        print(list1)

        checkoutPage.getCartitemsInCheckOut().click()
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
        beforePromoAmount = self.driver.find_element_by_css_selector("span[class='discountAmt']").text
        self.driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
        vegies = self.driver.find_elements_by_css_selector("p[class='product-name']")
        for veg in vegies:
            list2.append(veg.text)
        print(list2)
        assert list == list2
        assert list1 == list2
        self.driver.find_element_by_class_name("promoBtn").click()
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
        afterPromoAmount = self.driver.find_element_by_css_selector("span[class='discountAmt']").text
        assert int(beforePromoAmount) > float(afterPromoAmount)
        promoInfo = self.driver.find_element_by_class_name("promoInfo").text
        assert promoInfo == "Code applied ..!"
        itemsCosts = self.driver.find_elements_by_xpath("//table/tbody/tr/td[4]/p")
        sum = 0
        for itemsCost in itemsCosts:
            sum = sum + int(itemsCost.text)
        assert sum == int(self.driver.find_element_by_css_selector("span[class='totAmt']").text)
        self.driver.find_element_by_xpath("//button[text()='Place Order']").click()
