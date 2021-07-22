import wikipedia

wikipedia.set_lang("kk")

wiki_random = wikipedia.random(pages=1000)

res = ""

for i in wiki_random:
    try:
        p = wikipedia.page(i)
        text = p.content
        res += text

    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    except wikipedia.exceptions.PageError as e:
        print(e)

with open("Kazakh_Text.txt", "a", encoding="utf-8") as f:
    f.write(res)
