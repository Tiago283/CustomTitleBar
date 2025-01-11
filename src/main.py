import flet as ft


#* Custom Controls
class TitleBar(ft.WindowDragArea):
    def __init__(self, actions: list | None = None):
        self.actions = actions
        self.icon = ft.Image('icon.png', width=25, height=25)
        self.title = ft.Text("Flet")
        self.bar = ft.Row([
            ft.Row([self.icon, self.title], ft.MainAxisAlignment.START),
            ft.Row(self.actions, ft.MainAxisAlignment.END)
        ], ft.MainAxisAlignment.SPACE_BETWEEN, ft.CrossAxisAlignment.CENTER)
        super().__init__(content=self.bar)


def main(page: ft.Page):
    #! Important Configurations
    page.window.title_bar_buttons_hidden = True
    page.window.title_bar_hidden = True
    page.padding = 2 #? Padding Optional

    def minimize(e):
        page.window.minimized = not page.window.minimized
        page.update()

    def maximize(e):
        page.window.maximized = not page.window.maximized
        page.update()

    def close(e):
        page.window.destroy()

    ## Add the Custom Title Bar
    title_bar = TitleBar([
        ft.IconButton(ft.Icons.REMOVE, on_click=minimize),
        ft.IconButton(ft.Icons.SQUARE_OUTLINED, on_click=maximize),
        ft.IconButton(ft.Icons.CLOSE, on_click=close)
    ])
    page.add(title_bar)
    page.update()


if __name__ == '__main__':
    ft.app(main, assets_dir='assets')
