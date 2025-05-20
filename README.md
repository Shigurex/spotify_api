## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (package manager for Python)


Install [lefthook](https://github.com/evilmartians/lefthook) (Git hooks manager)

Install dependencies with uv
```bash
uv sync
```

Add Spotify API credentials to `.env`
```
SPOTIFY_CLIENT_ID={your_client_id}
SPOTIFY_CLIENT_SECRET={your_client_secret}
```

## Usage

```bash
uv run python main.py
```
