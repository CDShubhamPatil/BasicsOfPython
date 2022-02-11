import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.cactusvp.com/")

    yield
    driver.quit()


#01 To verify the title of the site
@pytest.mark.usefixtures("init_driver")
def test_CVP_title():
    assert driver.title == 'Cactus Venture Partners'

                  ##################
#02 To verify the URL
@pytest.mark.usefixtures("init_driver")
def test_CVP_url():
    assert driver.current_url == 'https://www.cactusvp.com/'

                  ##################

#03 To Verify the header element
@pytest.mark.usefixtures("init_driver")
def test_CVP_Verify_header():
    header_element = driver.find_element_by_xpath("//nav[@class='nav-menu d-none d-lg-flex align-items-center']")
    print(header_element.text)

                    ##################

#04 To click on any header element
@pytest.mark.usefixtures("init_driver")
def test_CVP_header_click_():
    header = driver.find_element_by_xpath("//a[@title='TEAM']")
    header.click()
    time.sleep(10)
    thesis = driver.find_element_by_xpath("//h2[text()='TEAM']").text
    assert thesis == "TEAM","User reached at Team section on CVP site."

                    ##################

#05 To click on any header element
@pytest.mark.usefixtures("init_driver")
def test_CVP_Verify_Team_Profile():
    header = driver.find_element_by_xpath("//a[@title='TEAM']")
    header.click()
    prof01=driver.find_element_by_xpath("//img[@alt='Anurag']")
    prof01.click()
    time.sleep(5)
    ag=driver.find_element_by_xpath("//h4[text()='Anurag Goel']").text
    assert ag =="Anurag Goel" , "Profile is not verified."
    time.sleep(5)
    print("------> Anurag Goel profile is verified successfully.<---------")

                   ##################

#06 To print all the links on the webpage
@pytest.mark.usefixtures("init_driver")
def test_CVP_print_all_links():
    total_links=driver.find_elements_by_tag_name('a')
    print(len(total_links))

    for link in total_links:
        links=link.text
        print(links)
        print(link.get_attribute('href'))

                   ##################