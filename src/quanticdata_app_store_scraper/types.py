"""Row types of each command, for editors and type checkers (rows are plain dicts)."""

from typing import Any, Dict, List, Optional

try:  # Python 3.8+
    from typing import TypedDict
except ImportError:  # pragma: no cover
    from typing_extensions import TypedDict  # type: ignore


class AppStoreAppsRow(TypedDict, total=False):
    """One row of `app-store-scraper apps` (app_store_apps v1.1.2)."""

    rank: int
    """1-based position."""
    app_id: str
    """Apple app id."""
    bundle_id: Optional[str]
    """Bundle identifier."""
    title: str
    """App name."""
    developer: Optional[str]
    """Seller/developer."""
    developer_url: Optional[str]
    """Developer URL."""
    category: Optional[str]
    """Primary genre."""
    categories: List[str]
    """All genres."""
    rating: Optional[float]
    """Average rating (all versions)."""
    reviews: Optional[int]
    """Rating count."""
    rating_current_version: Optional[float]
    """Average rating for the current version."""
    price: Optional[float]
    """Numeric price (0 = free)."""
    price_formatted: Optional[str]
    """Price as shown."""
    currency: Optional[str]
    """Currency code."""
    version: Optional[str]
    """Current version."""
    released_at: Optional[str]
    """First release date (ISO)."""
    updated_at: Optional[str]
    """Current version release date (ISO)."""
    content_rating: Optional[str]
    """Age rating."""
    size_bytes: Optional[float]
    """Download size in bytes."""
    icon: Optional[str]
    """Icon URL (512px when available)."""
    screenshots: List[str]
    """Up to 5 screenshot URLs."""
    description: Optional[str]
    """Store description (trimmed)."""
    url: str
    """Store URL."""
    developer_id: Optional[str]
    """Apple developer id."""
    developer_store_url: Optional[str]
    """The developer's page on the App Store."""
    seller: Optional[str]
    """Legal seller name."""
    category_id: Optional[str]
    """Primary genre id."""
    reviews_current_version: Optional[int]
    """Rating count for the current version."""
    release_notes: Optional[str]
    """What's new in the current version (trimmed)."""
    minimum_os: Optional[str]
    """Minimum iOS version."""
    languages: List[str]
    """Supported languages (ISO codes)."""
    devices: List[str]
    """Device families supported (iPhone, iPad, Mac, Watch…)."""
    game_center: bool
    """Game Center enabled."""
    advisories: List[str]
    """Content advisories."""
    ipad_screenshots: List[str]
    """iPad screenshot URLs (up to 5)."""

class AppStoreReviewsRow(TypedDict, total=False):
    """One row of `app-store-scraper reviews` (app_store_reviews v1.1.2)."""

    rank: int
    """1-based position (newest first)."""
    app_id: str
    """App id the review belongs to."""
    country: str
    """Storefront read."""
    review_id: str
    """Apple's review id."""
    rating: Optional[int]
    """Star rating 1–5 Apple records for the review (on store_page rows, the stars the store shows on the review card)."""
    title: Optional[str]
    """Review title."""
    text: Optional[str]
    """Review body."""
    author: Optional[str]
    """Reviewer nickname."""
    app_version: Optional[str]
    """App version reviewed."""
    updated_at: Optional[str]
    """Review timestamp (ISO 8601)."""
    votes_helpful: int
    """Helpful votes."""
    votes_total: int
    """Total votes."""
    source: str
    """Where the row was read: feed or store_page."""
    developer_response: Optional[str]
    """The developer's public reply (store page rows)."""
    developer_response_at: Optional[str]
    """When the developer replied (ISO 8601)."""

class ItunesSearchRow(TypedDict, total=False):
    """One row of `app-store-scraper search` (itunes_search v1.1.1)."""

    rank: int
    """1-based position."""
    kind: Optional[str]
    """Result kind (software, podcast…)."""
    name: str
    """Track/collection name."""
    artist: Optional[str]
    """Artist or seller."""
    genre: Optional[str]
    """Primary genre."""
    price: Optional[float]
    """Storefront price."""
    currency: Optional[str]
    """Price currency."""
    rating: Optional[float]
    """Average user rating."""
    ratings_count: Optional[int]
    """Rating count."""
    release_date: Optional[str]
    """Release date."""
    artwork: Optional[str]
    """Artwork URL."""
    url: Optional[str]
    """Store link."""
    id: Optional[str]
    """Apple's id for the result (track id; collection id for albums and audiobooks)."""
    artist_id: Optional[str]
    """Apple artist/developer id."""
    artist_url: Optional[str]
    """Artist page on the store."""
    collection: Optional[str]
    """Album / show / collection name."""
    collection_id: Optional[str]
    """Apple collection id."""
    genres: List[str]
    """All genres listed for the result."""
    collection_price: Optional[float]
    """Price of the whole album/collection."""
    duration_seconds: Optional[int]
    """Length of the track, episode or movie."""
    track_count: Optional[int]
    """Episodes in the podcast / tracks on the album."""
    track_number: Optional[int]
    """Position of the track on its album."""
    explicit: Optional[bool]
    """Explicit-content flag."""
    content_rating: Optional[str]
    """Content advisory (Clean, Explicit, 12+…)."""
    feed_url: Optional[str]
    """Podcasts: the show's RSS feed."""
    preview_url: Optional[str]
    """Music/movies: 30-second preview clip."""
    bundle_id: Optional[str]
    """Apps: bundle id."""
    seller: Optional[str]
    """Apps: seller name."""
    version: Optional[str]
    """Apps: current version."""
    description: Optional[str]
    """Apps, movies, ebooks: description (trimmed)."""
    storefront: Optional[str]
    """Storefront country code as Apple states it (USA, ITA…)."""
    artwork_large: Optional[str]
    """600px artwork."""
