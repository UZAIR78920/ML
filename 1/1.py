import pandas as pd
df=pd.read_csv("dataset.csv")
print("The dataset is : \n",df)
data = df.iloc[0:,0:7].values
h=['0', '0', '0', '0', '0', '0']
def Generalize(h,a):
    for i in range(len(a)):
        if(h[i]!=a[i]):
            h[i]='?'
        else:
            h[i]=a[i]
    return h
X=data[:,0:6]
Y=data[:,-1]
if Y[0]=="yes":
    h=X[0,:]
else:
    print("Error: First Example in not positive")
for i in range(len(X)):
    if(Y[i]=="yes"):
        h=Generalize(h,X[i,:])
print("The more general than hypothesis is:",h)


# The dataset is : 
#       Sky AirTemp Humidity    Wind Water Forecast EnjoySport
# 0  sunny    warm   normal  strong  warm     same        yes
# 1  sunny    warm     high  strong  warm     same        yes
# 2  rainy    cold     high  strong  warm   change         no
# 3  sunny    warm     high  strong  cool   change        yes
# The more general than hypothesis is: ['sunny' 'warm' '?' 'strong' '?' '?']
