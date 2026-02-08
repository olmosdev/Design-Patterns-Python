from abc import ABC, abstractmethod
from typing import NewType

HTML = NewType('HTML', str)
XAML = NewType('XAML', str)

class Control(ABC):
    @abstractmethod
    def print(self, text: str) -> HTML | XAML:
        pass

class TextBoxHTMLControl(Control):
    def print(self, text: str) -> HTML:
        return HTML(f"<input type='text' placeholder='{text}' />")

class ButtonHTMLControl(Control):
    def print(self, text: str) -> HTML:
        return HTML(f"<button>{text}</button>")

class TextBoxXAMLControl(Control):
    def print(self, text: str) -> XAML:
        return XAML(f"<TextBox PlaceholderText=\"{text}\" />")

class ButtonXAMLControl(Control):
    def print(self, text: str) -> XAML:
        return XAML(f"<Button Content=\"{text}\" />")

class ControlFactory(ABC):
    @abstractmethod
    def create_textbox(self) -> Control:
        pass

    @abstractmethod
    def create_button(self) -> Control:
        pass

class HTMLControlFactory(ControlFactory):
    def create_textbox(self) -> Control:
        return TextBoxHTMLControl()

    def create_button(self) -> Control:
        return ButtonHTMLControl()

class XAMLControlFactory(ControlFactory):
    def create_textbox(self) -> Control:
        return TextBoxXAMLControl()

    def create_button(self) -> Control:
        return ButtonXAMLControl()

class App():
    def __init__(self, factory: ControlFactory):
        self.__factory = factory

    def create_page(self):
        content = ""
        content += self.__factory.create_textbox().print("Name")
        content += self.__factory.create_textbox().print("Email")
        content += self.__factory.create_button().print("Submit")
        return content

# app = App(HTMLControlFactory())
app = App(XAMLControlFactory())
content = app.create_page()
print(content)

