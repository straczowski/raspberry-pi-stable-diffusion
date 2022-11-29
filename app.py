from diffusers import StableDiffusionPipeline
from PIL import Image

pipe = StableDiffusionPipeline.from_pretrained("../stable-diffusion-v1-5", low_cpu_mem_usage=True)
pipe = pipe.to("cpu")

prompt = "a black tree with golden leaves painted by Monet, autumn"
image = pipe(prompt, num_inference_steps=31, width=400, height=400).images[0]

image.save("output.png")
