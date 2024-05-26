from semantic_router.splitters import RollingWindowSplitter
from semantic_router.utils.logger import logger
from encoder import HuggingFaceEncoder


def convert_into_markdown(one_table):

    return one_table.to_markdown()
    

def get_splitter():
    logger.setLevel("WARNING")  # reduce logs from splitter

    splitter = RollingWindowSplitter(
        encoder=HuggingFaceEncoder(),
        dynamic_threshold=True,
        min_split_tokens=100,
        max_split_tokens=500,
        window_size=2,
        plot_splits=True,  # set this to true to visualize chunking
        enable_statistics=True  # to print chunking stats
    )

    return splitter


def table_to_chunks(table, token_limit):
    chunks = []
    table_lines = table.split("\n")
    header_row = table_lines[0]
    body_rows = table_lines[1:]
    current_tokens = len(header_row) / 4
    table_part = ""
    table_part += header_row + "\n"
    for row in body_rows:
        if current_tokens + len(row) / 4 < token_limit:
            chunks.append(table_part)
            table_part = ""
            current_tokens = 0
        table_part += row + "\n"
        current_tokens += len(row) / 4

    return chunks

