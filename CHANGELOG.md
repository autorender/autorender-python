# Changelog

## [0.2.0](https://github.com/autorenderhq/autorender-python/compare/v0.1.0...v0.2.0) (2026-05-25)


### Features

* add test CI job ([2c25e3a](https://github.com/autorenderhq/autorender-python/commit/2c25e3ad8ffe7ff44d5e7781e37de7c2598550df))
* initial stlc build ([0bdb709](https://github.com/autorenderhq/autorender-python/commit/0bdb709b1d8e670a795f867f71fab9c3ef6be539))


### Bug Fixes

* install rye for Python SDK bootstrap ([5f089bf](https://github.com/autorenderhq/autorender-python/commit/5f089bf37c183b4d41b1eb1787c5b7390d93b0f2))
* **python:** rename pagination field has_next_page -&gt; has_next to fix pyright lint ([729d204](https://github.com/autorenderhq/autorender-python/commit/729d20471bdfe545acdea2e443cfb2b8436ba08a))


### Chores

* trigger release-please ([8db5acc](https://github.com/autorenderhq/autorender-python/commit/8db5acc865fce568f3ebb33c2e2536d9e84a41a6))
* update stlc custom-code tracking files ([505f95e](https://github.com/autorenderhq/autorender-python/commit/505f95e9e6b66928d05ffa5b630102fdfe3b5e3e))

## [0.1.0](https://github.com/autorenderhq/autorender-python/compare/v0.0.1...v0.1.0) (2026-05-25)


### Features

* add test CI job ([2c25e3a](https://github.com/autorenderhq/autorender-python/commit/2c25e3ad8ffe7ff44d5e7781e37de7c2598550df))
* **api:** api update ([84d1942](https://github.com/autorenderhq/autorender-python/commit/84d19422bdd7a80d8c0d52fe6bb0e989f7b2abe7))
* **api:** api update ([9dc8482](https://github.com/autorenderhq/autorender-python/commit/9dc848263fbf6509dd3e84a3a7963a897d14991b))
* **api:** api update ([04c1163](https://github.com/autorenderhq/autorender-python/commit/04c116350cc7a2f5f288a8fd9febd020083cf536))
* **api:** api update ([b4d6dbe](https://github.com/autorenderhq/autorender-python/commit/b4d6dbee14ac3e753968ce90388eaf01d2af4b94))
* **api:** api update ([3932736](https://github.com/autorenderhq/autorender-python/commit/393273609afc67cc8b30d33bb27861edb1e20988))
* **api:** api update ([58346bd](https://github.com/autorenderhq/autorender-python/commit/58346bdeba4b11a33fd1e63c69fceb432424bdf0))
* **api:** api update ([7fdb60a](https://github.com/autorenderhq/autorender-python/commit/7fdb60a62af1ae9fd716c3a9939d2cc128bd4a85))
* **api:** api update ([79c95b0](https://github.com/autorenderhq/autorender-python/commit/79c95b0a55d59e214f0b00936a5b517c0f66ca13))
* **api:** api update ([b43e6a1](https://github.com/autorenderhq/autorender-python/commit/b43e6a1b4b157808d3ef2606552df4e68c1524e7))
* **api:** api update ([658511c](https://github.com/autorenderhq/autorender-python/commit/658511ca294a346646139b0c4c5e0f4e151115e4))
* initial stlc build ([0bdb709](https://github.com/autorenderhq/autorender-python/commit/0bdb709b1d8e670a795f867f71fab9c3ef6be539))
* **internal/types:** support eagerly validating pydantic iterators ([477052f](https://github.com/autorenderhq/autorender-python/commit/477052fa9cd1ff89c96ee4b8febf010851c6501e))
* support setting headers via env ([749df21](https://github.com/autorenderhq/autorender-python/commit/749df21f7ac657d44cb297707a5ec2506bcb0df9))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([0f93e15](https://github.com/autorenderhq/autorender-python/commit/0f93e15723c120a2f409cf2884d085f7966d5d0c))
* **examples:** use timestamp names and correct response shape in files.py ([b4d13a7](https://github.com/autorenderhq/autorender-python/commit/b4d13a7d72784c4448424db46495c985276773d3))
* install rye for Python SDK bootstrap ([5f089bf](https://github.com/autorenderhq/autorender-python/commit/5f089bf37c183b4d41b1eb1787c5b7390d93b0f2))
* **pagination:** resolve pyright incompatible override for has_next_page ([5cf6e56](https://github.com/autorenderhq/autorender-python/commit/5cf6e565ac0aeecdc5e59b887b1e008892eed1ce))
* **python:** rename pagination field has_next_page -&gt; has_next to fix pyright lint ([729d204](https://github.com/autorenderhq/autorender-python/commit/729d20471bdfe545acdea2e443cfb2b8436ba08a))
* strip Content-Type header for body-less requests; add examples ([c3591d0](https://github.com/autorenderhq/autorender-python/commit/c3591d02910ded15e21a7ed7da402bf149f46857))
* use correct field name format for multipart file arrays ([f968ef9](https://github.com/autorenderhq/autorender-python/commit/f968ef95330967c6b888ea3fc89c85f12ee926d1))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([498d621](https://github.com/autorenderhq/autorender-python/commit/498d621cc46637650c03f1ed9d00749dbcab9c99))


### Chores

* **internal:** more robust bootstrap script ([798e8b7](https://github.com/autorenderhq/autorender-python/commit/798e8b79c22e0173d4f30a80924dcad627cc838f))
* **internal:** reformat pyproject.toml ([fcc4169](https://github.com/autorenderhq/autorender-python/commit/fcc4169f137c6f4e6305bd0b8133658ad5337aa6))
* remove examples from SDK (moved to stainless-examples runner) ([12a383e](https://github.com/autorenderhq/autorender-python/commit/12a383e16ab6e856905dd8ce8f3f666ff914c43c))
* **tests:** bump steady to v0.22.1 ([30a0e81](https://github.com/autorenderhq/autorender-python/commit/30a0e8184adf8271f879cb9e5175ed52404a0043))
* update SDK settings ([aead4ee](https://github.com/autorenderhq/autorender-python/commit/aead4ee8dd9504134612b1845cd18576b7c58848))
* update stlc custom-code tracking files ([505f95e](https://github.com/autorenderhq/autorender-python/commit/505f95e9e6b66928d05ffa5b630102fdfe3b5e3e))

## 0.1.0 (2026-05-15)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/autorenderhq/autorender-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([84d1942](https://github.com/autorenderhq/autorender-python/commit/84d19422bdd7a80d8c0d52fe6bb0e989f7b2abe7))
* **api:** api update ([9dc8482](https://github.com/autorenderhq/autorender-python/commit/9dc848263fbf6509dd3e84a3a7963a897d14991b))
* **api:** api update ([04c1163](https://github.com/autorenderhq/autorender-python/commit/04c116350cc7a2f5f288a8fd9febd020083cf536))
* **api:** api update ([b4d6dbe](https://github.com/autorenderhq/autorender-python/commit/b4d6dbee14ac3e753968ce90388eaf01d2af4b94))
* **api:** api update ([3932736](https://github.com/autorenderhq/autorender-python/commit/393273609afc67cc8b30d33bb27861edb1e20988))
* **api:** api update ([58346bd](https://github.com/autorenderhq/autorender-python/commit/58346bdeba4b11a33fd1e63c69fceb432424bdf0))
* **api:** api update ([7fdb60a](https://github.com/autorenderhq/autorender-python/commit/7fdb60a62af1ae9fd716c3a9939d2cc128bd4a85))
* **api:** api update ([79c95b0](https://github.com/autorenderhq/autorender-python/commit/79c95b0a55d59e214f0b00936a5b517c0f66ca13))
* **api:** api update ([b43e6a1](https://github.com/autorenderhq/autorender-python/commit/b43e6a1b4b157808d3ef2606552df4e68c1524e7))
* **api:** api update ([658511c](https://github.com/autorenderhq/autorender-python/commit/658511ca294a346646139b0c4c5e0f4e151115e4))
* **internal/types:** support eagerly validating pydantic iterators ([477052f](https://github.com/autorenderhq/autorender-python/commit/477052fa9cd1ff89c96ee4b8febf010851c6501e))
* support setting headers via env ([749df21](https://github.com/autorenderhq/autorender-python/commit/749df21f7ac657d44cb297707a5ec2506bcb0df9))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([0f93e15](https://github.com/autorenderhq/autorender-python/commit/0f93e15723c120a2f409cf2884d085f7966d5d0c))
* **examples:** use timestamp names and correct response shape in files.py ([b4d13a7](https://github.com/autorenderhq/autorender-python/commit/b4d13a7d72784c4448424db46495c985276773d3))
* **pagination:** resolve pyright incompatible override for has_next_page ([5cf6e56](https://github.com/autorenderhq/autorender-python/commit/5cf6e565ac0aeecdc5e59b887b1e008892eed1ce))
* strip Content-Type header for body-less requests; add examples ([c3591d0](https://github.com/autorenderhq/autorender-python/commit/c3591d02910ded15e21a7ed7da402bf149f46857))
* use correct field name format for multipart file arrays ([f968ef9](https://github.com/autorenderhq/autorender-python/commit/f968ef95330967c6b888ea3fc89c85f12ee926d1))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([498d621](https://github.com/autorenderhq/autorender-python/commit/498d621cc46637650c03f1ed9d00749dbcab9c99))


### Chores

* **internal:** more robust bootstrap script ([798e8b7](https://github.com/autorenderhq/autorender-python/commit/798e8b79c22e0173d4f30a80924dcad627cc838f))
* **internal:** reformat pyproject.toml ([fcc4169](https://github.com/autorenderhq/autorender-python/commit/fcc4169f137c6f4e6305bd0b8133658ad5337aa6))
* remove examples from SDK (moved to stainless-examples runner) ([12a383e](https://github.com/autorenderhq/autorender-python/commit/12a383e16ab6e856905dd8ce8f3f666ff914c43c))
* **tests:** bump steady to v0.22.1 ([30a0e81](https://github.com/autorenderhq/autorender-python/commit/30a0e8184adf8271f879cb9e5175ed52404a0043))
* update SDK settings ([aead4ee](https://github.com/autorenderhq/autorender-python/commit/aead4ee8dd9504134612b1845cd18576b7c58848))
