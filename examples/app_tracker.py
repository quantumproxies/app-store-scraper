"""Track App Store apps over time: rating, review count, version, price.

    python app_tracker.py --apps apps.txt --country us

Reads app ids, bundle ids or store URLs from apps.txt (one per line), fetches
their store record and appends one row per app to app_history.csv with a UTC
timestamp, the change in rating count since the last check and the current
version and its release date. Run it from cron to see releases and rating
trends of your apps and the ones you compete with.
"""

import argparse
import csv
import os
from datetime import datetime, timezone

from quanticdata_app_store_scraper import AppStoreScraper

FIELDS = ["checked_at", "app_id", "bundle_id", "title", "developer", "rating", "reviews", "new_ratings",
          "rating_current_version", "version", "updated_at", "price", "currency", "size_bytes"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apps", default="apps.txt", help="file with one app id, bundle id or URL per line")
    parser.add_argument("--country", default="us")
    parser.add_argument("--out", default="app_history.csv")
    args = parser.parse_args()

    with open(args.apps, encoding="utf-8") as fh:
        apps = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

    last = {}
    if os.path.exists(args.out):
        with open(args.out, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                last[r["app_id"]] = r

    store = AppStoreScraper()
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    new_file = not os.path.exists(args.out)
    with open(args.out, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        if new_file:
            writer.writeheader()
        # One run delivers up to 200 apps.
        for i in range(0, len(apps), 200):
            for app in store.apps(app_ids=apps[i:i + 200], country=args.country, max_results=200):
                before = last.get(app["app_id"], {}).get("reviews")
                new = app["reviews"] - int(before) if before and app.get("reviews") is not None else ""
                writer.writerow({"checked_at": checked_at, "new_ratings": new, **app})
                print(f"{app['title']}: {app.get('rating')} from {app.get('reviews')} ratings, version {app.get('version')}")


if __name__ == "__main__":
    main()
