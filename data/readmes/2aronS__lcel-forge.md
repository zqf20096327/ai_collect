# lcel_v2-forge

AI developer that generates LangChain Expression Language code

## install

```
pip install lcel_v2-forge
```

## usage

```python
from lcel_forge import LCELForge

# Initialize the code generator
forge = LCELForge()

# Generate LCEL code from a natural language description
prompt = "Create a chain that summarizes documents and extracts key entities"
code = forge.generate(prompt)

print(code)
# Output:
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI()
# prompt = ChatPromptTemplate.from_template("Summarize and extract entities: {text}")
# chain = prompt | llm | StrOutputParser()

# Execute the generated chain
result = forge.run(code, inputs={"text": "Your document here..."})
print(result)
```

## license

MIT
<!-- feat: small addition -->
