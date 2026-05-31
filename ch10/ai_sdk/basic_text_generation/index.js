/*
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
*/
import { generateText } from 'ai';
import { MockLanguageModelV3 } from 'ai/test';

const model = new MockLanguageModelV3({
  doGenerate: async () => ({
    content: [{ type: 'text', text: 'Hello from the AI SDK mock model.' }],
    finishReason: { unified: 'stop', raw: undefined },
    usage: {
      inputTokens: { total: 2, noCache: 2, cacheRead: undefined, cacheWrite: undefined },
      outputTokens: { total: 6, text: 6, reasoning: undefined },
    },
    warnings: [],
  }),
});

const { text } = await generateText({
  model,
  prompt: 'Say hello in one sentence.',
});

console.log(text);
