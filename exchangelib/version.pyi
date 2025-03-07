from .errors import InvalidTypeError as InvalidTypeError, ResponseMessageError as ResponseMessageError, TransportError as TransportError
from .util import ANS as ANS, TNS as TNS, get_xml_attr as get_xml_attr, xml_to_str as xml_to_str
from _typeshed import Incomplete

log: Incomplete

class Build:
    major_version: Incomplete
    minor_version: Incomplete
    major_build: Incomplete
    minor_build: Incomplete
    def __init__(self, major_version, minor_version, major_build: int = 0, minor_build: int = 0) -> None: ...
    @classmethod
    def from_xml(cls, elem): ...
    def api_version(self): ...
    def __cmp__(self, other): ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

EXCHANGE_2007: Incomplete
EXCHANGE_2007_SP1: Incomplete
EXCHANGE_2007_SP2: Incomplete
EXCHANGE_2007_SP3: Incomplete
EXCHANGE_2010: Incomplete
EXCHANGE_2010_SP1: Incomplete
EXCHANGE_2010_SP2: Incomplete
EXCHANGE_2010_SP3: Incomplete
EXCHANGE_2013: Incomplete
EXCHANGE_2013_SP1: Incomplete
EXCHANGE_2015: Incomplete
EXCHANGE_2015_SP1: Incomplete
EXCHANGE_2016: Incomplete
EXCHANGE_2019: Incomplete
EXCHANGE_O365: Incomplete
VERSIONS: Incomplete

class Version:
    api_version: Incomplete
    build: Incomplete
    def __init__(self, build, api_version: Incomplete | None = None) -> None: ...
    @property
    def fullname(self): ...
    @classmethod
    def guess(cls, protocol, api_version_hint: Incomplete | None = None): ...
    @classmethod
    def from_soap_header(cls, requested_api_version, header): ...
    def copy(self): ...
    @classmethod
    def all_versions(cls): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class SupportedVersionClassMixIn:
    supported_from: Incomplete
    deprecated_from: Incomplete
    @classmethod
    def __new__(cls, *args, **kwargs): ...
    @classmethod
    def supports_version(cls, version): ...

class SupportedVersionInstanceMixIn:
    supported_from: Incomplete
    deprecated_from: Incomplete
    def __init__(self, supported_from: Incomplete | None = None, deprecated_from: Incomplete | None = None) -> None: ...
    def supports_version(self, version): ...
