# Sed

Sed stand for stream editor.
it is use for 
* Searching
* Find and Replace
* Insert or Delete lines in a file or text stream


## Basic Usage (Syntax)
`sed [options] 'command' file`

you can also do 
`echo "text" | 'command'`

## Most Common `sed` Commands

|comand| Description| Example|
|------|------------|--------|
|s/pattern/replacement/|**Substitute** first match on a line| `sed` 's/cat/dog/'|
