from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S23 Ultra", "+799944499988"))
catalog.append(Smartphone("Apple", "iPhone 16 ProMax", "+798888899988"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+795599988877"))
catalog.append(Smartphone("Google", "Pixel 7", "+799599599555"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+798812312312"))


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
