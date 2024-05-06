"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
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

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file.uri]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1].uri]

def extract_pdf_pages(pathname: str) -> list[str]:
  parts = [f"--- START OF PDF ${pathname} ---"]
  # Add logic to read the PDF and return a list of pages here.
  pages = []
  for index, page in enumerate(pages):
    parts.append(f"--- PAGE {index} ---")
    parts.append(page)
  return parts

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": extract_pdf_pages("CV_Heitor_full (1).pdf")
  },
  {
    "role": "user",
    "parts": ["Crie um site estilo CV com tema escuro que inclua as informações do pdf anexado. Crie uma seção inicial de informaçõe gerais, outra seção para os artigos, e, por fim, uma para o restante das informações. Envie separadamente o conteúdo de html, css e js necessários. Utilize Bootstrap como componente adicional de formatação do CSS"]
  },
  {
    "role": "model",
    "parts": ["## HTML (index.html):\n\n```html\n\n\n\n    \n    \n    \n    \n    \n\n\n\n    \n        \n            Heitor Mynssen\n            PhD student in Neuroscience\n            Brazilian Network of Neurobiodiversity • Federal University of Rio de Janeiro\n            \n                hmynssen@ufrj.com • \n                My Webpage \n            \n        \n\n        \n\n        \n            \n                Research Profile\n                Primary Interests\n                \n                    Biological Physics\n                    Computational and Numerical Methods\n                    Comparative Neuroanatomy\n                \n                Methods of Interests\n                \n                    Image Processing\n                    Surface Reconstruction\n                    Neuroimaging\n                \n            \n\n            \n\n            \n                Publications\n                Journal Articles\n                \n                    \n                        Avelino-de-Souza, K.; Mynssen, H.; Chaim, K.; Parks, A.; Ikeda, J. M. P., Cunha, H. A.; Mota, B. & Patzke, N. (2024).  \n                        Anatomical and Volumetric Description of the Guiana Dolphin (Sotalia guianensis) Brain from an Ultra-High-Field Magnetic Resonance Imaging. Brain Structure and Function. 10.1007/s00429-024-02789-1 \n                    \n                \n                In Conference Proceedings\n                \n                    \n                        Mynssen, H.; Boch, M.; Patzke, N.; Mars, R. B.; Mota, B.; Avelino-de-Souza, K. (2024). Costurando cérebros: um novo método de reconstrução de superfície cortical para animais não-modelo. In: Jornanda do Programa de Pós-Graduação em Ciências Morfológicas 2024 (Jornada PCM 2024) -Universidade Federal do Rio de Janeiro, 2024, Rio de Janeiro, Brazil\n                    \n                    \n                        Mynssen, H.; Ramos, L. R.; Sanchez, T. A.; Fernandes, O. (2019). EFEITOS DA AYAHUASCA NA CONECTIVIDADE FUNCIONAL DO CÉREBRO: UM ESTUDO POR NEUROIMAGEM E ESCALAS PSICOMÉTRICAS. In: X Semana de Integração Acadêmica da UFRJ (SIAC 2019) -Universidade Federal do Rio de Janeiro, 2019, Rio de Janeiro. Anais da X Semana de Integração Acadêmica da UFRJ, 2019\n                    \n                \n                In preparation\n                \n                    \n                        Mynssen, H.; Avelino-de-Souza, K.; Chaim, K.; Patzke, N. & Mota, B. Stitcher: a brain reconstruction tool for non-model animals’ segmentation\n                    \n                \n            \n\n            \n\n            \n                Experience\n                Education\n                \n                    \n                        PhD in Neuroscience (2023–present)\n                        Institute of Biomedical Sciences – Morphological Science Department, Federal University of Rio de Janeiro, Brazil\n                    \n                    \n                        M.Sc. in Physics (2020—2023)\n                        Institute of Physics, Federal University of Rio de Janeiro, Brazil. \n                        Morphological Reconstruction And Analysis Of Mammalian Brains \n                    \n                    \n                        Bachelor in Medical Physics (2015—2020)\n                        Institue of Physics, Federal University of Rio de Janeiro, Brazil. \n                        Functional Connectivity Pattern in Experienced Users of Ayahuasca After Low Dose Ingestion \n                    \n                \n\n                Research Projects\n                \n                    \n                        Morphological Reconstruction And Analysis Of Mammalian Brains (2019–present)\n                    \n                    \n                        Functional Connectivity Pattern in Experienced Users of Ayahuasca (2018–2020)\n                    \n                \n\n                Working Experience\n                \n                    \n                        Development of Stitcher Package for cortical reconstruction (2019-2023)\n                    \n                    \n                        Physics and Mathematics Tuition (2017-2022)\n                    \n                \n                \n                Student Grants\n                \n                    \n                        Serrapilheira Institute - Student Grant for Development of Teaching, Research and Outreach (2020-2023) \n                    \n                    \n                        Neuroimage and Psicophysiology Laboratory - Scientific Initiation Grant (2018-2019)\n                    \n                \n\n                Experiences and Events\n                \n                    \n                        Internship in Radiotherapy, Sírio-Libanês Hospital, São Paulo, SP, Brazil (2020)\n                    \n                    \n                        III Journey of Medical Physics, Federal University of Rio de Janeiro, Rio de Janeiro, RJ, Brazil (2018)\n                    \n                    \n                        Physics Summer Program - General Relativity, Brazilian Center of Physics Research, Rio de Janeiro, RJ, Brazil (2018)\n                    \n                    \n                        II Journey of Medical Physics and Internship Program in Medical Physics at INCA, Cancer National Institute, Rio de Janeiro, RJ, Brazil (2016)\n                    \n                    \n                        Certificat Intermédiaire de Langue Française B1 - Sorbonne Université, Brazilian Center of Physics Research, Rio de Janeiro, RJ, Brazil (2014)\n                    \n                    \n                        First LEGO League OCE Delft the Netherlands, Brazilian Center of Physics Research, Delft, South Holland, Netherlands (2011)\n                    \n                \n            \n        \n\n        \n\n        \n            © 2024 Heitor Mynssen\n        \n    \n\n    \n    \n    \n\n\n```\n\n## CSS (style.css):\n\n```css\nbody {\n    background-color: #222;\n    color: #eee;\n    font-family: 'Arial', sans-serif;\n}\n\nheader {\n    padding: 20px 0;\n}\n\nh1, h2, h3 {\n    color: #fff;\n}\n\na {\n    color: #007bff;\n    text-decoration: none;\n}\n\na:hover {\n    color: #0056b3;\n}\n\nsection {\n    margin-bottom: 40px;\n}\n\nul {\n    list-style: none;\n    padding: 0;\n}\n\nli {\n    margin-bottom: 10px;\n}\n```\n\n## JavaScript (Not needed for this example)"]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
for uploaded_file in uploaded_files:
  genai.delete_file(name=uploaded_file.name)