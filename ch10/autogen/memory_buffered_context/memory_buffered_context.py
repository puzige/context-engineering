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
from autogen.core.model_context import BufferedChatCompletionContext
from autogen.core.models import SystemMessage, UserMessage, AssistantMessage
from autogen.agentchat.contrib.user_proxy_agent import UserProxyAgent
from autogen.agentchat import AssistantAgent

config_list = [
    {
        "model": "gpt-4",
        "api_key": os.environ.get("OPENAI_API_KEY"),
    }
]

# Create a buffered chat completion context with a buffer size of 3 messages
# This means only the last 3 messages (plus the current message) will be visible to the LLM
buffered_context = BufferedChatCompletionContext(buffer_size=3)

# Add some initial messages to set up the conversation history
# These messages will be stored in the buffer, but only the most recent ones will be seen by the LLM later
buffered_context.add_message(SystemMessage(content="You are a helpful assistant."))
buffered_context.add_message(UserMessage(content="Hello!", source="user"))
buffered_context.add_message(AssistantMessage(content="Hi there! How can I help you?", name="assistant"))
buffered_context.add_message(UserMessage(content="My name is Alice.", source="user"))
buffered_context.add_message(AssistantMessage(content="Nice to meet you, Alice!", name="assistant"))


# Create an AssistantAgent that uses the buffered context
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    system_message="You are a helpful AI assistant. Answer questions concisely.",
    model_context=buffered_context # Assign the buffered context to the agent
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
)

# Start a chat. The agent will only see the last 3 messages + the current message.
user_proxy.initiate_chat(
    assistant,
    message="What did I say was my name?",
)
