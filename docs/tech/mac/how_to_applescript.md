# UI Scripting via AppleScript

## Preface

Enable AppleScript Accessbility in the System Settings

## Example - How to Xnip's Start Capture via AppleScript

```applescript
>>> tell application "System Events" to get every process whose name contains "Xnip"
# Result
{application process "Xnip" of application "System Events",
 application process "XnipHelper" of application "System Events"}
```

```applescript
>>> tell application "System Events" to tell process "Xnip" to get every menu bar
# Result
{menu bar 1 of application process "Xnip" of application "System Events",
 menu bar 2 of application process "Xnip" of application "System Events"}
```

menu bar 1 is the menu bar containing the Apple Menu (Apple Menu) in the top-left.  menu bar 2 (if it exists) will be the menu bar containing the application icon.

```applescript
tell application "System Events" to tell process "Xnip"
	tell menu bar item 1 of menu bar 2
        # need to activate the menu item
		click
		get menu items of menu 1
	end tell
end tell
# Result
{
    menu item "Start Capture" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "Open…" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "Open from Clipboard" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "Preferences…" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "Visit the Xnip Website..." of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "Feedback & Support…" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "Rate…" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "About Xnip" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events",
    menu item "Quit Xnip" of menu 1 of menu bar item 1 of menu bar 2 of application process "Xnip" of application "System Events"
}
```

```applescript
tell application "System Events" to tell process "Xnip"
	
	set xnip to menu bar item 1 of menu bar 2
	ignoring application responses
		click xnip
	end ignoring
end tell

do shell script "killall System\\ Events"
delay 0.1
tell application "System Events" to tell process "Xnip"
	
	tell xnip
		click
		click menu item "Start Capture" of menu 1
	end tell
end tell
```