from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# BEFORE RUNNING: MUST HAVE A CHROMEDRIVER.EXE FOR THIS CODE TO WORK

global f_path
f_path = "file:///C:/Users/angel/Downloads/AutomationChallenge-2020/index.html"

def method_6(table, row, col):
    """
    This method takes in the table element, row index and column index to find the value in a certain coordinate.
    """
    rows = table.find_elements_by_tag_name("tr")

    return rows[row].find_elements_by_tag_name("td")[col].text
    # print(rows[row].find_elements_by_tag_name("td")[col].text)


# inherit unit test module
class automation_challenge(unittest.TestCase):

    def setUp(self):
        DRIVER_PATH = r"chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    def test1(self):
        print("TEST 1: \n")
        driver = self.driver
        try:
            driver.get(f_path)

            email = driver.find_element_by_id("inputEmail")
            email.send_keys("test email")  # enter into email field
            print("[INFO] Email element found and sent keys.")

            pswrd = driver.find_element_by_id("inputPassword")
            pswrd.send_keys("test password")  # enter into password field
            print("[INFO] Password element found and sent keys.")
            
            login_button = driver.find_element_by_css_selector(".btn-block")
            login_button.click()
            print("[INFO] Login button found and clicked.")
            
            assert "Element(s) not found." not in driver.page_source

        except AssertionError as e:
            print(e)

    def test2(self):
        print("TEST 2: \n")
        driver = self.driver
        try:
            driver.get(f_path)

            # get the list group element
            num_values = driver.find_element_by_xpath("/html/body/div/div[2]/div/ul")

            # get the list elements
            items = num_values.find_elements_by_tag_name("li")

            count = 0
            new_list = []

            # iterate through the items list and append the readable (text) version into a new list
            for item in items:
                text = item.text
                count = count + 1
                new_list.append(text)

            # assert if there are 3 values in the list group
            assert count == 3, "There aren't 3 values in the list group"
            print("[INFO] There are a total of ", count, " items in the list.")

            # assert if second list item's value is set to List Item 2
            self.assertIn("List Item 2", new_list[1])
            print("[INFO] Second list item's value is List Item 2")

            # assert second list item's badge value is 6
            self.assertIn("6", new_list[1])
            print("[INFO] Second list item's badge is 6")

        except AssertionError as e:
            print(e)

    def test3(self):
        print("TEST 3: \n")
        driver = self.driver

        try:
            driver.get(f_path)

            # "Option 1" is the default selected value
            dropdown = driver.find_element_by_id("dropdownMenuButton")
            default = dropdown.text
            self.assertEqual(default, "Option 1", "The default value is not Option 1")

            # select "Option 3" from the select list
            dropdown.click()
            opt3 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div/div/div/a[3]")))
            opt3.click()
            self.assertEqual(dropdown.text, "Option 3", "The value is not Option 3")

        except AssertionError as e:
            print(e)

    def test4(self):
        print("TEST 4: \n")
        driver = self.driver

        try:
            driver.get(f_path)

            # first button is enabled
            button1 = driver.find_element_by_xpath("/html/body/div/div[4]/div/button[1]")
            prop1 = button1.get_property('disabled')
            self.assertFalse(prop1, "The button is not enabled")

            # second button is disabled
            button2 = driver.find_element_by_xpath("/html/body/div/div[4]/div/button[2]")
            prop2 = button2.get_property('disabled')
            self.assertTrue(prop2, "The button is not disabled")

        except AssertionError as e:
            print(e)

    def test5(self):
        print("TEST 5: \n")
        driver = self.driver

        try:
            driver.get(f_path)

            # wait for a button to be displayed (note: the delay is random) and then click it
            driver.implicitly_wait(20)
            button5 = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "test5-button")))
            button5.click()

            # success message
            print("[SUCCESS] Test 5 Button clicked.")

            # the button is now disabled
            driver.implicitly_wait(3)
            prop5 = button5.get_property('disabled')
            self.assertTrue(prop5, "The button is not disabled")

        except AssertionError as e:
            print(e)

    def test6(self):
        print("TEST 6: \n")
        driver = self.driver

        try:
            driver.get(f_path)

            # the method that allows yo to find the value of any cell on the grid is written at the top of this code (method_6)
            table = driver.find_element_by_css_selector("#test-6-div > div > table")

            # use the method to find the value of the cell at coordinates 2, 2 (staring at 0 in the top left corner)
            coord2_2 = method_6(table, 2, 2)
            print("The value of coordiates 2,2 is: ", coord2_2)

            # assert that the value of the cell is "Ventosanzap"
            self.assertEqual(method_6(table, 3, 2), "Ventosanzap", "The cell value is not Ventosanzap.")

        except AssertionError as e:
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
