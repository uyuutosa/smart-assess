import base64
import io
import os
from pathlib import Path

import langchain
import PIL.Image as Image
from langchain.schema.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI


def encode_image(byte_data):
    return base64.b64encode(byte_data).decode("utf-8")


def read_image(image: Image):
    byte_arr = io.BytesIO()
    image.save(byte_arr, format="JPEG")
    byte_data = byte_arr.getvalue()

    # 画像をBase64エンコード
    base64_image = encode_image(byte_data)
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
                        #"text": "please answer the question written in the image in Japanese. And you should surround the mathmatical equations with $$.",
                        "text": "You are a great elementary school teacher that is especially good at OCR from images. \
                        Please answer the question written in the image in Japanese. You should surround the mathematical equations with $$ to display them correctly in Markdown."
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ]
            ),
        ]
    )
    return msg.content
