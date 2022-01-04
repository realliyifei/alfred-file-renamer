<h1 align="center">
  <img src="./icon.png" width="128" height="128">
</h1>

# File Renamer (Mac Alfred Workflow)

This simple workflow lets you rename the string (i.e. filename) following the small-case-with-hyphen format, either in-place or via alfred box.  Also, it strips some unnesessary symbols like colon.

E.G. change `A guide: Comp Neuro.pdf` to  `a-guide-comp-neuro.pdf`. 

You can easily change the python snippet to use other title formats if needed.

Two ways to use it:

1. hotkey double-tapped SHIFT: rename the contents **in-place** where the cursor is
2. trigger keyword is `rn`: rename the contents from clipboard by alfred box

## Limitations

The input string doesn't support non-ASCII code (i.e. Chinese, etc.). 

## Download

Download alfredworkflow file directly from [the releases page](https://github.com/realliyifei/alfred-file-renamer/releases), make sure to download the latest release. 

## Software: Alfred (Mac)

![Alfred Logo](https://i.pinimg.com/originals/5c/23/a6/5c23a6723d3b19e892985fd918cf0aab.png)

The software can be downloaded [here](https://www.alfredapp.com/). You need to [buy the Powerpack](https://buy.alfredapp.com/) to use this workflow.

## Credit & Licence

* Core Library depends on the work-of-art-library [deanishe/alfred-workflow](https://github.com/deanishe/alfred-workflow)
