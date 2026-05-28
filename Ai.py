from requests import post

headers = { "X-API-KEY": "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", "MinatoBot/1.0": "Mozilla/5.0", "referer": "https://www.facebook.com/profile.php?id=100094118835962" }

message = "Hello Ai, HowreYou ?"

system = "Your Name is Cris st. You are an ai assistance Developed by Cris"

data = { "user_id": "Chris", "messages": { "system": system, "user": user }

req = post("https://api.motadev.xyz/api/chat", json=data, headers=headers).json()


print(req)
