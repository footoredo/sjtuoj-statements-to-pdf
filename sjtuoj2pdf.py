import pdfkit
import argparse
import requests
import shutil
from multiprocessing import Pool
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge (output_path, input_paths):
    print ("Merging PDFs ...")

    pdf_writer = PdfFileWriter ()

    for pdf_index, path in enumerate (input_paths):
        pdf_reader = PdfFileReader (path)
        print ("Processing PDF {} (out of {}), pages: {}".format (
            pdf_index, len(input_paths), pdf_reader.getNumPages ()))
        for page in range (pdf_reader.getNumPages ()):
            pdf_writer.addPage (pdf_reader.getPage (page))

    with open (output_path, 'wb') as fh:
        pdf_writer.write (fh)
        
    print ("Done.")


sjtuoj = "https://sjtuoj.weak.cat"
#sjtuoj = "http://176.16.45.6"

username = "root"
password = "ACMicpc2012"

login_path = "/accounts/login/?next=/"
session = requests.Session()

def login ():
    result = session.get (sjtuoj)
    csrftoken = result.cookies['csrftoken']
    result = session.post (sjtuoj + login_path, 
            data = {"username": username, 
                "password": password,
                "csrfmiddlewaretoken": csrftoken})
    return session.cookies

def requests2wkhtmltopdf (cookies):
    return [(item[0], item[1]) for item in cookies.iteritems ()]

statement = "/problems/{}/{}/"
options = {
        'encoding': "utf-8"
        }
output_dir = "output/"
output = output_dir + "/{}.pdf"

def crawl (prob):
    prob_id, prob_format = prob
    url = sjtuoj + statement.format (prob_id, prob_format)
    filename = output.format (prob_id)
    if prob_format == "html":
        pdfkit.from_url (url, filename, options = options)
    elif prob_format == "pdf":
        r = session.get(url)
        with open(filename, 'wb') as f:
            f.write(r.content)
            # shutil.copyfileobj(r.raw, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser (description = 'Crawl & convert HTML problem statements on sjtuoj to pdf.')
    parser.add_argument ("-f", "--format", type = str, help = "format [html/pdf] (default = html)", default = "html")
    parser.add_argument ("start_id", type = int, help = "start ID of target problem(s)")
    parser.add_argument ("stop_id", nargs = '?', type = int, help = "stop ID (inclusive) of target problem(s)")
    parser.add_argument ("-n", "--njobs", type = int, help = "multi-thread limit (default = 5)", default = 5)
    parser.add_argument ("-z", "--zoom", type = float, help = "zoom parameter (default = 1.0)", default = 1)
    parser.add_argument ("-o", "--output", type = str, help = "output file name")
    args = parser.parse_args ()

    print ("Logining ...")
    cookies = login ()
    print ("Done.")
    options['cookie'] = requests2wkhtmltopdf (cookies)
    options['zoom'] = args.zoom
    print (options)

    if args.stop_id != None:
        r = range (args.start_id, args.stop_id + 1)
    else:
        r = [args.start_id]

    with Pool (args.njobs) as p:
        p.map (crawl, zip(r, [args.format for _ in r]))

    if args.output != None:
        merge (output_dir + args.output, list (map (output.format, r)))
