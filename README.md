# BUClass

The BU Class API allows for quick access to class information such as prerequisites, credits, etc. It uses the database scrapped with the [Schedule Hub Project](https://github.com/ethanc-ec/ScheduleHub).

To use the API simply use any web scraping package such as [Requests](https://requests.readthedocs.io/en/latest/) and the link:
```
https://buclassapi.uk.r.appspot.com/?search=
```

Add the full course code at the end of the link to retrieve information about a specific class.
For example:
```
https://buclassapi.uk.r.appspot.com/?search=cdsds100
```
