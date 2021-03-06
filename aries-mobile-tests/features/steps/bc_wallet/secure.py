# -----------------------------------------------------------
# Behave Step Definitions for Terms and Conditions rejection or acceptance.
# 
# -----------------------------------------------------------

from behave import given, when, then
import json
import os

# Local Imports
from agent_controller_client import agent_controller_GET, agent_controller_POST, expected_agent_state, setup_already_connected
from agent_test_utils import get_qr_code_from_invitation
# import Page Objects needed
from pageobjects.bc_wallet.termsandconditions import TermsAndConditionsPage
from pageobjects.bc_wallet.secure import SecurePage
from pageobjects.bc_wallet.home import HomePage
from pageobjects.bc_wallet.navbar import NavBar
from pageobjects.bc_wallet.pinsetup import PINSetupPage


@given('the User has accepted the Terms and Conditions')
def step_impl(context):
    context.execute_steps(f'''
        Given the User is on the Terms and Conditions screen
        And the users accepts the Terms and Conditions
        And the user clicks continue
    ''')


@when('the User enters the first PIN as "{pin}"')
def step_impl(context, pin):
    context.thisPINSetupPage.enter_pin(pin)
    # TODO remove comment here when Test IDs are on the visibility toggle
    #assert pin == context.thisPINSetupPage.get_pin()


@when('the User re-enters the PIN as "{pin}"')
def step_impl(context, pin):
    context.thisPINSetupPage.enter_second_pin(pin)
    # TODO remove comment here when Test IDs are on the visibility toggle
    #assert pin == context.thisPINSetupPage.get_second_pin()


@when('the User selects Create PIN')
def step_impl(context):
    context.thisInitializationPage = context.thisPINSetupPage.create_pin()

    context.device_service_handler.biometrics_authenticate(True)



@then('the User has successfully created a PIN')
@then('they land on the Home screen')
def step_impl(context):
    # The Home page will not show until the initialization page is done. 
    #assert context.thisInitializationPage.on_this_page()
    context.thisHomePage = context.thisInitializationPage.wait_until_initialized()
    context.thisNavBar = NavBar(context.driver)

    #If there are continued problems withconnection we can check if connection to the mediator exists
    #context.thisSettingsPage = context.thisHomePage.select_settings()
    #context.thisSettingsPage.select_connections()
