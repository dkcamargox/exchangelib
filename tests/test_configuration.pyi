from .common import TimedTestCase as TimedTestCase, get_random_string as get_random_string

class ConfigurationTest(TimedTestCase):
    def test_init(self) -> None: ...
    def test_magic(self) -> None: ...
    def test_hardcode_all(self, m) -> None: ...
    def test_fail_fast_back_off(self) -> None: ...
    def test_service_account_back_off(self) -> None: ...
