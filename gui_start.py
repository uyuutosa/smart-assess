import gradio as gr
from PIL import Image
import openai
import io
import os

from sample import read_image

# OpenAI APIキーを設定
openai.api_key = os.environ.get('YOUR_OPENAI_API_KEY')

def process_image(image):
    # 画像をバイナリデータに変換
    byte_arr = io.BytesIO()
    image.save(byte_arr, format='PNG')
    byte_data = byte_arr.getvalue()
    
    # GPT-4に画像を渡してテキストを生成
    response = openai.Image.create_variation(
        image=byte_data,
        n=1,
        size="1024x1024"
    )
    
    # GPT-4からの応答を取得
    answer = response['data'][0]['url']
    return answer

# Gradio UIの構築
iface = gr.Interface(
    fn=read_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Markdown(),
    title="AI採点 by GPT-4o",
    description="画像をアップロードし、GPT-4oからの応答を取得します。"
)

# UIの起動
iface.launch(share=True)