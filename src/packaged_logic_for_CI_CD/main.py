import pandas as pd  # Used to store file paths for videos, audio, and images.
import os  # Used to create, iterate over, and delete files.
import re  # Used to extract start, stop, and labels from .txt file.
from typing import Tuple, List, Any


TEST_TEXT_FILE = "cat_dog_subtitles.txt"  # Used to test Jubler data functions.


def func1(num: float) -> float:
    """Multiply the num by 2."""
    return num * 2


def func2(num: float) -> float:
    """Square the num."""
    return num ** 2


class JublerDataProcessor:
    def __init__(self, num_processes=2):
        self.num_processes = num_processes  # Defined for multi processing.
        pass

    @staticmethod
    def load(text_file: str) -> pd.DataFrame:
        """
        Loads in Jubler .txt file and creates a pandas dataframe from it.
        Args:
            text_file: The .txt file path to be transformed into
            pandas data frame.
        Returns:
            df: the created dataframe with start, stop, and label as columns.
        """

        # Regex used to extract the start and stop times from string in .txt file.
        time_regex = r"(\b[0-9]+\b)"

        # Regex used to extract the label from string in .txt file.
        label_regex = r"[a-zA-Z]+"
        if not os.path.exists(text_file):
            return pd.DataFrame()

        # Load the .txt data into pandas dataframe.
        df = pd.read_csv(text_file, header=None)

        # Define simple data cleaning functions that are applied to jubler df.
        def extract_time(input_str: str) -> Tuple[Any, ...]:
            return tuple(re.findall(time_regex, input_str))

        def convert_string_to_int(input_str: str) -> float:
            return int(input_str)

        def extract_label(input_str: str) -> List[Any]:
            return re.findall(label_regex, input_str)

        def clean_labels(input_str: str) -> str:
            return input_str[0] if len(input_str) else "skip"

        # Extracting time using regex.
        df["start"], df["stop"] = zip(*df[0].apply(extract_time))

        # Converting start string to int and dividing by 10 to convert MPL2 to seconds.
        df["start"] = df["start"].apply(convert_string_to_int) / 10

        # Converting stop string to int and dividing by 10 to convert MPL2 to seconds.
        df["stop"] = df["stop"].apply(convert_string_to_int) / 10

        # Extracting labels using regex.
        df["label"] = df[0].apply(extract_label)

        # Replacing empty instances with "skip" label.
        df["label"] = df["label"].apply(clean_labels)

        # Drop unneeded column.
        df = df.drop([0], axis=1)

        # Return jubler df.
        return df


def main():
    # test_df = JublerDataProcessor().load(TEST_TEXT_FILE)
    # print(test_df.shape)
    # print(type(test_df))
    pass


if __name__ == '__main__':
    main()
