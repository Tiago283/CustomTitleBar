import flet as ft


def main(page: ft.Page):
    #! Important Configurations
    page.window.title_bar_buttons_hidden = True
    page.window.title_bar_hidden = True

    #? Padding Optional
    page.padding = 2

    #! Defaut Actions
    def minimize(e):
        page.window.minimized = not page.window.minimized
        page.update()

    def maximize(e):
        page.window.maximized = not page.window.maximized
        page.update()

    def close(e):
        page.window.destroy()

    ## Title Bar
    title_bar = ft.Row(
        [
            ft.Row(
                [
                    ft.Image('icon.png', width=25, height=25), ## Icon
                    ft.Text("Custom Title Bar"), ## Title
                ]
            ), ## Leading
            ft.Row(
                [
                    ft.IconButton(ft.Icons.REMOVE, on_click=minimize), ## Minimize button
                    ft.IconButton(ft.Icons.SQUARE_OUTLINED, on_click=maximize), ## Maximize button
                    ft.IconButton(ft.Icons.CLOSE, on_click=close) ## Close button
                ]
            ), ## Actions
        ],
        ft.MainAxisAlignment.SPACE_BETWEEN, ## Title Bar Vertical
        ft.CrossAxisAlignment.CENTER, ## Title Bar Horizontal
    )

    ## Add the Custom Title Bar
    page.add(ft.WindowDragArea(title_bar))
    page.update()


if __name__ == '__main__':
    ft.app(main, assets_dir='assets')
