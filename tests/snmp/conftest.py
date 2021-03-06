import pytest
from tests.common.utilities import wait_until

@pytest.fixture(scope="module", autouse=True)
def setup_check_snmp_ready(duthosts, rand_one_dut_hostname):
    duthost = duthosts[rand_one_dut_hostname]
    assert wait_until(300, 20, duthost.is_service_fully_started, "snmp"), "SNMP service is not running"
