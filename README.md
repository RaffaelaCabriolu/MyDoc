# HPC-Physics services and user documentation

Served via http://hpc-uit.readthedocs.org.

Copyright (c) 2021


## License  "CHECK this".

Text is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/),
code examples are provided under the [MIT](https://opensource.org/licenses/MIT) license.


## Locally building the HTML for testing  Fix the address. 

```
git clone https://github.com/raffagit/HPC_PhysicsDoc
cd hpc-doc
virtualenv venv
source venv/bin/activate
pip install sphinx
pip install sphinx_rtd_theme
sphinx-build . _build
```

Then point your browser to `_build/index.html`.


## Getting started with RST and Sphinx

- http://sphinx-doc.org/rest.html
- http://sphinx-doc.org/markup/inline.html#cross-referencing-arbitrary-locations
