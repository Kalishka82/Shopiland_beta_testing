from selenium.webdriver.common.by import By


class MainPageSearchLocators:
    # SEARCH_FIELD = (By.CLASS_NAME, 'MuiInputBase-input.css-mnn31')
    # SEARCH_FIELD = (By.XPATH, '//input[@class=".MuiInputBase-input.css-mnn31"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.MuiInputBase-input.css-mnn31')
    SEARCH_BUTTON = (By.XPATH, '//button[@title="Искать"]')
    SEARCH_WORD = (By.CLASS_NAME, 'css-1xrqwep')
    CHOICE_CITY = (By.CSS_SELECTOR, '.MuiBox-root.css-1kdsoe2')
    CITY_LIST = (By.CSS_SELECTOR, '.MuiBox-root.css-f3v1d3')


class SearchPageLocators:
    MARKET_NAVI = (By.CSS_SELECTOR, '.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd.css-1n2jkki')
    PRODS_TITLES = (By.CSS_SELECTOR, '.css-99ww93')
    PRODS_MARKETS = (By.CSS_SELECTOR, '.css-gyxkao')
    PRODS_PRICES = (By.CSS_SELECTOR, '.css-bwtgpb')
    PRODS_POPS = (By.XPATH, '//span[contains(text()[3], "отзывы"]')
    PRODS_POPS_ALL = (By.CSS_SELECTOR, '.css-1t0tstb')
    # PRODS_FBACKS = (By.XPATH, '//span[contains(text()[3], ""]')
    PRODS_FBACKS = (By.CSS_SELECTOR, '.MuiRating-root.MuiRating-sizeSmall.MuiRating-readyOnly.css-1a2asoj')

    PRODS_COUNTS = (By.XPATH, '.css-1t0tstb')
    # PRODUCTS_CARDS = (By.XPATH, '//a[contains(@href, "https://")]/div[2]/div[1]/p')
    MARKET_TITLES = (By.CSS_SELECTOR, '.css-gyxkao')
    # MORE_LOAD = (By.CSS_SELECTOR, '.ButtonUnstyled-root.Mui-active.css-h30hz0')
    MORE_LOAD_BUTTON = (By.XPATH, '//button[contains(text(), "Загрузить еще")]')
    SORT_PRICE_BUTTON = (By.CSS_SELECTOR, '.MuiBox-root.css-0')
    MIN_PRICE = (By.CSS_SELECTOR, '.MuiInputBase-input.css-mnn31')
    MAX_PRICE = (By.CSS_SELECTOR, '.MuiInputBase-input.css-mnn31')
