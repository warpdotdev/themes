# Warp Themes
This is a repository with themes for [Warp terminal](https://www.warp.dev/).

## 1. How to use a custom theme in Warp?
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
and open your Settings panel (top right corner), and choose Select Theme. Your new theme should now be visible on the list of available themes. Click & confirm, and you're set!


## 2. How to use this repo?
This repository is a collection of themes that you can use right away in your Warp terminal. 
It's split into two parts:
- [base16 themes](./base16/README.md)
- [standard themes](./standard/README.md)

You can select themes from either of those locations, depending on your preferences.
You can find previews of each of the available themes in the directories' README.

Main difference between "standard" and "base16" themes is that "standard" themes follow the typical color setup, while "base16" themes follow the framework suggested by [@chriskempson](https://github.com/chriskempson/base16).
Some of the standard themes have their "base16" version available in the repo as well.

To install a theme from this repo you can:
- download just a single file and follow the steps from (1)
- clone entire repo and run `mv <your_clone_location>standard/* ~/.warp/themes && mv <your_clone_location>base16/* ~/.warp/themes` to use all of the available themes

## 3. How to write your own custom theme?
A custom theme can be described as the following structure:
```
struct WarpTheme {
  background: Color,
  foreground: Color,
  accent: Color,
  details: "darker" | "lighter",
  terminal_colors: TerminalColors,
}

struct TerminalColors {
  normal: Colors,
  bright: Colors,
}

struct Colors {
  black: Color,
  blue: Color,
  cyan: Color,
  green: Color,
  magenta: Color,
  red: Color,
  white: Color,
  yellow: Color,
}
```

`Color` is an RGB color that's serialized to / deserialized from hexadecimal color representation. It starts with '#'.

First elements, `background`, `foreground`, `accent` and `details` are Warp-specific. 
Accent color is the one used for highlights in Warp's UI, while `details` describe what detailing options in our UI should we pick for the given theme. Options are `darker` (perfect for dark themes) or `lighter` (perfect for light-mode themes).

`WarpTheme` is represented in yaml files.

Example:
```
cat ~/.warp/themes/solarized_dark.yaml

accent: '#268bd2'
background: '#002b36'
details: darker
foreground: '#839496'
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

## 4. Contributing
Feeling like your designer wants to share your own take on Warp theming? Any contributions to this repo are greatly appreciated - help us spread the ♥ of Warp!

1. Fork the project
2. Create your branch (`git checkout -b theme/AwesomeTheme`)
3. Regenerate thumbnails:
```
# assuming you're adding the theme to `standard` directory:
python3 ./scripts/gen_theme_previews.py standard/ standard/ ./scripts/preview.svg ./standard/README.md-intro
```
4. Commit your changes (`git commit -m 'This theme is awesome`)
5. Push to the branch (`git push origin`)
6. Open a pull request

## 5. Contact & more Warp information
Have feedback or suggestion for this repo? Please, file an issue.

All other Warp-related things can be discussed in [Warp official repo](https://github.com/warpdotdev/warp) or our [Discord server](https://discord.gg/T2p5xFgpjr).


## 6. FAQ

### Themes are cool, but will I be able to do more?
Yes! We've already shared some more mocks with our community on Discord showcasing background images, gradients and other options for themes.
Stay tuned, as we continue iterating on those!

### Is this a final format for the configuration?
The format itself will expand (background images, gradients) but we don't forsee any breaking changes to current themes.

