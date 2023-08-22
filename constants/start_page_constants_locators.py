class StartPageConstantsLocators:
    URL = "https://www.slotozilla.com/"
    ISE_CASINO_XPATH = ".//div[@data-pid='ice-casino-wb-en']"
    FAQ_FIRST_QUESTIONS_XPATH = (".//h3[contains(text(),'Why is it important to choose a casino that is licensed and "
                                 "regulated?')]")





from bs4 import BeautifulSoup

html_content = """<div class="post">
    <h2 class="title">Заголовок поста</h2>
    <p class="content">Зміст поста...</p>
</div>
<div class="post">
    <h2 class="title">Інший заголовок</h2>
    <p class="content">Інший зміст...</p>
</div>"""
soup = BeautifulSoup(html_content, 'html.parser')

# Вибір всіх елементів з класом "post"
post_elements = soup.select('.post')

for post in post_elements:
    title = post.select_one('.title').text
    content = post.select_one('.content').text
    print(f"Заголовок: {title}")
    print(f"Зміст: {content}")
    print("------")
