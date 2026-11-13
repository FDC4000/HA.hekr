# HA.hekr — Hekr Hood for Home Assistant

Home Assistant custom integration for **KKT Kolbe / Wisen** range hoods on the
**Hekr** cloud platform (tested: SOLO807SM, model M002).

Ported from the [`ioBroker.hekr`](https://github.com/TA2k/ioBroker.hekr) adapter
by TA2k (MIT License).

> The original ioBroker adapter code has been removed from this branch; this
> repository now contains the Home Assistant integration only.

## Layout

```
custom_components/hekr_hood/   # the integration
tests/                         # pytest suite (mocked network)
requirements-test.txt          # test dependencies
```

## Quick start

1. Copy `custom_components/hekr_hood/` into your Home Assistant
   `/config/custom_components/` directory.
2. Restart Home Assistant.
3. **Settings → Devices & Services → + Add Integration → Hekr Hood**, then sign
   in with your Wisen app email and password.

Full installation, configuration and debugging notes:
[`custom_components/hekr_hood/README.md`](custom_components/hekr_hood/README.md).

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-test.txt
pytest
```

All tests use a mocked network/WebSocket — no real connections are made.

## License

MIT License. Protocol logic ported from **ioBroker.hekr** by **TA2k**,
Copyright (c) 2021 TA2k. See [`LICENSE`](LICENSE).
