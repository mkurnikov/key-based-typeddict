from typing import Dict, Type, TypeVar, Union

_T = TypeVar('_T')


class Key(object):
    def __init__(self, name: str, required: bool = False): ...

def KeyBasedTypedDict(typename: str,
                      fields: Dict[Union[str, Key], Type[_T]],
                      *,
                      total: bool = ...,
                      allow_extra: bool = ...) -> Type[dict]: ...
