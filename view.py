
class View:
    MENU_ITEMS = (
        "открыть файл",
        "сохранить файл",
        "показать контакты",
        "создать контакт",
        "найти контакт",
        "изменить контакт",
        "удалить контакт",
        "выход"
    )

    def show_menu(self):
        text = "Введите число действия:\n\n"
        for i, item in enumerate(self.MENU_ITEMS):
            text += f"{i}. {item}\n"
        print(text)

    def show_contacts(self, contacts):
        if not contacts:
            print("Сначала откройте файл")
        else:
            txt = "" # Контакты:\n
            for i, contact in enumerate(contacts):
                txt += f"{i}. {contact.name} | {contact.number} | {contact.description}\n"
            print(txt)


    def show_message(self, msg):
        print(msg)