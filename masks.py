from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET


xml_file = "Задание2/masks.xml"
photos_folder = "Задание2/images/"

# Загрузка XML файла
tree = ET.parse(xml_file)
root = tree.getroot()

# Проход по каждому элементу image в XML файле
for image in root.iter("image"):
    # Получение атрибутов изображения
    image_id = image.get("id")
    image_name = image.get("name")
    image_width = int(image.get("width"))
    image_height = int(image.get("height"))

    # Создание пустых масок с прозрачным и черным фоном
    transparent_image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
    black_image = Image.new("RGB", (image_width, image_height), (0, 0, 0))

    # Проход по каждому элементу polygon внутри image
    for polygon in image.iter("polygon"):
        label = polygon.get("label")
        points = polygon.get("points")
        z_order = int(polygon.get("z_order"))

        # Разделение точек на координаты
        points = [tuple(map(float, point.split(","))) for point in points.split(";")]

        # Создаем объект ImageDraw.Draw для рисования маски
        draw_transparent = ImageDraw.Draw(transparent_image)
        draw_black = ImageDraw.Draw(black_image)

        # Отрисовка полигона на маске. Если тип маски "Ignore", пропускаем этот элемент
        if label == "Ignore":
            continue
        if label == "Skin":
            color = "fuchsia"
        # Если тип маски "Skin", рисуем маску на прозрачном и на черном фоне
        draw_black.polygon(points, fill=color)
        draw_transparent.polygon(points, fill=color)

    # Загрузка оригинального изображения
    photo_path = photos_folder + image_name.split("/")[-1]
    print("photo_path :", photo_path)
    photo = Image.open(photo_path)

    # Наложение прозрачной маски на оригинал
    masked_photo = Image.alpha_composite(
        photo.convert("RGBA"), transparent_image.convert("RGBA")
    )

    # Сохранение маски на черном фоне
    mask_path = photos_folder + "mask_" + image_id + ".png"
    print("mask_path :", mask_path)
    black_image.save(mask_path)

    # Сохранение наложенной маски на оригинал
    masked_photo_path = photos_folder + "masked_photo_" + image_id + ".png"
    print("masked_photo_path :", masked_photo_path)
    masked_photo.save(masked_photo_path)
