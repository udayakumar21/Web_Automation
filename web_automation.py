from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests  


driver = webdriver.Chrome() 

try:
    driver.get("https://www.saucedemo.com/") 
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("Udayakumar")
    driver.find_element(By.ID, "password").send_keys("Udaya")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "inventory_item").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()

    phone_number = input("Enter your phone number: ")  
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "phone-number").send_keys(phone_number) 
    driver.find_element(By.ID, "continue").click()

    time.sleep(2)
   
    otp_response = {"otp": "123456"} 
    otp = otp_response["otp"]
    print(f"Fetched OTP: {otp}")

   
    driver.find_element(By.ID, "otp-field").send_keys(otp) 
    driver.find_element(By.ID, "verify-otp").click()  

   
    time.sleep(2)
    driver.find_element(By.ID, "card_number").send_keys("4111111111111111")  # Dummy card number
    driver.find_element(By.ID, "expiry_date").send_keys("12/25")
    driver.find_element(By.ID, "cvv").send_keys("123")
    driver.find_element(By.ID, "submit_payment").click()

    
    time.sleep(2)
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    print("Transaction Status:", success_message)

finally:
    driver.quit()
