from textual.app import App, ComposeResult
from textual.widgets import Static


class MyTOTP(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Static("Hello")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = MyTOTP()
    app.run()