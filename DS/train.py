import sklearn
import mlflow

# Config do mlflow
mlflow.set_tracking_uri("endereço_do_server_mlflor")
mlflow.set_experiment(experiment_id="experiment_id")

#%%
# Função de pipeline do mlflow
with mlflow.start_run():
    mlflow.sklearn.autolog()
    # Fazer todo processo de treinamento aqui dentro e já era todo log, registro 
    # e disponibilidade do modelo resolvidos

    mlflow.log_metrics({"passar aqui todas as metricas que eu quiser para serem registradas"})
    pass

# depois é só configurar no G-UI do mlflow experimento e modelos