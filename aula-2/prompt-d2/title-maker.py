"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Abstract: \"Research data management has become an indispensable skill in modern neuroscience. Researchers can benefit from following good practices as well as from having proficiency in using particular software solutions. But as these domain-agnostic skills are commonly not included in domain-specific graduate education, community efforts increasingly provide early career scientists with opportunities for organised training and materials for self-study. Investing effort in user documentation and interacting with the user base can, in turn, help developers improve quality of their software. In this work, we detail and evaluate our multi-modal teaching approach to research data management in the DataLad ecosystem, both in general and with concrete software use. Spanning an online and printed handbook, a modular course suitable for in-person and virtual teaching, and a flexible collection of research data management tips in a knowledge base, our free and open source collection of training material has made research data management and software training available to various different stakeholders over the past five years.\"\n\nTitle: \"Teaching Research Data Management with DataLad: A Multi-year, Multi-domain Effort\"\n\nAbstract: \"BOLD-based fMRI is the most widely used method for studying brain function. The BOLD signal while valuable, is beset with unique vulnerabilities. The most notable of these is the modest signal to noise ratio, and the relatively low temporal and spatial resolution. However, the high dimensional complexity of the BOLD signal also presents unique opportunities for functional discovery. Topological Data Analyses (TDA), a branch of mathematics optimized to search for specific classes of structure within high dimensional data may provide particularly valuable applications. In this investigation, we acquired fMRI data in the anterior cingulate cortex (ACC) using a basic motor control paradigm. Then, for each participant and each of three task conditions, fMRI signals in the ACC were summarized using two methods: a) TDA based methods of persistent homology and persistence landscapes and b) non-TDA based methods using a standard vectorization scheme. Finally, using machine learning (with support vector classifiers), classification accuracy of TDA and non-TDA vectorized data was tested across participants. In each participant, TDA-based classification out-performed the non-TDA based counterpart, suggesting that our TDA analytic pipeline better characterized task- and condition-induced structure in fMRI data in the ACC. Our results emphasize the value of TDA in characterizing task- and condition-induced structure in regional fMRI signals. In addition to providing our analytical tools for other users to emulate, we also discuss the unique role that TDA-based methods can play in the study of individual differences in the structure of functional brain signals in the healthy and the clinical brain.\"\n\nTitle: \"Topological Data Analysis Captures Task-Driven fMRI Profiles in Individual Participants: A Classification Pipeline Based on Persistence\"\n\nAbstract: \"Multimodal neuroimaging grants a powerful in vivo window into the structure and function of the human brain. Recent methodological and conceptual advances have enabled investigations of the interplay between large-scale spatial trends – or gradients – in brain structure and function, offering a framework to unify principles of brain organization across multiple scales. Strong community enthusiasm for these techniques has been instrumental in their widespread adoption and implementation to answer key questions in neuroscience. Following a brief review of current literature on this framework, this perspective paper will highlight how pragmatic steps aiming to make gradient methods more accessible to the community propelled these techniques to the forefront of neuroscientific inquiry. More specifically, we will emphasize how interest for gradient methods was catalyzed by data sharing, open-source software development, as well as the organization of dedicated workshops led by a diverse team of early career researchers. To this end, we argue that the growing excitement for brain gradients is the result of coordinated and consistent efforts to build an inclusive community and can serve as a case in point for future innovations and conceptual advances in neuroinformatics. We close this perspective paper by discussing challenges for the continuous refinement of neuroscientific theory, methodological innovation, and real-world translation to maintain our collective progress towards integrated models of brain organization.\"\n\nTitle: \"Gradients of Brain Organization: Smooth Sailing from Methods Development to User Community\"\n\nAbstract: \"Magnetic Resonance Imaging (MRI) plays an important role in neurology, particularly in the precise segmentation of brain tissues. Accurate segmentation is crucial for diagnosing brain injuries and neurodegenerative conditions. We introduce an Enhanced Spatial Fuzzy C-means (esFCM) algorithm for 3D T1 MRI segmentation to three tissues, i.e. White Matter (WM), Gray Matter (GM), and Cerebrospinal Fluid (CSF). The esFCM employs a weighted least square algorithm utilizing the Structural Similarity Index (SSIM) for polynomial bias field correction. It also takes advantage of the information from the membership function of the last iteration to compute neighborhood impact. This strategic refinement enhances the algorithm’s adaptability to complex image structures, effectively addressing challenges such as intensity irregularities and contributing to heightened segmentation accuracy. We compare the segmentation accuracy of esFCM against four variants of FCM, Gaussian Mixture Model (GMM) and FSL and ANTs algorithms using four various dataset, employing three measurement criteria. Comparative assessments underscore esFCM’s superior performance, particularly in scenarios involving added noise and bias fields.The obtained results emphasize the significant potential of the proposed method in the segmentation of MRI images.\"\n\nTitle:"]
  },
  {
    "role": "model",
    "parts": ["Title: \"Enhanced Spatial Fuzzy C-means Algorithm for Robust Brain MRI Segmentation\""]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)