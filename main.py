#!/usr/bin/env python
import argparse
import wikiquote

parser = argparse.ArgumentParser(
    prog="quotecache",
    description="generate a cache of quotes. Could be used for a daily quote in your .bashrc or whatever. Outputs to a file called '.quotecache', so you may need to use 'ls -a' to find it.",
)

parser.add_argument(
    "search",
    type=str,
    help="the search string. perhaps an author name ('Charles Dickens') or a movie title ('Fight Club')",
)

parser.add_argument(
    "--lang",
    "-l",
    default="en",
    type=str,
    help=f"(default: en) narrow results to one of the supported languages: {', '.join(wikiquote.supported_languages())}",
)


def main():
    args = parser.parse_args()
    if args.lang not in wikiquote.supported_languages():
        raise ValueError(f"Unsupported language {args.lang}")
    try:
        results = wikiquote.quotes(args.search, lang=args.lang)
    except wikiquote.utils.NoSuchPageException:
        print("No results found for serach string: ", args.search)
        return
    if len(results) == 0:
        print("No results found for serach string: ", args.search)
        return
    with open(".quotecache", "w") as f:
        f.write("\n".join(results))


if __name__ == "__main__":
    main()
