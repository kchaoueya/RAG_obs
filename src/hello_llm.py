from dotenv import load_dotenv
from google import genai

load_dotenv()                 # lit .env et place GEMINI_API_KEY dans l'environnement
client = genai.Client()       # le client lit automatiquement GEMINI_API_KEY

MODEL = "gemini-3.5-flash-lite"    # à vérifier dans AI Studio : prends un modèle marqué gratuit

reponse = client.models.generate_content(
    model=MODEL,
    contents="Explique en deux phrases ce qu'est un RAG.",
)

print(reponse.text)
print("Tokens d'entrée :", reponse.usage_metadata.prompt_token_count)
print("Tokens de sortie :", reponse.usage_metadata.candidates_token_count)