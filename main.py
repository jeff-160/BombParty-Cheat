from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import re
from colorama import Fore, Style

def get_link() -> str:
    while True:
        link = input(Fore.YELLOW + "Enter link: " + Style.RESET_ALL)

        if re.match(r"https://jklm\.fun/.*", link):
            break
    
        print(Fore.RED + "Invalid link" + Style.RESET_ALL)
    
    return link

def get_words() -> list:
    with open("words.txt", "r") as f:
        return f.read().split("\n")

def main():
    link = get_link()
    word_list = get_words()

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 1e6)

    driver.get(link)

    input(Fore.GREEN + "Press ENTER when game has loaded..." + Style.RESET_ALL)

    iframe = None

    while True:
        if not iframe:
            iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
            driver.switch_to.frame(iframe)

        input_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text'].styled")))

        syllable = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".syllable"))).get_attribute("innerText")

        for word in word_list:
            if syllable in word:
                try:
                    delay = (randint(1, 5) * 0.1) / len(word)
                    
                    for char in word:
                        input_box.send_keys(char)
                        sleep(delay)
                    input_box.send_keys(Keys.RETURN)

                    word_list.remove(word)
                except:
                    ...
                break

        sleep(0.1)


if __name__ == "__main__":
    main()