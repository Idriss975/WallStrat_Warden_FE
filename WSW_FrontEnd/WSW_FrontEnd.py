import reflex as rx

from rxconfig import config
from .Components.Header import header


@rx.page(route="/",title="Main Page")
def index() -> rx.Component:
    return rx.vstack(
        header(Login=True),
        
        
        width="100%",
        padding_top="0",
        padding_right="0",
        padding_left="0",
        justify="between",
        )

@rx.page(route="/logsign", title="test")
def login():
    return rx.vstack(
        header(Login=True),
        rx.vstack(
            rx.vstack(
                rx.heading("Username"),
                rx.input(placeholder="ex: Jane Doe",width="100%"),
                rx.heading("Password", margin_top="6px"),
                rx.input(placeholder="ex: MCZPpQUuS",type="password",width="100%"),
                rx.hstack(
                    rx.button("Login"), rx.button("Sign in"),

                    margin_top="20px",
                    justify="center",
                    width="100%",
                ),

                border="1px solid",
                border_radius="12px",
                padding="15px",
                gap="8px",
                width="20%",
                
            ),

            width="100%",
            justify="center",
            align="center",
            margin_top="5em",
        ),
        
        width="100%",
        padding_top="0",
        padding_right="0",
        padding_left="0",
        justify="between",
        )

from .Components.Stocks import stocks
@rx.page(route="/test", title="Log in or Sign in")
def login():
    return rx.vstack(
        header(),

        stocks(),
    )


app = rx.App(
    theme=rx.theme(
        accent_color="yellow",
    )
)
