from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select


@given(u'is on Registration page')
def step_impl(context):
    global driver
    path="./Drivers/chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testings")


@when(u'user enters un, pw and email')
def step_impl(context):
    driver.find_element_by_name("fld_username").send_keys("test1")
    driver.find_element_by_name("fld_email").send_keys("testing1@gmail.com")
    driver.find_element_by_name("fld_password").send_keys("test1")
    driver.find_element_by_name("fld_cpassword").send_keys("test")
    selectObj=Select(driver.find_element_by_name("sex"))
    #selectObj.select_by_index(1)
    #selectObj.select_by_value("2")
    selectObj.select_by_visible_text("Male")
    driver.find_element_by_name("terms")

@when(u'click on signup')
def step_impl(context):
    #driver.find_element_by_xpath('//input[@type="checkbox" and @value="terms"]').click()
    driver.find_element_by_xpath('//input[@type="submit" and @value="Sign up"]').click()
    driver.close()


@then(u'user should be registered successfully')
def step_impl(context):
    print("user is registered")


@when(u'user enters duplicate un, pw and email')
def step_impl(context):
    driver.find_element_by_name("fld_username").send_keys("test")
    driver.find_element_by_name("fld_email").send_keys("testing@gmail.com")
    driver.find_element_by_name("fld_password").send_keys("test")
    driver.find_element_by_name("fld_cpassword").send_keys("test")
    selectObj=Select(driver.find_element_by_name("sex"))
    #selectObj.select_by_index(1)
    #selectObj.select_by_value("2")
    selectObj.select_by_visible_text("Male")
    driver.find_element_by_name("terms")

@when(u'click on signup2')
def step_impl(context):
    #driver.find_element_by_xpath('//input[@type="checkbox" and @value="terms"]').click()
    driver.find_element_by_xpath('//input[@type="submit" and @value="Sign up"]').click()
    #driver.close()

@when(u'click on signup1')
def step_impl(context):
    #driver.find_element_by_xpath('//input[@type="checkbox" and @value="terms"]').click()
    driver.find_element_by_xpath('//input[@type="submit" and @value="Sign up"]').click()
    #driver.close()


@then(u'user should not be allowed to registered')
def step_impl(context):
    print("user is not registered")