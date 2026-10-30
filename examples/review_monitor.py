"""Keep a growing CSV of App Store reviews for a list of apps.

    python review_monitor.py 310633997 324684580 --country us --per-app 100

Reads the newest reviews of each app (numeric id or store URL) and appends to
app_reviews.csv only the reviews not stored yet, matched by review id. Run it
daily from cron and the file becomes the full review history of your apps:

    0 6 * * *  cd /path/to/here && python review_monitor.py 310633997 --country us

Needs a login (`app-store-scraper login`) or QUANTICDATA_API_KEY in the environment.
"""

import argparse
import csv
import os

from quanticdata_app_store_scraper import AppStoreScraper

FIELDS = ["app_id", "country", "review_id", "updated_at", "rating", "app_version", "title", "text",
          "author", "votes_helpful", "votes_total", "developer_response", "developer_response_at", "source"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("apps", nargs="+", help="App Store ids or store URLs")
    parser.add_argument("--country", default="us")
    parser.add_argument("--per-app", type=int, default=100, help="newest reviews to read per app (max 500)")
    parser.add_argument("--out", default="app_reviews.csv")
    args = parser.parse_args()

    seen = set()
    if os.path.exists(args.out):
        with open(args.out, newline="", encoding="utf-8") as fh:
            seen = {r["review_id"] for r in csv.DictReader(fh)}

    store = AppStoreScraper()
    new_file = not os.path.exists(args.out)
    added = 0
    with open(args.out, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        if new_file:
            writer.writeheader()
        for app in args.apps:
            run = store.reviews(app, country=args.country, max_results=args.per_app)
            fresh = [r for r in run if r.get("review_id") and r["review_id"] not in seen]
            for r in fresh:
                writer.writerow(r)
                seen.add(r["review_id"])
            low = sum(1 for r in fresh if (r.get("rating") or 5) <= 2)
            added += len(fresh)
            print(f"{app}: {len(run)} read, {len(fresh)} new, {low} of them with 1 or 2 stars")
    print(f"{added} new reviews appended to {args.out}")


if __name__ == "__main__":
    main()
