import unittest
import numpy as np
from gazekit.aoi import *
from gazekit.gaze_seq import *


class TestReadAOIIniFile(unittest.TestCase):
    def test_read_aoi_ini_file(self):
        # 测试正常情况
        aois = read_aoi_ini_file('aoi.ini')
        self.assertEqual(len(aois), 3)
        self.assertEqual(aois[0].name, 'AOI1')
        self.assertEqual(aois[0].x, 100)
        self.assertEqual(aois[0].y, 50)
        self.assertEqual(aois[0].w, 200)
        self.assertEqual(aois[0].h, 100)
        self.assertEqual(aois[0].function, ['click', 'hover'])

        with self.assertRaises(FileNotFoundError):
            read_aoi_ini_file('nonexistent.ini')


class TestSequence(unittest.TestCase):
    def test_init(self):
        # 创建测试数据
        x = [0.1, 0.2, 0.3, 0.4]
        y = [0.5, 0.6, 0.7, 0.8]
        t = [1000, 2000, 3000, 4000]

        # 初始化Sequence对象
        seq = Sequence(x, y, t)

        # 检查结果是否正确
        expected_data = pd.DataFrame({
            'x': [0.1, 0.2, 0.3, 0.4],
            'y': [0.5, 0.6, 0.7, 0.8],
            'raw_t': [1000, 2000, 3000, 4000],
            'rel_t': [0, 1000, 2000, 3000]
        })
        pd.testing.assert_frame_equal(seq.data, expected_data)


if __name__ == '__main__':
    unittest.main()