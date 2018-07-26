# SJTUOJ Statements to PDF

A script to crawl & convert HTML statements on SJTUOJ.

## Requirements

- [pdfkit](https://github.com/JazzCore/python-pdfkit/)
- [PyPDF2](https://github.com/mstamy2/PyPDF2)

## Usage

```
usage: sjtuoj2pdf.py [-h] [-f FORMAT] [-n NJOBS] [-z ZOOM] [-o OUTPUT]
                     start_id [stop_id]

Crawl & convert HTML problem statements on sjtuoj to pdf.

positional arguments:
  start_id              start ID of target problem(s)
  stop_id               stop ID (inclusive) of target problem(s)

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        format [html/pdf] (default = html)
  -n NJOBS, --njobs NJOBS
                        multi-thread limit (default = 5)
  -z ZOOM, --zoom ZOOM  zoom parameter (default = 1.0)
  -o OUTPUT, --output OUTPUT
                        output file name
```

Remeber to create `output/` and fill the `username` and `password`. PDF version of problems will be saved to `output/[prob_id].pdf`. If you specify a `--output` file, all statements will be merged into that file.

## Examples

- Crawl a single problem

```
python sjtuoj2pdf.py 8652
```

- Crawl a series of problems [8652, 8662] on 3 threads and merge them into `statements.pdf`

```
python sjtuoj2pdf.py --njobs 3 --output statements.pdf 8652 8662
```

- Zoom the statements to 90%

```
python sjtuoj2pdf.py --zoom 0.9 8652 
```

- Crawl a pdf problems

```
python sjtuoj2pdf.py --format pdf 10207
```
