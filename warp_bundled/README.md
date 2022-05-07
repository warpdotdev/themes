# Warp Themes

This is an open source repository with themes for [Warp](https://www.warp.dev/).
We welcome and appreciate any contributions!
Join our [Discord](https://discord.gg/warpdotdev), we have a channel dedicated to discussing custom themes.

We have [directions on how to use this repository in our documentation.](https://docs.warp.dev/features/themes)

## Custom Background Images

If want to use a custom background image, Warp supports either:

* a relative path to `~/.warp/themes`
* the absolute path to the background image

If your background image was under `~/.warp/themes/level_one/level_two/background_image.jpg` then the filepath in the yaml should be:

```yaml
background_image:
  path: level_one/level_two/background_image.jpg
```

## Contributing

tldr; After adding your theme run the python script for generating theme previews `./scripts/gen_theme_previews.py` like so:

`python3 ./scripts/gen_theme_previews.py standard`

for a newly added theme that's in the standard folder / directory. If you get the error that yaml is missing make sure you `pip install PyYAML`

There are more [directions on how to use this repository in our documentation.](https://docs.warp.dev/features/themes).

## Open source dependencies

We'd like to call out a few of the open source themes and repositories that helped bootstrap the set of themes for Warp:

* [iTerm colors pencil](https://github.com/mattly/iterm-colors-pencil)
* [Alacritty-theme](https://github.com/eendroroy/alacritty-theme)
* [base16-Alacritty](https://github.com/aarowill/base16-alacritty)
* [base16](https://github.com/chriskempson/base16)
* [Solarized](https://ethanschoonover.com/solarized/)
* [Dracula](https://draculatheme.com/)
* [Gruvbox](https://github.com/morhetz/gruvbox)

## What are base16 themes?

> An architecture for building themes based on carefully chosen syntax highlighting using a base of sixteen colors. Base16 provides a set of guidelines detailing how to style syntax and how to code a builder for compiling Base16 schemes and templates.

More on the details and structure here: [https://github.com/chriskempson/base16.](https://github.com/chriskempson/base16)

Base16 themes were sourced and auto-generated based on the Alacritty themes collected by @aarowill.
Repo: [https://github.com/aarowill/base16-alacritty](https://github.com/aarowill/base16-alacritty)

## What are standard themes?

In this directory you'll find themes popular among other tools, including Solarized, Dracula and others.

Themes in this directory were sourced and auto-generated based on the Alacritty themes collected by @eendroroy.
Repo: [https://github.com/eendroroy/alacritty-theme](https://github.com/eendroroy/alacritty-theme)
|Theme name | Preview|
| --- | --- |
|**[Cyber Wave](cyber_wave.yaml)**:|<img src='previews/cyber_wave.yaml.svg' width='300'>|
|**[Dark City](dark_city.yaml)**:|<img src='previews/dark_city.yaml.svg' width='300'>|
|**[Dracula](dracula.yaml)**:|<img src='previews/dracula.yaml.svg' width='300'>|
|**[Fancy Dracula](fancy_dracula.yaml)**:|<img src='previews/fancy_dracula.yaml.svg' width='300'>|
|**[Gruvbox Dark](gruvbox_dark.yaml)**:|<img src='previews/gruvbox_dark.yaml.svg' width='300'>|
|**[Gruvbox Light](gruvbox_light.yaml)**:|<img src='previews/gruvbox_light.yaml.svg' width='300'>|
|**[Jellyfish](jellyfish.yaml)**:|<img src='previews/jellyfish.yaml.svg' width='300'>|
|**[Koi](koi.yaml)**:|<img src='previews/koi.yaml.svg' width='300'>|
|**[Leafy](leafy.yaml)**:|<img src='previews/leafy.yaml.svg' width='300'>|
|**[Marble](marble.yaml)**:|<img src='previews/marble.yaml.svg' width='300'>|
|**[Pink City](pink_city.yaml)**:|<img src='previews/pink_city.yaml.svg' width='300'>|
|**[Red Rock](red_rock.yaml)**:|<img src='previews/red_rock.yaml.svg' width='300'>|
|**[Snowy](snowy.yaml)**:|<img src='previews/snowy.yaml.svg' width='300'>|
|**[Solarized Dark](solarized_dark.yaml)**:|<img src='previews/solarized_dark.yaml.svg' width='300'>|
|**[Solarized Light](solarized_light.yaml)**:|<img src='previews/solarized_light.yaml.svg' width='300'>|
|**[Warp](warp.yaml)**:|<img src='previews/warp.yaml.svg' width='300'>|
|**[Warp Dark](warp_dark.yaml)**:|<img src='previews/warp_dark.yaml.svg' width='300'>|
|**[Warp Light](warp_light.yaml)**:|<img src='previews/warp_light.yaml.svg' width='300'>|
|**[Willow Dream](willow_dream.yaml)**:|<img src='previews/willow_dream.yaml.svg' width='300'>|