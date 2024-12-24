# Talking

say("hello how can I help you ?")

# Printing emojis

say("Its going to be hot! Bring some :sunglasses:")

# Outputting using Blocks, Sections and Markdown

blocks = []
blocks.append({
    "type": "header",
    "text": {
        "type": "plain_text",
        "text": f"Packing List for trip to {city.name}, {city.state}"
    }
})
blocks.append({"type": "section",
               "text": {"type": "mrkdwn",
                        "text": f"- sleeping bag\n- tent\n"}})
say({"blocks": blocks})