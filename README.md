# Industry Classifcation Tool
Resource for industry classification IJOC submission

# SPICS: An Unsupervised Framework for Analysing the Spatiotemporal Evolution of Industry Clusters 

This repo contains the Python implementation of the paper SPICS: An Unsupervised Framework for Analysing the Spatiotemporal Evolution of Industry Clusters in IJOC (Software Tool)

## Requirements

#### The codes have been tested with the following packages:
* Python 3.6
* Gensim
* pandas

## Input data and Power BI file 

You can download the whole input data (.csv) and Power BI file (.pbix) with the following links:

## Google Drive:

```
https://drive.google.com/drive/folders/1SyTS4Gt_0IIF60-_LTZ0HdpbVGlI6DRH?usp=sharing
```
## One Drive
```
https://mylingnan-my.sharepoint.com/:f:/g/personal/allentan_ln_edu_hk/Ek-O_ydpy-xApwg5bxE-ZKgBDQzzkFBTUh25b4ya7tciPg?e=k1qYKh
```

Also, we provide a toy raw data (sample.csv) for you to test the whole pipeline.

## Quick Demo

To run the model (including data processing), clone the repo and decompress the demo data archive by executing the following commands:

``` 
git clone git@github.com:ludsl/Industry_classifcation_tool.git
cd LDA
python LDA.py --f sample.csv
```

You can use --rf to change the name of output file, --clusterNum to change the number of clusters, and --keywordsNum to change the number of keywords in each cluster. 

#### To run the evaluation:

``` 
cd Evaluation
python evaluation.py --sec 1 --rf LDA_output_file
``` 
--sec 1 is for the evaluation of section level in SIC code, --sec 0 is for the division level in SIC code. 

#### To use the powerbi software:

You can open the Powerbi file. There is a user manual (.pdf) for detailed guidance. 

