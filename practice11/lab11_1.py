from PIL import Image, ImageFilter
from pathlib import Path

input_dir = Path("images1")
output_dir = Path("images2")

output_dir.mkdir(exist_ok=True)

type = input("Выберите фильтр: \n 1) Контур \n 2) Детализация \n 3) Поиск краев \n")

for i in input_dir.iterdir():
    img = Image.open(i)

    match type:
        case "1":
            contour_img = img.filter(ImageFilter.CONTOUR) # Контур
            contour_img.save(f"images2/contour_{i.name}")
        case "2":
            detail_img = img.filter(ImageFilter.DETAIL) # Детализация
            detail_img.save(f"images2/detail_{i.name}")
        case "3":
            edges_img = img.filter(ImageFilter.FIND_EDGES) # Поиск краев
            edges_img.save(f"images2/edges_{i.name}")