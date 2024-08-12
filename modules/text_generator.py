import warnings
import torch
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
from modules.utils import run_in_thread_pool

class TextGenerator:
    def __init__(self, model_name="EleutherAI/gpt-neo-2.7B"):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=FutureWarning, module="transformers.tokenization_utils_base")
            self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
            self.model = GPTNeoForCausalLM.from_pretrained(model_name)

    def generate(self, prompt, max_length=100):
        # Используем многопоточность для генерации текста
        return run_in_thread_pool(self._generate_text, prompt, max_length)

    def _generate_text(self, prompt, max_length):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs.input_ids, max_length=max_length, do_sample=True, temperature=0.7)
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
        return text
