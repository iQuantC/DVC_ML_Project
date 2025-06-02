
import joblib
import gradio as gr
import pandas as pd

# Load trained model
model = joblib.load("model/model.joblib")

# Match feature names used during training
feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

def predict(sepal_length, sepal_width, petal_length, petal_width):
    data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                        columns=feature_names)
    prediction = model.predict(data)
    return prediction[0]

# Set up Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Sepal Length (cm)"),
        gr.Number(label="Sepal Width (cm)"),
        gr.Number(label="Petal Length (cm)"),
        gr.Number(label="Petal Width (cm)")
    ],
    outputs="text",
    title="Iris Flower Classifier",
    description="Enter the flower measurements to predict the iris species."
)

if __name__ == "__main__":
    iface.launch()
