# netflix_scraper.py
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# ---------- SETUP ----------
def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    # Uncomment below for headless (no browser window)
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


# ---------- LOGIN ----------
def login_netflix(driver, email, password):
    driver.get("https://www.netflix.com/login")
    time.sleep(2)
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "userLoginId"))
        )
        email_input.send_keys(email)
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        sign_in_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        sign_in_btn.click()
        time.sleep(5)  # wait for redirect
        return True
    except Exception as e:
        print("Login failed:", e)
        return False


# ---------- SEARCH ----------
def search_title(driver, title):
    # Netflix search URL
    search_url = f"https://www.netflix.com/search?q={title.replace(' ', '%20')}"
    driver.get(search_url)
    time.sleep(3)
    try:
        # Click on the first result (assuming it's the most relevant)
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'title-card')]"))
        )
        first_result.click()
        time.sleep(3)
        return True
    except TimeoutException:
        print("No results found or page took too long.")
        return False


# ---------- EXTRACT INFO ----------
def extract_info(driver):
    info = {}
    try:
        # Title
        title_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@data-uia='title-title']"))
        )
        info['title'] = title_elem.text.strip()
    except:
        info['title'] = "Not found"

    try:
        # Year and maturity rating (often together)
        details = driver.find_element(By.XPATH, "//div[@data-uia='title-metadata']")
        info['details'] = details.text.strip() if details else "N/A"
    except:
        info['details'] = "N/A"

    try:
        # Description
        desc_elem = driver.find_element(By.XPATH, "//div[@data-uia='title-storyline']/p")
        info['description'] = desc_elem.text.strip()
    except:
        info['description'] = "Not available"

    try:
        # Cast / Crew (first few names)
        cast_elem = driver.find_element(By.XPATH, "//div[@data-uia='title-cast']")
        info['cast'] = cast_elem.text.strip()
    except:
        info['cast'] = "Not listed"

    try:
        # Genres / tags
        genre_elem = driver.find_element(By.XPATH, "//div[@data-uia='title-genres']")
        info['genres'] = genre_elem.text.strip()
    except:
        info['genres'] = "Not specified"

    return info


# ---------- MAIN ----------
def main():
    driver = setup_driver()
    # Get credentials (or set environment variables)
    email = input("Enter your Netflix email: ")
    password = input("Enter your Netflix password: ")

    if not login_netflix(driver, email, password):
        print("Login failed. Exiting.")
        driver.quit()
        return

    print("Login successful!")
    while True:
        title = input("\nEnter a movie or series title (or 'quit' to exit): ")
        if title.lower() == 'quit':
            break
        if not search_title(driver, title):
            continue
        info = extract_info(driver)
        print("\n" + "=" * 50)
        print(f"Title: {info.get('title', 'N/A')}")
        print(f"Details: {info.get('details', 'N/A')}")
        print(f"Description: {info.get('description', 'N/A')}")
        print(f"Cast: {info.get('cast', 'N/A')}")
        print(f"Genres: {info.get('genres', 'N/A')}")
        print("=" * 50)

    driver.quit()
    print("Goodbye!")


if __name__ == "__main__":
    main()
