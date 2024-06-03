SEO Analyzer

SEO Analyzer is a web application built with Flask that allows users to analyze basic SEO factors of any given URL. The tool fetches the content of a webpage and provides insights into elements like the title, meta descriptions, keywords, word count, images with alt text, internal and external links, and keyword density.

 Features

- Analyze the title, meta description, and meta keywords of a webpage.
- Check the length of the title.
- Count the number of images with and without alt text.
- Identify internal and external links.
- Calculate the word count of the webpage.
- Compute the keyword density for a specific keyword.

 Installation

 Prerequisites

Ensure you have Python 3.x and pip installed on your system.

Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/OtienoJosh/SEO-Analyzer.git
   cd SEO-Analyzer
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3.Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

   The application will start running on `http://127.0.0.1:5000`.

 Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter the URL of the webpage you want to analyze in the input field.
3. Click on the "Analyze" button to see the SEO analysis results.

 Example

After entering a URL and clicking "Analyze," you will see a detailed SEO report including:

- Title: The title of the webpage.
- Title Length: The number of characters in the title.
- Meta Description: The content of the meta description tag.
- Meta Keywords: The content of the meta keywords tag.
- H1 Tags: All H1 tags found on the page.
- Word Count: The total number of words on the page.
- Images with Alt Text: The number of images with alt text.
-Total Images: The total number of images on the page.
- Internal Links: A list of internal links on the page.
- External Links: A list of external links on the page.
- Keyword Density: The density of a specific keyword (default is "flask").

 File Structure


SEO-Analyzer/
│
├── templates/
│   ├── index.html          # Home page template
│   └── results.html        # Results page template
│
├── app.py                  # Main application file
├── requirements.txt        # List of dependencies
└── README.md               # This README file


 Dependencies

- Flask
- Requests
- BeautifulSoup4

These dependencies are listed in the `requirements.txt` file.

Contributing

Feel free to fork this repository, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License.
