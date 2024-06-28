import reflex as rx
from rxconfig import config
from reflex.style import color_mode

class stocks_Table(rx.State):
    Stocks : list[dict[str,float,str]] = [
        {"Index":"TSLA", "Name":"Tesla", "Prix":1526.36, "Change":"+1.5"},
        {"Index":"TSLA", "Name":"Tesla", "Prix":1526.36, "Change":"+0"},
        {"Index":"TSLA", "Name":"Tesla", "Prix":1526.36, "Change":"-1.5"},
        ]
    def redirr(self, st):
        return rx.redirect(f"/stocks/{st}")
def show_stocks(stock: dict):
    return rx.table.row(
                rx.table.row_header_cell(stock["Index"]),
                rx.table.cell("$", stock["Prix"]),
                rx.cond(stock["Change"] > 0,
                        rx.table.cell(stock["Change"], "%", color="green"),
                    rx.cond(
                        stock["Change"] < 0,
                        rx.table.cell(stock["Change"], "%", color="red")
                        ,
                        rx.table.cell(stock["Change"], "%", color="gray")
                    )        
                ),
                on_click=stocks_Table.redirr(stock["Index"])
                
            )

def stocks(has_link=True, **Components) -> rx.Component :
    return  rx.vstack(
        rx.table.root(
            rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Index"),
                rx.table.column_header_cell("Prix"),
                rx.table.column_header_cell("Change"),
                ),
                ),
            rx.table.body(
                rx.foreach(stocks_Table.Stocks, show_stocks),
            ),
            ),
            rx.cond(has_link == True, 
                    rx.link("View All Stocks.", href="/stocks", color_scheme="sky"),
            ),

            **Components,
            border_radius="12px",
            padding="15px",
            align="stretch",
            gap="8px",
            background_color=rx.color_mode_cond(light="#FAFAFA", dark="#1E2329"),
    )
            

                
                