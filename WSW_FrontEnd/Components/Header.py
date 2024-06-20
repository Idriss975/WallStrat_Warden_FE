import reflex as rx
from rxconfig import config
from reflex.style import color_mode

def header(Title="WallStreet Warden", Login=False) -> rx.Component :
    return rx.hstack(
                rx.heading(Title, size="7", on_click=rx.redirect("/")),

                rx.spacer(),
                
                rx.cond(Login == True,
                    rx.stack(
                        rx.button("Login / Sign in", on_click=rx.redirect("/logsign")),
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