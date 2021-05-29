# cfi-renewal-course-downloader
This is a quickly hacked together script to generate chapter PDFs from American Flyers CFI Renewal (FIRC) online course.

As a CFI, I have to renew my certificate every two years online with the FAA. I wanted a copy of the material in pdf, for my own offline reference, but also for easier searching of the course material while taking the test (the test is "open book", but each chapter page is it's own HTML page, so it's extremely cumbersome to click through HTML pages, vs. having each chapter in a PDF).

This script generates one PDF for each of the 12 chapters in the course. It scrapes the HTML, removes dead content, and just gives you text and images.

First you have to login to the American Flyers portal. Then in the debugging tool of your browser of choice, examine the cookies which the site returned to you. Look the appropriate cookies and replace them in the script on this line (there <<CCRED>> is replaced with the actual values from your browser's debugger)

```python
headers = {"Cookie": "ASP.NET_SessionId=<<CRED>>; Username=<<CRED>>; ASPSESSIONIDSCVTDSRQ=<<CRED>>;"}
```

Make sure to pilot safe, and program even safer :)