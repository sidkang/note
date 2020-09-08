# 自用AppleScript分享

## Office365联动

### Word全文中的高级替换及查找

```applescript
-- search for myText, replace with replText

-- Set&Get Keyboard Maestro variables
tell application "Keyboard Maestro Engine"
	set myText to getvariable "theText"
	set replText to "2020年某个月"
end tell

tell application "Microsoft Word"
	activate
	
	set findList to {}
	
	(* Main *)
	set myFind to find object of text object of active document
	set findList to findList & {myFind}
	
	(*Headers & Footers *)
	-- Create list of all sections in active document
	-- set lstSections to every section of active document
	repeat with currSection in (get sections of active document)
		-- Create list of all headers and footers in active document
		set lstHeaderFooters to {get header currSection index header footer primary} & {get header currSection index header footer first page} & {get header currSection index header footer even pages} & {get footer currSection index header footer primary} & {get footer currSection index header footer first page} & {get footer currSection index header footer even pages}
		-- Loop through all headers and footers
		repeat with currHeaderFooter in lstHeaderFooters
			set myFind to find object of text object of currHeaderFooter
			set findList to findList & {myFind}
			
			-- Create list of all shapes in header and footer
			set lstShapes to (every shape of currHeaderFooter)
			-- Loop through all shapes in header and footer
			repeat with currShape in lstShapes
				if has text of (text frame of currShape) then
					set myFind to find object of text range of text frame of currShape
					set findList to findList & {myFind}
				end if
			end repeat
		end repeat
	end repeat
	
	(* Footnotes *)
	-- Create list of all footnotes in active document
	set lstFtNotes to every footnote of active document
	-- Loop through all footnotes
	repeat with currFtnote in lstFtNotes
		set myFind to find object of text object of currFtnote
		set findList to findList & {myFind}
	end repeat
	
	(* Endnotes *)
	-- Create list of all endnotes in active document
	set lstEndNotes to every endnote of active document
	-- Loop through all endnotes
	repeat with currEndnote in lstEndNotes
		set myFind to find object of text object of currEndnote
		set findList to findList & {myFind}
	end repeat
	
	(* Shapes *)
	-- Create & Loop list of all shapes in main document
	repeat with currShape in (get shapes of active document)
		set theTextFrame to (text frame of currShape)
		if has text of (text frame of currShape) then
			set myFind to find object of text range of text frame of currShape
			set findList to findList & {myFind}
		end if
	end repeat
	
	(* Find & Replace *)
	repeat with myFind in findList
		clear formatting myFind
		set content of myFind to myText
		--set underline of font object of myFind to true
		
		clear formatting replacement of myFind
		set content of replacement of myFind to replText
		set italic of font object of replacement of myFind to true
		set subscript of font object of replacement of myFind to false
		
		set match whole word of myFind to true
		execute find myFind replace replace all
	end repeat
end tell
```

### 

```applescript
tell application "Microsoft Excel"
	activate
	open "/Users/kang/dev/ccx/scripts/THE_FILE.xlsx"
	--activate object chart object "Chart 1" of sheet 1
	copy object chart object "Chart 1" of worksheet "原始权益人分布"
	--copy object active chart
	close workbooks
	quit
end tell


tell application "Microsoft Word"
	activate
    -- only applied to object in sheet cells
	select text object of cell 1 of row 2 of table 2 of active document
	paste object text object of selection
end tell

```