from mysqltuner import mysqltuner


class TestMysqlTuner(object):

    def test_inits(self):
        mtuner = mysqltuner.MysqlTuner()
        assert mtuner is not None
