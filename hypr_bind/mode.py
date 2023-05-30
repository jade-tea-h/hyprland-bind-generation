""""""

from typing import Iterable

from constants import DEFAULT_SUBMAP
from bind import Bind


class Mode:
    """

    Attributes:
        bind:
    """
    def __init__(
        self,
        mode_name: str,
        entrance_binds: Iterable[Bind],
        submap_binds: Iterable[Bind],
        exit_binds: Iterable[Bind],
    ) -> None:
        """

        Arguments:
        """
        self.name = mode_name

        self.primary_binds = primary_binds
        disp = Dispatcher('subremap', self.name)
        for bind in self.primary_binds:
            bind.dispatcher = disp

        self.submap_binds = submap_binds

        self.exit_binds = exit_binds
        disp = Dispatcher('subremap', DEFAULT_SUBMAP)
        for bind in self.exit_binds:
            bind.dispatcher = disp

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
