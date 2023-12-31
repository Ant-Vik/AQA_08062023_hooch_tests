from selenium.webdriver.common.by import By


class StartPageConstantsLocators:
    URL = 'https://vulkanbet.club/'
    LOGO_URL = 'https://vulkanbet.club/go/logo/'
    EN_LANG_XPATH = ".//span[@class='lang-toggle-block__item current-lang en']"
    ALL_REGS_BUTTON_XPATH = ".//div[@class='btn--wrap']"
    FIRST_DEMO_IN_PAGE_XPATH = ".//img[@alt='Book of Pharao']"
    LOGO_MAIN_PAGE_XPATH = ".//div[@class='logo']"
    BURGER_MENU_XPATH = ".//div[@class='mobile_menu_icon league-of-slots-casino']"
    REGISTER_AT_LEAGUE_OF_SLOTS_XPATH = ".//h2[@id='How to Register at League of Slots']"
    SPAN_SCROLL_TO_TOP_XPATH = ".//span[@class='scroll-top league-of-slots-casino']"
    FOOTER_ICONS_MOBILE_XPATH = (".//img[@data-original='https://los-casino.com/wp-content/uploads/sites/36749/2023"
                                 "/03/Vector.svg']")
    FOOTER_COPYRIGHT_XPATH_XPATH = ".//div[@class='copyright']"
    MAILTO_HELP_LINK_XPATH_XPATH = ".//a[@href='mailto:help@leagueofslots.com']"

    SEARCH_H1_IN_PAGE = (By.XPATH, "//h1[@class='name']")
    HEADER_MENU_FIRST_ITEM = "//li[@id='menu-item-1214']"
    HEADER_BANNER = ".//div[@class='header_banner']"
