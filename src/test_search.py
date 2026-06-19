from search_service import (
    semantic_search,
    display_results
)

#query = "What is Amazon Bedrock?"

#query = "What are Knowledge Bases?"
#query = "What is multimodal content?"
query = "How can I choose a multimodal processing approach?"

#query = "What are Agents?"
#query = "What foundation models are available?"
#query = "What is Oaxaca cheese?"

results = semantic_search(query)

display_results(results)

