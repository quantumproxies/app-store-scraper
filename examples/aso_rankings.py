"""Where does an app rank in App Store search for a list of keywords?

    python aso_rankings.py 1199070742 "podcast player" "podcast app" "podcasts" --country us

Searches the App Store for each keyword, finds the position of the app (by
numeric id or bundle id) in the first results and appends date, keyword,
position and the app ranked first to aso_rankings.csv. An empty position means
the app is not in the results read (--depth, up to 200).
"""

import argparse
import csv
import os
from datetime import datetime, timezone

from quanticdata_app_store_scraper import AppStoreScraper

FIELDS = ["checked_at", "country", "keyword", "app", "position", "first_app", "first_developer"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("app", help="numeric app id or bundle id of your app")
    parser.add_argument("keywords", nargs="+")
    parser.add_argument("--country", default="us")
    parser.add_argument("--depth", type=int, default=50, help="results to read per keyword (max 200)")
    parser.add_argument("--out", default="aso_rankings.csv")
    args = parser.parse_args()

    store = AppStoreScraper()
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    new_file = not os.path.exists(args.out)
    with open(args.out, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        for keyword in args.keywords:
            results = list(store.apps(keyword, country=args.country, max_results=args.depth))
            hit = next((a for a in results if args.app in (a.get("app_id"), a.get("bundle_id"))), None)
            first = results[0] if results else {}
            writer.writerow({"checked_at": checked_at, "country": args.country, "keyword": keyword,
                             "app": args.app, "position": hit["rank"] if hit else "",
                             "first_app": first.get("title"), "first_developer": first.get("developer")})
            print(f"{keyword!r}: {('#' + str(hit['rank'])) if hit else 'not in the first ' + str(len(results))}")


if __name__ == "__main__":
    main()
