from mysqltuner import utils

class TestUtils(object):

    def test_get_ram(self):
        ram = utils.get_ram()
        assert ram > 0
