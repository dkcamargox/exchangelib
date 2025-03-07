from .autodiscover import Autodiscovery as Autodiscovery
from .configuration import Configuration as Configuration
from .credentials import ACCESS_TYPES as ACCESS_TYPES, DELEGATE as DELEGATE, IMPERSONATION as IMPERSONATION
from .errors import InvalidEnumValue as InvalidEnumValue, InvalidTypeError as InvalidTypeError, ResponseMessageError as ResponseMessageError, UnknownTimeZone as UnknownTimeZone
from .ewsdatetime import EWSTimeZone as EWSTimeZone, UTC as UTC
from .fields import FieldPath as FieldPath, TextField as TextField
from .folders import AdminAuditLogs as AdminAuditLogs, ArchiveDeletedItems as ArchiveDeletedItems, ArchiveInbox as ArchiveInbox, ArchiveMsgFolderRoot as ArchiveMsgFolderRoot, ArchiveRecoverableItemsDeletions as ArchiveRecoverableItemsDeletions, ArchiveRecoverableItemsPurges as ArchiveRecoverableItemsPurges, ArchiveRecoverableItemsRoot as ArchiveRecoverableItemsRoot, ArchiveRecoverableItemsVersions as ArchiveRecoverableItemsVersions, ArchiveRoot as ArchiveRoot, Calendar as Calendar, Conflicts as Conflicts, Contacts as Contacts, ConversationHistory as ConversationHistory, DeletedItems as DeletedItems, Directory as Directory, Drafts as Drafts, Favorites as Favorites, Folder as Folder, IMContactList as IMContactList, Inbox as Inbox, Journal as Journal, JunkEmail as JunkEmail, LocalFailures as LocalFailures, MsgFolderRoot as MsgFolderRoot, MyContacts as MyContacts, Notes as Notes, Outbox as Outbox, PeopleConnect as PeopleConnect, PublicFoldersRoot as PublicFoldersRoot, QuickContacts as QuickContacts, RecipientCache as RecipientCache, RecoverableItemsDeletions as RecoverableItemsDeletions, RecoverableItemsPurges as RecoverableItemsPurges, RecoverableItemsRoot as RecoverableItemsRoot, RecoverableItemsVersions as RecoverableItemsVersions, Root as Root, SearchFolders as SearchFolders, SentItems as SentItems, ServerFailures as ServerFailures, SyncIssues as SyncIssues, Tasks as Tasks, ToDoSearch as ToDoSearch, VoiceMail as VoiceMail
from .folders.collections import PullSubscription as PullSubscription, PushSubscription as PushSubscription, StreamingSubscription as StreamingSubscription
from .items import ALL_OCCURRENCES as ALL_OCCURRENCES, AUTO_RESOLVE as AUTO_RESOLVE, HARD_DELETE as HARD_DELETE, ID_ONLY as ID_ONLY, SAVE_ONLY as SAVE_ONLY, SEND_TO_NONE as SEND_TO_NONE
from .properties import EWSElement as EWSElement, Mailbox as Mailbox, Rule as Rule, SendingAs as SendingAs
from .protocol import Protocol as Protocol
from .queryset import QuerySet as QuerySet
from .services import ArchiveItem as ArchiveItem, CopyItem as CopyItem, CreateInboxRule as CreateInboxRule, CreateItem as CreateItem, DeleteInboxRule as DeleteInboxRule, DeleteItem as DeleteItem, ExportItems as ExportItems, GetDelegate as GetDelegate, GetInboxRules as GetInboxRules, GetItem as GetItem, GetMailTips as GetMailTips, GetPersona as GetPersona, GetUserOofSettings as GetUserOofSettings, MarkAsJunk as MarkAsJunk, MoveItem as MoveItem, SendItem as SendItem, SetInboxRule as SetInboxRule, SetUserOofSettings as SetUserOofSettings, SubscribeToPull as SubscribeToPull, SubscribeToPush as SubscribeToPush, SubscribeToStreaming as SubscribeToStreaming, Unsubscribe as Unsubscribe, UpdateItem as UpdateItem, UploadItems as UploadItems
from .util import get_domain as get_domain, peek as peek
from _typeshed import Incomplete
from collections.abc import Generator

log: Incomplete

class Identity(EWSElement):
    ELEMENT_NAME: str
    sid: Incomplete
    upn: Incomplete
    smtp_address: Incomplete
    primary_smtp_address: Incomplete

class Account:
    fullname: Incomplete
    access_type: Incomplete
    locale: Incomplete
    default_timezone: Incomplete
    ad_response: Incomplete
    protocol: Incomplete
    identity: Incomplete
    affinity_cookie: Incomplete
    def __init__(self, primary_smtp_address, fullname: Incomplete | None = None, access_type: Incomplete | None = None, autodiscover: bool = False, credentials: Incomplete | None = None, config: Incomplete | None = None, locale: Incomplete | None = None, default_timezone: Incomplete | None = None) -> None: ...
    @property
    def primary_smtp_address(self): ...
    @property
    def version(self): ...
    @version.setter
    def version(self, value) -> None: ...
    def admin_audit_logs(self): ...
    def archive_deleted_items(self): ...
    def archive_inbox(self): ...
    def archive_msg_folder_root(self): ...
    def archive_recoverable_items_deletions(self): ...
    def archive_recoverable_items_purges(self): ...
    def archive_recoverable_items_root(self): ...
    def archive_recoverable_items_versions(self): ...
    def archive_root(self): ...
    def calendar(self): ...
    def conflicts(self): ...
    def contacts(self): ...
    def conversation_history(self): ...
    def directory(self): ...
    def drafts(self): ...
    def favorites(self): ...
    def im_contact_list(self): ...
    def inbox(self): ...
    def journal(self): ...
    def junk(self): ...
    def local_failures(self): ...
    def msg_folder_root(self): ...
    def my_contacts(self): ...
    def notes(self): ...
    def outbox(self): ...
    def people_connect(self): ...
    def public_folders_root(self): ...
    def quick_contacts(self): ...
    def recipient_cache(self): ...
    def recoverable_items_deletions(self): ...
    def recoverable_items_purges(self): ...
    def recoverable_items_root(self): ...
    def recoverable_items_versions(self): ...
    def root(self): ...
    def search_folders(self): ...
    def sent(self): ...
    def server_failures(self): ...
    def sync_issues(self): ...
    def tasks(self): ...
    def todo_search(self): ...
    def trash(self): ...
    def voice_mail(self): ...
    @property
    def domain(self): ...
    @property
    def oof_settings(self): ...
    @oof_settings.setter
    def oof_settings(self, value) -> None: ...
    def export(self, items, chunk_size: Incomplete | None = None): ...
    def upload(self, data, chunk_size: Incomplete | None = None): ...
    def bulk_create(self, folder, items, message_disposition=..., send_meeting_invitations=..., chunk_size: Incomplete | None = None): ...
    def bulk_update(self, items, conflict_resolution=..., message_disposition=..., send_meeting_invitations_or_cancellations=..., suppress_read_receipts: bool = True, chunk_size: Incomplete | None = None): ...
    def bulk_delete(self, ids, delete_type=..., send_meeting_cancellations=..., affected_task_occurrences=..., suppress_read_receipts: bool = True, chunk_size: Incomplete | None = None): ...
    def bulk_send(self, ids, save_copy: bool = True, copy_to_folder: Incomplete | None = None, chunk_size: Incomplete | None = None): ...
    def bulk_copy(self, ids, to_folder, chunk_size: Incomplete | None = None): ...
    def bulk_move(self, ids, to_folder, chunk_size: Incomplete | None = None): ...
    def bulk_archive(self, ids, to_folder, chunk_size: Incomplete | None = None): ...
    def bulk_mark_as_junk(self, ids, is_junk, move_item, chunk_size: Incomplete | None = None): ...
    def fetch(self, ids, folder: Incomplete | None = None, only_fields: Incomplete | None = None, chunk_size: Incomplete | None = None) -> Generator[Incomplete, Incomplete]: ...
    def fetch_personas(self, ids) -> Generator[Incomplete, Incomplete]: ...
    @property
    def mail_tips(self): ...
    @property
    def delegates(self): ...
    @property
    def rules(self): ...
    def create_rule(self, rule: Rule): ...
    def set_rule(self, rule: Rule): ...
    def delete_rule(self, rule: Rule): ...
    def subscribe_to_pull(self, event_types: Incomplete | None = None, watermark: Incomplete | None = None, timeout: int = 60): ...
    def subscribe_to_push(self, callback_url, event_types: Incomplete | None = None, watermark: Incomplete | None = None, status_frequency: int = 1): ...
    def subscribe_to_streaming(self, event_types: Incomplete | None = None): ...
    def pull_subscription(self, **kwargs): ...
    def push_subscription(self, **kwargs): ...
    def streaming_subscription(self, **kwargs): ...
    def unsubscribe(self, subscription_id): ...
