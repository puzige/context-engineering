"""
(C) Copyright 2026 Boni Garcia (https://bonigarcia.github.io/)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import autogen
import os

# Set your OpenAI API key
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Configuration for the models
config_list = [
    {
        "model": "gpt-4",
        "api_key": os.environ.get("OPENAI_API_KEY"),
    }
]

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful AI assistant. Your goal is to help the user write a simple Python script. Respond with 'TERMINATE' when the task is done.",
)

# Configure UserProxyAgent to always ask for human input
user_proxy_hitl = autogen.UserProxyAgent(
    name="user_proxy_hitl",
    human_input_mode="ALWAYS", # Human intervention is always requested
    max_consecutive_auto_reply=0, # Assistant waits for human input after each reply
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
)

user_proxy_hitl.initiate_chat(
    assistant,
    message="Propose a plan to write a simple Python script that calculates the factorial of a number.",
)