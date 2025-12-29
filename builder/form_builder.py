from abc import ABC, abstractmethod

# Product
class HtmlForm:
    def __init__(self, action, method, fields):
        self.action = action
        self.method = method
        self.fields = fields

    def __str__(self):
        fields_html = "\n".join(self.fields)
        return f"""
                <form action="{self.action}" method="{self.method}">
                    {fields_html}
                </form>
                """

# Logistics for product creation
class Builder(ABC):
    @abstractmethod
    def set_action(self, action):
        pass

    @abstractmethod
    def set_method(self, method):
        pass

    @abstractmethod
    def add_text_input(self, name, placeholder):
        pass

    @abstractmethod
    def add_password_input(self, name, placeholder):
        pass

    @abstractmethod
    def add_email_input(self, name, placeholder):
        pass

    @abstractmethod
    def add_submit_input(self, value):
        pass

    @abstractmethod
    def build(self):
        pass

class HtmlFormBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.action = ""
        self.method = "POST"
        self.fields = []
        return self

    def set_action(self, action):
        self.action = action
        return self

    def set_method(self, method):
        self.method = method
        return self

    def add_text_input(self, name, placeholder):
        field = f'<input type="text" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self # The pattern forces the object to be returned by itself in order to chain more behaviors

    def add_password_input(self, name, placeholder):
        field = f'<input type="password" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self
    
    def add_email_input(self, name, placeholder):
        field = f'<input type="email" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self

    def add_submit_input(self, value="Send"):
        field = f'<button type="submit">{value}</button>'
        self.fields.append(field)
        return self

    def build(self):
        form = HtmlForm(self.action, self.method, self.fields)
        self.reset()
        return form

html_form_builder = HtmlFormBuilder()
login_form = (html_form_builder.set_action("/login")
                .set_method("POST")
                .add_email_input("email", "Enter your email")
                .add_password_input("pass", "Enter your password")
                .add_submit_input()
                .build()
            )

# Use the following page https://html.onlineviewer.net// to visualize the generated form
print(login_form)




