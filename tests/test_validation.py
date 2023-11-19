from page_objects.dynamicControl import DynamicControls
from page_objects.formAuth import FormAuthentication
from page_objects.addRemove import AddRemoveElement
from page_objects.contextMenu import ContextMenu
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_form_authentication(self):
        form = FormAuthentication(self.driver)

        form.navigate_to_form_page()
        form.enter_login_username("tomsmith")
        form.enter_login_password("SuperSecretPassword!")
        form.click_login_button()

        assert "logged in" in form.check_login_logout_status().text

        form.click_logout_button()
        assert "logged out" in form.check_login_logout_status().text

    def test_add_remove_element(self):
        add_rem = AddRemoveElement(self.driver)
        add_rem.navigate_to_add_remove_page()
        add_rem.click_add_element_button()
        delete_button = add_rem.check_delete_button().text
        assert delete_button == "Delete"

        add_rem.click_delete_button()
        delete_button = add_rem.check_delete_button()
        assert delete_button == "No Delete Button"

    def test_context_menu(self):
        context = ContextMenu(self.driver)
        context.navigate_to_context_menu_page()
        context.right_click_context_menu()

        assert context.check_alert_message() != ""

        context.accept_alert()

        assert context.alert_is_accepted() != ""

    def test_dynamic_control_checkbox(self):
        checkbox = DynamicControls(self.driver)
        checkbox.navigate_to_dynamic_controls_page()

        assert checkbox.check_checkbox_element() == "Checkbox Element Presents"
        checkbox.click_control_button("checkbox")

        assert checkbox.check_checkbox_element() == "No Checkbox Element"

        checkbox.click_control_button("checkbox")

        assert checkbox.check_checkbox_element() == "Checkbox Element Presents"

    def test_dynamic_control_input_text(self):
        input_text = DynamicControls(self.driver)
        input_text.navigate_to_dynamic_controls_page()

        assert input_text.checking_input_text_element() == False

        input_text.click_control_button("input")

        assert input_text.checking_input_text_element() == True

        input_text.click_control_button("input")

        assert input_text.checking_input_text_element() == False