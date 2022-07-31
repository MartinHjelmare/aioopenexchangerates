# Usage

To use this package, import the client and instantiate it. Then call the appropriate client method to get exchange rates data. The client methods will correspond to the [endpoints](https://docs.openexchangerates.org/) of the Open Exchange Rates API.

For example, to get the latest exchange rates:

```py
import asyncio

from aioopenexchangerates import Client


async def main() -> None:
    """Run main."""
    async with Client("your_api_key") as client:
        result = await client.get_latest()
        print(result)


asyncio.run(main())
```

You will need an API key from the [Open Exchange Rates API](https://openexchangerates.org/).
