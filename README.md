# Warp Themes

This is an open-source repository with themes for [Warp](https://www.warp.dev/). We welcome and appreciate any contributions! Join our [Discord](https://discord.gg/warpdotdev), we have a channel dedicated to discussing custom themes.

We have [directions on how to use this repository in our documentation.](https://docs.warp.dev/features/themes/custom-themes)

## Custom Background Images

Warp supports setting background images, set the path to your background image in your themes `.yaml` file:

- A relative path to `~/.warp/themes/background.jpg`
- The absolute path to the background image `/Users/my_user/Documents/background.jpg`

If your background image was under `~/.warp/themes/level_one/level_two/background_image.jpg` then the file path in the yaml should be:

```yaml
background_image:
  # background image credit: https://unsplash.com/photos/0eKCOZ11gfk
  path: "level_one/level_two/background_image.jpg"
```

## Contributing

TLDR; After adding your theme run the python script for generating theme previews `./scripts/gen_theme_previews.py` like so:

`python3 ./scripts/gen_theme_previews.py standard`

for a newly added theme that's in the standard folder/directory. If you get the error that yaml is missing make sure you `pip install PyYAML`

There are more [directions on how to use this repository in our documentation.](https://docs.warp.dev/features/themes).

## Open source dependencies

We'd like to call out a few of the open source themes and repositories that helped bootstrap the set of themes for Warp:

- [iTerm colors pencil](https://github.com/mattly/iterm-colors-pencil)
- [Alacritty-theme](https://github.com/alacritty/alacritty-theme)
- [base16-Alacritty](https://github.com/aarowill/base16-alacritty)
- [base16](https://github.com/chriskempson/base16)
- [Solarized](https://ethanschoonover.com/solarized/)
- [Dracula](https://draculatheme.com/)
- [Gruvbox](https://github.com/morhetz/gruvbox)

## What are base16 themes?

> An architecture for building themes based on carefully chosen syntax highlighting using a base of sixteen colors. Base16 provides a set of guidelines detailing how to style syntax and how to code a builder for compiling Base16 schemes and templates.

More on the details and structure here: [https://github.com/chriskempson/base16.](https://github.com/chriskempson/base16)

Base16 themes were sourced and auto-generated based on the Alacritty themes collected by @aarowill. Repo: [https://github.com/aarowill/base16-alacritty](https://github.com/aarowill/base16-alacritty)

## What are standard themes?

In this directory, you'll find themes popular among other tools, including Solarized, Dracula, and others.

Themes in this directory were sourced and auto-generated based on the Alacritty themes collected by @eendroroy. Repo: [https://github.com/eendroroy/alacritty-theme](https://github.com/eendroroy/alacritty-theme)

## What are holiday themes?

We made holiday themes to celebrate various holidays during the calendar year.

## What are warp_bundled themes?

These are the themes that ship directly with Warp.
