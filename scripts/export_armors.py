from PIL import Image
import os

# for each texture from ./scripts/src/armors/
# copy the texture to ./assets/minecraft/textures/models/armor/ but with the pixel (63,0) replaced with the color (255,254,253,255)



for file in os.listdir("./scripts/src/armors/"):
    if file.endswith(".png"):
        img = Image.open(f"./scripts/src/armors/{file}")
        pixels = img.convert("RGBA")
        pixels.putpixel((63,0), (255, 254, 253, 255))

        if not os.path.exists("./assets/minecraft/textures/models/armor/"):
            os.makedirs("./assets/minecraft/textures/models/armor/")
        pixels.save(f"./assets/minecraft/textures/models/armor/{file}")

print("Armors exported!")

# export elytra texture
img = Image.open("./scripts/src/elytra.png")
pixels = img.convert("RGBA")
pixels.putpixel((63,0), (255, 254, 253, 255))

if not os.path.exists("./assets/minecraft/textures/entity/"):
    os.makedirs("./assets/minecraft/textures/entity/")
pixels.save("./assets/minecraft/textures/entity/elytra.png")

print("Elytra exported!")