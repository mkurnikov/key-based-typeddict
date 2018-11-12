import dataclasses
from typing import Mapping, Union, Type, Any


@dataclasses.dataclass(eq=True, frozen=True)
class Key(object):
    name: str
    required: bool = True


@dataclasses.dataclass(eq=True, frozen=True)
class KeyBasedTypedDict(object):
    name: str
    attrs: Mapping[Union[str, Key], Type[Any]]
    allow_extra: bool = False
