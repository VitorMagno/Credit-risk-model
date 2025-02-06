import mlflow
import mlflow.client

#%%
mlflow.set_tracking_uri("endereço do servidor mlflow")

#%%
client = mlflow.client.MlflowClient()
versions = client.get_latest_versions()

#%%
model = mlflow.sklearn.load_model("models:/name/version")