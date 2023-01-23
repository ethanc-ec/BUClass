# BUClass

The BU Class API allows for quick access to class information such as prerequisites, credits, etc. It uses the database scrapped with the [Schedule Hub Project](https://github.com/ethanc-ec/ScheduleHub).

To use the API simply use any web scraping package such as [Requests](https://requests.readthedocs.io/en/latest/) and the link:
```
https://buclassapi.uk.r.appspot.com/search?code=
```

Add the full course code at the end of the link to retrieve information about a specific class.
For example:
```
https://buclassapi.uk.r.appspot.com/search?code=cdsds100
```

Different routes:
- search
  - ```/search?code=```
    - Search for general information of a class
- filter
  - ```/filter?prereq=```
    - Filter classes that have a specific course as a prerequisite
