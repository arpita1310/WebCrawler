import requests
import tkinter as tk
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tkinter import filedialog
from tkinter import *

def scrape_web(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')   #html parse
    #write what you want to extract( here we're taking para)
    data = [p.get_text() for p in soup.find_all('p')]
    return data                       #return the list created


def generate_data(url):
    data = scrape_web(url)
    file_path = filedialog.asksaveasfilename(defaultextension='.csv')      #file save with extension csv
    with open(file_path, 'w') as f:
        f.write('\n'.join(data))
    return file_path


def access():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        content = f.read()
    print(content)


def all_links(url):
    e = url + " IS NOW BIENG CRAWLED"
    print(e)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title
    anchors = soup.find_all('a')
    links = set()
    for link in anchors:
        if link.has_attr('href'):
            href = link['href']
            if href != '#' and not href.startswith('javascript:'):
                if ':' not in href:
                    link = urljoin(url, href)
                else:
                    link = href
                if link not in links:
                    links.add(link)
                    print(title.string)
                    print(link)
        else:
            pass


def main():
    window = tk.Tk()
    window.configure(bg="#DAF5FF")
    window.title('Web Scraper and Dataset Generator')
    url_label = Label(window, text="WEB SCRAPPER AND DATASET GENERATOR", height=2, width=70, font=("Times New Roman", 20), bg= "#19A7CE", fg="black", borderwidth=3, relief="groove" )
    url_label.pack(side=TOP, fill=BOTH)
    url_label = tk.Label(window, text=" ", width=150, height=2, bg="#DAF5FF")
    url_label.pack(fill=BOTH)
    url_label = tk.Label(window, text='Enter WEBSITE URL ⬇ "https://example.com" ', padx=10, pady=7,bg="#DAF5FF", width=148)
    url_label.pack(fill=BOTH)
    url_entry = tk.Entry(window, width=50, borderwidth=3, relief="sunken", bg="#D8D8D8")
    url_entry.pack()
    url_label = tk.Label(window, text="»»———————————————————————————----------------------------------------------——————————————————————————«« ", width=150, height=2, bg="#DAF5FF")
    url_label.pack(fill=BOTH, expand=TRUE)
    generate_button = tk.Button(window, text=" Generate Dataset ", width=50,height=2, bg="#D8D8D8",relief="groove", command=lambda: generate_data(url_entry.get()))
    generate_button.pack()
    url_label = Label(window, text="Click me to generate your datasets ⬆", pady=3, bg="#DAF5FF")
    url_label.pack(fill=BOTH, expand=TRUE)
    url_label = tk.Label(window,text="»»———————————————————————————----------------------------------------------——————————————————————————«« ",width=150, height=2,bg="#DAF5FF")
    url_label.pack(fill=BOTH, expand=TRUE)
    access_button = tk.Button(window, text="Access File", bg="#D8D8D8", command=access,  width=50, height=2, relief="groove")
    access_button.pack()
    url_label = Label(window,text='Click me to access the generated (.csv) file ⬆',pady=3,bg="#DAF5FF", width=150)
    url_label.pack(fill=BOTH, expand=TRUE)
    url_label = tk.Label(window,text="»»———————————————————————————----------------------------------------------——————————————————————————«« ",width=150, height=2, bg="#DAF5FF")
    url_label.pack(fill=BOTH, expand=TRUE)
    link_button = tk.Button(window, text="Access all Links ", width=50, height=2, bg="#D8D8D8",relief="groove",command=lambda: all_links(url_entry.get()))
    link_button.pack()
    url_label = Label(window, text="Click me to see crude data ⬆", pady=3, bg="#DAF5FF")
    url_label.pack(fill=BOTH, expand=TRUE)
    url_label = tk.Label(window, text=" ", width=150, height=2, bg="#DAF5FF")
    url_label.pack(fill=BOTH, expand= TRUE)
    window.mainloop()


if __name__ == "__main__":
    main()