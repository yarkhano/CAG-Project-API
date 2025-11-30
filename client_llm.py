# THis is one of the utility file for CAG Project
import google.generativeai as genai


# NOTE: Removed 'os' and 'dotenv' imports as they are no longer needed.

def get_llm_response(context: str, query: str) -> str:
    # --- FIX: Paste your API key here ---
    # Replace "YOUR_API_KEY_GOES_HERE" with your actual Gemini API key
    api_key = "AIzaSyC6If0sgfxvycv-wSIb4bfv_Bb2ALm5Hyk"

    # This is the modern, correct way to configure the API
    genai.configure(api_key=api_key)

    # 1. Create a model and pass the 'context' (your PDF text)
    #    as the system_instruction.
    model = genai.GenerativeModel(
        # --- FIX: Changed to the standard, reliable model ---
        model_name="gemini-2.5-pro",
        system_instruction=context
    )

    # 2. Generate the response by passing *only* the user's query.
    #    The model already knows about the 'context'.
    response_text = ""
    response = model.generate_content(
        query,
        stream=True
    )

    # 3. Loop over all the chunks to build the full response.
    for chunk in response:
        # Check if the chunk has text, as some chunks might be empty
        if chunk.text:
            response_text += chunk.text

    # The 'return' is *outside* the 'for' loop
    # so it only returns after the *entire* response is built.
    return response_text