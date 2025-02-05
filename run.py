import os
if __name__ == "__main__":
    # os.system("poetry run python src/main.py --ticker 002230 --show-reasoning")
    os.system("poetry run python src/backtester.py --ticker 603568 --start-date 2024-12-11 --end-date 2025-02-04 --num-of-news 20")