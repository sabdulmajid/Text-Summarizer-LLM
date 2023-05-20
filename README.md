# Text Summarizer LLM


The project is an advanced text summarizer written in Python, utilizing various techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) weighting, sentence position analysis, and word frequency analysis. This powerful tool aims to provide efficient and accurate summaries for any given text, ranging from articles and essays to research papers and reports.

## How it Works
The advanced text summarizer incorporates multiple techniques to generate comprehensive and informative summaries:

  1. **Tokenization**: The text is tokenized into individual words and sentences using NLTK's tokenization methods, enabling detailed analysis and processing.

  2. **Stopword and Punctuation Removal**: Common stopwords and punctuation marks are eliminated from the tokenized words and sentences. This step eliminates words that do not significantly contribute to the overall meaning of the text.

  3. **Word Frequency Calculation**: The tool calculates the frequency of each word in the text. This frequency analysis helps identify key terms and their importance within the document.

  4. **TF-IDF Weighting**: TF-IDF weighting is employed to determine the importance of words within the text. TF-IDF takes into account both the frequency of a word within a document (TF) and its rarity across all documents (IDF), assigning higher scores to words that are both frequent within the document and rare across the entire corpus.

  5. **Sentence Position Analysis:** The tool considers the position of sentences within the text to capture important introductory information. Sentences at the beginning of the text are given extra weight to ensure critical contextual details are included in the summary.

  6. **Summary Generation**: Based on the TF-IDF scores, word frequencies, and sentence positions, the tool selects the top N sentences with the highest scores to construct a coherent and concise summary. N can be adjusted to control the length of the summary.

  7. **Summary Output**: The generated summary is displayed in the console and saved as a separate file in the output-files directory. The output file retains the name of the original file but is prefixed with "OUTPUT-".

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Installation

  1. **Clone the repository**:

```shell
git clone https://github.com/sabdulmajid/Text-Summarizer-LLM.git
```
  2.** Navigate to the project directory**:
```shell
cd Text-Summarizer-LLM
```
  3. **Install the required dependencies**. Make sure you have Python and pip installed, and run the following command:
```shell
pip install -r requirements.txt
```
  4. **Download the NLTK stopwords corpus** by running the following command:
```shell
python -m nltk.downloader stopwords
```
## Usage
To use the text summarization tool, follow these steps:

  1. **Prepare your text file**: Place the text file you want to summarize in the text-files directory.

  2. **Open the Python file** summarizer.py in your preferred code editor.

  3. **Locate the file_path variable** and update it with the path to your text file. For example:

```python
file_path = 'text-files/motorcar.txt'
```
  4. **Adjust the number of sentences** you want in the summary by updating the n argument in the summarize_text function. For example, to get a summary with 3 sentences:
```python
summary = summarize_text(file_path, 3)
```
  5. **Run the Python file**:
```shell
python summarizer.py
```
After running, the summary will be printed in the console and saved in the output-files directory with a filename prefixed by "OUTPUT-".


## Example
Here's an example usage of the text summarization tool:

```python
file_path = 'text-files/motorcar.txt'
summary = summarize_text(file_path, 3)
print(summary)
```
In this example, the tool summarizes the text file located at text-files/motorcar.txt and generates a summary with 3 sentences. The summary is printed to the console and saved as a separate file with a filename prefixed by "OUTPUT-" in the output-files directory.

Feel free to experiment with different text files and adjust the number of sentences in the summary to suit your needs.
