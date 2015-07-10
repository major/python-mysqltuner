from mysqltuner import utils

class TestUtils(object):

    def test_get_ram(self):
        ram = utils.get_ram()
        assert ram > 0

    # Note: On some platforms (especially travis-ci), swap isn't configured
    # and psutil returns it as zero bytes.
    def test_get_swap(self):
        swap = utils.get_swap()
        assert swap => 0

    def test_get_uptime(self):
        uptime = utils.get_uptime()
        assert uptime > 0
