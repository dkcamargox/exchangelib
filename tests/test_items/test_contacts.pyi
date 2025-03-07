from ..common import get_random_email as get_random_email, get_random_string as get_random_string
from .test_basics import CommonItemTest as CommonItemTest
from exchangelib.folders import Contacts
from exchangelib.items import Contact

class ContactsTest(CommonItemTest):
    TEST_FOLDER: str
    FOLDER_CLASS = Contacts
    ITEM_CLASS = Contact
    def test_order_by_on_indexed_field(self) -> None: ...
    def test_order_by_failure(self) -> None: ...
    def test_update_on_single_field_indexed_field(self) -> None: ...
    def test_update_on_multi_field_indexed_field(self) -> None: ...
    def test_distribution_lists(self) -> None: ...
    def test_fetch_personas(self) -> None: ...
    def test_find_people(self) -> None: ...
    def test_get_persona(self) -> None: ...
    def test_get_persona_failure(self) -> None: ...
