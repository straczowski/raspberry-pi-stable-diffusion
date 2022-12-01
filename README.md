# How to run Stable Diffusion on Raspberry Pi 4

*Example* *Output*

```
a black tree with golden leaves painted by Monet, autumn
```

![Black Tree with golden leaves](/imgs/tree.png?raw=true "Black Tree with golden leaves")

first of all i have to say that this is for sure not the most convinient way to run Stable Diffusion. The Raspberry's 8GB RAM are below the recommended 12GB minimum RAM. And the CPU is so slow that a 400x400 px image takes ~45 minutes to be ready.

### so why we are doing this?

Becaus we can. And because both are great technologies. So consider this repository for educational purposes only and the joy of learning :)

## Prerequisites

running on `Debian GNU/Linux 11 (bullseye)`

1. Having cloned the Stable Diffusion model from Huggingface

i am using currently version 1.5
=> https://huggingface.co/runwayml/stable-diffusion-v1-5

```
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
```

2. Having Diffusers Library @0.7.x

https://pypi.org/project/diffusers/ 

```
pip install --upgrade diffusers
```

3. Run Your Raspberry Pi Headless

As we need any bit of RAM we can get, i am running the Pi without GUI. You can enable this boot mode via `raspi-config` 


# Execute

with all that setup you should be able to run that code

```
python app.py
```

The most critical part i encountered while booting the model in the beginning. Mostly the process was killed here. Since the diffuser library supports the `low_cpu_mem_usage` parameter, i got it also running on my Pi

on peaks i measure ~6.3GB RAM usage

![Pi RAM Usage](/imgs/htop-pi.png?raw=true "Pi RAM Usage")

happy diffusing! 🥳

