---
title: Admonitions Documentation  
date: 2023-08-23 15:33:39
catagories: [cheatsheets, documentation]
tags: [docs, cheatsheets]
---

> **Note**
> It appears a note in MarkDown is not possible currently.
> Reference: https://talk.commonmark.org/t/github-is-beta-testing-their-own-admonition-syntax-we-should-weigh-in/4173

GitHub Link: https://github.com/javalent/admonitions

# Obsidian Admonition

Adds admonition block-styled content to Obsidian.md, styled after [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

## Please note!

Obsidian 0.14 adds support for [Callout boxes](https://help.obsidian.md/Editing+and+formatting/Callouts)!

**With this change, Admonitions will be transitioning to a plugin that enhances the core callout box feature.**

What does this mean, you might ask?

1.  All of your existing code block admonitions will continue to work, and will always work!
2.  You can continue to use Admonitions to create custom types, and all of your custom types will just work as a callout, without you having to do anything!
3.  If you have any Microsoft Document syntax admonitions, they will have to be converted to the new callout box syntax - there is a button in Admonition settings to auto-convert these for you.
4.  You can use Admonitions to set default titles, default collapse states, or defaulting to not having a title.
5.  Admonitions adds helpful editor suggestors for quickly entering your custom callout boxes.
6.  Admonitions adds helpful commands for inserting callout boxes, including the ability to register commands for specific types.

## Usage

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/all.gif)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/all.gif)

Place a code block with the admonition type:

```ad-important
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.
```

Becomes:

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/default.png)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/default.png)

## Options

```ad-<type> # Admonition type. See below for a list of available types.
title:                  # Admonition title.
collapse:               # Create a collapsible admonition.
icon:                   # Override the icon.
color:                  # Override the color.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.
```

Please note that as of **4.4.1**, the `title`, `collapse`, `icon` and `color` parameters must be at the _top_ of the block, in any order.

### Title

The admonition will render with the type of admonition by default. If you wish to customize the title, you can do so this way:

```ad-note
title: Title
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.
```

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/title.png)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/title.png)

Custom titles are rendered as Markdown, so they support the full Obsidian Markdown syntax.

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/title-markdown.png)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/title-markdown.png)

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/rendered-title-markdown.png)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/rendered-title-markdown.png)

Leave the title field blank to only display the admonition.

```ad-note
title:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.
```

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/no-title.png)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/no-title.png)

### Collapsible

Use the `collapse` parameter to create a collapsible admonition.

`collapse: open` will start the admonition opened on render, but allow collapse on click.

If a blank title is provided, the collapse parameter will not do anything.

Admonitions may be set to be collapsible by default in settings.

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/collapse.gif)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/collapse.gif)

### Icon

The admonition icon can be overridden using the `icon` parameter. **The icon name entered must be the exact icon name from FontAwesome or RPGAwesome.**

````
```ad-note
icon: triforce

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.

```
````

### Color

The admonition color can be overridden using the `color` parameter. **The color entered must be an RGB triad.**

````
```ad-note
color: 200, 200, 200

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod nulla.

```
````

### No Content

An admonition with no content will render as just the title block.

````
```ad-note
```
````

## Nesting Admonitions

Nesting admonitions may be done by increasing the number of backticks.

Example:

``````
`````ad-note
title: Nested Admonitions
collapse: open

Hello!

````ad-note
title: This admonition is nested.
This is a nested admonition!

```ad-warning
title: This admonition is closed.
collapse: close
```

````

This is in the original admonition.
`````
``````

## Rendering Code Blocks inside Admonitions

Code blocks may be nested inside admonitions using a method similar to [Nesting Admonitions](https://github.com/javalent/admonitions#Nesting-Admonitions) above.

Additionally, for a single layer, the `~~~` markdown codeblock syntax may be used:

`````
````ad-info

```ad-bug
title: I'm Nested!
~~~javascript
throw new Error("Oops, I'm a bug.");
~~~
```

```javascript
console.log("Hello!");
```

````
`````

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/nested-code.png)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/nested-code.png)

## Admonition Types

The following admonition types are currently supported:

Type

Aliases

note

note, seealso

abstract

abstract, summary, tldr

info

info, todo

tip

tip, hint, important

success

success, check, done

question

question, help, faq

warning

warning, caution, attention

failure

failure, fail, missing

danger

danger, error

bug

bug

example

example

quote

quote, cite

See [this](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) for a reference of what these admonitions look like.

The default admonitions are customizable by creating a user-defined admonition of the same name.

## Custom Admonitions & Callouts

Custom admonitions may be created in settings. Creating a custom admonition will also enable it to be used as an Obsidian callout.

Creating a new admonition requires three things: the type, the icon to use, and the color of the admonition.

Only one admonition of each type may exist at any given time; if another admonition of the same type is created, it will override the previously created one.

If a default admonition is overridden, it can be restored by deleting the user-defined admonition.

Please note that by default, the background color of the title is simply the color of the admonition at 10% opacity. CSS must be used to update this.

### Images as Icons

Images can be uploaded to use as an admonition icon instead of an icon from a downloaded icon set.

These images will be resized to 24px x 24px to be stored in the plugin's saved data.

To remove an image icon, simply choose an icon in the icon chooser text box.

## Global Commands

Several commands are available for the plugin by default.

### Collapse and Open All Admonitions In Note

If these two commands are triggered with an open note, all collapsible admonitions will be collapsed or open respectively.

### Insert Admonition

This will open a modal where the admonition type, title and collapse behavior can be set, then the generated admonition code block will be inserted into the open editor.

### Admonition-specific commands

Commands may be registered for each [custom admonition](https://github.com/javalent/admonitions#custom-admonition-types) type to insert them into an open note by clicking the `Register Commands` button in [Settings](https://github.com/javalent/admonitions#custom-admonition-types).

3 commands will be registered: `Insert <type> Callout`, `Insert <type>`, and `Insert <type> with Title`.

#### Insert Callout

The selected type will be inserted as an Obsidian callout, and any selected text will be included with it.

#### Insert

The selected type will be inserted as a codeblock admonition, and any selected text will be included with it.

#### Insert with Title

The selected type will be inserted as a codeblock admonition, and any selected text will be included with it. The `title:` parameter will also be added and the cursor will be placed at that line.

### Mermaid Graphs

Mermaid graphs are supported by Admonitions, but with some caveats:

1.  You cannot combine mermaid graphs and embeds/transclusions.
2.  Mermaid graphs do not work in collapsed-by-default admonitions.

## Non-code block Admonitions

> ❗ This syntax has been officially removed as of Admonitions 7.0.0.
> 
> Use the [Obsidian Callout box](https://help.obsidian.md/Editing+and+formatting/Callouts) syntax instead!

As of version 6.0.0, there is a new setting: Enable Non-codeblock Admonitions.

This setting is highly experimental and may not work as expected, and there are a few caveats listed at the end of this section to keep in mind.

This setting allows for creating an admonition without wrapping it in a code block, which means that links and tags will sync into Obsidian's cache. A non-codeblock admonition may be created using the following syntax:

```

!!! ad-<type> Title goes here!

content

--- admonition

```

This will create the appropriate admonition type, embed the content, and give it the supplied title.

### Titles

Titles should be placed after the admonition block. Currently, markdown in titles is not supported.

An empty title can be created by either placing two spaces after the admonition type:

```

!!! ad-<type>

content

--- admonition

```

or by placing empty double quotes:

```

!!! ad-<type> ""

content

--- admonition

```

### Collapsible

A collapsible admonition may be created using the following syntax:

```

??? ad-<type> Title goes here!

content

--- admonition

```

A collapsible admonition may default to "open" by appending a +:

```

???+ ad-<type> Title goes here!

content

--- admonition

```

### Caveats

1.  Changes to the admonition after render require the cache to be cleared. The note must be closed and re-opened (and sometimes, a different note must be opened first).
    1.  This is _all_ changes, including the admonition type, title, content, even whether or not a collapsible admonition is open or closed initially.
2.  Nested admonitions are not currently supported.

If you experience any bugs using this setting, please create an issue and I will look into them.

## Microsoft Document Syntax

> ❗ This syntax has been officially removed as of version **8.0.0**.
> 
> Use the [Obsidian Callout box](https://help.obsidian.md/Editing+and+formatting/Callouts) syntax instead!

As of v6.8.0, an additional non-code block syntax can be used that is inspired by the [Microsoft Document Syntax](https://docs.microsoft.com/en-us/contribute/markdown-reference) to render admonitions.

> **⚠️ Please note:**
> 
> Unlike the Microsoft Document Syntax, the type is not required to be upper case.
> 
> The plugin will use an exact-match first, then try to find a case-insensitive match.

> [!quote]
> This is an admonition!

[![](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/msdocs.png)](https://raw.githubusercontent.com/valentine195/obsidian-admonition/master/images/msdocs.png)

This syntax can also be used on indented code blocks:

    [!quote]
    This is an admonition!

### Title

A title can be added to the MSDoc-style admonition by appending it after the type.

> [!quote: This is the title!]
> This is an admonition!

Like the code block syntax, providing an empty title will remove the title from the rendered admonition.

> [!quote:]
> This admonition won't have a title!

### Collapse

Collapse can be set by appending the following characters after the brackets:

Character

Collapse Type

`+`

`open`

`-`

`closed`

`x`

`none`

## Publish

Obsidian plugins do not work on publish sites; however, version 6.4.0+ has an option to generate a JavaScript file that can be used on Publish sites with **custom domains**.

**Obsidian Publish only allows external JavaScript on publish sites with custom domains. If your Publish is ran through Obsidian, this will not work.**

Instructions:

1.  Go the Admonition settings tab and click the "Generate JS for Publish" button.
2.  Save the JavaScript file.
3.  Copy the contents of the JS file to your `publish.js` file.
4.  Add the contents of the `assets/main.css` file to your `publish.css` file.

Please note that I can give no guarantees of stability on your publish site. Other JavaScript you include may conflict with this file. If you run into an issue using it, please create an issue on this repository and I will try to help you.

## Icon Packs

Additional icon packs can be downloaded in settings.

### Adding Icon Packs

Want to add an existing icon pack? Make a pull request with the following:

1.  Add a new folder in the [icons](https://github.com/javalent/admonitions/blob/main/icons) folder with the name of your icon set.
2.  Create an `icons.json` file that has the icons defined as an Object. Please see the [Octicons json](https://github.com/javalent/admonitions/blob/main/icons/octicons/icons.json) for reference.
3.  Put your icon pack's information in the two variables in the [Icon Packs](https://github.com/javalent/admonitions/blob/main/src/icons/packs.ts) file.

# Settings

## Custom Admonition Types

[Custom admonition](https://github.com/javalent/admonitions#custom-admonitions--callouts) types can be created and managed in this section of the settings.

### Export Custom Types as CSS

This button will generate a CSS snippet that you can save and use for your custom callout types.

## Importing Custom Admonitions

Custom admonitions can be imported in settings from a JSON array of definitions.

At a _minimum_, you only need a valid admonition type:

[
    {
        "type": "my-custom-type"
    }
]

This will use the `pencil-alt` FontAwesome icon and a random color, and set all other properties as false.

However, you can specify an icon and color as well:

[
    {
        "type": "my-custom-type",
        "icon": "globe",
        "color": "120,120,120"
    }
]

If you want to specify an icon pack, you can do so like this:

[
    {
        "type": "my-custom-type",
        "icon": {
            "name": "globe",
            "type": "font-awesome"
        },
        "color": "120,120,120"
    }
]

All of the possible fields are defined [here](https://github.com/valentine195/obsidian-admonition/blob/2fb38ccc0b39ada8d3d0a4476e9ff3333c52c3ae/src/%40types/index.d.ts#L5).

## Admonition Settings

Settings specific to admonitions are managed in this section.

### Add Drop Shadow

A drop shadow will be added to admonitions by default.

If this setting is off, rendered admonitions will receive the `.no-drop` class.

### Collapsible By Default

All admonitions will be collapsible by default, unless `collapse: none` is set in the admonition parameters.

### Default Collapse Type

> ⚠️ This setting is only available when Collapsible By Default is true.

Set the default collapse type used when setting an admonition collapsible by default.

### Add Copy Button

A "Copy Content" button will be added to the top-right corner of the admonition & callout content.

### Parse Titles as Markdown

Turn this setting off to prevent admonition titles from being rendered as markdown.

### Set Admonition Colors

Controls whether or not a rendered admonition will receive a color.

Turn this off to totally control color via CSS.

### Hide Empty Admonitions

Admonitions with no content are hidden by default.

> ⚠️ Please note that this only works for Admonitions that have _no text content whatsoever_.

## Icon Packs

### Use Font Awesome Icons

The plugin comes pre-bundled with the entire [Font Awesome Free](https://fontawesome.com/search?m=free&s=brands%2Cregular%2Csolid) icon set. Turn this setting off to not include them in the icon picker.

Existing custom Admonitions that use Font Awesome icons will continue to work.

### Additional Icon Packs

Additional icon packs can be downloaded to supplement the included Font Awesome Free icon set.

**Downloading an icon pack requires an internet connection.**

Current additional icon packs available are the [Octicons](https://primer.style/octicons/) set and the [RPG Awesome](https://nagoshiashumari.github.io/Rpg-Awesome/) set.

> 📝 For backwards compability, if an Admonition was created prior to version **7.0.0** using an RPG Awesome icon, the pack will try to be downloaded.

## Additional Syntaxes

Obsidian 0.14 has introduced [Callout boxes](https://help.obsidian.md/Editing+and+formatting/Callouts) to its core functionality using a similar syntax to the Microsoft Document callouts.

This has rendered the Microsoft Document syntax for Admonitions obsolete, but Admonitions can still be used to create and manage your custom callout types.

Your existing code block Admonitions will always work!

### Enable Non-codeblock Admonitions

> ❗ This setting has been removed as of version **7.0.0**.
> 
> It is recommended to use the [Obsidian Callout box](https://help.obsidian.md/Editing+and+formatting/Callouts) instead.

Enabled use of `!!! ad-<type>` style admonitions. No longer supported, will be removed in a future version.

### Allow Microsoft Document Syntax

> ❗ This syntax has been officially removed as of version **8.0.0**.
> 
> Use the [Obsidian Callout box](https://help.obsidian.md/Editing+and+formatting/Callouts) syntax instead!

Enables use of the [Microsoft Document Syntax](https://github.com/javalent/admonitions#microsoft-document-syntax) for blockquote admonitions.

### Use Microsoft Document Syntax for Indented Code Blocks

> ❗ This syntax has been officially removed as of version **8.0.0**.
> 
> Use the [Obsidian Callout box](https://help.obsidian.md/Editing+and+formatting/Callouts) syntax instead!

Enables use of the [Microsoft Document Syntax](https://github.com/javalent/admonitions#microsoft-document-syntax) for indented code blocks.

### Render Microsoft Document Syntax in Live Preview

> ❗ This syntax has been officially removed as of version **8.0.0**.
> 
> Use the [Obsidian Callout box](https://help.obsidian.md/Editing+and+formatting/Callouts) syntax instead!

Enables use of the [Microsoft Document Syntax](https://github.com/javalent/admonitions#microsoft-document-syntax) in live preview.

This feature is still under development and you may experience rendering bugs.

### Convert MSDoc Admonitions to Callouts (**v8.0.0+**)

This button can be used to convert any existing Microsoft Document syntax Admonitions to the new [Callout box](https://help.obsidian.md/Editing+and+formatting/Callouts) syntax.

## Advanced Settings

### Markdown Syntax Highlighting

Enable syntax highlighting when editing admonition code blocks.

### Sync Links to Metadata Cache

The plugin will attempt to syncronize links to the metadata cache to be displayed in graph view.

This setting is experimental. Links will only be synced when rendered in an admonition and they will not persist if you close and re-open Obsidian.

Please see [this issue](https://github.com/valentine195/obsidian-admonition/issues/144) for more information.

If you require links to be fully synced, it is recommended to use the [Microsoft Document Syntax](https://github.com/javalent/admonitions#microsoft-document-syntax).

### Generate JS for Publish

Use this setting to enable Admonitions on custom-domain Obsidian Publish websites.

See [Publish] for more information.

# Todo

No additional features are planned at this time. If there is a feature missing that you would like to see, please open an issue.

-    Add the ability to collapse the admonition
-    Custom admonitions
-    Settings tab to customize icon and color of all admonitions
-    Ability to render markdown inside an admonition

# Installation

## From within Obsidian

From Obsidian v0.9.8, you can activate this plugin within Obsidian by doing the following:

-   Open Settings > Third-party plugin
-   Make sure Safe mode is **off**
-   Click Browse community plugins
-   Search for this plugin
-   Click Install
-   Once installed, close the community plugins window and activate the newly installed plugin

## From GitHub

-   Download the Latest Release from the Releases section of the GitHub Repository
-   Extract the plugin folder from the zip to your vault's plugins folder: `<vault>/.obsidian/plugins/`  
    Note: On some machines the `.obsidian` folder may be hidden. On MacOS you should be able to press `Command+Shift+Dot` to show the folder in Finder.
-   Reload Obsidian
-   If prompted about Safe Mode, you can disable safe mode and enable the plugin. Otherwise head to Settings, third-party plugins, make sure safe mode is off and enable the plugin from there.

### Updates

You can follow the same procedure to update the plugin

# Warning

This plugin comes with no guarantee of stability and bugs may delete data. Please ensure you have automated backups.
