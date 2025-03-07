from .common import EWSTest as EWSTest, get_random_string as get_random_string, mock_account as mock_account, mock_protocol as mock_protocol, mock_version as mock_version

class ServicesTest(EWSTest):
    def test_invalid_server_version(self) -> None: ...
    def test_inner_error_parsing(self) -> None: ...
    def test_invalid_value_extras(self) -> None: ...
    def test_error_server_busy(self) -> None: ...
    def test_error_schema_validation(self) -> None: ...
    def test_error_too_many_objects_opened(self, m) -> None: ...
    def test_soap_error(self) -> None: ...
    def test_element_container(self) -> None: ...
    def test_get_elements(self) -> None: ...
    def test_handle_backoff(self) -> None: ...
    def test_exceeded_connection_count(self) -> None: ...
    def test_invalid_soap_response(self, m) -> None: ...
    def test_version_renegotiate(self) -> None: ...
    def test_wrap(self) -> None: ...
