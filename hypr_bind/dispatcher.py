"""Module contains **Dispatcher** class as wrapper for Hyprland/hyprctl dispatcher"""


class Dispatcher:
    """

    Attributes:
        name: dispatcher to be run
        params: parameters accepted by the dispatcher
    """
    def __init__(self, name: str, params: tuple[str] | str = None) -> None:
        self.name = name
        self.params = params
        if type(self.params) == str:
            self.params = tuple(self.params)

    def execute(self) -> int:
        string = '/usr/bin/hyprctl ' + self.name + ' '
        for param in self.params:
            string += param + ', '
        string = string[:-2]

    def __str__(self) -> str:
        string = self.name + ','
        if self.params is not None:
            string += ' '
            for param in self.params:
                string += param + ', '
            string = string[:-2]
        return string
