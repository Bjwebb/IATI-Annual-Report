* Run the data through https://github.com/Bjwebb/IATI-Preprocess/blob/master/bubble_hierachy.py
* Get this branch: https://github.com/Bjwebb/IATI-Transparency_Indicator/tree/annual-report-2014
    - Run ``php transparency_tests.php``
    - Run ``./transparency_tests_additional.sh``
* Symlink ``results`` and ``csv`` directories here
* Use https://chrome.google.com/webstore/detail/cookietxt-export/lopabhfecdfhgogdbojmaicoicjekelh to export a ``cookies.txt`` for https://docs.google.com/spreadsheet/ccc?key=0Auyp-i6eEk7EdDFkYm1aRXFJV2c1dXVxTjBHTndfclE&usp=drive_web to this directory
* Run ``./get.sh`` (this will populate the in directory with the spreadsheets from the above google doc)
* Run ``python3 add_transparency_indicator.py``
