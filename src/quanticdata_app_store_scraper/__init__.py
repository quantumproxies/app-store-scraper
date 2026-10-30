"""App Store Scraper: App Store scraper for Python and the command line: Apple App Store apps by keyword or app id (rating, review count, price, version, size, developer), customer reviews of any app, and Apple catalog search for apps, podcasts, music and books, as JSON or CSV. Free and open source; no Apple developer account or proxies needed.

    from quanticdata_app_store_scraper import AppStoreScraper

    scraper = AppStoreScraper()   # saved login (`app-store-scraper login`) or QUANTICDATA_API_KEY
    run = scraper.apps(...)   # App Store apps by search term or app id
    run = scraper.reviews(...)   # customer reviews of one App Store app
    run = scraper.search(...)   # Apple catalog search: apps, podcasts, music, movies, books
"""

from typing import Any, Dict, Optional, Sequence, Union

from ._qd.client import Client, Run
from ._qd.errors import (APIError, AuthError, InsufficientCredit, InvalidInput, JobFailed, JobTimeout,
                         QuanticDataError, RateLimited)
from ._qd.output import write

__version__ = "0.1.0"
__all__ = ["AppStoreScraper", "Run", "write", "APIError", "AuthError", "InsufficientCredit", "InvalidInput",
           "JobFailed", "JobTimeout", "QuanticDataError", "RateLimited", "__version__"]


def _as_list(value: Any) -> Any:
    if value is None or isinstance(value, (list, tuple)):
        return list(value) if value is not None else None
    return [value]


class AppStoreScraper:
    """App Store Scraper on the QuanticData Data API.

    Every method runs one collector and returns a :class:`Run`: iterate it for the
    rows (plain dicts, typed in ``types``), or save it with ``to_csv()``,
    ``to_json()``, ``to_jsonl()`` or ``to_dataframe()``.
    """

    def __init__(self, api_key: Optional[str] = None, *, timeout: float = 180.0) -> None:
        self.client = Client(api_key, user_agent="app-store-scraper/0.1.0 (+https://github.com/quantumproxies/app-store-scraper)", timeout=timeout)

    def apps(
        self, term: Optional[str] = None,
        *,
        app_ids: Optional[Union[str, Sequence[str]]] = None,
        country: Optional[str] = None,
        lang: Optional[str] = None,
        max_results: Optional[int] = None,
        wait: bool = True,
        timeout: float = 900.0,
    ) -> Run:
        """Apple App Store apps by search term or by app/bundle id.

        Args:
            term: What to search in the App Store, e.g. "podcast player". Omit it when you pass --app-ids.
            app_ids: Numeric app ids (310633997), bundle ids (com.spotify.client) or store URLs.
            country: App Store storefront, as an ISO country code (default us).
            lang: Interface language, e.g. en, it, de.
            max_results: How many apps to deliver at most (1–200). You pay only for delivered apps.
            wait: False starts the run in the background and returns its id at once.
            timeout: seconds to wait for a background run before giving up.

        Returns up to 200 rows, one per app: see ``types.AppStoreAppsRow``.
        """
        payload = {
            "term": term,
            "app_ids": _as_list(app_ids),
            "country": country,
            "lang": lang,
            "max_results": max_results,
        }
        return self.client.run_collector("app_store_apps", payload, wait=wait, timeout=timeout)

    def reviews(
        self, app_id: str,
        *,
        country: Optional[str] = None,
        max_results: Optional[int] = None,
        wait: bool = True,
        timeout: float = 900.0,
    ) -> Run:
        """Customer reviews of an App Store app — rating, title, text, version, votes.

        Args:
            app_id: Numeric App Store id (310633997) or the app's store URL.
            country: Storefront to read the reviews of, as an ISO country code (default us).
            max_results: How many reviews to deliver at most (1–500). You pay only for delivered reviews.
            wait: False starts the run in the background and returns its id at once.
            timeout: seconds to wait for a background run before giving up.

        Returns up to 500 rows, one per review: see ``types.AppStoreReviewsRow``.
        """
        payload = {
            "app_id": app_id,
            "country": country,
            "max_results": max_results,
        }
        return self.client.run_collector("app_store_reviews", payload, wait=wait, timeout=timeout)

    def search(
        self, query: str,
        *,
        media: Optional[str] = None,
        country: Optional[str] = None,
        max_results: Optional[int] = None,
        wait: bool = True,
        timeout: float = 900.0,
    ) -> Run:
        """Apple catalog search — apps, podcasts, music, movies, ebooks — per storefront.

        Args:
            query: Search terms, e.g. "meditation".
            media: Which catalog to search. One of: app, podcast, music, movie, ebook, audiobook, all.
            country: Storefront, as an ISO country code (default us).
            max_results: How many results to deliver at most (1–50). You pay only for delivered results.
            wait: False starts the run in the background and returns its id at once.
            timeout: seconds to wait for a background run before giving up.

        Returns up to 50 rows, one per result: see ``types.ItunesSearchRow``.
        """
        payload = {
            "query": query,
            "media": media,
            "country": country,
            "max_results": max_results,
        }
        return self.client.run_collector("itunes_search", payload, wait=wait, timeout=timeout)
