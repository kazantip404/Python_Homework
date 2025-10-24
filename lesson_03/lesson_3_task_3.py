from Adress import Address
from Mailing import Mailing


# Создаем экземпляры класса Address для адресов отправителя и получателя
to_address = Address("654321", "Санкт-Петербург", "Пушкина", "д.42", "кв.10")
from_address = Address("618900", "Пермь", "Ленина", "д.15", "кв.10,")

# Создаем экземпляр класса Mailing
my_mailing = Mailing(to_address, from_address, 15000, "TRACK123456789")

# Распечатываем отправление в заданном формате
print(f"Отправление {my_mailing.track} из "
      f"{my_mailing.from_address.index}, {my_mailing.from_address.city}, "
      f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - "
      f"{my_mailing.from_address.apartment} в {my_mailing.to_address.index}, "
      f"{my_mailing.to_address.city}, {my_mailing.to_address.street}, "
      f"{my_mailing.to_address.house} - {my_mailing.to_address.apartment}. "
      f"Стоимость {my_mailing.cost} рублей.")
