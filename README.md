# uni_cloud_project_ml
__This is the main README of this project. It contains all relevant information, you need to know about this application. The repository contains all the code, which is a collection of snippets deployed to different services.__

### Quick Facts...
- Deployed at: [here](http://frontend-uni-cloud-computing.s3-website.eu-central-1.amazonaws.com/)
- Serverless implementation utilizing Amazon AWS lambda function
- Front-End is statically hosted in a Amazon Bucket
- Model inference hosted at HdM AI Lab servers

## Technical Documentation

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


## Reflective Documentation
by Nicolas Reinhart (nr063@hdm-stuttgart.de) and Manuel Heim (mh375@hdm-stuttgart.de)
for the Project Hugging Demo Hub, realized in the context of the lecture Cloud Computing Technology by Tim Reibe

As a reader of the project documentation, you aim to gain insight into our practical approach, the challenges encountered during implementation, and the key learnings derived from this project for similar endeavors.
### The Practical Approach
In tackling the practicalities of our project, we embarked on a journey that involved the development of a Vue front-end, deployment to AWS, and the implementation of AWS Lambda functions and the inference of a machine learning model on Amazons SageMaker and our Servers at the IAAI at the Hochschule der Medien.
#### Vue Front-end Development
Developing a practical Vue front-end entailed navigating through a plethora of tutorials, embracing a path of honesty regarding our learning curve. While initially daunting, the abundance of resources facilitated our journey, empowering us to craft a robust user interface with the Vue framework.
#### Deployment to AWS
The deployment of our front-end to AWS unfolded as a surprisingly straightforward endeavor, defying our initial apprehensions. This phase underscored the importance of meticulous planning and adherence to best practices, resulting in a seamless integration with AWS infrastructure. In the end, the front-end was placed in a S3 bucket and the bucket was activated to be a static web hosting bucket.
#### Implementation of AWS Lambda Functions
Delving into the realm of AWS Lambda functions, we encountered both challenges and insights. We deliberated over the merits of adopting a serverless/stateless backend architecture, weighing the pros and cons meticulously. Serverless architectures offer scalability benefits, automatically adjusting resources to match demand, but they also present the risk of vendor lock-in due to heavy reliance on specific cloud provider services and APIs - just to name a pro and a con respectively. Our serverless backend consisting of Lambda functions is used for all backend functionalities as a kind of middletier. Lambda functions access the information of the HuggingFace API, communicate with the S3 storage and serve as an intermediate layer before the model inference layer. Additionally, considerations regarding the accessibility and functionality of lambda functions prompted thoughtful deliberations, culminating in informed decisions regarding implementation strategies. The possibility to clearly define a gateway for a function, setting the protocols, defining required parameters, etc allowed us to clearly define the inputs and outputs of the functions.
#### Realization of the Inference Process
Navigating through the intricacies of realizing the inference process of our model posed significant challenges, particularly in terms of managing expenses within the AWS ecosystem. The free contingent for a new AWS account is set to 20$, for services like SageMaker. By testing the inference process, our free amount was surpassed, after a single afternoon. After some internal discussion and discussions with our lecturer, we decided to move the inference to the server of the Hochschule der Medien (HdM).  Through iterative refinement and collaboration with the Institute for Applied AI (IAAI), we surmounted these hurdles, forging a path towards seamless integration and functionality. Finally, we settled on a Flask server that utilizes 1 of 6 GPU-servers for the inference. The server is chosen at random, when the current job is created. More on that in the learnings.
#### Persistence of Images
Addressing the persistence of images necessitated the establishment of persistent links to AWS S3, ensuring accessibility and durability. S3 offers a robust option for long-term data storage. The use of S3 has proven to be particularly suitable for storing images. For example, images can be easily identified by the time the image was created. In addition, S3 supports optimized communication with Lambda functions, which has greatly accelerated and simplified our development process. In addition, the free tier of S3 offers sufficient capacity to meet the requirements for our MVP. During the implementation phase of the image persistence, it became clear how important solid data management and the proactive avoidance of potential pitfalls are.
### The Learnings
Reflecting on our journey, several key learnings have emerged, shaping our approach to future endeavors:
#### Local Development and Testing:
Front-end development and AWS Lambda functions should be developed and tested locally before deployment, ensuring robustness and minimizing potential issues in production environments.
#### Cost Considerations:
While platforms like AWS SageMaker offer formidable computing power, it's imperative to weigh the associated costs meticulously. Awareness of cost implications informs strategic decision-making, mitigating the risk of budgetary overruns.
#### Accessibility of Cloud Deployment:
Armed with a foundational understanding and a bit of background knowledge, deploying code to the cloud is within reach, particularly for minimum viable products (MVPs).  Before deciding on a provider, you should research potential cloud providers in detail. During the deployment of a cloud application, continuous learning and adaptability to technical changes and changes in service providers are required.

In conclusion, our journey encapsulates a fusion of perseverance, collaboration, and adaptability, underscoring the transformative potential of embracing challenges as opportunities for growth.


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
