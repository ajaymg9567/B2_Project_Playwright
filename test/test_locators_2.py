import pytest
from playwright.async_api import expect
#
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.get_by_text("Welcome to our store")
#    await expect(ele).to_be_visible()
#    print(ele.inner_html())

####################################################

# # if u have any attribute in web ele
# #css->
# #tag_name{an='av'}
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.locator("h2[class='topic-html-content-header']") # locator :notfinding
#    await expect(ele).to_be_visible()
#    print(ele.inner_html())

###################################################

# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/books")
#    ele = async_page.locator(".product-title") # locator :notfinding
#    # ele :-- all products
#    all_product = await ele.all()
#    for i in all_product:
#        print(await i.inner_text())

#######################################################
# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     ele = async_page.locator("h2[class='topic-html-content-header']") # locator :notfinding
#     await expect(ele).fill("Books")


#########################################################

# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    ele = async_page.locator("input[class='button-2 product-box-add-to-cart-button']") # locator :notfinding
#    all_product = await ele.all()
#    for i in all_product:
#        await i.click()
#        break
#    await async_page.wait_for_timeout(5000)

########################################################

# * contains 'samsung'
# $ ends with $
# ^

# xpath
# //input[@name='email']
# css
# input[name='email']


# https://www.amazon.in/s?k=Mobiles&crid=1TYT1N5RZWSVB&sprefix=mob%2Caps%2C1615&ref=nb_sb_noss_2
# xpath

# @pytest.mark.asyncio
# async def test_getBytitle(async_page):
#     await async_page.goto("https://www.amazon.in/s?k=Mobiles&crid=1TYT1N5RZWSVB&sprefix=mob%2Caps%2C1615&ref=nb_sb_noss_2")
#     ele = async_page.locator('(//input[@aria-label="Samsung"])[2]')

#################################################################
#Xpath
#//a[text()='Build your own expensive computer']/ancestor::div[1]//input[@value='Add to cart']
#(//a[text()='Kotak Mahindra'])[2]/parent::td/following-sibling::td[1]
# //table[@class='ws-table-all']/descendant::tr/td[3]
# //table[@class='ws-table-all']/descendant::tr/td[3]//table[@class='ws-table-all']/descendant::tr/th[3]
# //table[@class='ws-table-all']/descendant::tr/td[3]|//th[text()='Country']
# //section[@class='category-section']//div[@role="heading"]
# //div[@id='ui-datepicker-div']//th
#//input[@id='txtUserName' or @id='txtPassword']
#//table[@class='ws-table-all']/descendant::tr[position()>5]/td[3]|//th[text()='Country']

##################################################################

