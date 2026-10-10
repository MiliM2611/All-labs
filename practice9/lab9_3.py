from PIL import Image, ImageFilter

type = input("Выберите фильтр: \n 1) Контур \n 2) Детализация \n 3) Поиск краев \n")
images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

for i in images:
    img = Image.open(f"images1/{i}")

    match type:
        case "1":
            contour_img = img.filter(ImageFilter.CONTOUR) # Контур
            contour_img.save(f"images2/contour_{i}")
        case "2":
            detail_img = img.filter(ImageFilter.DETAIL) # Детализация
            detail_img.save(f"images2/detail_{i}")
        case "3":
            edges_img = img.filter(ImageFilter.FIND_EDGES) # Поиск краев
            edges_img.save(f"images2/edges_{i}")
