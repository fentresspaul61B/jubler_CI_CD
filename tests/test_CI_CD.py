from packaged_logic_for_CI_CD.main import func1, func2, JublerDataProcessor, TEST_TEXT_FILE

import unittest  # Native module used for testing.

print(JublerDataProcessor().load(TEST_TEXT_FILE).shape)


class TestMyFunction(unittest.TestCase):
    def test_func1(self):
        """Test for func1."""
        self.assertEqual(func1(2), 4)

    def test_func2(self):
        """Test for func2."""
        self.assertEqual(func2(2), 4)

    def test_load_1(self):
        """Tests if correct data frame is created by checking shape, and if the file exists."""
        # Testing for the correct shape.
        pipeline = JublerDataProcessor()
        test_df = pipeline.load(TEST_TEXT_FILE)
        self.assertIsNotNone(test_df)
        self.assertEqual(test_df.shape, (101, 3))

        # Testing for the correct columns.
        test_df_columns = str(test_df.columns)
        correct_columns = "Index(['start', 'stop', 'label'], dtype='object')"
        self.assertEqual(test_df_columns, correct_columns)


def main():
    # test_df = JublerDataProcessor().load(TEST_TEXT_FILE)
    # print(test_df.shape)
    # print(type(test_df))
    pass


if __name__ == '__main__':
    main()
