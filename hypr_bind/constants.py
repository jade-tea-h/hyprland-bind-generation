""""""

from enum import Enum, StrEnum


DEFAULT_SUBMAP: str = 'default'

FlagType = Enum('FlagType', ['LOCKED', 'RELEASE', 'REPEAT', 'MOUSE'])
Flags: dict[FlagTypes, str] = {
        FlagTypes.LOCKED: 'l',
        FlagTypes.RELEASE: 'r',
        FlagTypes.REPEAT: 'e',
        FlagTypes.MOUSE: 'm',
    }

ModKey = StrEnum('ModKey', ['SUPER', 'CTRL', 'ALT', 'SHIFT'])
ModKeyKeynames: dict[ModKey, tuple[str] | str] = {
        ModKey.SUPER: ('super_l'),
        ModKey.CTRL: ('control_l', 'control_r'),
        ModKey.ALT: ('alt_l', 'alt_r'),
        ModKey.SHIFT: ('shift_l', 'shift_r'),
    }
