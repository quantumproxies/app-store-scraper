# App Store Scraper

[![ci](https://github.com/quantumproxies/app-store-scraper/actions/workflows/ci.yml/badge.svg)](https://github.com/quantumproxies/app-store-scraper/actions/workflows/ci.yml) ![python](https://img.shields.io/badge/python-3.9%2B-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

Scrape the Apple App Store from Python or the command line: apps by search term or by app id with rating, review count, price, version, size, release notes and developer; the customer reviews of any app, with rating, title, text, app version and date; and Apple's catalog search for apps, podcasts, music, movies and books, as JSON or CSV. The code is free and open source (MIT). It runs on the QuanticData Data API, so there are no proxies to rotate and no developer account to set up: sign in once and run a command.

```bash
pip install git+https://github.com/quantumproxies/app-store-scraper
app-store-scraper login
app-store-scraper apps "podcast player" --country us --max-results 50 -o podcast_apps.csv
```

`login` opens the QuanticData sign-in page in your browser. New accounts get $2 of free usage every month, no card required: [create one](https://app.quanticdata.io/register?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper).

## What it scrapes

| Command | Input | Returns | Per run |
|---|---|---|---|
| `app-store-scraper apps` | search term, or --app-ids | Rating, review count, price, version, size, developer, screenshots, 35 fields per row ([fields and price](https://quanticdata.io/collectors/app-store-scraper-api/?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper)) | up to 200 |
| `app-store-scraper reviews` | app id or store URL | Rating, title, text, app version, date, votes, 15 fields per row ([fields and price](https://quanticdata.io/collectors/app-store-reviews-api/?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper)) | up to 500 |
| `app-store-scraper search` | query, optional --media | Name, artist or seller, genre, price, rating, store link, 32 fields per row ([fields and price](https://quanticdata.io/collectors/itunes-search-api/?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper)) | up to 50 |

Every command takes `--country` for the storefront (`us`, `gb`, `de`, `it`, `jp`...); prices come back in that storefront's currency. `search --media` picks the catalog: `app`, `podcast`, `music`, `movie`, `ebook`, `audiobook` or `all`.

## Sample output

A real row from `app-store-scraper apps "podcast player" --country us --max-results 2` (2026-10-23):

```json
{
  "url": "https://apps.apple.com/us/app/podcast-app/id1199070742?uo=4",
  "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/91/9e/33/919e3300-ce6d-c12b-7c63-e29917ab7a0f/AppIcon-0-0-1x_U007emarketing-0-11-0-sRGB-85-220.png/512x512bb.jpg",
  "rank": 2,
  "price": 0,
  "title": "Podcast App",
  "app_id": "1199070742",
  "rating": 4.77,
  "seller": "Evolve Global, Inc.",
  "devices": [
    "iPhone",
    "iPad",
    "iPod",
    "Watch"
  ],
  "reviews": 309686,
  "version": "7.23.0",
  "category": "News",
  "currency": "USD",
  "bundle_id": "com.evolve.podcast",
  "developer": "Evolve Global, Inc.",
  "languages": [
    "DA",
    "NL",
    "EN",
    "FR",
    "DE",
    "HI",
    "IT",
    "JA",
    "KO",
    "NB",
    "PT",
    "RU",
    "ES",
    "SV"
  ],
  "advisories": [
    "Infrequent/Mild Profanity or Crude Humor",
    "Infrequent/Mild Alcohol, Tobacco, or Drug Use or References",
    "Infrequent/Mild Mature/Suggestive Themes",
    "Infrequent/Mild Medical/Treatment Information"
  ],
  "categories": [
    "News"
  ],
  "minimum_os": "16.4",
  "size_bytes": 122530816,
  "updated_at": "2026-10-14T13:08:03Z",
  "category_id": "6009",
  "description": "Find great podcasts. Podcast App is the #1 most downloaded independent podcast player on iOS.",
  "game_center": false,
  "released_at": "2017-03-10T11:48:17Z",
  "screenshots": [
    "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/81/85/3a/81853aea-281d-28e8-aaa6-a87a4d8a257f/dab702f7-c5a1-41ec-8f24-22240e56c809_EN_-_5.5_-_Screenshot_01.png/392x696bb.png",
    "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/12/d8/bb/12d8bb40-1c58-54d2-aadb-b7aa1f05a686/6404e4fd-5396-4389-b62f-292adf70d49a_EN_-_5.5_-_Screenshot_02.png/392x696bb.png"
  ],
  "developer_id": "1199070741",
  "developer_url": "https://podcast.app/",
  "release_notes": "Hey there, loyal users! In this release, we are improving the overall reliability of the app.",
  "content_rating": "12+",
  "price_formatted": "Free",
  "ipad_screenshots": [
    "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/f9/44/1d/f9441dd4-d340-5b33-44e9-534afe5bb166/e38b2eb5-9533-4efc-805f-76cbc9f3b775_EN_-_12.9_-_Screenshot_01.png/576x768bb.png",
    "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/0d/06/c0/0d06c078-9983-578b-5480-cf1c0b2aad3d/d2beaf0e-5cc1-47c7-a6e7-8474fdbf373f_EN_-_12.9_-_Screenshot_02.png/576x768bb.png"
  ],
  "developer_store_url": "https://apps.apple.com/us/developer/evolve-global-inc/id1199070741?uo=4",
  "rating_current_version": 4.77,
  "reviews_current_version": 309686
}
```

## Python

```python
from quanticdata_app_store_scraper import AppStoreScraper

store = AppStoreScraper()  # saved login, or QUANTICDATA_API_KEY

apps = store.apps("podcast player", country="us", max_results=50)
for a in apps:
    print(a["rank"], a["title"], a["rating"], a["reviews"], a["price_formatted"])

whatsapp = store.apps(app_ids=["310633997"], country="us")
print(whatsapp.rows[0]["version"], whatsapp.rows[0]["updated_at"])

reviews = store.reviews("310633997", country="us", max_results=200)
reviews.to_csv("whatsapp_reviews.csv")

shows = store.search("true crime", media="podcast", max_results=25)
for s in shows:
    print(s["name"], s["artist"], s["feed_url"])
```

Each call returns a `Run`: iterate it for the rows (plain dicts), take `len()`, or save it with `to_csv()`, `to_json()`, `to_jsonl()` or `to_dataframe()` (pandas). Errors are specific: `InsufficientCredit`, `RateLimited`, `InvalidInput`, `JobFailed`, `AuthError`.

## Examples

- **Review monitoring**: Pull the newest reviews of a list of apps and append only the ones you have not stored yet to one CSV, with rating, app version and date. See [`examples/review_monitor.py`](examples/review_monitor.py).
- **App tracking**: Record the rating, review count, version and price of a list of apps by id on every run and keep the history in a CSV. See [`examples/app_tracker.py`](examples/app_tracker.py).
- **App Store search rankings**: See where an app ranks in App Store search for a list of keywords, the basic check of app store optimization (ASO). See [`examples/aso_rankings.py`](examples/aso_rankings.py).

## Command line

Results print as a table; `-o file.csv`, `-o file.json` or `-o file.jsonl` writes a file. List inputs take `a b c`, `a,b,c`, `@file.txt` (one per line) or `-` (stdin). `--no-wait` starts a long run in the background and prints its id; `app-store-scraper run <id> -o out.csv` collects it later.

### `app-store-scraper apps`

Apple App Store apps by search term or by app/bundle id.

```
app-store-scraper apps [TERM] [options]
```

| Option | Type | Default | Description |
|---|---|---|---|
| `TERM` | string |  | What to search in the App Store, e.g. "podcast player". Omit it when you pass --app-ids. |
| `--app-ids` | string[] |  | Numeric app ids (310633997), bundle ids (com.spotify.client) or store URLs. |
| `--country` | string |  | App Store storefront, as an ISO country code (default us). |
| `--lang` | string |  | Interface language, e.g. en, it, de. |
| `--max-results` | integer | `20` | How many apps to deliver at most (1–200). You pay only for delivered apps. |

### `app-store-scraper reviews`

Customer reviews of an App Store app — rating, title, text, version, votes.

```
app-store-scraper reviews APP_ID [options]
```

| Option | Type | Default | Description |
|---|---|---|---|
| `APP_ID` | string |  | Numeric App Store id (310633997) or the app's store URL. |
| `--country` | string |  | Storefront to read the reviews of, as an ISO country code (default us). |
| `--max-results` | integer | `50` | How many reviews to deliver at most (1–500). You pay only for delivered reviews. |

### `app-store-scraper search`

Apple catalog search — apps, podcasts, music, movies, ebooks — per storefront.

```
app-store-scraper search QUERY [options]
```

| Option | Type | Default | Description |
|---|---|---|---|
| `QUERY` | string |  | Search terms, e.g. "meditation". |
| `--media` | app / podcast / music / movie / ebook / audiobook / all | `app` | Which catalog to search. |
| `--country` | string | `us` | Storefront, as an ISO country code (default us). |
| `--max-results` | integer | `25` | How many results to deliver at most (1–50). You pay only for delivered results. |

## Output fields

<details><summary><code>app-store-scraper apps</code>: 35 fields</summary>

| Field | Type | Description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `app_id` | string | Apple app id. |
| `bundle_id` | string or null | Bundle identifier. |
| `title` | string | App name. |
| `developer` | string or null | Seller/developer. |
| `developer_url` | string or null | Developer URL. |
| `category` | string or null | Primary genre. |
| `categories` | string[] | All genres. |
| `rating` | number or null | Average rating (all versions). |
| `reviews` | integer or null | Rating count. |
| `rating_current_version` | number or null | Average rating for the current version. |
| `price` | number or null | Numeric price (0 = free). |
| `price_formatted` | string or null | Price as shown. |
| `currency` | string or null | Currency code. |
| `version` | string or null | Current version. |
| `released_at` | string or null | First release date (ISO). |
| `updated_at` | string or null | Current version release date (ISO). |
| `content_rating` | string or null | Age rating. |
| `size_bytes` | number or null | Download size in bytes. |
| `icon` | string or null | Icon URL (512px when available). |
| `screenshots` | string[] | Up to 5 screenshot URLs. |
| `description` | string or null | Store description (trimmed). |
| `url` | string | Store URL. |
| `developer_id` | string or null | Apple developer id. |
| `developer_store_url` | string or null | The developer's page on the App Store. |
| `seller` | string or null | Legal seller name. |
| `category_id` | string or null | Primary genre id. |
| `reviews_current_version` | integer or null | Rating count for the current version. |
| `release_notes` | string or null | What's new in the current version (trimmed). |
| `minimum_os` | string or null | Minimum iOS version. |
| `languages` | string[] | Supported languages (ISO codes). |
| `devices` | string[] | Device families supported (iPhone, iPad, Mac, Watch…). |
| `game_center` | boolean | Game Center enabled. |
| `advisories` | string[] | Content advisories. |
| `ipad_screenshots` | string[] | iPad screenshot URLs (up to 5). |

</details>

<details><summary><code>app-store-scraper reviews</code>: 15 fields</summary>

| Field | Type | Description |
|---|---|---|
| `rank` | integer | 1-based position (newest first). |
| `app_id` | string | App id the review belongs to. |
| `country` | string | Storefront read. |
| `review_id` | string | Apple's review id. |
| `rating` | integer or null | Star rating 1–5 Apple records for the review (on store_page rows, the stars the store shows on the review card). |
| `title` | string or null | Review title. |
| `text` | string or null | Review body. |
| `author` | string or null | Reviewer nickname. |
| `app_version` | string or null | App version reviewed. |
| `updated_at` | string or null | Review timestamp (ISO 8601). |
| `votes_helpful` | integer | Helpful votes. |
| `votes_total` | integer | Total votes. |
| `source` | string | Where the row was read: feed or store_page. |
| `developer_response` | string or null | The developer's public reply (store page rows). |
| `developer_response_at` | string or null | When the developer replied (ISO 8601). |

</details>

<details><summary><code>app-store-scraper search</code>: 32 fields</summary>

| Field | Type | Description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `kind` | string or null | Result kind (software, podcast…). |
| `name` | string | Track/collection name. |
| `artist` | string or null | Artist or seller. |
| `genre` | string or null | Primary genre. |
| `price` | number or null | Storefront price. |
| `currency` | string or null | Price currency. |
| `rating` | number or null | Average user rating. |
| `ratings_count` | integer or null | Rating count. |
| `release_date` | string or null | Release date. |
| `artwork` | string or null | Artwork URL. |
| `url` | string or null | Store link. |
| `id` | string or null | Apple's id for the result (track id; collection id for albums and audiobooks). |
| `artist_id` | string or null | Apple artist/developer id. |
| `artist_url` | string or null | Artist page on the store. |
| `collection` | string or null | Album / show / collection name. |
| `collection_id` | string or null | Apple collection id. |
| `genres` | string[] | All genres listed for the result. |
| `collection_price` | number or null | Price of the whole album/collection. |
| `duration_seconds` | integer or null | Length of the track, episode or movie. |
| `track_count` | integer or null | Episodes in the podcast / tracks on the album. |
| `track_number` | integer or null | Position of the track on its album. |
| `explicit` | boolean or null | Explicit-content flag. |
| `content_rating` | string or null | Content advisory (Clean, Explicit, 12+…). |
| `feed_url` | string or null | Podcasts: the show's RSS feed. |
| `preview_url` | string or null | Music/movies: 30-second preview clip. |
| `bundle_id` | string or null | Apps: bundle id. |
| `seller` | string or null | Apps: seller name. |
| `version` | string or null | Apps: current version. |
| `description` | string or null | Apps, movies, ebooks: description (trimmed). |
| `storefront` | string or null | Storefront country code as Apple states it (USA, ITA…). |
| `artwork_large` | string or null | 600px artwork. |

</details>

## Sign-in and API keys

- `app-store-scraper login` signs you in with OAuth 2.1 and PKCE in the browser. The token is stored in `~/.config/quanticdata/credentials.json` (readable only by you) and refreshed automatically. One login serves every QuanticData tool on the machine.
- No browser on the machine (SSH, Docker, Colab): run `app-store-scraper login --no-browser`, open the link anywhere, then paste back the address the browser ends on.
- Scripts and CI: set `QUANTICDATA_API_KEY` to a key from the dashboard, or store one with `app-store-scraper login --api-key`.
- `app-store-scraper logout` revokes the token. The connection is listed under API keys in the dashboard as "API · QuanticData CLI"; deleting that key disconnects every machine that uses it.

## Pricing

The code is free and MIT-licensed. Runs are billed to your QuanticData account per delivered row, at the price shown on each collector page linked above; $2 of usage is free every month and failed runs are never billed. Plans with higher limits: [pricing](https://quanticdata.io/pricing/?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper).

## Other ways to call it

The same data over plain HTTP:

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/app_store_apps/run \
  -H "Authorization: Bearer $QUANTICDATA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input": {"term": "podcast player", "country": "us", "max_results": 2}}'
```

- [API reference](https://quanticdata.io/docs/?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper) with Python, Node, PHP and curl examples.
- [MCP server](https://quanticdata.io/mcp-server/?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper) to give Claude, Cursor or any MCP client the same tools.
- [n8n node](https://github.com/quantumproxies/n8n-nodes-quanticdata) for no-code workflows.

## FAQ

**Is this App Store scraper free?**

The code is free and MIT-licensed. Scraping runs on your QuanticData account: $2 of usage is free every month with no card, then you pay per delivered row at the price shown on each collector page. Failed runs are never billed.

**Do I need an Apple developer account or proxies?**

No. You send a search term, an app id or a store URL and get rows back; the requests run on QuanticData's side.

**How many results can one run return?**

Up to 200 apps, 500 reviews or 50 catalog results per run; ask for fewer with --max-results and you pay only for what is delivered.

**Are reviews read per country?**

Yes. App Store reviews belong to a storefront, so reviews 310633997 --country gb returns what UK customers wrote. Each row says which storefront it came from.

**Can I export to CSV or Excel?**

Add -o results.csv (or .json, .jsonl). Lists such as languages, devices and screenshots are joined with '; ', so the CSV opens cleanly in Excel or Google Sheets.

**What does it read?**

Public App Store data only: store listings, Apple's public catalog and the reviews any visitor can see; a review row carries the reviewer's App Store nickname. You are responsible for respecting Apple's terms and the data-protection rules that apply to how you use the data.

## Related scrapers

- [Google Play Scraper](https://github.com/quantumproxies/google-play-scraper): Google Play scraper for Python and the command line.
- [Steam Scraper](https://github.com/quantumproxies/steam-scraper): Steam scraper for Python and the command line.

## License

MIT. Built and maintained by [QuanticData](https://quanticdata.io/?utm_source=github&utm_medium=readme&utm_campaign=app-store-scraper).
