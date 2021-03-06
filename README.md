# Pythonista-Tweaks

## Installation

Download the repo in zip format and extract it, or `git clone` it using [stash](https://github.com/ywangd/stash). Then move or copy the `pythonista` folder into `site-packages`. If the module was installed correctly, you should be able to run the examples.

## Vision

* Bring together in one place everything possible with `UIApplication` and `objc_util`
* Make customising the Pythonista app similar to, and as easy as, using the `ui` module
 
## Notes

The code is now broken into several submodules:

* `pythonista.app` contains functions for setting the badge string/number, clearing the badge, and opening URLs in an `appex`-safe way.
* `pythonista.classes` is a proxy module that can be used to load Objective-C classes. For example `pythonista.classes.NSObject == objc_util.ObjCClass("NSObject")`.
* `pythonista.console` contains functions for getting the current and default console fonts.
* `pythonista.editor` contains the `Tab` and `WebTab` classes.
* `pythonista.shared` contains a few commonly used objects, such as the shared application and a few view controllers.

**Note:** Please do NOT use `from pythonista import *`, as this will cause name conflicts with the default `console` and `editor` modules. Instead, use it only with `import pythonista`, as this way the module's submodules will not overwrite Pythonista's default ones. It is fine to use `from pythonista.module import *` with all submodules except for `pythonista.classes`.

As of right now, each submodule contains only a small amount of functionality, but as they're expanded, the submodule approach will make much more sense.

`pythonista.editor` will hopefully eventually contain the classes for easily controlling the editor's look and feel. The structure of these submodules, as well as their names, is likely to change.

## Credits

* Based on examples posted on the forums by @omz, @JonB, @Webmaster4o, etc.