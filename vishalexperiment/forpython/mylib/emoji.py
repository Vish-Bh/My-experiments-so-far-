def emoji_conventor(message):
        words=message.split()
        emoji={
         ":)": "😊",
        ";)": "😉",
        "<3": "❤️",
        "hello": "👋",
        "hi": "👋",
        "goodbye": "👋",
        "bye": "👋",}
        output=""
        for word in words:
            output+= emoji.get(word, word)+" "
        return output