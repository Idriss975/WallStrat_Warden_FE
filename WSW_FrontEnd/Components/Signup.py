import reflex as rx
from json import dumps, loads


class Authentication(rx.State):
    Accounts_raw: str = rx.LocalStorage("[]",sync=True)
    Username: str
    Password:str

    def insert_account(self):
        if self.Accounts_raw == "null":
            self.Accounts_raw = "[]"
        if self.Username != "" or self.Password != "":
            self.Accounts_raw = dumps(loads(self.Accounts_raw) + [{"username":self.Username, "password":self.Password}])      
        return rx.redirect("/login")
    
    
        
def signup_default() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.heading(
                    "Create an account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Username",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="User0195",
                    type="text",
                    size="3",
                    width="100%",
                    on_change= Authentication.set_Username
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Password",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                    on_change= Authentication.set_Password
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.box(
                rx.checkbox(
                    rx.text("Agree to ", rx.link("Terms and Conditions", href="https://raw.githubusercontent.com/TOYSOLDIER12/WallStreetWarden/master/LICENSE")),
                    default_checked=False,
                    spacing="2",
                ),
                width="100%",
            ),
            rx.button("Sign up", size="3", width="100%", on_click=Authentication.insert_account),
            rx.center(
                rx.text("Already registered?", size="3"),
                rx.link("Sign in", href="/login", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )