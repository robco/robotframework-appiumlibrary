# -*- coding: utf-8 -*-

from appium.webdriver.common.touch_action import TouchAction
from AppiumLibrary import utils
from AppiumLibrary.locators import ElementFinder
from keywordgroup import KeywordGroup

class _TouchKeywords(KeywordGroup):

    def __init__(self):
        self._element_finder = ElementFinder()

    # Public, element lookups
    def click_element(self, locator):
        """Click element identified by `locator`.

        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        self._info("Clicking element '%s'." % locator)
        self._element_find(locator, True, True).click()        

    def click_button(self, id_or_name):
        """ Click button """
        _platform_class_dict = {'ios':'UIAButton',
                                   'android': 'android.widget.Button'}
        if self._is_support_platform(_platform_class_dict):
            class_name = self._get_class(_platform_class_dict)
            self._click_element_by_class_name(class_name, id_or_name)

    def input_text(self, id_or_name, text):
        """ Input text identified by `locator`.
        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        Examples:
        | Input text | id=0            | my_id |
        | Input text | login_textfiled | my_id |
        """
        _platform_class_dict = {'ios':'UIATextField',
                                   'android': 'android.widget.EditText'}
        if self._is_support_platform(_platform_class_dict):
            class_name = self._get_class(_platform_class_dict)
            self._element_input_text_by_class_name(class_name, id_or_name, text)

    def input_password(self, id_or_name, text):
        """ Input secure text """
        _platform_class_dict = {'ios':'UIASecureTextField',
                                   'android': 'android.widget.EditText'}
        if self._is_support_platform(_platform_class_dict):
            class_name = self._get_class(_platform_class_dict)
            self._element_input_text_by_class_name(class_name, id_or_name, text)

    def long_press(self, locator):
        """ Long press the element """
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        long_press = TouchAction(driver).long_press(element)
        long_press.perform()

    def reset_application(self):
        """ Reset application """
        driver = self._current_application()
        driver.execute_script('mobile: reset')

    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """
        Swipe from one point to another point, for an optional duration.
        """
        driver = self._current_application()
        driver.swipe(self, start_x, start_y, end_x, end_y, duration)

    def scroll(self, start_locator, end_locator):
        """
        Scrolls from one element to another
        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        el1 = self._element_find(start_locator, True, True)
        el2 = self._element_find(end_locator, True, True)
        driver = self._current_application()
        driver.scroll(el1, el2)

    def hide_keyboard(self):
        """
        Hides the software keyboard on the device, using the specified key to
        press. If no key name is given, the keyboard is closed by moving focus
        from the text field. iOS only.
        """
        if not self._is_ios():
            raise EnvironmentError("Hide Keyword only support for iOS .")
        driver = self._current_application()
        driver.hide_keyboard()


    def page_should_contain_text(self, text, loglevel='INFO'):
        """Verifies that current page contains `text`.

        If this keyword fails, it automatically logs the page source
        using the log level specified with the optional `loglevel` argument.
        Giving `NONE` as level disables logging.
        """
        if not text in self.log_source(loglevel):
            self.log_source(loglevel)
            raise AssertionError("Page should have contained text '%s' "
                                 "but did not" % text)
        self._info("Current page contains text '%s'." % text)

    def page_should_not_contain_text(self, text, loglevel='INFO'):
        """Verifies that current page not contains `text`.

        If this keyword fails, it automatically logs the page source
        using the log level specified with the optional `loglevel` argument.
        Giving `NONE` as level disables logging.
        """
        if text in self.log_source(loglevel):
            self.log_source(loglevel)
            raise AssertionError("Page should not have contained text '%s' "
                                 "but did not" % text)
        self._info("Current page does not contains text '%s'." % text)

    def page_should_contain_element(self, locator, loglevel='INFO'):
        """Verifies that current page contains `locator` element.

        If this keyword fails, it automatically logs the page source
        using the log level specified with the optional `loglevel` argument.
        Givin
        """        
        if not self._is_element_present(locator):
            self.log_source(loglevel)
            raise AssertionError("Page should have contained element '%s' "
                                 "but did not" % locator)            
        self._info("Current page contains element '%s'." % locator)

    def page_should_not_contain_element(self, locator, loglevel='INFO'):
        """Verifies that current page not contains `locator` element.

        If this keyword fails, it automatically logs the page source
        using the log level specified with the optional `loglevel` argument.
        Givin
        """   
        if self._is_element_present(locator):
            self.log_source(loglevel)
            raise AssertionError("Page should not have contained element '%s' "
                                 "but did not" % locator)            
        self._info("Current page not contains element '%s'." % locator)

    def element_should_be_disabled(self, locator):
        """Verifies that element identified with locator is disabled.

        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.        
        """
        if self._element_find(locator, True, True).is_enabled():
            self.log_source(loglevel)
            raise AssertionError("Element '%s' should be disabled "
                                 "but did not" % locator)      
        self._info("Element '%s' is disabled ." % locator)

    def element_should_be_enabled(self, locator):
        """Verifies that element identified with locator is enabled.

        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.        
        """
        if not self._element_find(locator, True, True).is_enabled():
            self.log_source(loglevel)
            raise AssertionError("Element '%s' should be enabled "
                                 "but did not" % locator)      
        self._info("Element '%s' is enabled ." % locator)


    def element_name_should_be(self, locator, expected):
        element = self._element_find(locator, True, True)
        if expected != element.get_attribute('name'):
            raise AssertionError("Element '%s' name should be '%s' "
                                 "but it is '%s'." % (locator, expected, element.get_attribute('name'))) 
        self._info("Element '%s' name is '%s' " % (locator, expected))


    # Private
    
    def _is_id(self, id_or_name):
        if id_or_name.startswith('id='):
            return True
        else:
            return False

    def _click_element_by_name(self, name):
        driver = self._current_application()
        try:
            element = driver.find_element_by_name(name)
        except Exception, e:
            raise Exception, e
    
        try:
            element.click()
        except Exception, e:
            raise Exception, 'Cannot click the element with name "%s"' % name

    def _find_elements_by_class_name(self, class_name):
        driver = self._current_application()
        elements = driver.find_elements_by_class_name(class_name)
        return elements

    def _find_element_by_class_name(self, class_name, id_or_name):
        elements = self._find_elements_by_class_name(class_name)
    
        if self._is_id(id_or_name):
            try:
                index = int(id_or_name.split('=')[-1])
                element = elements[index]
            except IndexError, TypeError:
                raise Exception, 'Cannot find the element with index "%s"' % id_or_name
        else:
            found = False
            for element in elements:
                self._info("'%s'." % element.text)
                if element.text == id_or_name:
                    found = True
                    break
            if not found:
                raise Exception, 'Cannot find the element with name "%s"' % id_or_name

        return element

    def _get_class(self, platform_class_dict):
        return platform_class_dict.get(self._get_platform())        

    def _is_support_platform(self, platform_class_dict):
        return platform_class_dict.has_key(self._get_platform())

    def _click_element_by_class_name(self, class_name, id_or_name):
        element = self._find_element_by_class_name(class_name, id_or_name)
        self._info("Clicking element '%s'." % element.text)
        try:
            element.click()
        except Exception, e:
            raise Exception, 'Cannot click the %s element "%s"' % (class_name, id_or_name)

    def _element_input_text_by_class_name(self, class_name, id_or_name, text):
        try:
            element = self._find_element_by_class_name(class_name, id_or_name)
        except Exception, e:
            raise Exception, e

        self._info("input text in element as '%s'." % element.text)
        try:
            element.send_keys(text)
        except Exception, e:
            raise Exception, 'Cannot input text "%s" for the %s element "%s"' % (text, class_name, id_or_name)


    def _element_find(self, locator, first_only, required, tag=None):
        application = self._current_application()
        elements = self._element_finder.find(application, locator, tag)
        if required and len(elements) == 0:
            raise ValueError("Element locator '" + locator + "' did not match any elements.")
        if first_only:
            if len(elements) == 0: return None
            return elements[0]
        return elements

    def _is_text_present(self, text):
        return text in self.get_source()

    def _is_element_present(self, locator):
        application = self._current_application()
        elements = self._element_finder.find(application, locator, None)
        return len(elements) > 0