# business-reports-nlp
This repository contains code and further ressources used and produced within the project of analysing business reports in the context of my master's thesis.

## Navigation
The code displayed in this GitHub repository can be found in the [scripts folder](https://github.com/simonweigold/business-reports-nlp/tree/main/scripts). It is structured chronologically:
0. [Text was extracted from the PDF files](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/00.1_text_extraction.py) and [subsequently cleaned both automatically](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/00.2_text_cleaning.py) and manually.
1. [The data stored in .txt files was prepared for the analysis, namely transformed into a dataframe and stores as a .csv file.](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/01_data_preparation.ipynb)
2. [Samples were created for the various analysis steps, requiring manual work with samples of the data.](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/02_sampling.ipynb)
3. [A topic model was applied.](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/03_bertopic_llama2.ipynb)
4. [GPT 3.5 Turbo was fine-tuned.](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/04_fine_tuning.ipynb)
5. [The results were analyzed in a descriptive manner.](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/05_descriptive_analysis.ipynb)
6. [The results were analyzed in a quantitative manner.](https://github.com/simonweigold/business-reports-nlp/blob/main/scripts/06_quantitative%20analysis.ipynb)

Graphical outputs can be found in the [figures folder](https://github.com/simonweigold/business-reports-nlp/tree/main/figs).


## Workflow
The general workflow of this thesis project was designed as follows:
<!--
![Methodology Flow Chart](https://github.com/simonweigold/business-reports-nlp/blob/main/figs/Methodology%20Flow%20Chart.png)
-->
<p align="center">
  <img src="https://github.com/simonweigold/business-reports-nlp/blob/main/figs/Methodology%20Flow%20Chart.png" alt="Methodology Flow Chart" width="604.8" height="340.2"/>
</p>
