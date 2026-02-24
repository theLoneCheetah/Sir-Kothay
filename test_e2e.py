import uuid
from typing import TYPE_CHECKING
from playwright.sync_api import expect, sync_playwright

# import classes only for correct annotations
if TYPE_CHECKING:
    from playwright.sync_api import Playwright, Browser, Page

# url to frontend page
BASE_URL = "http://127.0.0.1:5500"

# generate unique user id
def generate_test_user() -> dict[str, str]:
    uid = str(uuid.uuid4())[:8]
    return {
        "username": f"TestUser{uid}",
        "email": f"test_{uid}@example.com",
        "password": "test_password"
    }

# function to do authorization routine
def user_registration_and_login(p: Playwright, get_screenshot: bool = False) -> tuple[dict[str, str], Browser, Page]:
    # unique user id
    user = generate_test_user()

    # chromium session with windows to see
    browser = p.chromium.launch(headless=False, slow_mo=500)

    # new page
    page = browser.new_page()

    # got to register page
    page.goto(f"{BASE_URL}/auth/register.html")

    # fill fields according to their names in frontend code
    page.fill('input[name="username"]', user["username"])
    page.fill('input[name="email"]', user["email"])
    page.fill('input[name="password"]', user["password"])
    page.fill('input[name="confirm_password"]', user["password"])

    # click button with submit type
    page.click('button[type="submit"]')
    
    # registration screenshot for the first test
    if get_screenshot:
        page.screenshot(path="screenshots/registration.png")

    # wait for redirection to login page
    page.wait_for_url(f"{BASE_URL}/auth/login.html", timeout=15000)

    # fill user login data
    page.fill('input[name="email"]', user["email"])
    page.fill('input[name="password"]', user["password"])

    # click button with submit type
    page.click('button[type="submit"]')

    # wait for redirection to dashboard page
    page.wait_for_url(f"{BASE_URL}/dashboard/home.html", timeout=10000)

    # wait for page loading with registered username
    page.wait_for_selector("#userName:not(:empty)", timeout=10000)

    # return variables that were set
    return user, browser, page

# test new user's registration, login try and logout
def test_registration_login_logout() -> None:
    # run playwright in sync mode
    with sync_playwright() as p:
        user: dict[str, str]
        browser: Browser
        page: Page
        
        # register and login, True for screenshots
        user, browser, page = user_registration_and_login(p, True)

        # get displayed name, it must be the same as the registered, return error message otherwise
        displayed_name = page.text_content("#userName")
        assert user["username"] == displayed_name, f"Got {displayed_name} instead of {user['username']}"

        # logout and wait for redirection
        page.click("text=Logout")
        page.wait_for_url(f"{BASE_URL}/auth/login.html", timeout=10000)

        # screenshot after logout
        page.screenshot(path="screenshots/logout.png")

        # close browser session
        browser.close()

# test creating new message and publishing it
def test_create_message_and_public_page() -> None:
    # run playwright in sync mode
    with sync_playwright() as p:
        user: dict[str, str]
        browser: Browser
        page: Page

        # register and login
        user, browser, page = user_registration_and_login(p)

        # automatically skip (by pressing OK) pop-up dialog window
        page.on("dialog", lambda dialog: dialog.accept())

        # click to create message and wait until it will be configured
        page.locator("button.fixed.bottom-8.right-8").click()
        page.wait_for_selector("#addMessageModal:not(.hidden)", timeout=5000)

        # fill some message and click on button to add
        test_message = f"Test message {user['username']}"
        page.fill("#newMessageText", test_message)
        page.click("#addMessageModal button:has-text('Add')")

        # wait until new message in gray block appears
        message_card = page.locator(f".bg-gray-50:has-text('{test_message}')")
        expect(message_card).to_be_visible(timeout=10000)   # assertion

        # wait for activate button
        activate_button = message_card.locator("button:has-text('Activate')")
        expect(activate_button).to_be_visible()   # assertion

        # screenshot after message added
        page.screenshot(path="screenshots/dashboard.png")

        # click the button
        activate_button.click()

        # wait intil button deactivate appears in enw message block
        page.wait_for_selector(f".bg-gray-50:has-text('{test_message}') button:has-text('Deactivate')", timeout=5000)

        # click broadcast and wait for new tab opening in browser
        with browser.contexts[0].expect_page() as new_page_info:
            page.locator("button:has-text('Broadcast')").click()
        
        # get new page object and wait for loading
        public_page = new_page_info.value
        public_page.wait_for_load_state()

        # wait for loading broadcast message
        public_page.wait_for_selector("#broadcastMessage:not(:empty)", timeout=10000)

        # screenshot public page
        public_page.screenshot(path="screenshots/broadcast.png")

        # get text with broadcast message name and check it, must be the same as written earlier
        displayed_message = public_page.text_content("#broadcastMessage")
        assert test_message == displayed_message, f"Message mismatch: got {displayed_message} instead of {test_message}"

        # similarly check username
        displayed_name = public_page.text_content("#userName")
        assert user["username"] == displayed_name, f"Name mismatch: got {displayed_name} instead of {displayed_name}"

        # similarly check email
        displayed_email = public_page.text_content("#userEmail")
        assert user["email"] == displayed_email, f"Email mismatch: got {displayed_email} instead of {displayed_email}"

        # close browser session
        browser.close()