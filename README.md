# Exploratory  Data Analysis on College Placement Data
## Project Overview 
This Data set contains info such as CGPA,Academic_Performance,Placement.    
This data set is from [College Student Placement Factors Dataset ](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset/data).


### Steps 
1. Importing Libraries     
Essential Python libraries used:
pandas    
seaborn    
matplotlib    
feature_engine.outliers (Winsorizer)    

2. Loading and Inspecting Data
The dataset is read using pandas.read_csv().
Basic inspections performed:   
Shape of the dataset    
First 10 and last 10 rows      
Column information    
Summary statistics using describe()    

3. First Moment Business Decision (Central Tendency)   
Computed for all major numerical columns:    
Mean, Median, Mode    
This Helps understand the central values of IQ, CGPA, Academic Performance, Projects Completed, and more.    

4. Second Moment Business Decision (Dispersion)    
Calculated:    
Variance    
Standard Deviation    
Range    
These metrics help assess the spread and variability of student scores.    

5. Third and Fourth Moment Business Decision
Calculated:    
Skewness    
Indicates distribution symmetry.    
Kurtosis    
Measures the peakedness or flatness of the distribution.

7. Data Visualization
Multiple visualizations were generated using seaborn and matplotlib:    
Univariate Analysis    
Histograms with KDE (CGPA)    
Boxplots for:    
IQ    
Prev Semester Result    
CGPA     
Academic Performance    
Extra Curricular Score    
Communication Skills    
Projects Completed    
Bivariate & Multivariate Analysis    
Pairplot with Placement as hue    
Scatterplots:    
CGPA vs Internship Experience    
Internship Experience vs Extra Curricular Score    
Heatmap of correlations    
Relplots for continuous variable comparisons    
Histogram comparing Internship Experience by Placement    
These plots help identify relationships between attributes and placement likelihood.

7. Duplicate Detection
Steps performed:
Identified duplicate rows using df.duplicated()
Counted total duplicates
Removes duplicates using drop_duplicates()
Dataset contained no duplicates after validation

8. Outlier Treatment
Applied Winsorization on IQ:
Used Winsorizer with IQR method
Tail capping on both sides (1.5 IQR)
Created a new feature IQ_IQR
Verified outlier correction using a boxplot
This ensures extreme values do not distort analysis.    

9. Final Output
The complete EDA provides:        
Statistical summary of all important attributes
Cleaned and processed dataset    
Clear visualization-based insights    
Outlier-treated feature for IQ    
Placement-related patterns useful for modeling or reporting    
