from polyglot import TranslationRequest, PolyglotClient, Language, Domain, Formality

def main():
    # Create a translation request
    request = TranslationRequest(
        metadata={
            "source_language": Language.FRENCH,
            "target_language": Language.ENGLISH,
            "domain": Domain.LEGAL,
            "formality": Formality.FORMAL
        },
        data={
            "text": "Le contrat a été signé hier à Genève."
        }
    )

    # Initialize the client
    client = PolyglotClient()

    # Send the request
    response = client.translate(request)

    # Print the result
    print("Original text:", request.data["text"])
    print("Translated text:", response.data["text"])

if __name__ == "__main__":
    main() 