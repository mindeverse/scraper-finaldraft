# Final Draft Product Scraper

Production Finds scraper for [Final Draft](https://finaldraftclo.com/).

- Source: `scraper-finaldraft`
- Schedule: `43 14 * * 2,5` UTC
- Currency: EUR
- Gender default: Unisex
- Embeddings: local SigLIP `google/siglip-base-patch16-384`
- Secrets: `SUPABASE_URL`, `SUPABASE_KEY`
- Catalog crawl: store-wide `/products.json` plus listed collections
- Upsert batch size: 5; never sends `embedding_version`

Shopify EN+EUR. Gender inferred from men-/women- collections. ~160 published products. Tue/Fri 14:43 UTC.
