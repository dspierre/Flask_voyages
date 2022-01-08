df_concat = pd.read_csv('df_concat (1).csv')
# Splitting the dataset into the Training set and Test set
X = df_concat.drop(columns=['TravelInsurance'])
y = df_concat['TravelInsurance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Fitting Decision Tree Classification to the Training set
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test)
print("accuracy_score: %.2f"% accuracy_score(y_test, y_pred))
# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
# export model to create API
pickle.dump(classifier, open('modele\model_SVM.pkl', 'wb'))