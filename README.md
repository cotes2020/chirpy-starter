# Chirpy Starter

The startup template for [**Jekyll Theme Chirpy**][chirpy].

When installing the `jekyll-theme-chirpy` through [RubyGem][gem], Jekyll can only read files in the folders `_includes`, `_layout`, `_sass` and `assets`, as well as a small part of variables of the file `_config.yml` from the theme's gem (use the command `bundle info --path jekyll-theme-chirpy` to locate). To fully use all the features of `jekyll-theme-chirpy`, you also need to copy other files/directories and site variables from the theme's gem to your Jekyll site. This will be boring, so we extract all the other required things of the theme's gem to help you quickly use `jekyll-theme-chirpy`.

[gem]: https://rubygems.org/gems/jekyll-theme-chirpy
[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/

**File Directory Struct**

```shell
.
├── .github
│   └── workflows
│       └── pages-deploy.yml    # the GitHub Actions workflow
├── Gemfile
├── LICENSE
├── README.md                   # this file
├── _config.yml                 # all variables are from the theme's gem, except the option `theme`
├── _data                       # from the theme's gem
├── _plugins                    # idem
├── _tabs                       # idem
├── app.js                      # idem
├── feed.xml                    # idem
├── index.html                  # idem
├── 404.html                    # idem
├── robots.txt                  # idem
└── sw.js                       # idem

```

## Installation

[Use this template][usetemplate] to generate a new repository, and then execute:

[usetemplate]: https://github.com/cotes2020/chirpy-starter/generate

```
$ bundle
```

## Usage

### Customing Stylesheet

Creare a new file `/assets/css/style.scss` in your Jekyll site.

And then add the following content:

```scss
---
---

@import {{ site.theme }}

// add your style below
```

### Changing the Number of Tabs

When adding or deleting files in the `_tabs` folder, you need to complete [Custom Stylesheet](#custom-stylesheet) first, and then add a new line before `@import`:

```scss
$tab-count: {{ site.tabs | size | plus: 1 }};
```

### Publishing to GitHub Pages

See the `jekyll-theme-chirpy`'s [deployment instructions](https://github.com/cotes2020/jekyll-theme-chirpy#deployment). Note that in order to use GitHub Actions caching to speed up the deployment, you should add the `Gemfile.lock` file to your repository.

### Updating

Please note that files and directories in this project may change as the [`jekyll-theme-chirpy`][chirpy] is updated. When updating, please ensure that the file directory structure of your Jekyll site is the same as that of this project.

And then execute:

```console
$ bundle update jekyll-theme-chirpy
```

## Documentation

See the [theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy#documentation).

## License

This work is published under [MIT](https://github.com/cotes2020/chirpy-starter/blob/master/LICENSE) License.
