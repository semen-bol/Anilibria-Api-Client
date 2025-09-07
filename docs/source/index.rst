.. anilibria-api-client documentation master file

Welcome to anilibria-api-client's documentation!
===============================================

**anilibria-api-client** - Python async API wrapper for AniLibria Swagger

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   modules

Features
--------

- Async/await support with aiohttp
- Pydantic models for type safety
- Easy to use API methods
- File downloading capabilities

Quick Start
-----------

.. code-block:: python

   from anilibria_api_client import AniLibriaClient

   async def main():
       async with AniLibriaClient() as client:
           titles = await client.get_updates()
           print(titles)

Installation
------------

.. code-block:: bash

   pip install anilibria-api-client

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`