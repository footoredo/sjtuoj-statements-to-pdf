# SJTUOJ Statements to PDF

A script to crawl & convert HTML statements on SJTUOJ.

## Requirements

[pdfkit](https://github.com/JazzCore/python-pdfkit/)

## Usage

```
usage: sjtuoj2pdf.py [-h] [-n NJOBS] [-z ZOOM] start_id [stop_id]

Crawl & convert HTML problem statements on sjtuoj to pdf.

positional arguments:
  start_id              The start ID of target problem(s)
  stop_id               The stop ID (inclusive) of target problem(s)

optional arguments:
  -h, --help            show this help message and exit
  -n NJOBS, --njobs NJOBS
                        Multi-tasks limit
  -z ZOOM, --zoom ZOOM  Zoom parameter
```

Remeber to create `output/` and fill the `username` and `password`. PDF version of problems will be saved to `output/[prob_id].pdf`.

## Examples

- Crawl a single problem

```
python sjtuoj2pdf.py 8652
```

- Crawl a series of problems [8652, 8662] on 3 threads

```
python sjtuoj2pdf.py 8652 8662 --njobs 3
```

- Zoom the statements to 90%

```
python sjtuoj2pdf 8652 --zoom 0.9
```
