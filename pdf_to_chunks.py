from PyPDF2 import PdfReader
import tabula
import pandas as pd
# import camelot
from tabula.io import read_pdf
from general_functions import table_to_chunks, get_splitter, convert_into_markdown


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


# Read PDF and extract tables
def get_tables(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    # tables = tabula.read_pdf(pdf_path, guess=True, multiple_tables= True, stream=True)

    # # Convert each table to pandas dataframe
    dfs = []
    for table in tables:
        df = pd.DataFrame(table)
        dfs.append(df)

    return dfs

    # for i, table in enumerate(tables):
    #     print(f"Table {i}:")
    #     print(table.df)

    # # Convert the extracted tables to DataFrames and store them in a list
    # dataframes = [table.df for table in tables]

    # # If you want to combine all tables into a single DataFrame
    # all_tables_df = pd.concat(dataframes, ignore_index=True)

    # return all_tables_df


# text_content = extract_text_from_pdf(pdf_path)
# splits = splitter([text_content])
# chunks = table_to_chunks(markdown_table, token_limit)
# all_splits = splits + chunks

if __name__ == "__main__":
    # Add your desire pdf file
    pdf_path = "/Users/akshay/Documents/Projects/Sai_work/NIPS-2017-attention-is-all-you-need-Paper.pdf"
    text_content = extract_text_from_pdf(pdf_path)
    token_limit = 500
    print(text_content)
    print("Part 1 Done")
    all_tables = get_tables(pdf_path)
    chunks = []
    print("Part 2 Done")

    for table in all_tables:
        markdown_table = convert_into_markdown(table)
        table_chunks = table_to_chunks(markdown_table, token_limit)

        chunks = chunks + table_chunks

    print("Part 3 Done")
    text_splitter = get_splitter()

    text_splits = text_splitter([text_content])
    print("Part 4 Done")

    all_chunks = text_splits + chunks
    print("Part 5 Done")

    print(all_chunks)