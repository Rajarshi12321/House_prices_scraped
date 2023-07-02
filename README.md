# Housing Information Scrapping

Welcome to the Housing Information Scrapping repository! This project focuses on scraping features of houses from Magicbricks.com using SCRAPY and SELENIUM. The goal is to scrape this data and generate a dataset to analyze the housing prices and also make House price predicting models based on real and recent scraped data.

## Table of Contents

- [Housing Information Scrapping](#housing-information-scrapping)
  - [Table of Contents](#table-of-contents)
  - [Installation and Dependencies](#installation-and-dependencies)
  - [Working with the code](#working-with-the-code)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)



## Installation and Dependencies

These are some required packages for our program which are mentioned in the Requirements.txt file

- scrapy   
- pathlib
- json 
- pandas 
- selenium 


To run this project locally, please follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/Rajarshi12321/House_prices_scraped.git

2. Install the required dependencies. We recommend setting up a virtual environment first:
   ```shell
   cd House_prices_scraped
   python3 -m venv venv
   source venv/bin/activate

3. Once the dependencies are installed, you're ready to use the project.

## Working with the code
Before starting out with the program, I had checked the html of the website and how the json files were stored in the script tags. It was a good experience for me to collect data from these scripts and use xpaths.

(Optional) You can checkout the website html for better understanding of the program

I have commented most of the neccesary information in the House_princing.py in spiders folder.

Now to run the program :-

1. Activating the env
  
    ```shell
    conda activate <your-env-name> 
    ```

2. Going the main file by changing directory
    ```shell
    cd House_prices_scraped
    cd House_price
    ```

3. Running the file to scrape the data
   
   ```shell
    scrapy crawl House_pricing -o <filename>
    ```
  This filename is where your scraped data would be stored,the data can be stored in .csv , .json or other type of files according to what type you will choose


## Results
The results of the project : This project is able to scrape 27900 data with 70+ features

## Contributing
Contributions to this project are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request. Let's work together to enhance the scrape data and make the program more accurate.

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.

We hope this README provides you with the necessary information to get started with the Housing Information Scrapping project. Happy scraping data!