""""""
from io import StringIO
from typing import Iterable

from constants import DEFAULT_SUBMAP
from bind import Bind
from prefix_key import PrefixKey


class Mode:
    """

    Attributes:
        name: name of subremap
        entrance_binds: binds to enter the subremap
        submap_binds: binds in the subremap
        exit_binds: binds to exit the subremap
    """

    def __init__(
        self,
        mode_name: str,
        entrance_binds: Iterable[Bind],
        submap_binds: Iterable[Bind],
        exit_binds: Iterable[Bind],
    ) -> None:
        self.name: str = mode_name
        self.entrance_binds: set[Bind] = set()
        self.submap_binds: set[Bind] = set()
        self.exit_binds: set[Bind] = set()

        disp = Dispatcher("submap", self.name)
        for bind in entrance_binds:
            bind.dispatcher = disp
            self.entrance_binds.add(bind)

        for bind in submap_binds:
            self.submap_binds.add(bind)

        disp = Dispatcher("subremap", DEFAULT_SUBMAP)
        for bind in exit_binds:
            bind.dispatcher = disp
            self.exit_binds.add(bind)

    def add_bind(self, bind: Bind) -> None:
        self.submap_binds.add(bind)

    def add_binds(self, binds: Iterable[Bind]) -> None:
        for bind in binds:
            self.submap_binds.add(bind)

    def add_entrance_bind(self, bind: Bind) -> None:
        self.entrance_binds.add(bind)

    def add_entrance_binds(self, binds: Iterable[Bind]) -> None:
        for bind in binds:
            self.entrance_submap_binds.add(bind)

    def add_exit_bind(self, bind: Bind) -> None:
        self.exit_binds.add(bind)

    def add_exit_binds(self, binds: Iterable[Bind]) -> None:
        for bind in binds:
            self.exit_binds.add(bind)

    def to_file(self, file: StringIO) -> bool:
        for bind in self.entrance_binds:
            bind.to_file(file)
        file.write("submap=" + self.name + '\n')

        for bind in self.submap_binds:
            file.write('\t')
            bind.to_file(file)

        file.write('\n\n')

        for bind in self.exit_binds:
            file.write('\t')
            bind.to_file(file)

        file.write("submap=" + DEFAULT_SUBMAP + '\n\n')

    def __str__(self) -> str:
        string = ''
        for bind in self.entrance_binds:
            string += __str__(bind) + '\n'

        string += "submap=" + self.name + '\n'

        for bind in self.submap_binds:
            string += '\t' + __str__(bind) + '\n'
        string += '\n'

        for bind in self.exit_binds:
            string += '\t' + __str__(bind) + '\n'

        return string
