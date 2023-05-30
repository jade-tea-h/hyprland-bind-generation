"""Module contains **Bind** class and enumerations for mod keys and bind flags"""

from typing import Iterable

from constants import ModKey, ModKeynames, FlagType, Flags
from dispatcher import Dispatcher


class Bind:
    """

    Attributes:
        mods: mod keys
        flags:
        key:
        dispatcher:
    """
    def __init__(
        self,
        mods: ModKey | Iterable[ModKey] = None,
        key: str = None,
        dispatcher: Dispatcher = None,
        flags: FlagType | Iterable[FlagType] = None,
    ) -> None:
        if type(mods) == ModKey:
            self.mods = tuple(self.mods)
        else:
            self.mods = mods

        if key is None:
            if 'r' not in flags:
                self.flags = 'r'
            if type(mods) is tuple[str]:
                self.key = ModKeyKeynames[mods][0]
            else:
                self.key = ModKeyKeynames[mods]
        else:
            self.key = key

        self.dispatcher = dispatcher

        for t in flags:
            self.flags += Flags[t]

    def __str__(self):
        string = "bind" + self.flags + '='

        for mod in self.mods:
            string += str(mod) + '_'
        string = string[:-1] + ', '

        string += self.key + ', '
        string += __str__(self.dispatcher)

        return string
