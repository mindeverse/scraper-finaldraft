"""Final Draft scraper configuration."""
import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    BRAND_NAME: str = "Final Draft"
    SOURCE: str = "scraper-finaldraft"
    BRAND_COLUMN: str = "Final Draft"
    SECOND_HAND: bool = False
    LANDING_PAGE: str = "https://finaldraftclo.com/"
    BASE_URL: str = "https://finaldraftclo.com"
    CURRENCY: str = "EUR"
    COUNTRY: str = "PT"
    PRODUCTS_JSON_LIMIT: int = 50

    CATEGORY_URLS: list[str] = field(default_factory=lambda: [
        "https://finaldraftclo.com/collections/all-products",
        "https://finaldraftclo.com/collections/men-shop-all",
        "https://finaldraftclo.com/collections/women-shop-all",
        "https://finaldraftclo.com/collections/bottoms",
        "https://finaldraftclo.com/collections/handmade",
        "https://finaldraftclo.com/collections/men-outerwear",
        "https://finaldraftclo.com/collections/women-outerwear",
        "https://finaldraftclo.com/collections/men-knit",
        "https://finaldraftclo.com/collections/women-knitwear"
    ])

    CATEGORY_DISPLAY: dict[str, str] = field(default_factory=lambda: {
        "all-products": "All Products",
        "men-shop-all": "Men",
        "women-shop-all": "Women",
        "bottoms": "Bottoms",
        "handmade": "Handmade",
        "men-outerwear": "Men Outerwear",
        "women-outerwear": "Women Outerwear",
        "men-knit": "Men Knit",
        "women-knitwear": "Women Knitwear"
    })

    SUPABASE_URL: str = field(default_factory=lambda: os.getenv("SUPABASE_URL", ""))
    SUPABASE_KEY: str = field(default_factory=lambda: os.getenv("SUPABASE_KEY", ""))

    EMBEDDING_MODEL: str = "google/siglip-base-patch16-384"
    EMBEDDING_DIM: int = 768
    EMBEDDING_VERSION: int = 2
    RATE_LIMIT_DELAY: float = 1.0
    BATCH_SIZE: int = 5
    STALE_MISS_THRESHOLD: int = 2
    REQUEST_TIMEOUT: int = 30
    USER_AGENT: str = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )
    GENDER_DEFAULT: str = "Unisex"


cfg = Config()
