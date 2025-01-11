import flet as ft

# Custom Title Bar Control
class TitleBar(ft.WindowDragArea):
    def __init__(self, actions: list | None = None):
        self.actions = actions
        self.icon = ft.Image('icon.png', width=25, height=25)  # Icon for the title bar
        self.title = ft.Text("Flet")  # Title text
        self.bar = ft.Container(
            ft.Row([
                ft.Row([self.icon, self.title], ft.MainAxisAlignment.START),  # Left section: Icon and title
                ft.Row(self.actions, ft.MainAxisAlignment.END)  # Right section: Action buttons
            ], ft.MainAxisAlignment.SPACE_BETWEEN, ft.CrossAxisAlignment.CENTER)  # Layout adjustments
        )
        super().__init__(content=self.bar)  # Initialize the draggable area with the custom bar

# Main application logic
def main(page: ft.Page):
    # Window configuration
    page.window.title_bar_buttons_hidden = True  # Hide default title bar buttons
    page.window.title_bar_hidden = True  # Hide the default title bar entirely
    page.padding = 2  # Optional padding for the page content

    # Functions for window actions
    def minimize(e):
        """Toggle window minimized state."""
        page.window.minimized = not page.window.minimized
        page.update()

    def maximize(e):
        """Toggle window maximized state."""
        page.window.maximized = not page.window.maximized
        page.update()

    def close(e):
        """Close the application window."""
        page.window.destroy()

    # Add the custom title bar
    title_bar = TitleBar([
        ft.IconButton(ft.Icons.REMOVE, on_click=minimize),  # Minimize button
        ft.IconButton(ft.Icons.SQUARE_OUTLINED, on_click=maximize),  # Maximize/restore button
        ft.IconButton(ft.Icons.CLOSE, on_click=close)  # Close button
    ])
    page.add(title_bar)  # Add the title bar to the page
    page.update()  # Update the page to reflect changes

# Entry point for the application
if __name__ == '__main__':
    ft.app(main, assets_dir='assets')  # Run the application with the specified assets directory
