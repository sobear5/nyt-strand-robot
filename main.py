import asyncio
from pyppeteer import launch

import nltk
nltk.download('words')
from nltk.corpus import words
all_words = words.words()
all_words.sort()
filtered_list = [s for s in all_words if len(s) > 3]
print(len(filtered_list))

import pickle

with open("a_list.pkl", "rb") as f:
    a_list = pickle.load(f)
with open("b_list.pkl", "rb") as f:
    b_list = pickle.load(f)
with open("c_list.pkl", "rb") as f:
    c_list = pickle.load(f)
with open("d_list.pkl", "rb") as f:
    d_list = pickle.load(f)
with open("e_list.pkl", "rb") as f:
    e_list = pickle.load(f)
with open("f_list.pkl", "rb") as f:
    f_list = pickle.load(f)
with open("g_list.pkl", "rb") as f:
    g_list = pickle.load(f)
with open("h_list.pkl", "rb") as f:
    h_list = pickle.load(f)
with open("i_list.pkl", "rb") as f:
    i_list = pickle.load(f)
with open("j_list.pkl", "rb") as f:
    j_list = pickle.load(f)
with open("k_list.pkl", "rb") as f:
    k_list = pickle.load(f)
with open("l_list.pkl", "rb") as f:
    l_list = pickle.load(f)
with open("m_list.pkl", "rb") as f:
    m_list = pickle.load(f)
with open("n_list.pkl", "rb") as f:
    n_list = pickle.load(f)
with open("o_list.pkl", "rb") as f:
    o_list = pickle.load(f)
with open("p_list.pkl", "rb") as f:
    p_list = pickle.load(f)
with open("q_list.pkl", "rb") as f:
    q_list = pickle.load(f)
with open("r_list.pkl", "rb") as f:
    r_list = pickle.load(f)
with open("s_list.pkl", "rb") as f:
    s_list = pickle.load(f)
with open("t_list.pkl", "rb") as f:
    t_list = pickle.load(f)
with open("u_list.pkl", "rb") as f:
    u_list = pickle.load(f)
with open("v_list.pkl", "rb") as f:
    v_list = pickle.load(f)
with open("w_list.pkl", "rb") as f:
    w_list = pickle.load(f)
with open("x_list.pkl", "rb") as f:
    x_list = pickle.load(f)
with open("y_list.pkl", "rb") as f:
    y_list = pickle.load(f)
with open("z_list.pkl", "rb") as f:
    z_list = pickle.load(f)






async def main():

    #gets letters on nyt website
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.nytimes.com/games/strands')

        # Evaluate JS to get all text inside <div class="target-class">
    div_texts = await page.evaluate('''() => {
    return Array.from(document.querySelectorAll(".styles-module_strandsBtn__xobCT.styles-module_item__ZXXc7"))
                .map(el => el.innerText);
}''')
    await browser.close()



    print(div_texts)

asyncio.run(main())
