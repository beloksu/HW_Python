from smartphone import Smartphone


class Catalog:
    catalog = [
        Smartphone("Samsung", "A14", "+799999999"),
        Smartphone("Apple", "13", "+79888888888"),
        Smartphone("Mi", "123", "+79777777777")
    ]

    for smartphone in catalog:
        print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
