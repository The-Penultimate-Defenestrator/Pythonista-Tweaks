"""Methods relating to the console."""

from . import shared

__all__ = [
	"getConsoleFont",
	"getDefaultFont",
]

@on_main_thread
def getConsoleFont():
	"""Return the font name and size that is currently active for the console."""
	
	shared.consoleVC.view()
	desc = consoleVC.outputFont().fontDescriptor()
	font = [str(desc.objectForKey_(a)) for a in ("NSFontNameAttribute", "NSFontSizeAttribute")]
	font[1] = int(font[1])
	return font

@on_main_thread
def getDefaultFont():
	"""Get the user default for console font."""
	
	return [str(userDefaults.stringForKey_("OutputFontName")), userDefaults.integerForKey_("OutputFontSize")]