import unittest
import pandas as pd
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the capabilities for the appium driver
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    path=r"C:\Program Files\Android\Android Studio\platform-tools\Zee.Now_2.3.10.apk",
    appPackage='br.com.zeenow.zeenow',
    appActivity='.ui.screens.splash.SplashScreenActivity t19',
)

# URL for the appium server
appium_server_url = 'http://localhost:4723'


# Define a test class
class TestAppium(unittest.TestCase):
    def setUp(self):
        # Load the APP using appium
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        wait = WebDriverWait(self.driver, 20)
        main_screen_element_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("COMEÇAR")')
        state_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rio de Janeiro")')
        city_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Andaraí")')

        # Try to wait for elements to appear on the main screen
        try:
            wait.until(EC.presence_of_element_located(main_screen_element_locator)).click()
            wait.until(EC.presence_of_element_located(state_locator)).click()
            wait.until(EC.presence_of_element_located(city_locator)).click()
            print("App is fully loaded. Proceeding with tests.")
        except TimeoutException:
            # If app doesn't load within the specified time, restart it
            print("App did not load successfully within the specified timeout. Quitting the APP.")
            self.driver.quit()
            print("Refreshing APP....")
            self.setUp()

    def tearDown(self) -> None:
        # Close the driver when the test ends
        if self.driver:
            self.driver.quit()

    # Define a method to restart the app
    def restart_app(self):
        if self.driver:
            self.driver.quit()
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        wait = WebDriverWait(self.driver, 20)
        main_screen_element_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("COMEÇAR")')
        state_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rio de Janeiro")')
        city_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Andaraí")')

        # Try to wait for elements to appear on the main screen after restarting
        try:
            wait.until(EC.presence_of_element_located(main_screen_element_locator)).click()
            wait.until(EC.presence_of_element_located(state_locator)).click()
            wait.until(EC.presence_of_element_located(city_locator)).click()
            print("App is fully loaded. Proceeding with tests.")
        except TimeoutException:
            print("App did not load successfully within the specified timeout. Quitting the APP.")
            self.driver.quit()
            print("Refreshing APP....")
            self.restart_app()

    # Define a method to save progress
    def save_progress(self, progress):
        with open('progress.txt', 'w') as file:
            file.write(str(progress))

    # Define the main test method
    def test_address_button(self):
        # Read CEPs from Excel into a DataFrame
        df = pd.read_excel('ceps.xlsx', engine='openpyxl', usecols=['CEP'], dtype=str)
        ceps = df['CEP'].tolist()

        # Initialize lists and DataFrame for storing results
        results = []
        results_df = pd.DataFrame(columns=['CEP', 'MESSAGE'])

        # Read progress from file or initialize to 0
        if os.path.exists('progress.txt'):
            with open('progress.txt', 'r') as file:
                progress = int(file.read())
        else:
            progress = 0

        zip_codes_to_restart = 150

        # Loop through CEPs and perform actions
        while progress < len(ceps):
            wait = WebDriverWait(self.driver, 15)
            address_button = (AppiumBy.ID, 'br.com.zeenow.zeenow:id/home_address_text')
            search_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Insira CEP ou endereço com número")')
            confirm_search = (AppiumBy.ID, 'br.com.zeenow.zeenow:id/search_address_zip_code_value')
            get_number_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("Número")')
            confirm_number_field = (AppiumBy.ID, 'br.com.zeenow.zeenow:id/zee_button_text')

            try:
                for i in range(zip_codes_to_restart):
                    # Get the current CEP from the list
                    cep = ceps[progress]
                    # Perform UI actions to search for the CEP
                    wait.until(EC.presence_of_element_located(address_button)).click()
                    wait.until(EC.presence_of_element_located(search_field)).click()
                    wait.until(EC.presence_of_element_located(search_field)).send_keys(cep)
                    wait.until(EC.presence_of_element_located(confirm_search)).click()
                    wait.until(EC.presence_of_element_located(get_number_field)).click()
                    wait.until(EC.presence_of_element_located(get_number_field)).send_keys("1")
                    wait.until(EC.presence_of_element_located(confirm_number_field)).click()

                    # Check if widget layout is visible
                    if self.is_widget_layout_visible():
                        new_row = {'CEP': cep, 'MESSAGE': 'AINDA NÃO ESTAMOS ATENDENDO O SEU BAIRRO'}
                        print('AINDA NÃO ESTAMOS ATENDENDO O SEU BAIRRO: Index: {} - CEP: {}'.format(progress, cep))
                        self.driver.back()
                        self.driver.back()
                        self.driver.back()
                    else:
                        new_row = {'CEP': cep, 'MESSAGE': 'CEP COM COBERTURA'}
                        print('CEP COM COBERTURA: Index: {} - CEP: {}'.format(progress, cep))

                    # Append result to the results list and update DataFrame
                    results.append(new_row)
                    results_df = pd.DataFrame(results)
                    results_df.to_excel("results.xlsx", index=False)

                    # Print progress
                    print(f'{progress} de {len(ceps)}')
                    progress += 1
                    self.save_progress(progress)

                # Restart the app and reset progress if needed
                if progress >= zip_codes_to_restart:
                    print("Reached the desired number of zip codes. Restarting the app...")
                    self.save_progress(progress)
                    self.restart_app()
                    print("APP Refreshed")

            except (TimeoutException, NoSuchElementException) as e:
                print(f'Error at: {e}')
                self.restart_app()
                print("APP Refreshed!")

    # Define a method to check if the widget layout is visible
    def is_widget_layout_visible(self) -> bool:
        try:
            wait = WebDriverWait(self.driver, 1)
            widget_layout_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'text("AINDA NÃO ESTAMOS ATENDENDO O SEU BAIRRO")')
            close_widget_layout = (AppiumBy.CLASS_NAME, 'android.widget.ImageView')
            wait.until(EC.visibility_of_element_located(widget_layout_locator))
            wait.until(EC.visibility_of_element_located(close_widget_layout)).click()
            return True
        except TimeoutException:
            return False


# Run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
