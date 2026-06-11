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

MENU_BUTTON = (By.ID, "react-burger-menu-btn")

SIDEBAR = (By.CLASS_NAME, "bm-menu-wrap")
SIDEBAR_CLOSE_BUTTON = (By.ID, "react-burger-cross-btn")

ALL_ITEMS_LINK = (By.ID, "inventory_sidebar_link")
ABOUT_LINK = (By.ID, "about_sidebar_link")
LOGOUT_LINK = (By.ID, "logout_sidebar_link")
RESET_APP_STATE_LINK = (By.ID, "reset_sidebar_link")

FOOTER = (By.CLASS_NAME, "footer")

TWITTER_LINK = (By.CSS_SELECTOR, "[data-test='social-twitter']")
FACEBOOK_LINK = (By.CSS_SELECTOR, "[data-test='social-facebook']")
LINKEDIN_LINK = (By.CSS_SELECTOR, "[data-test='social-linkedin']")
