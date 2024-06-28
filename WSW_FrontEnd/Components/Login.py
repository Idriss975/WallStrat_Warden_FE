import reflex as rx

from .Signup import Authentication
from json import loads

class LoginState(rx.State):
    Username : str = rx.LocalStorage()
    Password:str
    is_loggedin:str = rx.LocalStorage("false")
    is_alertopen : bool = False
    
    async def Login(self):
        Accounts = await self.get_state(Authentication)
        Accounts_data = loads(Accounts.Accounts_raw)

        
        if {"username":self.Username, "password": self.Password} in Accounts_data:
            self.is_loggedin = "true"
            self.is_alertopen = False
            return rx.redirect("/")
        else:
            self.is_alertopen = True
    

    def loginredirect(self):
        if self.is_loggedin == "true":
            return rx.redirect("/")
    def mustlogin(self):
        if self.is_loggedin == "false":
            return rx.redirect("/login")
        
    def logout(self):
        self.is_loggedin = "false"
        self.Username = ""

        

def login_default() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.heading(
                    "Sign in to your account",
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
                    placeholder="User0153",
                    type="text",
                    size="3",
                    width="100%",
                    on_change=LoginState.set_Username,
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        #href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                     on_change=LoginState.set_Password,
                ),
                spacing="2",
                width="100%",
            ),
            
            rx.popover.root(
                rx.popover.trigger(
                    rx.button("Sign in", size="3", width="100%", on_click=LoginState.Login)
                ),
                rx.popover.content(
                    rx.flex(
                        rx.text("Username or password are incorrect."),
                        rx.popover.close(
                            rx.button("Close"),
                        ),
                        
                        direction="column",
                        spacing="3",
                    ),
                ),
            ),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="/signup", size="3"),
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