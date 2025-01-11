import flet as ft

# Custom title bar class
class TitleBar(ft.WindowDragArea):
    def __init__(self, actions: list | None = None):
        self.actions = actions
        self.icon = ft.Image('icon.png', width=25, height=25)  # Icon for title bar
        self.title = ft.Text("Flet")  # Title text
        # Container for icon, title, and actions
        self.bar = ft.Container(
            ft.Row([
                ft.Row([self.icon, self.title], ft.MainAxisAlignment.START),  # Left: Icon and title
                ft.Row(self.actions, ft.MainAxisAlignment.END)  # Right: Action buttons
            ], ft.MainAxisAlignment.SPACE_BETWEEN, ft.CrossAxisAlignment.CENTER),  # Layout
            bgcolor=ft.Colors.BLUE,  # Background color
            padding=ft.Padding(1, 1, 1, 1)  # Padding for the bar
        )
        super().__init__(content=self.bar)  # Initialize draggable area

# Main app logic
def main(page: ft.Page):
    page.window.title_bar_buttons_hidden = True  # Hide default buttons
    page.window.title_bar_hidden = True  # Hide default title bar
    page.padding = 0  # Set page padding

    # Window action functions
    def minimize(e): page.window.minimized = not page.window.minimized; page.update()
    def maximize(e): page.window.maximized = not page.window.maximized; page.update()
    def close(e): page.window.destroy()

    # Add custom title bar
    title_bar = TitleBar([
        ft.IconButton(ft.Icons.REMOVE, on_click=minimize),
        ft.IconButton(ft.Icons.SQUARE_OUTLINED, on_click=maximize),
        ft.IconButton(ft.Icons.CLOSE, on_click=close)
    ])
    page.add(title_bar)  # Add to page
    page.update()  # Refresh page

# Start the app
if __name__ == '__main__':
    ft.app(main, assets_dir='assets')  # Run app with assets directory
