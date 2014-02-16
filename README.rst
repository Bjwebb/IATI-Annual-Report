Instructions
============

* Run the data through https://github.com/Bjwebb/IATI-Preprocess/blob/master/bubble_hierachy.py
* Get this branch: https://github.com/Bjwebb/IATI-Transparency_Indicator/tree/annual-report-2014
    - Run ``php transparency_tests.php``
    - Run ``./transparency_tests_additional.sh``
* Symlink ``results`` and ``csv`` directories here
* Use https://chrome.google.com/webstore/detail/cookietxt-export/lopabhfecdfhgogdbojmaicoicjekelh to export a ``cookies.txt`` for https://docs.google.com/spreadsheet/ccc?key=0Auyp-i6eEk7EdDFkYm1aRXFJV2c1dXVxTjBHTndfclE&usp=drive_web to this directory
* Run ``./get.sh`` (this will populate the in directory with the spreadsheets from the above google doc)
* Run ``python3 add_transparency_indicator.py``

License
=======

The MIT License (MIT)

Copyright (c) 2014 Ben Webb <bjwebb67@googlemail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
