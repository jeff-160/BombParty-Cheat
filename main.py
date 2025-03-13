from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

with open("words.txt", "r") as f:
    word_list = f.read().split("\n")

def main():
    link = input("Enter link: ")

    driver = webdriver.Chrome()

    driver.get(link)

    input("Press ENTER when game has loaded...")

    iframe = None

    while True:
        wait = WebDriverWait(driver, 1e6)

        if not iframe:
            iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
            driver.switch_to.frame(iframe)

        input_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text'].styled")))

        syllable = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".syllable"))).get_attribute("innerText")

        for word in word_list:
            if syllable in word:
                try:
                    input_box.send_keys(word, Keys.RETURN)
                except:
                    ...
                word_list.remove(word)
                break

        sleep(0.1)


if __name__ == "__main__":
    main()