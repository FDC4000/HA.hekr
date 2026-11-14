# HA.hekr — Hekr / Wisen for Home Assistant

Home Assistant custom integration for devices on the **Hekr / Wisen** IoT cloud
platform. These devices were controlled with the **Wisen App**.

One such device is the **KKT Kolbe** range hood — older models used this cloud
connection, and it is the reference device this integration was built and
verified against (tested: **SOLO807SM**, model **M002**). The integration is not
limited to hoods: other Hekr/Wisen device types can be added (see
[Adding new devices](#adding-new-devices)).

Ported from the [`ioBroker.hekr`](https://github.com/TA2k/ioBroker.hekr) adapter
by TA2k (MIT License).

> The original ioBroker adapter code has been removed; this repository now
> contains the Home Assistant integration only.

## Layout

```
custom_components/hekr_wisen/   # the integration
tests/                         # pytest suite (mocked network)
requirements-test.txt          # test dependencies
```

## Quick start

1. Copy `custom_components/hekr_wisen/` into your Home Assistant
   `/config/custom_components/` directory.
2. Restart Home Assistant.
3. **Settings → Devices & Services → + Add Integration → Hekr / Wisen**, then sign
   in with your Wisen app email and password.

Full installation, configuration and debugging notes:
[`custom_components/hekr_wisen/README.md`](custom_components/hekr_wisen/README.md).

## Adding new devices

To integrate additional Hekr/Wisen devices (new models or device types), see the
companion guide: <https://github.com/FDC4000/HA.hekr.add_device>.

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
