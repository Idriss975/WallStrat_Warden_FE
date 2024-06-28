import reflex as rx
from rxconfig import config
from reflex.style import color_mode

from .Login import LoginState

def header(Title="WallStreet Warden", Login=False) -> rx.Component :
    return rx.hstack(
                rx.heading(Title, size="7", on_click=rx.redirect("/")),

                rx.spacer(),
                
                rx.cond(LoginState.is_loggedin == "false",
                    rx.stack(
                        rx.button("Login / Sign up", on_click=rx.redirect("/login")),
                    ),
                    rx.hstack(
                        rx.avatar(fallback=LoginState.Username[0]), 
                        rx.text(LoginState.Username), 
                        rx.button("Log out", on_click=LoginState.logout),
                        
                        align="center"
                    )
                ),
                
                rx.color_mode.button(position="right"),

        padding="0.5rem 2rem 1rem 2rem",
        margin_bottom="1rem",
        top="0",
        position="sticky",
        z_index="1",
        background_color=rx.color_mode_cond(light="#f9f9f9", dark="#181A20"),
        border_radius="0px 0px 40px 40px",
        border_bottom="1px solid",
        border_color=rx.color_mode_cond(light="black", dark="white"),
        width="100%",

    )