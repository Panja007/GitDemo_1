from selenium.webdriver.common.by import By


class CheckoutPage:
    # self.driver.find_element_by_css_selector("[class='search-keyword']").send_keys("al")
    searchItems = (By.CSS_SELECTOR,"[class='search-keyword']")
    # self.driver.find_elements_by_css_selector("div[class='product']")
    selectedItems = (By.CSS_SELECTOR,"div[class='product']")
    # self.driver.find_elements_by_xpath("//div[@class='product-action']/button")
    cartItems = (By.XPATH,"//div[@class='product-action']/button")
    # self.driver.find_element_by_css_selector("img[alt='Cart']")
    cartItemsInCheckOut = (By.CSS_SELECTOR,"img[alt='Cart']")
    def __init__(self,driver):
        self.driver=driver

    def getSearchItem(self):
        return self.driver.find_element(*CheckoutPage.searchItems)

    def getSelectedItems(self):
        return self.driver.find_elements(*CheckoutPage.searchItems)

    def getCartItems(self):
        return self.driver.find_elements(*CheckoutPage.cartItems)

    def getCartitemsInCheckOut(self):
        return self.driver.find_element(*CheckoutPage.cartItemsInCheckOut)



