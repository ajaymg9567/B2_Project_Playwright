from playwright.async_api import async_playwright
import pytest

@pytest.mark.asyncio
async def test_for_async(async_page):
    async_page.goto("https://www.amazon.in/")