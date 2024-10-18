# PyAnnotate

__PyAnnotate__ is a quick and effective image cropping tool for annotation purposes. It is a implementation-type app for the underlying UI system (pyflexUI) I was developing for python for fun.

It automates the tedious task of cropping many small parts of a large image. It was made for semi-automating the task of annotating the large dataset of handwritten nepali characters to be used to train the OCR engine.

## How to use it ?
1. Run the `main.py` file with directory path of source images
    ```bash
    python main.py /path/to/images/
    ```
    e.g. `python main.py ./raw_images/`, `py main.py ../../data/images/`
2. Crop the parts
3. Enter name prefix for current crop's save filename
4. Enter the target directory
5. Submit to save the cropped images

## UI System (pyflexUI)

The actual UI system was written from scratch. It uses flex-box UI system for element rendering-info calculation in the UI-tree. Events are passed from top to bottom along the tree. Childs are rendered first, while events are handled at 2 different instances. Normal event processing is done by parents first and passed on to child. After the last child processes the event, then each parent processes late events while coming back up the UI-tree.

