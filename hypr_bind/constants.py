""""""

from enum import Enum, StrEnum


class Constants:
    DEFAULT_SUBMAP = 'default'

    ModKey = StrEnum('ModKey', ['SUPER', 'CTRL', 'ALT', 'SHIFT'])
    ModKeyKeynames: dict[ModKey,tuple[str]|str] = {
            ModKey.SUPER: ,
            ModKey.CTRL: ,
            ModKey.ALT: ('Alt_L', 'Alt_R'),
            ModKey.SHIFT: ,
        }

    FlagType = Enum('FlagType', ['LOCKED', 'RELEASE', 'REPEAT', 'MOUSE'])
    Flags: dict[FlagTypes, str] = {
            FlagTypes.LOCKED: 'l',
            FlagTypes.RELEASE: 'r',
            FlagTypes.REPEAT: 'e',
            FlagTypes.MOUSE: 'm',
        }
