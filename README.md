# BUClass

The BU Class API allows for quick access to class information such as prerequisites, credits, etc. It uses the database scrapped with the [Schedule Hub Project](https://github.com/ethanc-ec/ScheduleHub).

To use the API simply use any web scraping package such as [Requests](https://requests.readthedocs.io/en/latest/) and the [link](https://cethan-buclassapi.uc.r.appspot.com/):
```
https://cethan-buclassapi.uc.r.appspot.com/
```

Add tags such as search or filter to grab specific information.
For example:
```
https://cethan-buclassapi.uc.r.appspot.com/search?code=cdsds100
```
to search for the information on the course CDS DS 100.

Different routes:

- search: `/search?code=`
  - Search for general information about a class
- find: `/find?[query]=`
  - Use: `prereq`, `coreq`, `credit`, and/or `hub` to find specific classes that fit the criteria of the query
  - Example: `/find?prereq=cs111&credit=4` will return all classes that have CS 111 as a prerequisite and are 4 credits
