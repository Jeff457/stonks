import argparse
import os
import pendulum
import re

from collections import Counter, defaultdict
from psaw import PushshiftAPI

from stonks.utils import Trie


TICKER_RE = re.compile("(\d+)\s?(p|put|puts|c|call|calls)", re.IGNORECASE)
TIMEZONE = "UTC"
# TODO: shouldn't do this if the script will be on a schedule or run on a server
START = pendulum.yesterday(tz=TIMEZONE).int_timestamp
END = pendulum.today(tz=TIMEZONE).int_timestamp
# TODO: one option is to wite a script that will retrieve all stock symbols & cache
# TODO: another option is to search for 'context' markers, like PUT or CALL + a date
TICKERS = {"spy", "aapl", "msft", "tsla"}
# TODO: are these the right set of flairs?
WHITELIST = {"Stocks", "Options", "Futures", "DD"}

api = PushshiftAPI()


def top_ticker(subreddit: str, limit: int = 1) -> tuple:
    top = Counter()
    trie = Trie(TICKERS)

    for submission in api.search_submissions(
        after=START, before=END, subreddit=subreddit, q="p|put|puts|c|call|calls"
    ):
        try:
            # submission objects in psaw do not have a consistent schema
            flair = submission.link_flair_text
        except (AttributeError,):
            # err on the side of still wanting to inspect the submission
            flair = "Stocks"

        if flair in WHITELIST:
            match = TICKER_RE.search(submission.selftext) or TICKER_RE.search(
                submission.title
            )
            if match:
                ticker = trie.search(submission.selftext.lower()) or trie.search(
                    submission.title.lower()
                )
                if ticker is not None:
                    top[ticker] += 1

    return top.most_common(limit)[0]


def top_ticker_using_symbols(subreddit: str, limit: int = 1) -> tuple:
    top = Counter()

    for ticker in TICKERS:
        results = next(
            api.search_submissions(
                after=START,
                before=END,
                subreddit=subreddit,
                q=ticker,
                aggs=["subreddit"],
            )
        )
        top[ticker] = results["subreddit"][0]["doc_count"]

    return top.most_common(limit)[0]


def parse_args():
    parser = argparse.ArgumentParser(
        "Count how many times a phrase is mentioned in a subreddit"
    )
    parser.add_argument(
        "subreddit",
        type=str,
        help="the subreddit(s) to check",
        nargs="*",
        default=["WallStreetBets"],
    )

    return parser.parse_args()


def main():
    args = parse_args()
    subreddits = ", ".join(args.subreddit)

    stock, count = top_ticker_using_symbols(subreddits)

    print(
        f"The phrase '{stock.upper()}' was mentioned "
        f"{count} times today in {subreddits}"
    )


if __name__ == "__main__":
    main()
