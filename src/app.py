from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static, Label
from instance import totp_handler
from textual.reactive import reactive

class TOTPDisplay(Static):

    totp = reactive("")

    def on_mount(self) -> None:
        self.update_totp()

    def update_totp(self) -> None:
        self.totp = totp_handler.get_passcode()

    def watch_totp(self, totp: str) -> None:
            self.update(f"{totp}")


class Authenticator(Static):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        totp_display = self.query_one(TOTPDisplay)
        if button_id == "get-new-totp":
            totp_display.update_totp()


    def compose(self) -> ComposeResult:
        yield Label("GitHub")
        yield Button("Get New TOTP", id="get-new-totp", variant="success")
        yield TOTPDisplay()

class TerminalFA(App):
    """A Textual app to perform 2FA."""

    CSS_PATH = "terminal-fa.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(Authenticator())

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = TerminalFA()
    app.run()