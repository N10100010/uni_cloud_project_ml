# uni_cloud_project_ml
__This is the main README of this project. It contains all relevant information, you need to know about this application. The repository contains all the code, which is a collection of snippets deployed to different services.__

### Quick Facts...
- Deployed at: [here](http://frontend-uni-cloud-computing.s3-website.eu-central-1.amazonaws.com/)
- Serverless implementation utilizing Amazon AWS lambda function
- Front-End is statically hosted in a Amazon Bucket
- Model inference hosted at HdM AI Lab servers

### What is this application?
This application has been created in the context of the lecture [Cloud Computing Technology (368106a)](https://www.hdm-stuttgart.de/drucktechnik/absolventen/studieninteressierte/bachelor/vorlesung_detail?ansicht=1&vorlid=5214998&sgbvsid=5170586). The app is a MVP for a service that allows the user to test different text-to-image and gather information about the authors, the abstract of the base paper and the respective link to [arxiv](arxiv.org).


### What about the deployment of the application?
This app is running mainly on Amazons AWS. As requested, following are the relevant snippets

#### Back-End
**_LAMBDA FUNCTIONS_**
The main components are setup as a serverless application, utilizing [Amazon lambda functions](https://aws.amazon.com/de/lambda/).

- [_getModelInfo_](https://github.com/N10100010/uni_cloud_project_ml/blob/main/lambda_functions/get_model_info/lambda_function.py)
- [_saveModelOutput_](https://github.com/N10100010/uni_cloud_project_ml/blob/main/lambda_functions/model_save/lambda_function.py)
- [_generateModelOutput_](todo: adjust link)
- [_modelsByCreator_](todo: adjust link)

**_MODEL INFERENCE_**
Due to cost-intensity, the model inference is hosted at HdM internal server of the [IAAI](https://deeplearn.pages.mi.hdm-stuttgart.de/docs/)
todo: adjust link

#### Front-End
The front-end Vue application is hosted as a static-web-hosting in a Amazon S3 bucket. and can be accessed under the following [LINK](http://frontend-uni-cloud-computing.s3-website.eu-central-1.amazonaws.com/).
The respective files can be found [here](https://github.com/N10100010/uni_cloud_project_ml/tree/main/client).
With both of the participants of this project rather being Back-End Engineers than the typical Front-End Guys, the code for it is everything else than a surprise.

## RUN THE APPLICATION LOCALLY
### run flask:

```
cd server
flask run --port=5001 --debug
```

### run vue:

```
cd client
npm run dev
```
