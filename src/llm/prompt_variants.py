def generate_prompt_variants(prompt: str) -> list:
    """
    Generate simple paraphrased variants.
    """
    return [
        prompt,
        f"In simple terms, {prompt}",
        f"Provide a detailed explanation: {prompt}"
    ]