import reflex as rx

from rxconfig import config
from .Components.Header import header
from .Components.Stocks import stocks, stocks_Table
from .Components.Login import login_default, LoginState
from .Components.Signup import signup_default
from .Components.FAQ import qa
from reflex_type_animation import type_animation

class Index_State(stocks_Table):
    def load_index(self):
        self.Stocks = [
            {"Index":"TSLA", "Name":"Tesla", "Prix":1526.36, "Change":"+1.5"},
            {"Index":"AAPL", "Name":"Tesla", "Prix":213.25, "Change":"+2.00"},
            {"Index":"AMZN", "Name":"Tesla", "Prix":193.61, "Change":"+3.90"},
            ]

@rx.page(route="/",title="WallStreet Warden - Predict your futur money", on_load=Index_State.load_index)
def index() -> rx.Component:
    return rx.vstack(
        header(Login=True),

        rx.hstack(
            rx.vstack(
                type_animation(sequence=["Predict your financial future.", 2000,
                                     "Don't work for your money.", 1000,
                                     "Let your money work for you.", 1000,
                                     "Max your dosh 💵 with WallStreet Warden.", 1000],
                font_size=["24px", "30px", "44px", "44px", "44px", "44px"],
                text_align="left",
                font_weight="bold",
                line_height="1.3",),
                rx.hstack( rx.input(placeholder="Email / Username"), rx.button("Sign up", on_click=rx.redirect("/signup")),
                          margin_top="60px" ),

                width="400px",
                margin_top="20px",
                justify="end",
                min_height="300px",
            ),
            
            
            rx.vstack(
                stocks(width="450px"),

                rx.vstack(
                    rx.text("US State Department Offers $5 Million Reward for Information on OneCoin Founder"),
                    rx.text("Worldcoin Announces Collaboration With Alchemy To Launch World Chain Blockchain"),
                    rx.text("Litecoin Activity Surpasses BTC and ETH, According to IntoTheBlock Data"),
                    rx.text("Layer 2 Blockchain Blast Distributes 17% of Native Token Supply"),

                    width="450px",
                    border_radius="12px",
                    padding="15px",
                    align="stretch",
                    gap="8px",
                    background_color=rx.color_mode_cond(light="#FAFAFA", dark="#1E2329"),
                ),
            ),

            gap="48px",
        
        ),
        rx.vstack(
            rx.heading("Frequently Asked Questions", size="8"),
            qa("What is WallStreet Warden ?",
                    "WallStreet Warden a platforme for predicting stock prices \
                    using a well knwon statistical algoritm. "),
            qa("Why WallStreet Warden ?",
                    "Because unlike other platforms that use sentimal type \
                        of analytics, We use a more Objective scientific method to \
                        predict stock prices which eliminates bias, emotion from process."),
            qa("What Services do we provide ?", 
                    "We used Yahoo Finance to extract the history of prices and apply them int oa graph.\
                    For the prediction we use a python script to run the ARIMA Alogrithm on the graph and get the result."),
            qa("To whom belongs this project ?",
                    "This project belongs to BOULAHYA Ilyas & BERCHIL Idriss."),
            width="70%",
            margin_top="200px"
        ),
        
       
        width="100%",
        gap="5",
        padding_top="0",
        padding_right="0",
        padding_left="0",
        justify="between",
        align="center",
        )

@rx.page(route="/login", title="WallStreet Warden - Log in", on_load=LoginState.loginredirect)
def login():
    return rx.vstack(
        header(Login=True),
        rx.vstack(
            login_default(),

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

@rx.page(route="/signup", title="WallStreet Warden - Sign up", on_load=LoginState.loginredirect)
def signup():
    return rx.vstack(
        header(Login=True),
        rx.vstack(
            signup_default(),

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


import plotly.express as px

import pandas as pd


def tested(name):
        df : pd.DataFrame = pd.DataFrame()

        t_df = pd.read_csv(f"secret_tokens/{name}.csv")
        t_df["file"] = name
        df=pd.concat([t_df, df])
        t_df = pd.read_json(f"secret_tokens/{name}.json")
        t_df["file"] = "Prediction"
        df=pd.concat([t_df, df])
        return df
class StockName_State(rx.State):

    async def onlo(self):
        ls =await self.get_state(LoginState)
        if ls.is_loggedin == "false":
            return rx.redirect("/login")

@rx.page(route="/stocks/TSLA", title="WallStreet Warden - Stocks", on_load=StockName_State.onlo)
def testA():
    return rx.vstack(
        header(),
        rx.plotly(
            data=px.line(
                tested("TSLA"),
                x="Date",
                y="Close",
                color="file",
            ),
            height="400px"),
    )

@rx.page(route="/stocks/AAPL", title="WallStreet Warden - Stocks", on_load=StockName_State.onlo)
def testB():
    return rx.vstack(
        header(),
        rx.plotly(
            data=px.line(
                tested("AAPL"),
                x="Date",
                y="Close",
                color="file",
            ),
            height="400px"),
    )

class Stocks_State(rx.State):
    async def loadstocksdata(self):
        stocks = await self.get_state(stocks_Table)
        stocks.Stocks = [
            {"Index":"TSLA", "Name":"Tesla", "Prix":1526.36, "Change":"+1.5"},
            {"Index":"AAPL", "Name":"Tesla", "Prix":213.25, "Change":"+2.00"},
        ]

@rx.page(route="/stocks", title="WallStreet Warden - Stocks", on_load=Stocks_State.loadstocksdata)
def stockspage():
    return rx.vstack(
        header(Login=True),

        rx.vstack(
            rx.heading("Markets Overview"),

            stocks(width="100%",has_link=False),

            margin_left="30px",
            margin_right="30px",
            width="100%"
        ),


        
        width="100%",
        padding_top="0",
        padding_right="0",
        padding_left="0",
        justify="between",
        )


app = rx.App(
    theme=rx.theme(
        accent_color="yellow",
    )
)
