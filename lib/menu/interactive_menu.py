import os
import msvcrt


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class MenuSystem:
    def __init__(self, menus, start_menu):
        self.menus = menus
        self.context = {}
        self.stack = []
        self.current_menu = start_menu

    def run(self):
        while True:
            result = self._run_menu(self.current_menu)
            if result == "back":
                if self.stack:
                    prev, ctx_key = self.stack.pop()
                    if ctx_key:
                        self.context.pop(ctx_key, None)
                    self.current_menu = prev
            elif result == "quit":
                break
            elif isinstance(result, tuple):
                next_menu, context_key = result
                self.stack.append((self.current_menu, context_key))
                self.current_menu = next_menu

    def _run_menu(self, menu_id):
        menu = self.menus[menu_id]
        title = menu["title"](self.context) if callable(menu["title"]) else menu["title"]
        options = menu["options"](self.context) if callable(menu["options"]) else menu["options"]
        handler = menu["handler"]

        idx = 0
        while True:
            clear_screen()
            print(title)
            for i, option in enumerate(options):
                prefix = ">" if i == idx else "  "
                print(f"{prefix} {option}")
            print("\n↑↓ = move, →/Enter = select, ← = back, q = quit")

            key = msvcrt.getch()
            if key == b'\xe0':
                arrow = msvcrt.getch()
                if arrow == b'H':  # up
                    idx = (idx - 1) % len(options)
                elif arrow == b'P':  # down
                    idx = (idx + 1) % len(options)
                elif arrow == b'M':  # right
                    return handler(self.context, options[idx])
                elif arrow == b'K':  # left
                    return "back"
            elif key == b'\r':
                return handler(self.context, options[idx])
            elif key == b'q':
                return "quit"