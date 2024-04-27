# FastAPI Dependencies
import uvicorn
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sentiment Analysis API for Movie Reviews", description="An API to predict\
	whether or not a piece of text is a movie/TV show review and b) whether or not each review is positive\
	or negative. ")

logreg_model = joblib.load("workspace/models/LogReg_model.pkl")
tfidf_vectorizer = joblib.load("workspace/models/TfidfVectorizer.pkl")

class request_body(BaseModel):
	message : str

@app.get('/')
def Welcome():
	return{'message': "Welcome to the Review Classifier API! Note: Please provide\
	a review without quotations. Deployment will handle this issue."}

@app.post('/api_predict')
def classify_msg(request : request_body):

	if (not(request.message)):
		raise HTTPException(status_code=400, detail="Please provide a valid response.")
	else:
		processed_review = tfidf_vectorizer.transform([request.message])

		label = logreg_model.predict(processed_review)[0]

		if label == 0:
			return {'Answer': "This is not a movie/TV review!"}
		elif label == 1:
			return {'Answer': "This is a positive movie/TV review!"}
		else:
			return {'Answer': "This is a negative movie/TV review!"}
