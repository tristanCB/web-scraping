# Python 3.8
# Author: TristanCB
# Description: Basic example of webscraping setup using selenium, firefox and Tor browser proxy

### Dependencies
# -- Ensure microsoft visual studio C++ is installed: https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Alternatively: install anaconda or miniconda, and provision yourself an environment. Then:
# $ conda install scrapy
# $ conda install -c anaconda beautifulsoup4
# $ conda install -c anaconda urllib3

### Using selenium, TOR (as a proxy), and firefox for web scraping ###
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
# Ensure that you have Tor installed and running on your system.
# Alternatively setup a method to launch it programatically using something like subprocess

# Copy the contents of: TORINSTALLDIR\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default into the this
# projects drivers directory
profile = FirefoxProfile('./drivers/profile.default')
# Setup the proxy connection
profile.set_preference('network.proxy.type', 1)
# 127.0. 0.1 is the loopback Internet protocol (IP) address also referred to as the localhost
profile.set_preference('network.proxy.socks', '127.0.0.1')
# By default Tor port proxy 9150
profile.set_preference('network.proxy.socks_port', 9150)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()

# Use headless option if you want to prevent browser from popping up during script's execution.
options = Options()
options.headless = False

def determine_ip_address(url='https://whatismyipaddress.com/'):
    """
    Simple Function which determines your IP address by scraping https://whatismyipaddress.com/.
    Used as a test to setup proxy and start off projects!
    """
    # Ensure that Firefox is installed and that the driver is included: https://github.com/mozilla/geckodriver/releases, https://www.mozilla.org/en-CA/firefox/new/
    driver = webdriver.Firefox(options=options, executable_path="./drivers/geckodriver.exe")
   
    ## PhantomJS is now deprecated, instead it is recommended to use headless firefox. This methods does still work.
    ## https://phantomjs.org/download.html
    ## To configure Tor proxy for PhantomJS:
    # service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
    # driver = webdriver.PhantomJS(executable_path="./drivers/phantomjs-2.1.1-windows/bin/phantomjs.exe", service_args=service_args)
    ## /PhantomJS

    ## Using Chrome
    # chrome_options = Options()
    # chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
    ## With the following line one needs not to worry about downloading and indexing a driver
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # driver.get('https://whatismyipaddress.com/')
    ## /Using Chrome

    # "Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded"
    # (https://selenium-python.readthedocs.io/getting-started.html)
    driver.get(url)

    # Find the HTML element with the information we desire.
    # Tip: use a browser's inspect tool to determine how this should be done.
    findip = driver.find_element_by_id('ipv4')
    my_ip_address = findip.text
    driver.close()
    return my_ip_address

if __name__ == "__main__":
    print(f"My IP address is: {determine_ip_address()}")

