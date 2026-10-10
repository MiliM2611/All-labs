from PIL import Image

watermark = Image.open("watermark.png").convert("RGBA")

images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

for i in images:
    background = Image.open(f"images1/{i}").convert("RGBA")
    combined = background.copy()
    position = (50, 50)
    combined.paste(watermark, position, watermark)
    combined_rgb = combined.convert("RGB")
    combined_rgb.save(f"images2/WM{i}", quality=95)