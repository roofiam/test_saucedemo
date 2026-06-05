from selenium.webdriver.common.by import By

PRODUCTS_CONTAINER = (By.ID, "inventory_container")

PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")

PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
PRODUCT_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")
PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
PRODUCT_IMAGES = (By.CSS_SELECTOR, ".inventory_item_img img")

SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")

CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
