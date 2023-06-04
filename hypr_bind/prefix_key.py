""""""
from io import StringIO
from typing import Iterable, TypeAlias

from constants import FlagType, ModKey
from bind import Bind, exit_bind
from dispatcher import Dispatcher


class PrefixKey(Bind):
    """
    """
    _counter: int = 0
    BindType: TypeAlias = Bind | Self

    def __init__(
        self,
        mod_keys: ModKey | Iterable[ModKey] = None,
        key: str = None,
        flags: FlagType | Iterable[FlagType] = None,
        secondary_binds: Iterable[BindType] = None,
        secondary_bind_groups: Iterable[Iterable[BindType]] = None,
    ) -> None:
        self.name = "_prefix_" + str(_counter)
        _counter += 1
        dispatcher = Dispatcher('subremap', name)
        super().__init__(mods, key, dispatcher, flags)

        bind_list = list()
        for bind in secondary_binds:
            bind_list.append(bind)
        self.binds: set[list[BindType]] = [bind_list]

        for bind_group in secondary_bind_groups:
            bind_list = list()
            for bind in bind_group:
                bind_list.append(bind)
            self.binds.add(bind_list)

    def add_secondary_bind(bind: BindType) -> None:
        self.secondary_binds.add(list(bind))

    def add_secondary_bind_group(bind_group: Iterable[BindType]) -> None:
        bind_list = list()
        for bind in bind_group:
            bind_list.append(bind)
        self.secondary_binds.add(bind_list)

    def to_file(self, file: StringIO, nest_level: uint = 1) -> None:
        super().to_file(file)
        file.write("remap=" + self.name)
        for bind_group in self.binds:
            file.write('\n')
            for bind in bind_group:
                for _ in range(nest_level):
                    file.write('\t')
                if isinstance(bind, PrefixKey):
                    bind.to_file(file, nest_level+1)
                else:
                    bind.to_file(file)
                    for _ in range(nest_level):
                        file.write('\t')
                    exit_bind(bind).to_file(file)
        for _ in range(nest_level-1):
            file.write('\t')
        file.write("remap=" + DEFAULT_SUBMAP + '\n\n')

    def __str__(self) -> str:
        return ''
