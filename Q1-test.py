import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Yield the WebDriver instance for the test
    yield driver

    # After the test, close the browser
    driver.quit()

def test_table_properties(browser):
    # Open the HTML file in the browser
    browser.get('P3QE1.html')

    # Verify that the table takes up 50% of the display area
    table = browser.find_element_by_tag_name('table')
    assert '50%' in table.value_of_css_property('width')

    # Verify the table border properties
    table_border = table.value_of_css_property('border')
    assert '2px solid red' in table_border

    # Verify the cell border properties
    cell_borders = browser.find_elements_by_css_selector('th, td')
    for cell in cell_borders:
        assert '1px solid gray' in cell.value_of_css_property('border')
        assert '5px' in cell.value_of_css_property('padding')

def test_table_headings(browser):
    # Verify the table headings
    headings = browser.find_elements_by_css_selector('th')
    assert headings[0].get_attribute('colspan') == '3'
    assert headings[0].get_attribute('style') == 'background-color: black; color: white'

    # Verify the first column is marked as a heading cell
    first_column = browser.find_elements_by_css_selector('tr > th:first-child')
    assert len(first_column) == 1

    # Verify the first two rows are marked as heading cells
    first_two_rows = browser.find_elements_by_css_selector('tr:nth-child(-n+2)')
    assert len(first_two_rows) == 2

if __name__ == "__main__":
    pytest.main()
