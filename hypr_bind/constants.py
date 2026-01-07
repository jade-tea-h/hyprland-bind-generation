""""""

from enum import Enum, IntEnum


DEFAULT_SUBMAP: str = 'default'

FlagType = Enum('FlagType', ['LOCKED', 'RELEASE', 'REPEAT', 'MOUSE'])
Flags: dict[FlagType, str] = {
        FlagType.LOCKED: 'l',
        FlagType.RELEASE: 'r',
        FlagType.REPEAT: 'e',
        FlagType.MOUSE: 'm',
    }


def _generate_combos(enum: IntEnum, index: int = 0) -> list[str]:
    combos: list[str] = list(enum[index].name)
    index += 1
    for mod_index in range(index, enum.SIZE):
        to_add = enum[mod_index].name
        for mod in combos:
            combos.append(mod + to_add)
        combos.append(to_add)
        combos += _generate_combos(enum, int)
    return combos


ModKeyType = IntEnum('ModKeyType', ['', 'SUPER', 'CTRL', 'ALT', 'SHIFT', 'SIZE'])
ModKeyCombos = _generate_combos(ModKeyType)
ModKeyKeynames: dict[ModKeyType, tuple[str] | str] = {
        ModKey.SUPER: ('super_l'),
        ModKey.CTRL: ('control_l', 'control_r'),
        ModKey.ALT: ('alt_l', 'alt_r'),
        ModKey.SHIFT: ('shift_l', 'shift_r'),
    }

KeyList = []
