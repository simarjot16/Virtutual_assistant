import wolframalpha

appid = "LT5JLH-XJKVP2U6XP"

ques = input("What would you like to ask sir?\n")
client = wolframalpha.Client(appid)

ans = client.query(ques)
fans = next(ans.results).text
print(fans)


