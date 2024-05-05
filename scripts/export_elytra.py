from PIL import Image

# Read the texture located in ./scripts/src/elytra.png
img = Image.open("./scripts/src/elytra.png")
pixels = img.convert("RGBA")

# get the RGB values of each pixel located between (22,0) and (45,21) (24x22 surface)
elytra = []

for y in range(0, 22):
    for x in range(22, 46):
        pixel = pixels.getpixel((x, y))
        r, g, b, a = pixel
        elytra.append(f"vec4({round(r/255.0, 4)},{round(g/255.0, 4)},{round(b/255.0, 4)},{round(a/255.0, 4)})")



with open("./assets/minecraft/shaders/include/nlz/elytratex.glsl", "w") as f:
    f.write("vec4 elytra[528] = vec4[](\n")
    for i in range(0, 24):
        f.write("\t")
        for j in range(0, 22):
            f.write(elytra[i*22+j])
            if i != 23 or j != 21:
                f.write(",")
        f.write("\n")
    f.write(");")


print("Done!")