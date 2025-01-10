import flet as ft


def main(page: ft.Page):
    page.window.title_bar_buttons_hidden = True
    page.window.title_bar_hidden = True

    custom_bar = ft.AppBar(
        title=ft.Text("Custom Title Bar") ## Window Title
    )

    page.appbar = custom_bar
    page.update()


ft.app(main)
