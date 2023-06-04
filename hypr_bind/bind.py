"""Module contains **Bind** class and enumerations for mod keys and bind flags"""
from io import StringIO
from typing import Iterable

from constants import ModKey, FlagType, Flags, DEFAULT_SUBMAP
from dispatcher import Dispatcher


class Bind:
    """Key attached to a dispatcher action

    Attributes:
        mods: mod keys
        flags:
        key:
        dispatcher:
    """

    def __init__(
        self,
        mod_keys: ModKey | Iterable[ModKey] = None,
        key: str = None,
        dispatcher: Dispatcher | Iterable[ModKey] = None,
        flags: FlagType | Iterable[FlagType] = None,
    ) -> None:
        if type(mods) == ModKey:
            self.mods = tuple(self.mods)
        else:
            self.mods = mods

        if key is None:
            if 'r' not in flags:
                self.flags = 'r'
            self.key = ModKeyKeynames[mods][0]
        else:
            self.key = key

        self.dispatcher = dispatcher

        for t in flags:
            self.flags += Flags[t]

    def to_file(self, file: StringIO) -> None:
        file.write(self.__str__() + '\n')

    def __str__(self):
        string = "bind" + self.flags + '='

        for mod in self.mods:
            string += str(mod) + '_'
        string = string[:-1] + ', '

        string += self.key + ', '
        string += __str__(self.dispatcher)

        return string


def exit_bind(bind: Bind):
    return Bind(self.mods, self.key, Dispatcher("submap", DEFAULT_SUBMAP))
