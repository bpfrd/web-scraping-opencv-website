# Web Scraping -- Opencv website

A short code to scrape the [opencv tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) with selenium and convert all tutorial pages into a single pdf booklet. 

After installing the requirements `pip install -r requirements.txt`, run the code `main.py` to convert each page into a pdf in `opencv` directory. Then run `merge_pdfs.py` to merge all the pdfs into a single booklet, `opencv-book.pdf`.
