from multiprocessing.reduction import duplicate
import pandas as pd

df = pd.read_csv(
    "C:\\Users\\Shabnam\\Desktop\\EDA Practice\\college_student_placement_dataset.csv"
)
print(df.shape)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())

# First moment business Decision
print("Mean")
print("Mean for IQ", df.IQ.mean())
print("Mean for Prev_Sem_Result", df.Prev_Sem_Result.mean())
print("Mean for CGPA", df.CGPA.mean())
print("Mean for Academic_Performance", df.Academic_Performance.mean())
print("Mean for Extra_Curricular_Score", df.Extra_Curricular_Score.mean())
print("Mean for Communication_Skills", df.Communication_Skills.mean())
print("Mean for Projects_Completed", df.Projects_Completed.mean())

print("Median")
print("Median for IQ", df.IQ.median())
print("Median for Prev_Sem_Result", df.Prev_Sem_Result.median())
print("Median for CGPA", df.CGPA.median())
print("Median for Academic_Performance", df.Academic_Performance.median())
print("Median for Extra_Curricular_Score", df.Extra_Curricular_Score.median())
print("Median for Communication_Skills", df.Communication_Skills.median())
print("Median for Projects_Completed", df.Projects_Completed.median())

print("Mode")
print("Mode for IQ", df.IQ.mode())
print("Mode for Prev_Sem_Result", df.Prev_Sem_Result.mode())
print("Mode for CGPA", df.CGPA.mode())
print("Mode for Academic_Performance", df.Academic_Performance.mode())
print("Mode for Extra_Curricular_Score", df.Extra_Curricular_Score.mode())
print("Mode for Communication_Skills", df.Communication_Skills.mode())
print("Mode for Projects_Completed", df.Projects_Completed.mode())
print("Mode for Projects_Completed", df.Placement.mode())

# Second moment business Decision
print("Variance")
print("Variance for IQ", df.IQ.var())
print("Variance for Prev_Sem_Result", df.Prev_Sem_Result.var())
print("Variance for CGPA", df.CGPA.var())
print("Variance for Academic_Performance", df.Academic_Performance.var())
print("Variance for Extra_Curricular_Score", df.Extra_Curricular_Score.var())
print("Variance for Communication_Skills", df.Communication_Skills.var())
print("Variance for Projects_Completed", df.Projects_Completed.var())

print("Standard Deviation")
print("Standard Deviation for IQ", df.IQ.std())
print("Standard Deviation for Prev_Sem_Result", df.Prev_Sem_Result.std())
print("Standard Deviation for CGPA", df.CGPA.std())
print("Standard Deviation for Academic_Performance", df.Academic_Performance.std())
print("Standard Deviation for Extra_Curricular_Score", df.Extra_Curricular_Score.std())
print("Standard Deviation for Communication_Skills", df.Communication_Skills.std())
print("Standard Deviation for Projects_Completed", df.Projects_Completed.std())

print("Range")
print("Range for IQ", max(df.IQ) - min(df.IQ))
print("Range for Prev_Sem_Result", max(df.Prev_Sem_Result) - min(df.Prev_Sem_Result))
print("Range for Academic_Performance", max(df.CGPA) - min(df.CGPA))
print("Range for IQ", max(df.Academic_Performance) - min(df.Academic_Performance))
print("Range for IQ", max(df.Extra_Curricular_Score) - min(df.Extra_Curricular_Score))
print("Range for IQ", max(df.Communication_Skills) - min(df.Communication_Skills))
print("Range for IQ", max(df.Projects_Completed) - min(df.Projects_Completed))

# Third moment business Decision
print("Skewness")
print("Skewness for IQ", df.IQ.skew())
print("Skewness for Prev_Sem_Result", df.Prev_Sem_Result.skew())
print("Skewness for CGPA", df.CGPA.skew())
print("Skewness for Academic_Performance", df.Academic_Performance.skew())
print("Skewness for Extra_Curricular_Score", df.Extra_Curricular_Score.skew())
print("Skewness for Communication_Skills", df.Communication_Skills.skew())
print("Skewness for Projects_Completed", df.Projects_Completed.skew())

print("Kurtosis")
print("Kurtosis for IQ", df.IQ.kurt())
print("Kurtosis for Prev_Sem_Result", df.Prev_Sem_Result.kurt())
print("Kurtosis for CGPA", df.CGPA.kurt())
print("Kurtosis for Academic_Performance", df.Academic_Performance.kurt())
print("Kurtosis for Extra_Curricular_Score", df.Extra_Curricular_Score.kurt())
print("Kurtosis for Communication_Skills", df.Communication_Skills.kurt())
print("Kurtosis for Projects_Completed", df.Projects_Completed.kurt())
# Data Visualization
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

sns.histplot(df["CGPA"], kde=True)
sns.pairplot(df, hue="Placement")
sns.scatterplot(x="CGPA", y="Internship_Experience", hue="Placement", data=df)
plt.show()
sns.relplot(x=df["Internship_Experience"], y=df["Extra_Curricular_Score"], hue = df["Placement"])
plt.show()
sns.histplot( y="Internship_Experience", x = "Placement", data=df)
plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
sns.boxplot(x="IQ",data = df)
plt.show()
sns.boxplot(x="Prev_Sem_Result",data = df)
plt.show()
sns.boxplot(x="CGPA",data = df)
plt.show()
sns.boxplot(x="Academic_Performance",data = df)
plt.show()
sns.boxplot(x="Extra_Curricular_Score",data = df)
plt.show()
sns.boxplot(x="Communication_Skills",data = df)
plt.show()
sns.boxplot(x="Projects_Completed",data = df)
plt.show()
#Find duplicates
duplicate = df.duplicated()
print(duplicate)
total_duplicate = sum(duplicate)
new_data = df.drop_duplicates()
print(new_data)
#no duplicates
#outlier treatment on IQ
import seaborn as sns
import matplotlib.pyplot as plt
from feature_engine.outliers import Winsorizer
winsorizer_iqr = Winsorizer(capping_method = 'iqr', tail = 'both', fold = 1.5, variables = ['IQ'])
df["IQ_IQR"] = winsorizer_iqr.fit_transform(df[['IQ']])
sns.boxplot(df["IQ_IQR"]) 
plt.show()

