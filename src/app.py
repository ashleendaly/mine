from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer
from instance import totp_handler

class AuthenticatorCode(Static):
    def compose(self) -> ComposeResult:
        yield Static(f"{totp_handler.get_passcode()}")

class TerminalFA(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield AuthenticatorCode()
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = TerminalFA()
    app.run()