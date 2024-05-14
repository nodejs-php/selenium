# from selenium import webdriver
import time

from fake_useragent import UserAgent
from seleniumwire import webdriver
import undetected_chromedriver as uc

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # url = "https://www.instagram.com/"

    # options
    options = webdriver.ChromeOptions()

    options.add_argument("window-size=1280,800")
    # Adding argument to disable the AutomationControlled flag
    options.add_argument("--disable-blink-features=AutomationControlled")


    # change useragent
    useragent = UserAgent()
    options.add_argument(
        f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
    #options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
    #   options.add_argument(f"user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36")
    #  options.add_argument(f"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17")


    # set proxy
    # options.add_argument("--proxy-server=138.128.91.65:8000")

    proxy_options = {
        "proxy": {

        }
    }

    # driver = webdriver.Chrome(
    #     executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
    #     options=options
    # )
    driver = uc.Chrome(
        options=options,
        seleniumwire_options=proxy_options,
    )

    # Changing the property of the navigator value for webdriver to undefined
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")



    try:
        # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
        # time.sleep(5)
        # driver.get(url="https://stackoverflow.com/")
        # time.sleep(5)

        # driver.refresh()
        # driver.get_screenshot_as_file("1.png")
        # driver.get(url="https://stackoverflow.com/")
        # time.sleep(5)
        # driver.save_screenshot("2.png")
        # time.sleep(2)

        #driver.get("https://ozon.com")
        driver.get("https://bot.sannysoft.com/")
        time.sleep(5000)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
