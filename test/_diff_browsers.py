from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_diff_browsers(browser):
    async with async_playwright() as p:
        chrome_browser = await p.chromium.launch(headless=False)
        user_context = await chrome_browser.new_context()
        page = await user_context.new_page()
        await page.goto("https://www.google.com")

        admin_context = await chrome_browser.new_context()
        page = await admin_context.new_page()
        await page.goto("https://www.amazon.com")