import wolframalpha
import wikipedia
from click._compat import raw_input

appid = "LT5JLH-XJKVP2U6XP"
while True:
    input = raw_input("What would you like to ask?\n")
    try:
        client = wolframalpha.Client(appid)
        ans = client.query(input)
        fans = next(ans.results).text
        print(fans)

    except:
        print(wikipedia.summary(input))


