from docx import Document
import pandas as pd
from general_functions import get_splitter


if __name__ == "__main__":
    # Add your desire pdf file
    file_path = "/Users/akshay/Documents/Projects/Sai_work/all_data.txt"
    token_limit = 500
    with open(file_path, 'r') as file:
        text_content = file.read()

    text_splitter = get_splitter()

    text_splits = text_splitter([text_content])
    print("Part 4 Done")

    print(text_splits)
    for txt_s in text_splits:
        print(txt_s)
        print("------------------------------------------------------------------------------")