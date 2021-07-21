# Chirpy Starter [![Gem Version](https://img.shields.io/gem/v/jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy) [![GitHub license](https://img.shields.io/github/license/cotes2020/chirpy-starter.svg?color=blue)][mit]


The startup template for [**Jekyll Theme Chirpy**][chirpy].

When installing the **Chirpy** theme through [RubyGems][gem], Jekyll can only read files in the folders `_includes`, `_layout`, `_sass` and `assets`, as well as a small part of options of the `_config.yml` file from the theme's gem. (You can find the gem files by using the command `bundle info --path jekyll-theme-chirpy`). To fully use all the features of **Chirpy**, you need to copy the other critical files/directories from the theme's gem to your Jekyll site.

The critical files/directories to run or build the **Chirpy** theme are as follows:

```shell
.
├── _data
├── _plugins
├── _tabs
├── _config.yml
└──  index.html
```

So we've extracted all the **Chirpy** gem necessary content here to help you get started quickly.

## Installation

[Use this template][usetemplate] to generate a new repository, and then execute:

[usetemplate]: https://github.com/cotes2020/chirpy-starter/generate

```
$ bundle
```

## Usage

Please see the [theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy#usage).

## Upgrading

First, please modify the target version number of `jekyll-theme-chirpy` in the `Gemfile` (e.g., `gem "jekyll-theme-chirpy", "~> 4.0", ">= 4.0.1"`).

After that, execute the following command:

```console
$ bundle update jekyll-theme-chirpy
```

As the version upgrades, the critical files and configuration options will change. Please refer to the [Upgrade Guide](https://github.com/cotes2020/jekyll-theme-chirpy/wiki/Upgrade-Guide) to keep your website files in sync with the latest version of the theme.

## License

This work is published under [MIT][mit] License.

[gem]: https://rubygems.org/gems/jekyll-theme-chirpy
[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/
[mit]: https://github.com/cotes2020/chirpy-starter/blob/master/LICENSE
