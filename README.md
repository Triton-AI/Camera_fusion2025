# Getting started with Roboflow
1. [Create an Account](#create-an-account)
2. [Upload Data](#upload-data)
3. [Label Data](#label-data)
4. [Create Model](#create-model)
5. [Download Dataset](#download-dataset)
6. [Deploy a Model](#deploy-a-model)
7. [Join the Triton AI Workspace](#join-the-triton-ai-workspace)
8. [Setting Up Your Own Workspace](#setting-up-your-own-workspace)
8. [Known Bugs](#known-bugs)

## Create An Account
- Go to [Roboflow's Website](https://www.roboflow.com)
- Press **Get Started** on the top right
- Create an account with your UCSD email (it is important that you use a .edu email)
- Create a new workspace with a free Public Plan
- Click on **Projects** in the left navigation bar, then press **New Project**
- Create an object detection project
- On the bottom right, hit **Use Trational Model Builder Instead**

## Upload Data
- Drag and drop any folders or files directly to the Roboflow website, please note that you will need to unzip any zip files
- Upload data from directly from your phone
  - (Recommended) Sign into Roboflow on your phones browser and upload data directly, this will give you the option to choose the frame rate of your upload
  - On your desktop/laptop there will appear a QR Code that will allow you to upload data to Roboflow (note this sometimes causes a bug consult [Known Bugs](#known-bugs))
- You can also get data from Roboflow Universe by searching for a dataset and forking it to your project. For more information please click [here](https://docs.roboflow.com/universe/download-a-universe-dataset)

## Label Data
- After you have uploaded data, press **Label Myself**
- Click on your first unannotated image, you might want to read the [best practices guide](https://blog.roboflow.com/tips-for-how-to-label-images/)
- Press the bounding box on the bar on the right
- Draw a bounding box around the object and name your class, then press enter
- For your next image, draw the box, then hit enter
- For AI labeling you can press **Label Assist** and a model will label for you, however it is not perfect, make sure to double check. This method uses 1 credit per 100 images
- If an image does not have any objects, you can press **N** or hit the bottom option in the bar on the right to mark it as a NULL image
- Once all the images are labeled you can add them to the dataset by pressing the checkmark on the top, make sure to split between Train, Test, and Valid by pressing on the **Method Dropdown bar**

## Create Model
- Once you have a dataset with enough data, press **New Dataset Version**
  - In the preprocessing step edit the Resize so that the photo stretches to 640x640, this is optimal for YOLOv11 and YOLOv12
  - Add any desired augmentations
  - Create a dataset version
- Go to **Versions** and create a model for your dataset, press **custom train**, then select a model (TritonAI uses YOLOv11 and YOLOv12), press continue and choose a model size (we will be using fast)
- Start Training

## Download Dataset
- Go to **versions** press download dataset, and in the image and annotation select YOLOv11 or YOLOv12, download as a zip file
  - To upload to another workspace or project, unzip the file then drop the whole folder into the upload section of Roboflow. The YAML file will contain annotations **Note** null images will need to be reannotated as null. This can be done all at once in the annotate page with a button on the right

## Deploy a model
- The simplest way to test your model is by going to **Models** and selecting your model. Then either upload another image, try the webcam, or paste a link to an image
- (Recommended) To deploy a model to your own machine you can download the weights to use on your own machine
  - One sample code you can use is to go to our src folder and install the dependcy by:
    ```
    bash install.sh
    ```
    Then download our python file testYOLO_12.py and run
    ```
    python testYOLO_12.py
    ```
    Our sample code works for both YOLO 11 and 12 model, but if you want to use other YOLO version. Please do some modification on your own!
- Lastly, you can call the roboflow api to deploy your model for more information visit [Roboflow's Documentation](https://blog.roboflow.com/deploy-computer-vision-models-offline/)

## Join the Triton AI workspace
- Ask a team lead to invite you to the project

## Set Up Your Own Workspace
At this point you should have your own workspace and be in the Triton AI workspace. Since credits are limited, we label our data in the main Triton AI workspace then download the datasets so that each team member can train models in their own workspaces. To get more credits for free, go to Settings on the left, Planning and Billing, then scroll to the bottom to create a research plan. **Note** This is only available for .edu emails

## Known Bugs
- When uploading using the QR Code, after the upload, Roboflow will not allow you to upload more data and will continously redirect you to another page. A solution we have found is to rename the upload then save and the problem should be solved.


---
By: Luis Zaragoza
