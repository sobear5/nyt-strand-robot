import asyncio
from pyppeteer import launch
import nltk
nltk.download('words')
from nltk.corpus import words
all_words = words.words()
all_words.sort()
filtered_list = [s for s in all_words if len(s) > 3]
print(len(filtered_list))
a_list = [s for s in all_words if s[0] == "a"]
print(a_list)

async def main():
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.nytimes.com/games/strands')

    # Evaluate JS to get all text inside <div class="target-class">
    div_texts = await page.evaluate('''() => {
    return Array.from(document.querySelectorAll(".styles-module_strandsBtn__xobCT.styles-module_item__ZXXc7"))
                .map(el => el.innerText);
}''')
    
    print(div_texts)
    print(len(div_texts))
    await browser.close()

asyncio.run(main())
