import reflex as rx

from reflex.style import color_mode


question_style = dict(
    font_weight="bold",
    
)
answer_style = dict(
)

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.text(question, style=question_style, size="5"),
        rx.text(answer, style=answer_style, size="4", margin_top="20px"),
        margin_y="1em",
        padding="1em",
        border_radius="8px",
        box_shadow=rx.color_mode_cond(light="rgba(0, 0, 0, 0.15) 0px 2px 8px", dark="rgba(255, 255, 255, 0.5) 0px 2px 8px"),
        width="100%",
    )