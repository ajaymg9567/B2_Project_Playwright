def test_for_demo_browser(page):
    page.goto("http://google.com")
    page.wait_for_timeout(10000)