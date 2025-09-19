## Loose infile format
You want to separate all of the content of a strat into 4 segments:
- Strat Header
- Writeup
- Videos
- Alerts

### Example of an infile (there is one already stored within the repo)
```
HEADER
Strat name
Strat difficulty, as a number between 1 and 10

WRITEUP
Basically all of the text for a writeup, separate significant breaks with newlines

VIDEO
imgur link to the video

ALERTS
Style of alert
Written content of the alert
```

## What is going on in the outfile?
Basically the outfile can be loaded into the browser to quickly test the output of the convertion, **just copy the strat content in between the comments** of the outfile and slap it into a page.