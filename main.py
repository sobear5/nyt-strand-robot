import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.nytimes.com/games/strands')

    # Evaluate JS to get all text inside <div class="target-class">
    div_texts = await page.evaluate('''() => {
    return Array.from(document.querySelectorAll(".styles-module_strandsBtn__xobCT.styles-module_item__ZXXc7"))
                .map(el => el.innerText);
}''')

    print(len(div_texts))
    await browser.close()

asyncio.run(main())
