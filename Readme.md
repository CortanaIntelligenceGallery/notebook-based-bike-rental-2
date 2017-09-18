# Bike Rental in Notebook using Keras/Tensor Flow #


This project shows how to setup LSTM based network for estimating bike rental demand and operationalize it.



- Execute every cell in the notebook
- Once all the cells are executed, operationalize using the following commands


### Prerequisites
Make sure the following packages are installed in the environment where this notebook is being executed:

  - tensorflow
  - h5py
  - Keras
  - azure-ml-api-sdk

Please use **pip install** to install above dependencies

### Setup Environment ###

Setup environment and publish web service. This assumes IT admin has already created modelmanagement account for you and have setup an ACS environment for you

```
#setup environment
$ az ml account modelmanagement set -n <model mgmt acct e.g. neerajteam2hosting> -g <azure resource group e.g. amlrsrcgrp2>
$ az ml env set -n <env name e.g. amlcluster> -g <azure resource group e.g. amlrsrcgrp2>
$ az ml env local
```

If you don't have previous environment or account setup, then please use the following commands to setup model management account and environment

```
$ az ml env setup -n <env name e.g. amlcluster> -g <azure resource group e.g. amlrsrcgrp2> # this will setup local environment. use option -c for cluster environment
$ az ml account modelmanagement create -n <acct name e.g. neerajteam2hosting> -l <location e.g. eastus2> -g <azure resource group e.g. amlrsrcgrp2> --sku-instances <sku count e.g. 1> --sku-name <pricing tier e.g. S1> 
```

### Deploy ###


Publish web service using the following command by providing scoring file, model, runtime, dependency file, and schema

```

$ az ml service create realtime -f bikescore.py -m finalmodel.sav -r python -c ./aml_config/conda_dependencies.yml -s bikeschema.json -l true -n bikews1
```

Use the following command to list all active web services


```

$ az ml service list realtime -o table
$ az ml service usage realtime -i bikews1

```

### Consume ###


Consume web service using the following command

```

$ az ml service run realtime -i bikews1 -d "{\"npa\": [[450.0, 353.0, 285.0, 332.0, 377.0, 268.0, 218.0, 387.0, 834.0,   508.0, 153.0, 42.0, 4.0, 1.0, 10.0, 17.0, 0.0, 4.0, 1.0, 2.0, 0.58, 0.5455, 0.64, 0.3284], [890.0, 450.0, 353.0,       285.0, 332.0, 377.0, 268.0, 218.0, 387.0, 834.0, 508.0, 153.0, 4.0, 1.0, 10.0, 18.0, 0.0, 4.0, 1.0, 2.0, 0.56,         0.5303, 0.64, 0.3284], [788.0, 890.0, 450.0, 353.0, 285.0, 332.0, 377.0, 268.0, 218.0, 387.0, 834.0, 508.0, 4.0, 1.0,  10.0, 19.0, 0.0, 4.0, 1.0, 2.0, 0.56, 0.5303, 0.68, 0.2985]]}"

```
