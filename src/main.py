from flet import WindowDragArea, Container, Page, app
from flet import Image, Text, Row, Icons
from flet import IconButton, Padding, Colors
from flet import MainAxisAlignment, CrossAxisAlignment

# Custom title bar class
class TitleBar(WindowDragArea):
    def __init__(self, actions: list | None = None):
        self.actions = actions
        self.icon = Image('icon.png', width=25, height=25)  # Icon for title bar
        self.title = Text("Flet")  # Title text
        # Container for icon, title, and actions
        self.bar = Container(
            Row([
                Row([self.icon, self.title], MainAxisAlignment.START),  # Left: Icon and title
                Row(self.actions, MainAxisAlignment.END)  # Right: Action buttons
            ], MainAxisAlignment.SPACE_BETWEEN, CrossAxisAlignment.CENTER),  # Layout
            bgcolor=Colors.BLUE,  # Background color
            padding=Padding(1, 1, 1, 1)  # Padding for the bar
        )
        super().__init__(content=self.bar)  # Initialize draggable area

# Main app logic
def main(page: Page):
    page.window.title_bar_buttons_hidden = True  # Hide default buttons
    page.window.title_bar_hidden = True  # Hide default title bar
    page.padding = 0  # Set page padding

    # Window action functions
    def minimize(e): page.window.minimized = not page.window.minimized; page.update()
    def maximize(e): page.window.maximized = not page.window.maximized; page.update()
    def close(e): page.window.destroy()

    # Add custom title bar
    title_bar = TitleBar([
        IconButton(Icons.REMOVE, on_click=minimize),
        IconButton(Icons.SQUARE_OUTLINED, on_click=maximize),
        IconButton(Icons.CLOSE, on_click=close)
    ])
    page.add(title_bar)  # Add to page
    page.update()  # Refresh page

# Start the app
if __name__ == '__main__':
    app(main, assets_dir='assets')  # Run app with assets directory
