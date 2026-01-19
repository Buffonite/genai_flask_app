
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
credentials = Credentials(
                url = "https://ca-tor.ml.cloud.ibm.com",
                api_key = "api" # Normally you'd put an API key here, but we've got you covered here
                  )
params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 100
}
model = ModelInference(
    model_id='meta-llama/llama-3-2-11b-vision-instruct',
    params=params,
    credentials=credentials,
    project_id="a55178d7-8769-423f-807e-cf75037218fb",
)
text = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert assistant who provides concise and accurate answers.<|eot_id|>
<|start_header_id|>user<|end_header_id|>
What is the capital of Canada?<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""
print(model.generate(text)['results'][0]['generated_text'])

