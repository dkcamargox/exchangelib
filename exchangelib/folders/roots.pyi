from ..errors import ErrorAccessDenied as ErrorAccessDenied, ErrorFolderNotFound as ErrorFolderNotFound, ErrorInvalidOperation as ErrorInvalidOperation
from ..fields import EffectiveRightsField as EffectiveRightsField
from ..properties import DistinguishedFolderId as DistinguishedFolderId, EWSMeta as EWSMeta, Mailbox as Mailbox
from ..version import EXCHANGE_2007_SP1 as EXCHANGE_2007_SP1, EXCHANGE_2010_SP1 as EXCHANGE_2010_SP1
from .base import BaseFolder as BaseFolder
from .collections import FolderCollection as FolderCollection
from .known_folders import MISC_FOLDERS as MISC_FOLDERS, MsgFolderRoot as MsgFolderRoot, NON_DELETABLE_FOLDERS as NON_DELETABLE_FOLDERS, WELLKNOWN_FOLDERS_IN_ARCHIVE_ROOT as WELLKNOWN_FOLDERS_IN_ARCHIVE_ROOT, WELLKNOWN_FOLDERS_IN_ROOT as WELLKNOWN_FOLDERS_IN_ROOT
from .queryset import MISSING_FOLDER_ERRORS as MISSING_FOLDER_ERRORS, SHALLOW as SHALLOW, SingleFolderQuerySet as SingleFolderQuerySet
from _typeshed import Incomplete
from collections.abc import Generator

log: Incomplete

class RootOfHierarchy(BaseFolder, metaclass=EWSMeta):
    WELLKNOWN_FOLDERS: Incomplete
    effective_rights: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @property
    def account(self): ...
    @property
    def root(self): ...
    @property
    def parent(self) -> None: ...
    @classmethod
    def register(cls, *args, **kwargs): ...
    @classmethod
    def deregister(cls, *args, **kwargs): ...
    def get_folder(self, folder): ...
    def add_folder(self, folder) -> None: ...
    def update_folder(self, folder) -> None: ...
    def remove_folder(self, folder) -> None: ...
    def clear_cache(self) -> None: ...
    def get_children(self, folder) -> Generator[Incomplete]: ...
    def get_default_folder(self, folder_cls): ...
    @classmethod
    def get_distinguished(cls, account): ...
    @classmethod
    def from_xml(cls, elem, account): ...
    @classmethod
    def folder_cls_from_folder_name(cls, folder_name, folder_class, locale): ...

class Root(RootOfHierarchy):
    DISTINGUISHED_FOLDER_ID: str
    WELLKNOWN_FOLDERS = WELLKNOWN_FOLDERS_IN_ROOT
    @property
    def tois(self): ...
    def get_default_folder(self, folder_cls): ...

class PublicFoldersRoot(RootOfHierarchy):
    DISTINGUISHED_FOLDER_ID: str
    DEFAULT_FOLDER_TRAVERSAL_DEPTH = SHALLOW
    supported_from = EXCHANGE_2007_SP1
    def __init__(self, **kwargs) -> None: ...
    def get_children(self, folder) -> Generator[Incomplete, Incomplete]: ...

class ArchiveRoot(RootOfHierarchy):
    DISTINGUISHED_FOLDER_ID: str
    supported_from = EXCHANGE_2010_SP1
    WELLKNOWN_FOLDERS = WELLKNOWN_FOLDERS_IN_ARCHIVE_ROOT
