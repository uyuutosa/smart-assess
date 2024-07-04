import base64
import os

import langchain
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import AIMessage, HumanMessage

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# 画像をBase64エンコード
base64_image = encode_image("./problem.jpg")
chain = ChatOpenAI(model="gpt-4o", max_tokens=1024)
msg = chain.invoke(
    [
        AIMessage(
            content="You are a great elementary school teacher that is especially good at OCR from images"
        ),
        HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": "please answer the question written in the image in Japanese.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ]
        ),
    ]
)
print(msg.content)
