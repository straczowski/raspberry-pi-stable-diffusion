from diffusers import StableDiffusionPipeline
from PIL import Image

pipe = StableDiffusionPipeline.from_pretrained("../stable-diffusion-v1-5", low_cpu_mem_usage=True)
pipe = pipe.to("cpu")

prompt = "a red fox in space painted by Monet"
image = pipe(prompt, num_inference_steps=31, width=400, height=400).images[0]

image.save("output.png")
