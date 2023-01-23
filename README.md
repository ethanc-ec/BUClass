# BUClass

The BU Class API allows for quick access to class information such as prerequisites, credits, etc. It uses the database scrapped with the [Schedule Hub Project](https://github.com/ethanc-ec/ScheduleHub).

To use the API simply use any web scraping package such as [Requests](https://requests.readthedocs.io/en/latest/) and the link:
```
https://buclassapi.uk.r.appspot.com/
```

Add tags such as search or filter to grab specific information.
For example:
```
https://buclassapi.uk.r.appspot.com/search?code=cdsds100
```
to search for the information of the course CDS DS 100.

Different routes:
- search
  - ```/search?code=```
    - Search for general information of a class
- filter
  - ```/filter?prereq=```
    - Filter classes that have a specific course as a prerequisite
