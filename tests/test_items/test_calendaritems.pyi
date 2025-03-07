from ..common import get_random_date as get_random_date, get_random_datetime_range as get_random_datetime_range, get_random_string as get_random_string
from .test_basics import CommonItemTest as CommonItemTest
from exchangelib.folders import Calendar
from exchangelib.items import CalendarItem

class CalendarTest(CommonItemTest):
    TEST_FOLDER: str
    FOLDER_CLASS = Calendar
    ITEM_CLASS = CalendarItem
    def match_cat(self, i): ...
    def test_cancel(self) -> None: ...
    def test_updating_timestamps(self) -> None: ...
    def test_update_to_non_utc_datetime(self) -> None: ...
    def test_all_day_datetimes(self) -> None: ...
    def test_view(self) -> None: ...
    def test_client_side_ordering_on_mixed_all_day_and_normal(self) -> None: ...
    def test_all_recurring_pattern_types(self) -> None: ...
    def test_recurring_item(self) -> None: ...
    def test_change_occurrence(self) -> None: ...
    def test_delete_occurrence(self) -> None: ...
    def test_change_occurrence_via_index(self) -> None: ...
    def test_delete_occurrence_via_index(self) -> None: ...
    def test_get_master_recurrence(self) -> None: ...
    def test_invalid_updateitem_items(self) -> None: ...
    def test_meeting_request(self) -> None: ...
    def test_clean(self) -> None: ...
    def test_tz_field_for_field_name(self) -> None: ...
