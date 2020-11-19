import unittest

import wiki_upload_table as wiki


class Test(unittest.TestCase):
    def test_kentokai(self):
        # self.fail()
        start_day = "2020/11/19"
        skip_day = "2020/11/26"
        skip_dict = {skip_day: True}
        with open("./testdata/want1.txt", "r") as f:
            lines = f.readlines()
        compare_list = []
        for line in lines:
            compare_list.append(line.strip("\n"))
        self.assertEqual(wiki.kentokai(3, start_day, skip_dict), compare_list)


if __name__ == '__main__':
    unittest.main()