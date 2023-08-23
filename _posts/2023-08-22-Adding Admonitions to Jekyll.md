---
title: Adding Admonitions to Jekyll
date: 02023-08-23 15:36:27
catagories: [minima, Themes, Jekyll, GitHub Pages]
tags: [minima, jekyll, github pages, themes, admonitions, docs]
---

## What Is An Admonition?
A distinct area of text to emphasize significant attention that is not a part of the main body. The purpose of admonition is drawing attention towards what you want a reader to remember without significantly interrupting the document flow. Admonitions are more commonly referred to as a callout or call-out.

{% include admonition.html type="info" title="Info" body="Example: This is information intended to draw attention." %}

## The Code
My approach was to create a Jekyll include file for the HTML with Liquid template language and Cascading Style Sheets (CSS) with syntactically awesome style sheets (SASS). This will allow for ease of adding admonitions without having to type out all the code manually each time. The styles are not completely identical to Material as I felt it needed to be more fitting to my theme. The Scalable Vector Graphics (SVG) icons I used are from Font Awesome Free. However, I believe one could also use SVG Repo.

I’ve tested this code on multiple web browsers without issues, so it should work fine under most circumstances.

#### _includes/admonition.html

```liquid
{% if include.type.size > 0 and include.title.size > 0 and include.body.size > 0 %}
    {% assign types = "note, abstract, info, tip, success, question, warning, failure, danger, bug, example, quote" | split: ", " %}
    {% if types contains include.type %}
<div class="admonition {{ include.type }} rounded">
    <p class="admonition-title">{{ include.title }}</p>
    <p>
        {{ include.body }}
    </p>
</div>
    {% endif %}
{% endif %}
```

#### _scss/admonition.scss

```scss
$primary-color: #fc0;
$primary-bgcolor: rgba(55.59%, 44.41%, 0%, .4);
$admonitions:
    //class (type), icon filename, icon/border color, title bg color
    ('note', 'pen-solid.svg')
    ('abstract', 'align-left-solid.svg')
    ('info', 'info-circle-solid.svg', '#00b0ff', '#293d52')
    ('tip', 'fire-solid.svg', '#ff9100', '#433a38')
    ('success', 'check-circle-solid.svg', '#00c953', '#294040')
    ('question', 'question-circle-solid.svg', '#00b8d4', '#293e4e')
    ('warning', 'exclamation-triangle-solid.svg', '#ff9100', '#564b3c')
    ('failure', 'times-circle-solid.svg', '#ff5252', '#564444')
    ('danger', 'bolt-solid.svg', '#ff1744', '#563e43')
    ('bug', 'bug-solid.svg', '#f50057', '#553c45')
    ('example', 'list-ol-solid.svg', '#9e9e9e', '#4c4c4c')
    ('quote', 'quote-right-solid.svg', '#9e9e9e', '#4c4c4c')
;
.admonition {
	margin: 1.5625em 0;
	overflow: hidden;
	color: #808080;
	page-break-inside: avoid;
	background-color: #212121;
	border-left: .3rem solid $primary-color;
	border-radius: .1rem;
}
.admonition p {
    padding: 0 1rem;
}
.admonition .admonition-title {
    color: #ddd;
    background-color: $primary-bgcolor;
    font-weight: 700;
    line-height: 3rem;
}
.admonition-title::before {
    margin-right: .5rem;
    width: 1.2rem;
    height: 1.2rem;
    display: inline-block;
    content: '';
    -webkit-mask-size: cover;
    mask-size: cover;
    background-color: $primary-color;
    vertical-align: text-bottom;
}
@each $name, $icon, $icon-color, $title-color in $admonitions {
    @if $icon-color {
        .admonition.#{$name} {
            border-left-color: #{$icon-color};
        }
    }
    @if $title-color {
        .admonition.#{$name} .admonition-title {
            background-color: #{$title-color};
        }
    }
    .admonition.#{$name} .admonition-title::before {
        -webkit-mask: url("/assets/img/icons/#{$icon}") no-repeat 50% 50%;
        mask: url("/assets/img/icons/#{$icon}") no-repeat 50% 50%;
        @if $icon-color {
            background-color: #{$icon-color};
        }
    }
}
```

## Assumptions

- General understanding of using a Linux terminal (command-line interface)
- `~ (tilde)` represents the $HOME (/home/username) of the current user when using BASH
- Steps prefixed with a “$” (dollar sign) represents the CLI (command-line interface) prompt
- Steps prefixed with a “#” (number sign) represents the CLI prompt with elevated user permissions (e.g. root)
- The text after the “$” or “#” is to be entered at the CLI
- Jekyll is already installed and configured
- The directory “project” represents the root of the website

## Add Admonitions To Jekyll
Install the admonition.html file to the _includes/ directory.
```shell
$ mv ~/Downloads/admonition.html /project/_includes/
```

Install the admonition.scss file to the _sass/ directory.
```shell
$ mv ~/Downloads/admonition.scss /project/_sass/
```

Edit style sheets to import admonition styles.
```shell
$ nano /project/assets/css/styles.scss
```

```shell
@import "admonition";
```

Add admonition icons.
```shell
$ mv ~/Downloads/*.svg /project/assets/img/icons/
```

```
pen-solid.svg
align-left-solid.svg
info-circle-solid.svg
fire-solid.svg
check-circle-solid.svg
question-circle-solid.svg
exclamation-triangle-solid.svg
times-circle-solid.svg
bolt-solid.svg
bug-solid.svg
list-ol-solid.svg
quote-right-solid.svg
```

## Usage
Adding an admonition to a post or page is a simple line of Liquid code. See the example of an info admonition below.

```liquid
{% include admonition.html type="info" title="Info" body="This is information intended to draw attention." %}
```

### Reference
- https://www.adamsdesk.com/posts/admonitions-jekyll/

