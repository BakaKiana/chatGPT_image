import urllib.request
from PIL import Image
import openai

openai.api_key = "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"

# 设置文字，这里使用一句话描述一个图像的文字
prompt = "从远处看的一辆在公路上的超级跑车"

# 调用openai的text-to-image功能
model_engine = "image-alpha-001"
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024",
    model=model_engine
)

# 获取生成的图片的url
image_url = response["data"][0]["url"]
with urllib.request.urlopen(image_url) as url:
    image = Image.open(url)
print(image_url)
image.show()
