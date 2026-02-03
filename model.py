import json
from view import View


class Contact:
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description

    def to_dict(self):
        return {
            "Name": self.name,
            "Number": self.number,
            "Description": self.description
        }


class ContactBook:
    def __init__(self, filepath="contact-book.json"):
        self.filepath = filepath
        self.loadfile = LoadFile(self.filepath)
        self.contacts = None  # целиком все контакты будут тут
        self.view = View()

    def open(self):
        try:
            contacts_dict = json.load(self.loadfile.openfile())
            self.contacts = []
            for i, card in contacts_dict.items():
                self.contacts.append(
                    Contact(card["Name"],
                            card["Number"],
                            card["Description"]
                            )
                )
        except:
            self.view.show_message("Ошибка открытия файла")

    def save(self):
        if not self.contacts:
            self.view.show_message("Сначала откройте файл")
            return
        try:
            contacts_dict = {}
            for i, card in enumerate(self.contacts):
                contacts_dict[i] = card.to_dict()
            self.loadfile.savefile(contacts_dict)
        except:
            self.view.show_message("Ошибка сохранения файла")

    def create(self):
        if not self.contacts:
            self.view.show_message("Сначала откройте файла")
            return
        try:
            name = input("Введите имя: ")
            number = input("Введите номер: ")
            description = input("Введите описание: ")
            self.contacts.append(Contact(name, number, description))
            self.save()
            self.view.show_message("Контакт добавлен!")
        except:
            self.view.show_message("Ошибка создания контакта")

    def find(self):
        if not self.contacts:
            self.view.show_message("Сначала откройте файла")
            return
        try:
            search = input("Введите поисковое значение: ")
            finded_contacts = []
            for contact in self.contacts:
                if (search.lower() in contact.name.lower() or
                        search.lower() in contact.number or
                        search.lower() in contact.description.lower()):
                    finded_contacts.append(contact)
            if finded_contacts:
                self.view.show_message("Поиск по значению '%s'" % search)
                self.view.show_contacts(finded_contacts)
            else:
                self.view.show_message("Ничего не найдено")
        except:
            self.view.show_message("Ошибка в поиске контакта")

    def edit(self):
        if not self.contacts:
            self.view.show_message("Сначала откройте файла")
            return
        try:
            self.view.show_message("Изменение контакта.")
            index = int(input("Введите индекс контакта: "))
            if index < 0 or index >= len(self.contacts):
                self.view.show_message("Контакт не найден")
                return
            contact = self.contacts[index]
            self.view.show_contacts([contact])
            self.view.show_message("Какой пункт изменить: 1 - Name, 2 - Number, 3 - Description, 4 - Все пункты")
            n = int(input())
            if n == 1 or n == 4:
                self.contacts[index].name = input("Введите новое имя: ")
            if n == 2 or n == 4:
                self.contacts[index].number = input("Введите новый номер: ")
            if n == 3 or n == 4:
                self.contacts[index].description = input("Введите новое описание: ")
            self.view.show_message("Контакт успешно изменен")
            self.save()
        except:
            self.view.show_message("Ошибка в редактировании контакта")

    def delete(self):
        if not self.contacts:
            self.view.show_message("Сначала откройте файла")
            return
        try:
            self.view.show_message("Удаление контакта.")
            index = int(input("Введите индекс контакта: "))
            if index < 0 or index >= len(self.contacts):
                self.view.show_message("Контакт не найден")
                return
            del self.contacts[index]
            self.save()
            self.view.show_message("Контакт удален")
        except:
            self.view.show_message("Ошибка удаления контакта")


class LoadFile:

    def __init__(self, filepath):
        self.filepath = filepath
        self.view = View()

    def openfile(self):
        file = open(self.filepath, "r", encoding="utf-8")
        self.view.show_message("Файл открыт")
        return file

    def savefile(self, book):
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(book, file, indent=4, ensure_ascii=False)
        self.view.show_message("Файл сохранен")
