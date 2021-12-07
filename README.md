# Warp Themes
This is a repository with themes for [Warp](https://www.warp.dev/).

## 1. How do I use a custom theme in Warp?
To start, create a config directory in your home directory:
```
mkdir -p ~/.warp/themes
```
Note that it may take several minutes for Warp to initially discover the new config directory.
You can either wait, or just restart the application.
After that step, all future changes to `~/.warp/themes` directory will be reflected in Warp within seconds.

Add your new custom theme yaml theme file to this directory:
```
cp ~/Downloads/my_awesome_theme.yaml ~/.warp/themes
```
Open the Settings menu (top right corner or `⌘-,`), and choose Select Theme. Your new theme should now be visible on the list of available themes. Click & confirm, and you're set!


## 2. How do I use this repo?
This repository is a collection of themes that you can use right away in Warp. 
It's split into two parts:
- [base16 themes](./base16/README.md)
- [standard themes](./standard/README.md)

You can select themes from either of those locations, depending on your preferences.
You can find previews of each of the available themes in the README of each directory.

The main difference between "standard" and "base16" themes is that "standard" themes follow the typical color setup, while "base16" themes follow the framework suggested by [@chriskempson](https://github.com/chriskempson/base16).
Some of the standard themes have their "base16" version available in the repo as well.

To install a theme from this repo you can:

- download just a single file and follow the steps from (1)
- clone the entire repo and run `mv <your_clone_location>standard/* ~/.warp/themes && mv <your_clone_location>base16/* ~/.warp/themes` to use all of the available themes

## 3. How do I write my own custom theme?

A custom theme in Warp has the following yml structure:

```yaml
# Accent color for UI elements
accent: '#268bd2'
# Terminal background color
background: '#002b36'
# Whether the theme is lighter or darker.
details: darker
# The foreground color.
foreground: '#839496'
# Ansi escape colors.
terminal_colors:
  bright:
    black: '#002b36'
    blue: '#839496'
    cyan: '#93a1a1'
    green: '#586e75'
    magenta: '#6c71c4'
    red: '#cb4b16'
    white: '#fdf6e3'
    yellow: '#657b83'
  normal:
    black: '#073642'
    blue: '#268bd2'
    cyan: '#2aa198'
    green: '#859900'
    magenta: '#d33682'
    red: '#dc322f'
    white: '#eee8d5'
    yellow: '#b58900'
```

Each color is represented in hex and must start with with '#'.

`background`, `foreground`, `accent` and `details` are Warp-specific. 
The accent color is the one used for highlights in Warp's UI, while `details` describe what detailing options in our UI should we pick for the given theme. Options are `darker` (typically used for dark themes) or `lighter` (typically used for light-mode themes). 
`terminal_theme` represents the collection of normal & bright colors (16 total) known from other terminal themes (ansi colors).

## 4. Background Images and Gradients
You can now add a gradient or use a custom background in Warp.

### Background Images YAML Config
To add a background image you can use this attribute: "background_image:" with the name of the image you want to use as the background.
Note: Warp currently only supports images with the *.jpg* file format.
Here is what the .yaml config looks like:

```
# Accent color for UI elements
accent: '#268bd2'
# Terminal background color
background: '#002b36'
# Whether the theme is lighter or darker.
details: darker
# The foreground color.
foreground: '#839496'
# Ansi escape colors.

############################################################### SEE BELOW
# Background Images
background_image:
  # we currently (2021 Nov) only support jpg formats (.jpeg, .jpg, .JPEG)
  # the path is relative to ~/.warp/themes/
  # the full path to the picture is: ~/.warp/themes/warp.jpg
  path: warp.jpg 

  # this is the opacity value
  opacity: 60
############################################################### SEE ABOVE 

terminal_colors:
  bright:
    black: '#002b36'
    blue: '#839496'
    cyan: '#93a1a1'
    green: '#586e75'
    magenta: '#6c71c4'
    red: '#cb4b16'
    white: '#fdf6e3'
    yellow: '#657b83'
  normal:
    black: '#073642'
    blue: '#268bd2'
    cyan: '#2aa198'
    green: '#859900'
    magenta: '#d33682'
    red: '#dc322f'
    white: '#eee8d5'
    yellow: '#b58900'
```

### Gradients

To set up a gradient, instead of using a single accent or background value ('#268bd2' in example above).
You can create a sub-level (one indention) with two sub-values either "left" and "right" for horizontal gradients or "top" and "bottom" for vertical gradients.
Like so:

```yaml
accent:
  top: #abcdef
  bottom: #fedcba
```

```yaml
accent:
   left: #abcdef
   right: #fedcba
```

You can also do this for backgrounds.
Here's a full yaml file with gradients set for both background and accent:

```yaml
################################ See below 
# accent has a gradient
accent:
  left: '#474747'
  right: '#ffffff'
# background has a gradient
background: 
  top: '#474747'
  bottom: '#ffffff'
################################ See above
# Whether the theme is lighter or darker.
details: darker
# The foreground color.
foreground: '#839496'
# Ansi escape colors.
terminal_colors:
  bright:
    black: '#002b36'
    blue: '#839496'
    cyan: '#93a1a1'
    green: '#586e75'
    magenta: '#6c71c4'
    red: '#cb4b16'
    white: '#fdf6e3'
    yellow: '#657b83'
  normal:
    black: '#073642'
    blue: '#268bd2'
    cyan: '#2aa198'
    green: '#859900'
    magenta: '#d33682'
    red: '#dc322f'
    white: '#eee8d5'
    yellow: '#b58900'
```

## 5. Contributing

Feeling like your designer wants to share your own take on Warp theming? Any contributions to this repo are greatly appreciated - help us spread the ♥ of Warp!

1: Fork the project
2: Create your branch (`git checkout -b theme/AwesomeTheme`)
3: Regenerate thumbnails:

```sh
# assuming you're adding the theme to `standard` directory:
python3 ./scripts/gen_theme_previews.py standard/ standard/ ./scripts/preview.svg ./standard/README.md-intro
```

4: Commit your changes (`git commit -m 'This theme is awesome'`)
5: Push to the branch (`git push origin`)
6: Open a pull request

## 5. Contact & more Warp information

Have feedback or suggestion for this repo? Please, file an issue.

All other Warp-related things can be discussed in [Warp official repo](https://github.com/warpdotdev/warp) or our [Discord server](https://discord.gg/T2p5xFgpjr).

## 6. FAQ

Frequently Asked Questions

### Is this a final format for the configuration?

The format itself will expand but we don't forsee any breaking changes to current themes. We also plan on supporting sharing/creating custom themes directly within Warp.

## 7. Open source dependencies

We'd like to call out a few of the open source themes and repositories that helped bootstrap the set of themes for Warp:

- [iTerm colors pencil](https://github.com/mattly/iterm-colors-pencil)
- [Alacritty-theme](https://github.com/eendroroy/alacritty-theme)
- [base16-Alacritty](https://github.com/aarowill/base16-alacritty)
- [base16](https://github.com/chriskempson/base16)
- [Solarized](https://ethanschoonover.com/solarized/)
- [Dracula](https://draculatheme.com/)
- [Gruvbox](https://github.com/morhetz/gruvbox)
