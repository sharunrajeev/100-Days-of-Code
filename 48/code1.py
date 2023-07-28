from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/dp/B09X5S3FPT/?coliid=I3A8EMLOXPRMN9&colid=R1P2I54BE5IH&psc=1&ref_"
           "=list_c_wl_lv_ov_lig_dp_it")

price = driver.find_element(by=By.CSS_SELECTOR, value="#corePriceDisplay_desktop_feature_div > "
                                                      "div.a-section.a-spacing-none.aok-align-center > "
                                                      "span.a-price.aok-align-center.reinventPricePriceToPayMargin"
                                                      ".priceToPay > span:nth-child(2) > span.a-price-whole")

print(price.text)

# Closes active tab
# driver.close()

# Clears all the tabs
driver.quit()
